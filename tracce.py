# -*- coding: utf-8 -*-
"""Scheda "Tracce": file IGC dei voli -> termiche, planate, vento stimato dalla deriva,
meteo del giorno; poi l'insieme delle tracce -> termiche di servizio (punti dove si sale
spesso), rotte tipiche (passaggi da una termica all'altra) e come cambiano col vento in
quota, col periodo dell'anno e con l'ora.

Le tracce si caricano a mano (per esempio scaricate una per una da XContest per uso
personale) e vengono conservate nella cartella Drive "Tracce IGC" tramite la web app
Apps Script del progetto; se non risponde restano sul server finché l'app non si riavvia."""
import json, math, os, re, urllib.request, urllib.parse
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import pandas as pd
import streamlit as st
import pydeck as pdk

ROMA = ZoneInfo("Europe/Rome")
DIR_LOC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tracce_locali")
SETTORI = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


def _url():
    import osservazioni
    return osservazioni._url()


# ------------------------------------------------------------------ LETTURA IGC
def leggi_igc(testo):
    """Ritorna (info, DataFrame con t, lat, lon, alt)."""
    info = {"pilota": "", "vela": "", "data": None}
    righe = []
    giorno = None
    for r in testo.splitlines():
        r = r.strip()
        if r.startswith("HFDTE"):
            m = re.search(r"(\d{2})(\d{2})(\d{2})", r[5:])
            if m:
                giorno = date(2000 + int(m.group(3)), int(m.group(2)), int(m.group(1)))
        elif r.startswith("HFPLT"):
            info["pilota"] = r.split(":", 1)[-1].strip()
        elif r.startswith("HFGTY"):
            info["vela"] = r.split(":", 1)[-1].strip()
        elif r.startswith("B") and len(r) >= 35:
            try:
                hh, mm, ss = int(r[1:3]), int(r[3:5]), int(r[5:7])
                la = int(r[7:9]) + int(r[9:14]) / 60000.0
                if r[14] == "S": la = -la
                lo = int(r[15:18]) + int(r[18:23]) / 60000.0
                if r[23] == "W": lo = -lo
                p_alt, g_alt = int(r[25:30]), int(r[30:35])
                righe.append((hh * 3600 + mm * 60 + ss, la, lo, g_alt if g_alt > 0 else p_alt))
            except ValueError:
                continue
    if not righe or giorno is None:
        raise ValueError("file IGC senza data o senza punti")
    d = pd.DataFrame(righe, columns=["sec", "lat", "lon", "alt"])
    # passaggio della mezzanotte UTC
    salto = (d["sec"].diff() < -43200).cumsum() * 86400
    d["sec"] = d["sec"] + salto
    t0 = datetime(giorno.year, giorno.month, giorno.day, tzinfo=timezone.utc)
    d["t"] = [t0 + timedelta(seconds=int(s)) for s in d["sec"]]
    d = d.drop_duplicates("sec").reset_index(drop=True)
    info["data"] = d["t"].iloc[0].astimezone(ROMA).date()
    return info, d


def _bearing(la1, lo1, la2, lo2):
    y = math.sin(math.radians(lo2 - lo1)) * math.cos(math.radians(la2))
    x = (math.cos(math.radians(la1)) * math.sin(math.radians(la2)) -
         math.sin(math.radians(la1)) * math.cos(math.radians(la2)) * math.cos(math.radians(lo2 - lo1)))
    return (math.degrees(math.atan2(y, x)) + 360) % 360


def _dist(la1, lo1, la2, lo2):
    dy = (la2 - la1) * 111320
    dx = (lo2 - lo1) * 111320 * math.cos(math.radians((la1 + la2) / 2))
    return math.hypot(dx, dy)


def settore(gr, v=None, calmo=10):
    if gr is None or pd.isna(gr): return "—"
    if v is not None and not pd.isna(v) and v < calmo: return "debole"
    return SETTORI[int((gr % 360) / 45 + .5) % 8]


