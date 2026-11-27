# -*- coding: utf-8 -*-
"""Scheda "Osservazioni sul campo": per ogni uscita (volo, scialpinismo, alpinismo,
escursione) si registra quello che si è trovato e, nello stesso momento, si salva quello che
il modello prevedeva per quel posto e quel giorno. Il confronto previsto/osservato è il modo
per capire quanto fidarsi delle previsioni, zona per zona, e migliorarsi."""
import json, os, math, urllib.request, urllib.parse
from datetime import date, datetime, timedelta
import pandas as pd
import streamlit as st
import pydeck as pdk

# Web app Google Apps Script collegata al foglio "Neve FVG — osservazioni sul campo"
# (Drive, 2.16 - METEO FVG). Vuoto = archivio provvisorio sul server.
OSSERVAZIONI_URL = ("https://script.google.com/macros/s/"
                    "AKfycbzf4N1_BdN7fZDwCL3GGHX9KEAZ2fZJ60folZ4ffNW91Z5FnaOoVMZTwQ7jiTZVyon9/exec")
FILE_OSS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "osservazioni.json")
CAMPI = ["data", "attivita", "zona", "luogo", "quota", "lat", "lon", "autore", "inserita",
         "note", "osservato", "previsto"]

ATTIVITA = ["\U0001FA82 Volo (parapendio, hike & fly)", "\U0001F3BF Scialpinismo",
            "⛏️ Alpinismo, cascate, misto", "\U0001F97E Escursione, ciaspole"]
SUPERFICIE = {  # osservato -> tipi della diagnosi compatibili
    "polverosa": {"polvere", "assesta", "fredda"},
    "ventata / lastroni / croste da vento": {"ventata", "fredda"},
    "crosta portante (rigelo)": {"rigelo", "crosta"},
    "crosta non portante": {"crosta", "rigelo", "ventata"},
    "firn / primaverile": {"rigelo"},
    "bagnata / marcia": {"bagnata"},
    "brina di superficie": {"fredda", "assesta"},
    "ghiaccio / vetrato": {"crosta", "rigelo"},
    "poca neve, sassi": {"scarsa"},
}
SERVIVA = ["sci", "ciaspole", "ramponi", "picca", "ramponcini", "niente di particolare"]
SEGNALI = ["valanghe spontanee recenti", "whumpf / assestamenti", "fessurazioni",
           "accumuli da vento", "cornici", "neve fresca > 30 cm", "pioggia su neve",
           "forte rialzo termico", "palle di neve / chiocciole"]
FORZA = {"calmo": (0, 5), "debole": (5, 15), "moderato": (15, 25), "forte": (25, 40),
         "molto forte": (40, 200)}
DIR8 = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


# ------------------------------------------------------------------ ARCHIVIO
def _url():
    try:
        return st.secrets.get("OSSERVAZIONI_URL", "") or OSSERVAZIONI_URL
    except Exception:
        return OSSERVAZIONI_URL


@st.cache_data(ttl=120, show_spinner=False)
def _leggi_remoto(url):
    with urllib.request.urlopen(url + ("&" if "?" in url else "?") + "azione=leggi",
                                timeout=25) as f:
        return json.load(f)


def _norm(o):
    for k in ("osservato", "previsto"):
        if isinstance(o.get(k), str):
            try:
                o[k] = json.loads(o[k]) if o[k] else {}
            except Exception:
                o[k] = {}
        o.setdefault(k, {})
    return o


def leggi():
    url = _url()
    if url:
        try:
            r = _leggi_remoto(url)
            return [_norm(dict(x)) for x in (r if isinstance(r, list) else r.get("righe", []))]
        except Exception:
            pass
    try:
        return [_norm(x) for x in json.load(open(FILE_OSS, encoding="utf-8"))]
    except Exception:
        return []