# ------------------------------------------------------------------ ANALISI DI UN VOLO
def analizza(d):
    """Termiche (spirali con salita) e planate di un volo."""
    d = d.copy()
    n = len(d)
    hdg = [float("nan")] * n
    vs = [0.0] * n
    for i in range(1, n):
        if _dist(d.lat[i - 1], d.lon[i - 1], d.lat[i], d.lon[i]) > 1:
            hdg[i] = _bearing(d.lat[i - 1], d.lon[i - 1], d.lat[i], d.lon[i])
    d["hdg"] = pd.Series(hdg).ffill()
    dh = d["hdg"].diff().fillna(0)
    dh = ((dh + 180) % 360) - 180                       # variazione di rotta con segno
    d["dh"] = dh
    d["vz"] = d["alt"].diff() / d["sec"].diff().replace(0, 1)
    # finestra mobile di 30 s: quanto si gira e quanto si sale
    t = d["sec"].values
    giro = [0.0] * n
    sal = [0.0] * n
    j = 0
    cum = d["dh"].cumsum().values
    for i in range(n):
        while t[i] - t[j] > 30:
            j += 1
        giro[i] = abs(cum[i] - cum[j])
        sal[i] = (d["alt"].iloc[i] - d["alt"].iloc[j]) / max(t[i] - t[j], 1)
    d["giro30"] = giro
    d["sal30"] = sal
    d["spirale"] = d["giro30"] >= 200

    termiche = []
    in_t, i0 = False, 0
    for i in range(n + 1):
        s = bool(d["spirale"].iloc[i]) if i < n else False
        if s and not in_t:
            in_t, i0 = True, i
        elif not s and in_t:
            # chiude solo se la pausa supera 15 s
            k = i
            while k < n and not d["spirale"].iloc[k] and t[k] - t[i - 1] <= 15:
                k += 1
            if k < n and d["spirale"].iloc[k]:
                continue
            in_t = False
            seg = d.iloc[max(i0 - 15, 0):i]                # include l'ingresso
            dur = seg["sec"].iloc[-1] - seg["sec"].iloc[0]
            if dur < 30:
                continue
            base = float(seg["alt"].min()); top = float(seg["alt"].max())
            i_top = seg["alt"].idxmax()
            seg = seg.loc[:i_top]
            dur = max(seg["sec"].iloc[-1] - seg["sec"].iloc[0], 1)
            guad = top - float(seg["alt"].iloc[0])
            if guad < 40:
                continue
            # deriva: retta tempo-posizione dentro la termica -> vento
            vento_v = vento_d = None
            if dur >= 60 and len(seg) > 10:
                tt = seg["sec"] - seg["sec"].mean()
                den = float((tt ** 2).sum())
                if den > 0:
                    vy = float((tt * (seg["lat"] - seg["lat"].mean())).sum()) / den * 111320
                    vx = float((tt * (seg["lon"] - seg["lon"].mean())).sum()) / den * 111320 * \
                        math.cos(math.radians(seg["lat"].mean()))
                    vento_v = math.hypot(vx, vy) * 3.6
                    vento_d = (math.degrees(math.atan2(vx, vy)) + 180) % 360   # da dove viene
            termiche.append(dict(
                lat=float(seg["lat"].mean()), lon=float(seg["lon"].mean()),
                base=base, top=top, guadagno=guad, durata=int(dur),
                salita=guad / dur, ora=seg["t"].iloc[0].astimezone(ROMA).hour + \
                seg["t"].iloc[0].astimezone(ROMA).minute / 60,
                t0=seg["t"].iloc[0], vento_v=vento_v, vento_d=vento_d))
    # planate tra le termiche
    planate = []
    for a, b in zip(termiche, termiche[1:]):
        dist = _dist(a["lat"], a["lon"], b["lat"], b["lon"])
        dt = (b["t0"] - a["t0"]).total_seconds() - a["durata"]
        perso = a["top"] - b["base"]
        if dt > 0 and dist > 200:
            planate.append(dict(da=(a["lat"], a["lon"]), a=(b["lat"], b["lon"]), dist=dist,
                                efficienza=(dist / perso if perso > 0 else None),
                                vel=dist / dt * 3.6, rotta=_bearing(a["lat"], a["lon"], b["lat"], b["lon"])))
    tot = 0.0
    for i in range(1, n):
        tot += _dist(d.lat[i - 1], d.lon[i - 1], d.lat[i], d.lon[i])
    riass = dict(
        decollo=(float(d.lat.iloc[0]), float(d.lon.iloc[0])), quota_decollo=int(d.alt.iloc[0]),
        quota_max=int(d.alt.max()), durata_min=int((t[-1] - t[0]) / 60),
        ora_decollo=d["t"].iloc[0].astimezone(ROMA).strftime("%H:%M"),
        km_percorsi=round(tot / 1000, 1),
        km_max_dal_decollo=round(max(_dist(d.lat.iloc[0], d.lon.iloc[0], la, lo)
                                     for la, lo in zip(d.lat[::10], d.lon[::10])) / 1000, 1),
        n_termiche=len(termiche),
        salita_media=(round(sum(x["guadagno"] for x in termiche) /
                            max(sum(x["durata"] for x in termiche), 1), 2) if termiche else None))
    vv = [x for x in termiche if x["vento_v"] is not None]
    if vv:
        u = sum(x["vento_v"] * math.sin(math.radians(x["vento_d"])) for x in vv) / len(vv)
        w = sum(x["vento_v"] * math.cos(math.radians(x["vento_d"])) for x in vv) / len(vv)
        riass["vento_stimato"] = (round(math.hypot(u, w)), (math.degrees(math.atan2(u, w)) + 360) % 360)
    return riass, termiche, planate, d


# ------------------------------------------------------------------ METEO DEL GIORNO
@st.cache_data(ttl=30 * 24 * 3600, show_spinner=False)
def meteo_giorno(lat, lon, giorno_iso):
    """Cosa diceva il modello quel giorno nel punto di decollo, ore 11-16."""
    g = date.fromisoformat(giorno_iso)
    base = ("https://api.open-meteo.com/v1/forecast" if (date.today() - g).days <= 85
            else "https://historical-forecast-api.open-meteo.com/v1/forecast")
    p = {"latitude": round(lat, 3), "longitude": round(lon, 3), "timezone": "Europe/Rome",
         "start_date": giorno_iso, "end_date": giorno_iso, "wind_speed_unit": "kmh",
         "hourly": "temperature_2m,dew_point_2m,wind_speed_850hPa,wind_direction_850hPa,"
                   "wind_speed_700hPa,wind_direction_700hPa,boundary_layer_height,cape,"
                   "cloud_cover_low,freezing_level_height"}
    with urllib.request.urlopen(base + "?" + urllib.parse.urlencode(p), timeout=30) as f:
        js = json.load(f)
    h = pd.DataFrame(js["hourly"])
    h["ora"] = pd.to_datetime(h["time"]).dt.hour
    x = h[(h["ora"] >= 11) & (h["ora"] <= 16)]

    def media(c):
        return float(x[c].mean()) if c in x and x[c].notna().any() else None

    def vett(v, dd):
        u = (x[v] * x[dd].map(lambda a: math.sin(math.radians(a)))).mean()
        w = (x[v] * x[dd].map(lambda a: math.cos(math.radians(a)))).mean()
        return float(math.hypot(u, w)), float((math.degrees(math.atan2(u, w)) + 360) % 360)

    v8, d8 = vett("wind_speed_850hPa", "wind_direction_850hPa")
    v7, d7 = vett("wind_speed_700hPa", "wind_direction_700hPa")
    t, td = media("temperature_2m"), media("dew_point_2m")
    return dict(v850=v8, d850=d8, v700=v7, d700=d7, blh=media("boundary_layer_height"),
                cape=media("cape"), nuv_bassa=media("cloud_cover_low"),
                zt=media("freezing_level_height"),
                base_cumuli=(round(js.get("elevation", 0) + 125 * (t - td))
                             if t is not None and td is not None else None))