def salva(o):
    url = _url()
    riga = {k: (json.dumps(o[k], ensure_ascii=False) if k in ("osservato", "previsto")
                else o.get(k, "")) for k in CAMPI}
    if url:
        try:
            req = urllib.request.Request(url, data=json.dumps(riga).encode("utf-8"),
                                         headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=25) as f:
                f.read()
            _leggi_remoto.clear()
            return "foglio"
        except Exception:
            pass                                        # ripiego: archivio sul server
    tutte = []
    try:
        tutte = json.load(open(FILE_OSS, encoding="utf-8"))
    except Exception:
        pass
    tutte.append(riga)
    json.dump(tutte, open(FILE_OSS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return "locale"


# ------------------------------------------------------------------ PREVISTO
def _dir_media(v, d):
    u = sum(a * math.sin(math.radians(b)) for a, b in zip(v, d))
    w = sum(a * math.cos(math.radians(b)) for a, b in zip(v, d))
    return (math.degrees(math.atan2(u, w)) + 360) % 360 if (u or w) else None


def card8(x):
    return "—" if x is None or pd.isna(x) else DIR8[int((x % 360) / 45 + .5) % 8]


@st.cache_data(ttl=6 * 3600, show_spinner=False)
def aria_prevista(lat, lon, giorno_iso, quota):
    """Quello che il modello dava per quel punto e quel giorno, ore 11-16."""
    g = date.fromisoformat(giorno_iso)
    base = ("https://api.open-meteo.com/v1/forecast" if (date.today() - g).days <= 85
            else "https://historical-forecast-api.open-meteo.com/v1/forecast")
    p = {"latitude": lat, "longitude": lon, "timezone": "Europe/Rome", "wind_speed_unit": "kmh",
         "start_date": giorno_iso, "end_date": giorno_iso,
         "hourly": "temperature_2m,dew_point_2m,wind_speed_10m,wind_direction_10m,"
                   "wind_speed_850hPa,wind_direction_850hPa,wind_speed_700hPa,"
                   "wind_direction_700hPa,boundary_layer_height,cloud_cover_low,cape,"
                   "precipitation,freezing_level_height"}
    if quota:
        p["elevation"] = quota
    with urllib.request.urlopen(base + "?" + urllib.parse.urlencode(p), timeout=30) as f:
        h = pd.DataFrame(json.load(f)["hourly"])
    h["ora"] = pd.to_datetime(h["time"]).dt.hour
    x = h[(h["ora"] >= 11) & (h["ora"] <= 16)]
    m = lambda c: float(x[c].mean()) if c in x and x[c].notna().any() else None
    t, td = m("temperature_2m"), m("dew_point_2m")
    return dict(
        v10=m("wind_speed_10m"), d10=_dir_media(x["wind_speed_10m"], x["wind_direction_10m"]),
        v850=m("wind_speed_850hPa"),
        d850=_dir_media(x["wind_speed_850hPa"], x["wind_direction_850hPa"]),
        v700=m("wind_speed_700hPa"),
        d700=_dir_media(x["wind_speed_700hPa"], x["wind_direction_700hPa"]),
        blh=m("boundary_layer_height"), nuv_bassa=m("cloud_cover_low"), cape=m("cape"),
        pioggia=float(x["precipitation"].sum()), zt=m("freezing_level_height"),
        base_cumuli=(round((quota or 0) + 125 * (t - td)) if t is not None and td is not None
                     else None))


def neve_prevista(zona_nome, giorno):
    import montagna, manto
    z = next((z for z in montagna.ZONE if z["nome"] == zona_nome), None)
    if not z:
        return {}
    tab, _ = montagna.dati_neve(date.today())
    g = manto.diagnosi(tab[z["id"]], giorno, z["q"])
    if not g:
        return {}
    out = {k: g[k] for k in ("tipo", "titolo", "attrezzatura", "problemi")}
    out["hs"] = round(g["hs"]); out["quota_modello"] = z["q"]
    if giorno == date.today():
        try:
            b = montagna.bollettino_cache(date.today().isoformat()).get(z["micro"], {})
            out["grado_bollettino"] = b.get("grado")
        except Exception:
            pass
    return out


# ------------------------------------------------------------------ CONFRONTO
def confronto(o):
    """Lista di (aspetto, previsto, osservato, esito) con esito True/False/None."""
    ob, pr = o.get("osservato", {}), o.get("previsto", {})
    out = []
    n = pr.get("neve", {})
    if n and ob.get("superficie"):
        compat = set().union(*[SUPERFICIE.get(s, set()) for s in ob["superficie"]])
        out.append(("Neve in superficie", f"{n.get('titolo','')}",
                    ", ".join(ob["superficie"]), n.get("tipo") in compat))
    if n and ob.get("serviva"):
        att = n.get("attrezzatura", "")
        pre_ramp = "ramponi" in att and "solo in cresta" not in att
        oss_ramp = any(s in ob["serviva"] for s in ("ramponi", "picca"))
        out.append(("Picca e ramponi", "sì" if pre_ramp else "no",
                    "sì" if oss_ramp else "no", pre_ramp == oss_ramp))
    if n and ob.get("neve_suolo") not in (None, ""):
        try:
            diff = abs(float(ob["neve_suolo"]) - float(n.get("hs", 0)))
            out.append(("Neve al suolo (cm)", f"{n.get('hs')} (modello a {n.get('quota_modello')} m)",
                        f"{ob['neve_suolo']} a {o.get('quota')} m", diff <= 30))
        except Exception:
            pass
    a = pr.get("aria", {})
    if a and ob.get("vento_dir") and ob.get("vento_dir") != "variabile":
        prev_d = a.get("d10") if a.get("d10") is not None else a.get("d850")
        if prev_d is not None:
            dd = abs((DIR8.index(ob["vento_dir"]) * 45 - prev_d + 180) % 360 - 180)
            out.append(("Direzione del vento", f"{card8(prev_d)} ({a.get('v10', 0):.0f} km/h al suolo, "
                        f"{a.get('v850', 0):.0f} a 850 hPa)", ob["vento_dir"], dd <= 45))
    if a and ob.get("vento_forza"):
        lo, hi = FORZA[ob["vento_forza"]]
        v = a.get("v10")
        if v is not None:
            out.append(("Forza del vento", f"{v:.0f} km/h", ob["vento_forza"],
                        lo - 5 <= v <= hi + 5))
    if a and ob.get("base_cumuli"):
        bc = a.get("base_cumuli")
        if bc:
            out.append(("Base dei cumuli (m)", f"{bc}", f"{ob['base_cumuli']}",
                        abs(bc - float(ob["base_cumuli"])) <= 400))
    if a and ob.get("termiche"):
        blh = a.get("blh") or 0
        pre = "deboli" if blh < 800 else "medie" if blh < 1600 else "forti"
        out.append(("Termiche", f"{pre} (strato limite {blh:.0f} m)", ob["termiche"],
                    None if ob["termiche"] == "assenti" else pre == ob["termiche"]))
    return out


def card_oss(o, card):
    ob = o.get("osservato", {})
    righe = []
    if o.get("luogo"): righe.append(f"<b>{o['luogo']}</b>")
    for k, eti in [("superficie", "neve"), ("serviva", "serviva"), ("segnali", "⚠️"),
                   ("termiche", "termiche"), ("turbolenza", "turbolenza")]:
        v = ob.get(k)
        if v:
            righe.append(f"{eti}: {', '.join(v) if isinstance(v, list) else v}")
    if ob.get("vento_dir"):
        righe.append(f"vento {ob.get('vento_dir')} {ob.get('vento_forza','')}")
    c = confronto(o)
    if c:
        ok = sum(1 for x in c if x[3]); tot = sum(1 for x in c if x[3] is not None)
        righe.append(f"previsione azzeccata su {ok}/{tot} aspetti")
    if o.get("note"): righe.append(str(o["note"]))
    card(f"\U0001F463 {o.get('data','')} · {o.get('attivita','')} · {o.get('quota','')} m",
         "<br>".join(righe), "b")


# ------------------------------------------------------------------ UI
def scheda_osservazioni(card, kv, df_siti=None):
    import montagna
    st.markdown("#### \U0001F4DD Osservazioni sul campo")
    st.caption("Dopo ogni uscita scrivi cosa hai trovato. Insieme all'osservazione viene "
               "salvato quello che i modelli prevedevano per quel posto e quel giorno: neve "
               "(stato del manto della zona) e aria (vento, strato limite, base dei cumuli). "
               "Col tempo si vede dove e quando le previsioni funzionano.")
    if not _url():
        st.info("Archivio provvisorio: finché non è collegato il foglio Google le "
                "osservazioni restano sul server e si perdono al riavvio dell'app. "
                "Scaricale col pulsante in fondo.", icon="ℹ️")

    att = st.segmented_control("Attività", ATTIVITA, default=ATTIVITA[1], key="oss_att") \
        or ATTIVITA[1]
    volo = att == ATTIVITA[0]
    zone = [z["nome"] for z in montagna.ZONE] + ["Fuori dalle 16 zone"]
    dec = None
    if volo and df_siti is not None:
        d_ = df_siti[df_siti["tipo"].isin(["decollo", "hike&fly"])].sort_values("nome")
        nomi = ["—"] + list(d_["nome"])
        sc = st.selectbox("Decollo", nomi, key="oss_dec")
        if sc != "—":
            dec = d_[d_["nome"] == sc].iloc[0]

    with st.form("oss_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        giorno = c1.date_input("Giorno", value=date.today(), format="DD/MM/YYYY")
        zv = montagna.zona_vicina(float(dec["lat"]), float(dec["lon"])) if dec is not None else None
        zona = c2.selectbox("Zona", zone, index=zone.index(zv["nome"]) if zv else 0)
        luogo = st.text_input("Dove di preciso", value=(dec["nome"] if dec is not None else ""),
                              placeholder="es. canale nord dello Zuc dal Bôr")
        c1, c2, c3 = st.columns(3)
        q0 = int(float(dec["quota"])) if dec is not None and str(dec.get("quota")) not in ("", "None", "nan") else 1600
        quota = c1.number_input("Quota (m)", 0, 3000, q0, 50)
        espo = c2.selectbox("Esposizione", ["varie"] + DIR8)
        fascia = c3.selectbox("Quando", ["mattina", "mezzogiorno", "pomeriggio", "tutto il giorno"])

        neve, aria = {}, {}
        with st.expander("❄️ Neve", expanded=not volo):
            c1, c2 = st.columns(2)
            neve["neve_suolo"] = c1.number_input("Neve al suolo (cm)", 0, 600, 0, 5)
            neve["sprofondamento"] = c2.number_input("Sprofondamento scarpone (cm)", 0, 150, 0, 5)
            neve["superficie"] = st.multiselect("Neve in superficie", list(SUPERFICIE))
            neve["serviva"] = st.multiselect("Cosa è servito davvero", SERVIVA)
            neve["segnali"] = st.multiselect("Segnali di pericolo", SEGNALI)
        with st.expander("\U0001FA82 Aria e volo", expanded=volo):
            c1, c2 = st.columns(2)
            aria["vento_dir"] = c1.selectbox("Vento al decollo / in cresta: da", ["—", "variabile"] + DIR8)
            aria["vento_forza"] = c2.selectbox("Forza", ["—"] + list(FORZA))
            c1, c2 = st.columns(2)
            aria["termiche"] = c1.selectbox("Termiche", ["—", "assenti", "deboli", "medie", "forti"])
            aria["turbolenza"] = c2.selectbox("Turbolenza", ["—", "nulla", "leggera", "media", "forte"])
            c1, c2, c3 = st.columns(3)
            aria["base_cumuli"] = c1.number_input("Base cumuli (m, 0 = niente)", 0, 5000, 0, 100)
            aria["quota_max"] = c2.number_input("Quota max raggiunta (m)", 0, 5000, 0, 50)
            aria["durata_min"] = c3.number_input("Durata volo (min)", 0, 600, 0, 5)
            aria["brezza"] = st.selectbox("Brezza di valle", ["—", "assente", "debole", "forte"])
            aria["sovrasviluppi"] = st.checkbox("Sovrasviluppi / temporali")
        voto = st.slider("Com'è andata la giornata rispetto a quello che ti aspettavi?", 1, 5, 3,
                         help="1 molto peggio · 3 come previsto · 5 molto meglio")
        note = st.text_area("Note", placeholder="strati, test, valanghe viste, punti di innesco, "
                                                "dove si saliva, errori di previsione…")
        autore = st.text_input("Nome (facoltativo)")
        ok = st.form_submit_button("Salva osservazione", type="primary")

    if ok:
        ob = {k: v for k, v in {**neve, **aria}.items()
              if v not in ("—", [], 0, False, None, "")}
        ob["esposizione"] = espo; ob["quando"] = fascia; ob["voto"] = voto
        zobj = next((z for z in montagna.ZONE if z["nome"] == zona), None)
        lat = float(dec["lat"]) if dec is not None else (zobj["lat"] if zobj else None)
        lon = float(dec["lon"]) if dec is not None else (zobj["lon"] if zobj else None)
        prev = {}
        with st.spinner("Salvo anche cosa prevedeva il modello…"):
            try:
                if zobj and not volo or (zobj and neve.get("superficie")):
                    prev["neve"] = neve_prevista(zona, giorno)
            except Exception as e:
                prev["neve_errore"] = str(e)
            try:
                if lat is not None:
                    prev["aria"] = aria_prevista(lat, lon, giorno.isoformat(), int(quota))
            except Exception as e:
                prev["aria_errore"] = str(e)
        o = dict(data=giorno.isoformat(), attivita=att, zona=zona, luogo=luogo,
                 quota=int(quota), lat=lat, lon=lon, autore=autore, note=note,
                 inserita=datetime.now().isoformat(timespec="minutes"),
                 osservato=ob, previsto=prev)
        try:
            dove = salva(o)
            if dove == "foglio":
                st.success("Salvata nel foglio Google.")
            else:
                st.warning("Il foglio Google non ha risposto: salvata sul server (provvisoria). "
                           "Scaricala dal pulsante in fondo per non perderla.")
            c = confronto(o)
            if c:
                st.markdown("**Previsto e osservato**")
                st.dataframe(pd.DataFrame(
                    [(a, p, s, "✅" if e else "❌" if e is False else "—") for a, p, s, e in c],
                    columns=["Aspetto", "Previsto", "Osservato", ""]), hide_index=True)
        except Exception as e:
            st.error(f"Non sono riuscito a salvarla ({e}). Riprova.")

    tutte = leggi()
    st.divider()
    st.markdown(f"#### Archivio — {len(tutte)} osservazioni")
    if not tutte:
        st.caption("Ancora nessuna osservazione.")
        return

    # mappa delle osservazioni
    pts = []
    for o in tutte:
        if o.get("lat") in (None, "") or o.get("lon") in (None, ""):
            continue
        c = confronto(o)
        tot = [x[3] for x in c if x[3] is not None]
        quota_ok = (sum(tot) / len(tot)) if tot else None
        col = [150, 150, 150] if quota_ok is None else \
              [34, 160, 70] if quota_ok >= .7 else [225, 170, 20] if quota_ok >= .4 else [200, 45, 45]
        pts.append(dict(lat=float(o["lat"]), lon=float(o["lon"]), col=col,
                        nome=f"{o.get('data','')} · {o.get('luogo') or o.get('zona','')}",
                        att=o.get("attivita", ""),
                        esito=("—" if quota_ok is None else f"{quota_ok*100:.0f}% azzeccato")))
    if pts:
        st.pydeck_chart(pdk.Deck(
            layers=[pdk.Layer("ScatterplotLayer", data=pd.DataFrame(pts),
                              get_position=["lon", "lat"], get_fill_color="col", get_radius=900,
                              radius_min_pixels=7, radius_max_pixels=16, pickable=True,
                              stroked=True, get_line_color=[255, 255, 255],
                              line_width_min_pixels=1)],
            map_style=None, initial_view_state=pdk.ViewState(latitude=46.38, longitude=13.05,
                                                             zoom=7.9),
            tooltip={"html": "<b>{nome}</b><br/>{att}<br/>previsione: {esito}"}), height=380)
        with st.expander("ℹ️ Come leggere la mappa"):
            st.markdown("Ogni punto è un'uscita. Colore = quanto la previsione salvata quel "
                        "giorno corrispondeva a quello che hai trovato: 🟢 ≥ 70% degli aspetti, "
                        "🟡 40–70%, 🔴 meno, ⚪ niente da confrontare.")

    # affidabilità per zona
    righe = []
    for o in tutte:
        for a, p, s, e in confronto(o):
            if e is not None:
                righe.append(dict(zona=o.get("zona"), aspetto=a, ok=int(bool(e))))
    if righe:
        r = pd.DataFrame(righe).groupby(["zona", "aspetto"])["ok"].agg(["mean", "count"])
        r = r.reset_index().rename(columns={"mean": "azzeccate", "count": "uscite"})
        r["azzeccate"] = (r["azzeccate"] * 100).round().astype(int).astype(str) + "%"
        st.markdown("**Quanto ci prendono le previsioni, per zona**")
        st.dataframe(r, hide_index=True, width="stretch")

    for o in sorted(tutte, key=lambda o: str(o.get("data", "")), reverse=True)[:30]:
        with st.expander(f"{o.get('data','')} · {o.get('attivita','')} · "
                         f"{o.get('luogo') or o.get('zona','')}"):
            card_oss(o, card)
            c = confronto(o)
            if c:
                st.dataframe(pd.DataFrame(
                    [(a, p, s, "✅" if e else "❌" if e is False else "—") for a, p, s, e in c],
                    columns=["Aspetto", "Previsto", "Osservato", ""]), hide_index=True)
    flat = pd.DataFrame([{**{k: o.get(k) for k in CAMPI if k not in ("osservato", "previsto")},
                          "osservato": json.dumps(o.get("osservato"), ensure_ascii=False),
                          "previsto": json.dumps(o.get("previsto"), ensure_ascii=False)}
                         for o in tutte])
    st.download_button("Scarica tutte le osservazioni (CSV)", flat.to_csv(index=False),
                       file_name="osservazioni.csv")