# ------------------------------------------------------------------ ARCHIVIO
@st.cache_data(ttl=300, show_spinner=False)
def _elenco_remoto(url):
    with urllib.request.urlopen(url + "?azione=tracce", timeout=30) as f:
        return json.load(f)


@st.cache_data(ttl=30 * 24 * 3600, show_spinner=False)
def _scarica_remoto(url, fid):
    with urllib.request.urlopen(url + "?azione=igc&id=" + urllib.parse.quote(fid), timeout=60) as f:
        return f.read().decode("utf-8", "replace")


def elenco():
    """[(nome, chiave)] di tutte le tracce disponibili."""
    out = []
    url = _url()
    if url:
        try:
            for x in _elenco_remoto(url):
                out.append((x["nome"], ("drive", x["id"])))
        except Exception:
            pass
    if os.path.isdir(DIR_LOC):
        nomi = {n for n, _ in out}
        for f in sorted(os.listdir(DIR_LOC)):
            if f not in nomi:
                out.append((f, ("locale", os.path.join(DIR_LOC, f))))
    return out


def testo(chiave):
    tipo, k = chiave
    if tipo == "drive":
        return _scarica_remoto(_url(), k)
    return open(k, encoding="utf-8", errors="replace").read()


def salva(nome, contenuto):
    url = _url()
    if url:
        try:
            dati = json.dumps({"azione": "igc", "nome": nome, "testo": contenuto}).encode("utf-8")
            req = urllib.request.Request(url, data=dati, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as f:
                f.read()
            _elenco_remoto.clear()
            return "drive"
        except Exception:
            pass
    os.makedirs(DIR_LOC, exist_ok=True)
    open(os.path.join(DIR_LOC, nome), "w", encoding="utf-8").write(contenuto)
    return "locale"


@st.cache_data(ttl=30 * 24 * 3600, show_spinner=False)
def elabora(nome, contenuto):
    """Analisi completa di una traccia (in cache per contenuto)."""
    info, d = leggi_igc(contenuto)
    riass, term, plan, d2 = analizza(d)
    try:
        met = meteo_giorno(riass["decollo"][0], riass["decollo"][1], info["data"].isoformat())
    except Exception:
        met = {}
    punti = d2.iloc[::max(len(d2) // 600, 1)][["lon", "lat", "alt"]].values.tolist()
    for x in term:
        x["t0"] = x["t0"].isoformat()
    return dict(nome=nome, info={**info, "data": info["data"].isoformat()}, riass=riass,
                termiche=term, planate=plan, meteo=met, percorso=punti)


def settore_volo(v):
    """Settore del vento in quota del giorno: dal modello (700 hPa) o, se manca, dalla
    deriva delle spirali."""
    m = v.get("meteo") or {}
    if m.get("d700") is not None:
        return settore(m.get("d700"), m.get("v700"))
    ve = v["riass"].get("vento_stimato")
    return settore(ve[1], ve[0]) + "*" if ve else "—"


# ------------------------------------------------------------------ INSIEME DELLE TRACCE
def termiche_di_servizio(voli, raggio=450):
    """Raggruppa le termiche di tutti i voli in punti ricorrenti."""
    tutte = []
    for v in voli:
        m = v["meteo"]
        for x in v["termiche"]:
            tutte.append({**x, "volo": v["nome"], "data": v["info"]["data"],
                          "sett700": settore_volo(v),
                          "v700": m.get("v700"), "blh": m.get("blh")})
    tutte.sort(key=lambda x: -x["guadagno"])
    gruppi = []
    for x in tutte:
        best = None
        for g in gruppi:
            if _dist(g["lat"], g["lon"], x["lat"], x["lon"]) <= raggio:
                best = g; break
        if best is None:
            gruppi.append({"lat": x["lat"], "lon": x["lon"], "membri": [x]})
        else:
            best["membri"].append(x)
            k = len(best["membri"])
            best["lat"] += (x["lat"] - best["lat"]) / k
            best["lon"] += (x["lon"] - best["lon"]) / k
    out = []
    for i, g in enumerate(gruppi):
        m = pd.DataFrame(g["membri"])
        out.append(dict(
            id=i, lat=g["lat"], lon=g["lon"], n=len(m), voli=m["volo"].nunique(),
            salita=round(m["salita"].mean(), 1), top=int(m["top"].median()),
            base=int(m["base"].median()), ora=round(m["ora"].median(), 1),
            ore=sorted({int(h) for h in m["ora"]}),
            venti=m["sett700"].value_counts().to_dict(),
            mesi=sorted({int(str(dd)[5:7]) for dd in m["data"]})))
    return pd.DataFrame(out), pd.DataFrame(tutte)


def rotte_tipiche(voli, servizio, raggio=450):
    """Passaggi da una termica di servizio all'altra, contati su tutti i voli."""
    if servizio.empty:
        return pd.DataFrame()
    conta = {}
    for v in voli:
        seq = []
        for x in v["termiche"]:
            dd = [(_dist(r.lat, r.lon, x["lat"], x["lon"]), r.id) for r in servizio.itertuples()]
            dmin, idm = min(dd)
            if dmin <= raggio and (not seq or seq[-1] != idm):
                seq.append(idm)
        for a, b in zip(seq, seq[1:]):
            conta[(a, b)] = conta.get((a, b), 0) + 1
    s = servizio.set_index("id")
    righe = [dict(da=a, a=b, n=c, lon0=s.loc[a, "lon"], lat0=s.loc[a, "lat"],
                  lon1=s.loc[b, "lon"], lat1=s.loc[b, "lat"]) for (a, b), c in conta.items()]
    return pd.DataFrame(righe)


# ------------------------------------------------------------------ UI
COL_SETT = {"N": [70, 130, 230], "NE": [60, 180, 200], "E": [60, 170, 110],
            "SE": [150, 190, 60], "S": [230, 180, 40], "SW": [235, 120, 40],
            "W": [210, 60, 60], "NW": [160, 80, 200], "debole": [160, 160, 160], "—": [120, 120, 120]}


def scheda_tracce(card, kv, df_siti=None):
    st.markdown("#### \U0001F6F0️ Tracce dei voli")
    st.caption("Carica i file IGC dei voli (i tuoi, o scaricati uno per uno da XContest per "
               "uso personale). L'app trova le termiche (dove si gira e si sale), le planate, il "
               "vento in quota stimato dalla deriva delle spirali e recupera il meteo previsto "
               "quel giorno. Mettendo insieme le tracce vengono fuori le termiche di servizio, "
               "le rotte tipiche e come cambiano con vento, periodo e ora.")
    with st.expander("➕ Carica tracce IGC", expanded=False):
        up = st.file_uploader("File .igc", type=["igc"], accept_multiple_files=True,
                              key="igc_up")
        if up and st.button("Salva e analizza", type="primary"):
            esiti = []
            for f in up:
                cont = f.getvalue().decode("utf-8", "replace")
                try:
                    leggi_igc(cont)
                except Exception as e:
                    esiti.append(f"❌ {f.name}: {e}"); continue
                dove = salva(f.name, cont)
                esiti.append(f"✅ {f.name} ({'Drive' if dove == 'drive' else 'provvisoria sul server'})")
            st.write("\n".join(f"- {x}" for x in esiti))
        st.caption("Su XContest: apri il volo, scarica il file IGC (serve l'accesso). "
                   "Le tracce non vengono scaricate in automatico.")

    lista = elenco()
    if not lista:
        st.info("Ancora nessuna traccia. Caricane qualcuna qui sopra.")
        return
    voli, errori = [], []
    with st.spinner(f"Analizzo {len(lista)} tracce…"):
        for nome, k in lista:
            try:
                voli.append(elabora(nome, testo(k)))
            except Exception as e:
                errori.append(f"{nome}: {e}")
    if errori:
        st.caption("Non lette: " + "; ".join(errori[:5]))
    if not voli:
        return

    # ---- filtri: condizioni
    c1, c2, c3 = st.columns(3)
    sett_tutti = sorted({settore_volo(v) for v in voli})
    f_sett = c1.multiselect("Vento a 700 hPa (dal modello)", sett_tutti, default=sett_tutti,
                            key="trc_sett")
    stagioni = {"inverno": [12, 1, 2], "primavera": [3, 4, 5], "estate": [6, 7, 8],
                "autunno": [9, 10, 11]}
    f_stag = c2.multiselect("Periodo", list(stagioni), default=list(stagioni), key="trc_stag")
    f_ore = c3.slider("Ora delle termiche", 8, 20, (9, 19), key="trc_ore")
    mesi_ok = {m for s in f_stag for m in stagioni[s]}
    sel = [v for v in voli
           if settore_volo(v) in f_sett
           and int(v["info"]["data"][5:7]) in mesi_ok]
    for v in sel:
        v["termiche"] = [x for x in v["termiche"] if f_ore[0] <= x["ora"] <= f_ore[1]]
    st.caption(f"{len(sel)} voli su {len(voli)} con questi filtri.")
    if not sel:
        return
    serv, tutte = termiche_di_servizio(sel)
    rotte = rotte_tipiche(sel, serv)

    # ---- mappa
    strati = []
    path = [dict(path=[[p[0], p[1]] for p in v["percorso"]], nome=v["nome"],
                 col=COL_SETT[settore_volo(v).rstrip("*")])
            for v in sel]
    strati.append(pdk.Layer("PathLayer", data=path, get_path="path", get_color="col",
                            width_min_pixels=1, opacity=0.35, pickable=False))
    if not rotte.empty:
        rotte["w"] = rotte["n"].clip(upper=10)
        strati.append(pdk.Layer("LineLayer", data=rotte, get_source_position=["lon0", "lat0"],
                                get_target_position=["lon1", "lat1"], get_width="w",
                                width_scale=2, get_color=[255, 255, 255, 200], pickable=False))
    if not serv.empty:
        serv["r"] = 150 + serv["n"] * 60
        serv["col"] = [[226, 116, 28] if s >= 2 else [225, 170, 20] if s >= 1 else [90, 160, 255]
                       for s in serv["salita"]]
        serv["venti_t"] = [", ".join(f"{k} {v}" for k, v in sorted(x.items(), key=lambda z: -z[1]))
                           for x in serv["venti"]]
        serv["ore_t"] = [f"{min(o)}–{max(o) + 1}" if o else "" for o in serv["ore"]]
        strati.append(pdk.Layer("ScatterplotLayer", id="servizio", data=serv,
                                get_position=["lon", "lat"], get_radius="r", get_fill_color="col",
                                opacity=0.85, stroked=True, get_line_color=[255, 255, 255],
                                line_width_min_pixels=1, pickable=True))
    c_lat = sum(v["riass"]["decollo"][0] for v in sel) / len(sel)
    c_lon = sum(v["riass"]["decollo"][1] for v in sel) / len(sel)
    st.pydeck_chart(pdk.Deck(
        layers=strati, map_style=None,
        initial_view_state=pdk.ViewState(latitude=c_lat, longitude=c_lon, zoom=10),
        tooltip={"html": "<b>Termica di servizio</b><br/>{n} termiche in {voli} voli<br/>"
                         "salita media {salita} m/s · top mediano {top} m<br/>"
                         "ore {ore_t} · vento 700 hPa: {venti_t}"}), height=520)
    with st.expander("ℹ️ Come leggere la mappa"):
        st.markdown("**Linee sottili** = tracce, colorate secondo il vento a 700 hPa del giorno "
                    "(N blu, E verde, S giallo, SW arancio, W rosso, NW viola, grigio = debole). "
                    "**Cerchi** = termiche di servizio: punti dove più voli hanno trovato "
                    "salita (raggio 450 m); più grande = più usata, arancio ≥ 2 m/s, giallo "
                    "≥ 1 m/s, blu più debole. **Linee bianche** = rotte tipiche: passaggi da "
                    "una termica di servizio all'altra, più spesse se ripetute in più voli. "
                    "Cambia i filtri sopra per vedere cosa succede con altro vento, periodo, ora.")

    # ---- tabelle di sintesi
    if not serv.empty:
        st.markdown("**Termiche di servizio**")
        t = serv.sort_values(["voli", "n"], ascending=False)[
            ["id", "n", "voli", "salita", "base", "top", "ore_t", "venti_t", "lat", "lon"]]
        t.columns = ["#", "termiche", "voli", "salita m/s", "base m", "top m", "ore",
                     "vento 700 hPa nei giorni", "lat", "lon"]
        st.dataframe(t.head(30), hide_index=True, width="stretch")
    if not tutte.empty:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Con che vento (700 hPa)**")
            g = tutte.groupby("sett700").agg(termiche=("salita", "size"),
                                             salita=("salita", "mean"), top=("top", "median"))
            st.dataframe(g.round(1), width="stretch")
        with c2:
            st.markdown("**A che ora**")
            tutte["fascia"] = (tutte["ora"] // 1).astype(int)
            g = tutte.groupby("fascia").agg(termiche=("salita", "size"),
                                            salita=("salita", "mean"), top=("top", "median"))
            st.bar_chart(g["salita"], height=180)
            st.caption("Salita media per ora del giorno.")
        tutte["mese"] = tutte["data"].str[5:7].astype(int)
        g = tutte.groupby("mese").agg(termiche=("salita", "size"), salita=("salita", "mean"),
                                      top=("top", "median"))
        st.markdown("**Per mese**")
        st.dataframe(g.round(1).T, width="stretch")

    # ---- elenco voli
    st.markdown("**Voli**")
    righe = []
    for v in sel:
        r, m = v["riass"], v["meteo"]
        ve = r.get("vento_stimato")
        righe.append({
            "data": v["info"]["data"], "volo": v["nome"], "pilota": v["info"]["pilota"],
            "decollo ore": r["ora_decollo"], "durata min": r["durata_min"],
            "quota max": r["quota_max"], "km dal decollo": r["km_max_dal_decollo"],
            "termiche": r["n_termiche"], "salita media": r["salita_media"],
            "vento dalle spirali": (f"{ve[0]} km/h da {settore(ve[1])}" if ve else "—"),
            "vento 700 hPa (modello)": (f"{m['v700']:.0f} km/h da {settore(m['d700'])}"
                                        if m.get("v700") is not None else "—"),
            "strato limite m": round(m["blh"]) if m.get("blh") else None,
            "base cumuli stimata": m.get("base_cumuli"),
        })
    st.dataframe(pd.DataFrame(righe).sort_values("data", ascending=False),
                 hide_index=True, width="stretch")
    st.caption("* = vento del giorno ricavato dalle spirali perché il modello non era "
               "disponibile. "
               "Il vento dalle spirali è la deriva media delle termiche: un controllo "
               "indipendente del vento previsto. Base cumuli stimata = quota del punto + "
               "125 × (temperatura − punto di rugiada).")
