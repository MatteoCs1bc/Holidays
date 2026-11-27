# -*- coding: utf-8 -*-
"""Schede 'Neve per zona' e 'Rotte di volo' (+ elenco documenti meteo FVG).

Dati: Open-Meteo (modelli, alla quota di riferimento di ogni zona), link alle
stazioni ARPA FVG-OSMER, tile di thermal.kk7.ch (CC BY-NC-SA 4.0).
Niente di questo sostituisce il bollettino valanghe."""
import json, math, urllib.request, urllib.parse
from datetime import date, datetime, timedelta
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

HOST_APP = "holidays-fmd923jzymr5fncrthpnrl.streamlit.app"   # ?src= chiesto da kk7
INIZIO_MESE, INIZIO_GIORNO = 11, 1                          # stagione dal 1 novembre

# ------------------------------------------------------------------ ZONE
# Coordinate = punto rappresentativo in quota; q = quota di riferimento per il manto.
# Sono APPROSSIMATE: si correggono qui. "osmer" = stazioni ARPA FVG vicine (da verificare).
ZONE = [
 dict(id="dolfri", nome="Dolomiti Friulane", lat=46.390, lon=12.530, q=1800,
      osmer="Forni di Sopra, Claut", note="Val Cimoliana, Monfalconi, Spalti di Toro"),
 dict(id="prealpi", nome="Prealpi Maniago–Aviano", lat=46.140, lon=12.560, q=1300,
      osmer="Piancavallo, Barcis", note="Piancavallo, Raut, Cavallo"),
 dict(id="pesarina", nome="Val Pesarina", lat=46.525, lon=12.640, q=1600,
      osmer="Forni Avoltri, Comeglians", note="Pradibosco, Siera, Clap Grande"),
 dict(id="sappada", nome="Sappada", lat=46.575, lon=12.700, q=1800,
      osmer="Sappada / Forni Avoltri", note="Peralba, Siera, Lastroni"),
 dict(id="zoncolan", nome="Zona Zoncolan", lat=46.500, lon=12.925, q=1750,
      osmer="Ravascletto, Comeglians", note="Zoncolan, Tamai, Arvenis"),
 dict(id="gemonese", nome="Gemonese", lat=46.300, lon=13.200, q=1500,
      osmer="Gemona, Musi", note="Chiampon, Cuarnan, Glemina"),
 dict(id="tagliam", nome="Val Tagliamento", lat=46.420, lon=12.760, q=1500,
      osmer="Enemonzo, Forni di Sopra", note="Ampezzo, Passo Pura, Forni di Sotto"),
 dict(id="avostanis", nome="Carnia — Avostanis / Monte Croce", lat=46.580, lon=13.000, q=1900,
      osmer="Paluzza, Timau", note="Avostanis, Pal Piccolo, Passo Monte Croce Carnico"),
 dict(id="amariana", nome="Carnia — Amariana / Verzegnis", lat=46.395, lon=13.000, q=1600,
      osmer="Tolmezzo, Enemonzo", note="Amariana, Verzegnis, Lago di Cavazzo"),
 dict(id="tramontina", nome="Zona Tramontina", lat=46.300, lon=12.790, q=1400,
      osmer="Chievolis, Meduno", note="Val Tramontina, Val Meduna"),
 dict(id="sernio", nome="Sernio / Grauzaria", lat=46.475, lon=13.170, q=1800,
      osmer="Paularo, Moggio", note="Sernio, Grauzaria, Val Aupa"),
 dict(id="zuc", nome="Zuc dal Bôr / Cjavals", lat=46.450, lon=13.270, q=1900,
      osmer="Pontebba, Moggio", note="Zuc dal Bôr, Cjavals, Val Aupa / Val Alba"),
 dict(id="resia", nome="Val Resia", lat=46.370, lon=13.350, q=1700,
      osmer="Musi, Resia", note="Sella Carnizza, Canin sud"),
 dict(id="raccolana", nome="Val Raccolana", lat=46.390, lon=13.470, q=1800,
      osmer="Sella Nevea", note="Sella Nevea, Montasio, Canin nord"),
 dict(id="tarvisio", nome="Pontebba – Tarvisio", lat=46.520, lon=13.420, q=1600,
      osmer="Tarvisio, Pontebba, Malborghetto", note="Pramollo, Lussari, Val Canale"),
 dict(id="mangart", nome="Zona Mangart", lat=46.445, lon=13.650, q=2000,
      osmer="Fusine / Tarvisio", note="Mangart, Laghi di Fusine, Ponze"),
]

GIORN = ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "rain_sum",
         "snowfall_sum", "wind_speed_10m_max", "wind_gusts_10m_max",
         "wind_direction_10m_dominant", "sunshine_duration"]
ORARIE = ["temperature_2m", "freezing_level_height", "snow_depth", "cloud_cover",
          "wind_speed_700hPa", "wind_direction_700hPa"]


def inizio_stagione(oggi=None):
    oggi = oggi or date.today()
    a = oggi.year if oggi.month >= INIZIO_MESE else oggi.year - 1
    return date(a, INIZIO_MESE, INIZIO_GIORNO)


def _json(url, timeout=40):
    with urllib.request.urlopen(url, timeout=timeout) as f:
        return json.load(f)


def _url(base, extra):
    p = {"latitude": ",".join(str(z["lat"]) for z in ZONE),
         "longitude": ",".join(str(z["lon"]) for z in ZONE),
         "elevation": ",".join(str(z["q"]) for z in ZONE),
         "timezone": "Europe/Rome", "wind_speed_unit": "kmh",
         "daily": ",".join(GIORN), "hourly": ",".join(ORARIE)}
    p.update(extra)
    return base + "?" + urllib.parse.urlencode(p)


@st.cache_data(ttl=3 * 3600, show_spinner=False)
def scarica_stagione(oggi_iso):
    """Una sola richiesta per tutte le 16 zone (Open-Meteo accetta liste di punti).
    Fino a 92 giorni indietro basta l'API forecast; oltre si usa l'archivio
    delle previsioni (historical-forecast) e si attacca la previsione."""
    oggi = date.fromisoformat(oggi_iso)
    ini = inizio_stagione(oggi)
    giorni = (oggi - ini).days
    if giorni <= 90:
        r = _json(_url("https://api.open-meteo.com/v1/forecast",
                       {"past_days": max(giorni, 1), "forecast_days": 7}))
        return r if isinstance(r, list) else [r]
    st_ = _json(_url("https://historical-forecast-api.open-meteo.com/v1/forecast",
                     {"start_date": ini.isoformat(),
                      "end_date": (oggi - timedelta(days=3)).isoformat()}), timeout=90)
    pr = _json(_url("https://api.open-meteo.com/v1/forecast",
                    {"past_days": 2, "forecast_days": 7}))
    st_ = st_ if isinstance(st_, list) else [st_]
    pr = pr if isinstance(pr, list) else [pr]
    out = []
    for a, b in zip(st_, pr):
        m = {}
        for blocco in ("daily", "hourly"):
            m[blocco] = {k: a[blocco][k] + b[blocco][k] for k in a[blocco]}
        out.append(m)
    return out


def tabella_zona(raw, q):
    """Dati giornalieri di una zona, con gli orari riassunti per giorno."""
    d = pd.DataFrame(raw["daily"]).rename(columns={"time": "data"})
    d["data"] = pd.to_datetime(d["data"]).dt.date
    h = pd.DataFrame(raw["hourly"])
    h["t"] = pd.to_datetime(h["time"])
    h["data"] = h["t"].dt.date
    h["ora"] = h["t"].dt.hour
    g = h.groupby("data")
    agg = pd.DataFrame({
        "zt_max": g["freezing_level_height"].max(),
        "zt_min": g["freezing_level_height"].min(),
        "neve_suolo": g["snow_depth"].last() * 100,          # m -> cm
        "v700_max": g["wind_speed_700hPa"].max(),
    })
    agg["v700_dir"] = g.apply(lambda x: _dir_media(x["wind_speed_700hPa"],
                                                   x["wind_direction_700hPa"]))
    notte = h[h["ora"] <= 6].groupby("data")
    agg["nuv_notte"] = notte["cloud_cover"].mean()
    d = d.merge(agg.reset_index(), on="data", how="left")
    d = d.drop_duplicates("data").sort_values("data").reset_index(drop=True)
    d["hn72"] = d["snowfall_sum"].rolling(3, min_periods=1).sum()
    d["neve_stagione"] = d["snowfall_sum"].fillna(0).cumsum()
    d["q"] = q
    d["eventi"] = [eventi_giorno(d, i) for i in range(len(d))]
    return d


def _dir_media(v, dd):
    v, dd = pd.Series(v).fillna(0), pd.Series(dd).fillna(0)
    u = (v * dd.map(lambda x: math.sin(math.radians(x)))).sum()
    w = (v * dd.map(lambda x: math.cos(math.radians(x)))).sum()
    return (math.degrees(math.atan2(u, w)) + 360) % 360 if (u or w) else float("nan")


CARD = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
def card8(deg):
    return "—" if pd.isna(deg) else CARD[int((deg % 360) / 45 + .5) % 8]
def sottovento(deg):
    return "—" if pd.isna(deg) else CARD[int(((deg + 180) % 360) / 45 + .5) % 8]


def _n(x, d=0.0):
    return d if x is None or pd.isna(x) else float(x)


def eventi_giorno(d, i):
    """Regole semplici e dichiarate. Ritorna lista di (livello, testo).
    livello: r alto, o marcato, y da tenere d'occhio, b informazione."""
    r = d.iloc[i]
    q = r["q"]
    ev = []
    hn = _n(r["snowfall_sum"]); hn72 = _n(r["hn72"]); pioggia = _n(r["rain_sum"])
    suolo = _n(r["neve_suolo"]); raff = _n(r["wind_gusts_10m_max"]); v7 = _n(r["v700_max"])
    zt = _n(r["zt_max"], -1); tmin = _n(r["temperature_2m_min"], 0)
    neve_c_e = suolo > 5 or hn72 > 5
    if hn72 >= 50:
        ev.append(("r", f"Nevicata importante: {hn72:.0f} cm in 72 h"))
    elif hn72 >= 30:
        ev.append(("o", f"Molta neve fresca: {hn72:.0f} cm in 72 h"))
    elif hn >= 10:
        ev.append(("y", f"Neve fresca: {hn:.0f} cm in 24 h"))
    elif hn >= 1:
        ev.append(("b", f"Spolverata: {hn:.0f} cm"))
    if pioggia >= 1 and neve_c_e:
        ev.append(("o" if pioggia >= 10 else "y",
                   f"Pioggia su neve: {pioggia:.0f} mm a {q} m — neve bagnata, poi crosta"))
    if (raff >= 50 or v7 >= 40) and (hn72 >= 5 or (neve_c_e and v7 >= 55)):
        ev.append(("o", f"Vento forte con neve trasportabile (700 hPa {v7:.0f} km/h da "
                        f"{card8(r['v700_dir'])}): accumuli sui versanti {sottovento(r['v700_dir'])}"))
    elif v7 >= 60:
        ev.append(("y", f"Vento in quota {v7:.0f} km/h da {card8(r['v700_dir'])}"))
    if zt > q + 300 and neve_c_e:
        ev.append(("y", f"Zero termico a {zt:.0f} m, sopra la quota {q} m: fusione"))
        if i + 1 < len(d) and _n(d.iloc[i + 1]["temperature_2m_min"], 0) < -1:
            ev.append(("b", "Notte seguente sotto zero: rigelo, crosta portante al mattino"))
    if i >= 1:
        dzt = zt - _n(d.iloc[i - 1]["zt_max"], zt)
        if dzt >= 1000 and neve_c_e:
            ev.append(("o", f"Rialzo termico brusco: zero termico +{dzt:.0f} m in 24 h"))
    nuv = _n(r["nuv_notte"], 100)
    if neve_c_e and nuv < 30 and tmin <= -8:
        ev.append(("y", f"Notte serena e fredda ({tmin:.0f} °C): brina di superficie / "
                        "neve che si sfaccetta, possibile strato debole se poi nevica"))
    return ev


def stato_zona(d, oggi):
    """Livello sintetico sugli ultimi 3 giorni e prossimi 2."""
    fin = d[(d["data"] >= oggi - timedelta(days=3)) & (d["data"] <= oggi + timedelta(days=2))]
    liv = [e[0] for ev in fin["eventi"] for e in ev]
    for l in ("r", "o", "y"):
        if l in liv:
            return l
    return "g"


ETI_LIV = {"r": "\U0001F534 attenzione alta", "o": "\U0001F7E0 marcato",
           "y": "\U0001F7E1 da seguire", "g": "\U0001F7E2 tranquillo", "b": "ℹ️"}


# ------------------------------------------------------------------ UI NEVE
def scheda_neve(card, kv):
    oggi = date.today()
    ini = inizio_stagione(oggi)
    st.markdown("#### ❄️ Manto nevoso per zona")
    st.caption(f"Stagione dal {ini:%d/%m/%Y}. Ogni zona è letta alla sua quota di riferimento "
               "con i modelli di Open-Meteo: neve fresca, pioggia, zero termico, vento al suolo "
               "e a 700 hPa (~3000 m), notti serene. Ultimi giorni = analisi del modello, "
               "prossimi 7 = previsione. Le stazioni ARPA-OSMER sono indicate per il confronto.")
    st.warning("È un diario meteo, NON un bollettino valanghe. Prima di uscire leggi il "
               "bollettino di ARPA FVG e quello AINEVA.", icon="⚠️")
    c1, c2, c3 = st.columns(3)
    c1.link_button("Bollettino neve e valanghe FVG", "https://www.meteo.fvg.it/neve.php",
                   width="stretch")
    c2.link_button("AINEVA bollettini", "https://bollettini.aineva.it/",
                   width="stretch")
    c3.link_button("Stazioni ARPA-OSMER", "https://www.meteo.fvg.it/",
                   width="stretch")
    try:
        with st.spinner("Scarico la stagione per 16 zone…"):
            raw = scarica_stagione(oggi.isoformat())
    except Exception as e:
        st.error(f"Open-Meteo non risponde ({e}). Riprova tra poco.")
        return
    tab = {z["id"]: tabella_zona(r, z["q"]) for z, r in zip(ZONE, raw)}

    # --- quadro riassuntivo
    righe = []
    for z in ZONE:
        d = tab[z["id"]]
        o = d[d["data"] == oggi]
        o = o.iloc[0] if len(o) else d.iloc[-1]
        pass7 = d[(d["data"] > oggi - timedelta(days=7)) & (d["data"] <= oggi)]
        fut = d[d["data"] > oggi]
        righe.append({
            "Zona": z["nome"], "Quota": z["q"],
            "Stato": ETI_LIV[stato_zona(d, oggi)],
            "Neve al suolo (mod.) cm": round(_n(o["neve_suolo"])),
            "Fresca 72h cm": round(_n(o["hn72"])),
            "Fresca 7 gg cm": round(pass7["snowfall_sum"].sum()),
            "Fresca stagione cm": round(d[d["data"] <= oggi]["snowfall_sum"].sum()),
            "Pioggia 7 gg mm": round(pass7["rain_sum"].sum()),
            "Zero term. oggi m": int(_n(o["zt_max"])),
            "Vento 700 oggi": f"{_n(o['v700_max']):.0f} {card8(o['v700_dir'])}",
            "Neve prossimi 7 gg cm": round(fut["snowfall_sum"].sum()),
        })
    st.dataframe(pd.DataFrame(righe), hide_index=True, width="stretch")
    st.caption("La neve al suolo è quella della cella del modello: in valli strette e "
               "versanti al sole può essere molto diversa dalla realtà. Le soglie sono "
               "indicative: neve 72 h ≥ 30 cm, pioggia su neve, vento 700 hPa ≥ 40 km/h "
               "con neve fresca, zero termico 300 m sopra la quota, notti serene ≤ −8 °C.")

    # --- dettaglio
    st.divider()
    nomi = [z["nome"] for z in ZONE]
    scelta = st.selectbox("Zona da guardare nel dettaglio", nomi, key="neve_zona")
    z = ZONE[nomi.index(scelta)]
    d = tab[z["id"]]
    lv = stato_zona(d, oggi)
    card(f"{z['nome']} · {z['q']} m", f"{z['note']}<br>Stazioni OSMER vicine: {z['osmer']} "
         f"(da verificare)<br>Punto: {z['lat']:.3f}, {z['lon']:.3f}", lv if lv != "g" else "g")
    idx = d.set_index(pd.to_datetime(d["data"]))
    st.markdown("**Neve fresca e pioggia (giornaliere)**")
    st.bar_chart(idx[["snowfall_sum", "rain_sum"]].rename(
        columns={"snowfall_sum": "neve cm", "rain_sum": "pioggia mm"}), height=220)
    st.markdown(f"**Zero termico (max e min del giorno) rispetto alla quota {z['q']} m**")
    zt = idx[["zt_max", "zt_min"]].rename(columns={"zt_max": "zero term. max",
                                                   "zt_min": "zero term. min"})
    zt["quota zona"] = z["q"]
    st.line_chart(zt, height=220)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Neve al suolo (modello, cm)**")
        st.area_chart(idx[["neve_suolo"]].rename(columns={"neve_suolo": "cm"}), height=180)
    with c2:
        st.markdown("**Vento: raffica al suolo e 700 hPa (km/h)**")
        st.line_chart(idx[["wind_gusts_10m_max", "v700_max"]].rename(
            columns={"wind_gusts_10m_max": "raffica", "v700_max": "700 hPa"}), height=180)

    st.markdown("**Diario della stagione**")
    for _, r in d.sort_values("data", ascending=False).iterrows():
        fut = r["data"] > oggi
        if not r["eventi"] and not fut and r["data"] < oggi - timedelta(days=14):
            continue
        testo = "<br>".join(f"{ETI_LIV[l].split()[0]} {t}" for l, t in r["eventi"]) \
                or "nessun evento rilevante"
        sotto = (f"neve {_n(r['snowfall_sum']):.0f} cm · pioggia {_n(r['rain_sum']):.0f} mm · "
                 f"T {_n(r['temperature_2m_min']):.0f}/{_n(r['temperature_2m_max']):.0f} °C · "
                 f"zero term. {_n(r['zt_min']):.0f}–{_n(r['zt_max']):.0f} m · "
                 f"raffica {_n(r['wind_gusts_10m_max']):.0f} km/h · 700 hPa "
                 f"{_n(r['v700_max']):.0f} da {card8(r['v700_dir'])}<br>{testo}")
        liv = max((e[0] for e in r["eventi"]), key="byor".find, default="n") \
            if r["eventi"] else "n"
        sfera = "\U0001F52E " if fut else ""
        card(sfera + f"{r['data']:%a %d/%m}" + (" · previsione" if fut else ""), sotto, liv)
    st.caption("I giorni senza eventi più vecchi di 2 settimane sono nascosti.")
    with st.expander("Tabella completa della zona"):
        st.dataframe(d.drop(columns=["eventi", "q"]), hide_index=True)
        st.download_button("Scarica CSV", d.drop(columns=["eventi"]).to_csv(index=False),
                           file_name=f"neve_{z['id']}_{oggi}.csv")


# ------------------------------------------------------------------ ROTTE
ROTTE = [
 dict(nome="Gemonese → Musi → Stol (verso est)", tipo="andata e ritorno ~60 km",
      punti=[("Cuarnan", 46.274, 13.176), ("Chiampon", 46.300, 13.215),
             ("Musi", 46.320, 13.280), ("Gran Monte", 46.290, 13.355),
             ("Stol", 46.280, 13.520)],
      vento="debole S–SW, 700 hPa < 20 km/h", periodo="mar–giu, base > 1800 m",
      ragiona="La linea delle Prealpi Giulie è esposta a sud e si accende presto. Sui Musi "
              "convergono la brezza della pianura e quella della Val Resia: lì la base sale ma "
              "è anche il primo posto dove la cumuli cresce e sovrasviluppa (convergenza OSMER). "
              "Il rientro verso ovest è contro la brezza di pianura del pomeriggio: si torna alti."),
 dict(nome="Gemona → Carnia → Zoncolan", tipo="andata e ritorno ~80 km",
      punti=[("San Simeone", 46.330, 13.102), ("Amariana", 46.405, 13.035),
             ("Tolmezzo", 46.400, 13.015), ("Arvenis", 46.480, 12.890),
             ("Zoncolan", 46.506, 12.932)],
      vento="S debole; evitare N in quota", periodo="apr–lug, dopo le 11",
      ragiona="Si entra in Carnia quando la base supera le creste (≥ 2000 m). La brezza di "
              "valle del Tagliamento nel pomeriggio è forte da S: spinge all'andata, frena al "
              "ritorno in basso. Con vento da N a 700 hPa la Carnia interna è sottovento delle "
              "Carniche: turbolenza e rotori, giornata da evitare."),
 dict(nome="Prealpi Carniche: Valinis → Raut → Piancavallo", tipo="andata e ritorno ~70 km",
      punti=[("Valinis (Meduno)", 46.231, 12.807), ("Monte Raut", 46.195, 12.660),
             ("Maniago", 46.177, 12.676), ("Piancavallo", 46.105, 12.520)],
      vento="S–SE debole", periodo="mar–giu",
      ragiona="Fronte prealpino esposto a sud, sopra la pianura: termica regolare e presto. "
              "Nel pomeriggio la brezza di mare entra e crea una linea di convergenza a ridosso "
              "dei rilievi (base più alta, ma anche dove partono i temporali). Valli trasversali "
              "(Cellina, Meduna) da passare alti per la brezza che le risale."),
 dict(nome="Triangolo Carnia nord: Zoncolan – Monte Croce – Pramollo", tipo="triangolo ~90 km",
      punti=[("Zoncolan", 46.506, 12.932), ("Paluzza", 46.533, 13.015),
             ("Paularo", 46.530, 13.120), ("Pramollo", 46.555, 13.280),
             ("Pontebba", 46.505, 13.305), ("Tolmezzo", 46.400, 13.015)],
      vento="debole variabile; NO nord, NO föhn", periodo="mag–ago",
      ragiona="Valli interne: partenza più tardi, ma base alta in estate. La dorsale di "
              "confine (Carniche) fa da barriera: con N in quota si forma föhn a sud e la zona "
              "diventa pericolosa. Verso Pramollo il confine con l'Austria; il lato austriaco "
              "(Gail) ha regime di brezze proprio."),
 dict(nome="Dolomiti Friulane: Forni → Mauria → Pura → Tolmezzo", tipo="lineare ~50 km",
      punti=[("Varmost (Forni di Sopra)", 46.430, 12.600), ("Passo Mauria", 46.452, 12.512),
             ("Passo Pura", 46.419, 12.748), ("Verzegnis", 46.390, 12.990),
             ("Tolmezzo", 46.400, 13.015)],
      vento="W–SW debole", periodo="giu–ago",
      ragiona="Alta Val Tagliamento: versanti sud del lato nord della valle lavorano bene. "
              "Spostandosi a est la valle si allarga e la brezza da S diventa forte. Atterraggi "
              "rari tra Forni e Ampezzo: tenere sempre la piana di Villa Santina in planata."),
]

KK7_STRATI = {
    "Skyways (tutte le stagioni)": "skyways_all_all",
    "Termiche (tutte le stagioni)": "thermals_all_all",
    "Termiche luglio, mattina": "thermals_jul_07",
}


def link_kk7(lat, lon, z=12):
    return f"https://thermal.kk7.ch/#{lat:.4f},{lon:.4f},{z},0,0,2"


@st.cache_data(ttl=3600, show_spinner=False)
def meteo_rotta(punti):
    """Per ogni punto della rotta, ore 11–16 dei prossimi 3 giorni: strato limite,
    vento 850/700 hPa, precipitazione."""
    p = {"latitude": ",".join(str(x[1]) for x in punti),
         "longitude": ",".join(str(x[2]) for x in punti),
         "timezone": "Europe/Rome", "forecast_days": 3, "wind_speed_unit": "kmh",
         "hourly": "boundary_layer_height,wind_speed_850hPa,wind_direction_850hPa,"
                   "wind_speed_700hPa,wind_direction_700hPa,precipitation,cloud_cover_low"}
    r = _json("https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(p))
    r = r if isinstance(r, list) else [r]
    fr = []
    for (nome, _, _), x in zip(punti, r):
        h = pd.DataFrame(x["hourly"]); h["t"] = pd.to_datetime(h["time"])
        h = h[(h["t"].dt.hour >= 11) & (h["t"].dt.hour <= 16)]
        h["giorno"] = h["t"].dt.date; h["punto"] = nome
        fr.append(h)
    return pd.concat(fr)


def verdetto_rotta(h):
    out = []
    for g, x in h.groupby("giorno"):
        blh = x["boundary_layer_height"].mean()
        v7 = x["wind_speed_700hPa"].max(); v8 = x["wind_speed_850hPa"].max()
        d7 = _dir_media(x["wind_speed_700hPa"], x["wind_direction_700hPa"])
        pr = x["precipitation"].sum(); nb = x["cloud_cover_low"].mean()
        nord = not pd.isna(d7) and (d7 >= 300 or d7 <= 60) and v7 >= 25
        if pr > 1 or v7 >= 35 or nord:
            l = "r"
        elif blh < 800 or v7 >= 25 or nb > 70:
            l = "y"
        else:
            l = "g"
        mot = []
        if nord: mot.append("vento da nord in quota: föhn/rotori a sud delle Carniche")
        if pr > 1: mot.append(f"pioggia {pr:.1f} mm")
        if v7 >= 25: mot.append(f"700 hPa fino a {v7:.0f} km/h da {card8(d7)}")
        if blh < 800: mot.append(f"strato limite basso (~{blh:.0f} m sul suolo)")
        if nb > 70: mot.append("nuvole basse")
        out.append((g, l, blh, v8, v7, d7, ", ".join(mot) or "niente di ostativo nel modello"))
    return out


def mappa_kk7(strati, rotte, siti, h=520):
    feats = []
    for r in rotte:
        feats.append({"nome": r["nome"], "pts": [[p[1], p[2], p[0]] for p in r["punti"]]})
    js = json.dumps({"strati": strati, "rotte": feats, "siti": siti, "src": HOST_APP})
    html = """
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<div id="m" style="height:%dpx;border-radius:12px"></div>
<script>
const D = %s;
const m = L.map('m').setView([46.38, 13.0], 9);
const topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
  {maxZoom:16, attribution:'© OpenTopoMap, © OpenStreetMap'}).addTo(m);
const osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
  {maxZoom:18, attribution:'© OpenStreetMap'});
const over = {};
for (const [eti, nome] of Object.entries(D.strati)) {
  const maxN = nome.startsWith('skyways') ? 13 : 12;
  over[eti] = L.tileLayer('https://thermal.kk7.ch/tiles/' + nome + '/{z}/{x}/{y}.png?src=' + D.src,
    {tms:true, maxNativeZoom:maxN, maxZoom:16, opacity:0.75,
     attribution:'thermal.kk7.ch (CC BY-NC-SA 4.0)'});
}
const first = Object.keys(over)[0]; if (first) over[first].addTo(m);
const col = ['#e2741c','#3c91e6','#22a046','#cc2b2b','#8e44ad','#e0a500'];
const gR = L.layerGroup().addTo(m);
D.rotte.forEach((r,i) => {
  const ll = r.pts.map(p => [p[0], p[1]]);
  L.polyline(ll, {color: col[i %% col.length], weight: 4, opacity: .9}).bindTooltip(r.nome).addTo(gR);
  r.pts.forEach(p => L.circleMarker([p[0],p[1]], {radius:4, color: col[i %% col.length]})
     .bindTooltip(p[2]).addTo(gR));
});
const gS = L.layerGroup().addTo(m);
D.siti.forEach(s => L.marker([s[0], s[1]]).bindPopup('<b>'+s[2]+'</b><br>'+(s[3]||'')).addTo(gS));
over['Rotte'] = gR; over['Decolli'] = gS;
L.control.layers({'Topo': topo, 'OSM': osm}, over, {collapsed:false}).addTo(m);
</script>""" % (h, js)
    components.html(html, height=h + 10)


def scheda_rotte(card, kv, df_siti=None):
    st.markdown("#### \U0001F9ED Rotte di volo")
    st.caption("Mappe di thermal.kk7.ch (Michael von Känel): skyways = dove passano davvero "
               "i voli registrati; termiche = punti di salita frequenti. Licenza CC BY-NC-SA 4.0, "
               "uso non commerciale. Sopra ci sono le prime ipotesi di rotta da verificare.")
    sel = st.multiselect("Strati kk7", list(KK7_STRATI), default=list(KK7_STRATI)[:1],
                         key="kk7_strati")
    rot = st.multiselect("Rotte da disegnare", [r["nome"] for r in ROTTE],
                         default=[r["nome"] for r in ROTTE], key="kk7_rotte")
    siti = []
    if df_siti is not None and len(df_siti):
        x = df_siti[(df_siti["tipo"].isin(["decollo", "hike&fly"])) &
                    df_siti["lat"].between(45.9, 46.75) & df_siti["lon"].between(12.3, 13.9)]
        siti = [[float(r.lat), float(r.lon), str(r.nome), str(r.vento or "")]
                for r in x.itertuples()]
    mappa_kk7({k: KK7_STRATI[k] for k in sel},
              [r for r in ROTTE if r["nome"] in rot], siti)
    st.caption("Se uno strato non compare, il nome del tile non è quello giusto: si apre "
               "la mappa completa su kk7 con i pulsanti qui sotto (filtri per mese e ora).")
    cols = st.columns(4)
    for i, z in enumerate(ZONE):
        cols[i % 4].link_button(z["nome"].replace("Carnia — ", ""), link_kk7(z["lat"], z["lon"]),
                                width="stretch")

    st.divider()
    st.markdown("#### Come leggere kk7 per costruire una rotta")
    for t, s in [
        ("1. Le skyways sono strade, non garanzie",
         "Una linea spessa vuol dire che tanti piloti sono passati di lì: è la traccia del "
         "percorso che funziona in media. Non dice se funziona OGGI. Si usa per scegliere "
         "dove andare, il meteo del giorno dice se andarci."),
        ("2. Filtra per mese e ora",
         "Su kk7 il filtro del mese (±2) e la fascia mattina/mezzogiorno/sera cambiano molto "
         "la mappa: in primavera si accendono prima le Prealpi esposte a sud, d'estate le "
         "valli interne della Carnia."),
        ("3. Hotspot = punti di innesco",
         "Gli hotspot sono le termiche più ricorrenti: costole, paesi al sole, cambi di "
         "pendenza. Sulla rotta sono le 'stazioni di servizio' dove cercare la salita quando "
         "si è bassi."),
        ("4. Incrocia con il meteo FVG",
         "Brezza di mare nel pomeriggio = convergenza sulle Prealpi (Virgilio, Nordio). "
         "Nord in quota = föhn e rotori a sud della dorsale di confine. Bora = est forte "
         "e turbolento sul Carso e sulle Prealpi Giulie. Strato limite basso = termiche "
         "corte, si resta sulla prima linea."),
    ]:
        card(t, s, "b")

    st.divider()
    st.markdown("#### Ipotesi di rotta e prossimi 3 giorni")
    st.caption("Per ogni rotta: modello Open-Meteo sui punti della rotta, ore 11–16. "
               "Verde = niente di ostativo, giallo = limitante, rosso = no.")
    for r in ROTTE:
        with st.expander(f"{r['nome']} · {r['tipo']}"):
            kv([("Vento adatto", r["vento"]), ("Periodo", r["periodo"]),
                ("Punti", " → ".join(p[0] for p in r["punti"]))])
            st.write(r["ragiona"])
            st.link_button("Apri su thermal.kk7", link_kk7(r["punti"][0][1], r["punti"][0][2], 11))
            try:
                h = meteo_rotta(tuple(r["punti"]))
                for g, l, blh, v8, v7, d7, mot in verdetto_rotta(h):
                    card(f"{g:%a %d/%m}", f"strato limite ~{blh:.0f} m · 850 hPa max {v8:.0f} · "
                         f"700 hPa max {v7:.0f} km/h da {card8(d7)}<br>{mot}", l)
            except Exception as e:
                st.caption(f"Meteo della rotta non disponibile ({e}).")
    st.caption("Le rotte sono un punto di partenza da discutere: vanno confrontate con le "
               "tracce reali (XContest, kk7) e con chi le vola.")


# ------------------------------------------------------------------ DOCUMENTI
DRIVE = "https://docs.google.com/document/d/"
DOC_PROGETTO = [
    ("Bignami meteo FVG e volo", DRIVE + "1bsVMA3b4VeUDOSNH6E7BydYBeUIVnasC7kjfYaFpArA"),
    ("Bibliografia ragionata v2", DRIVE + "1hwr6PAHeUvNFyB3fg6CahcDyf6OVanE7p3MKx2YtVso"),
    ("Indice del progetto", DRIVE + "1oXhyOR1wiXUM2hS7VBY1O0C3S7An_qPkF1EeiUgc0Sc"),
    ("Trascrizione conferenza Virgilio", DRIVE + "1kAKH1n0NDCytpAdhy1BGmN5TxpvGK88qkz7LlG-yamw"),
]


def scheda_documenti(card):
    st.markdown("#### \U0001F4DA Documenti meteo FVG e volo")
    st.caption("Documenti del progetto su Drive (2.16 - METEO FVG) e bibliografia. "
               "✅ = PDF scaricato (nome file indicato) · ❌ = non scaricabile · \U0001F517 = solo pagina web "
               "(articolo HTML, a pagamento o da acquistare).")
    for t, u in DOC_PROGETTO:
        st.markdown(f"- [{t}]({u})")
    try:
        import os
        docs = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           "documenti.json"), encoding="utf-8"))
    except Exception:
        docs = []
    for sez in dict.fromkeys(d["sez"] for d in docs):
        with st.expander(sez or "Altro"):
            for d in [x for x in docs if x["sez"] == sez]:
                ic = "✅" if d.get("scaricato") else "❌" if d.get("errore") else "\U0001F517"
                extra = f" — *{d['errore']}*" if d.get("errore") else \
                        (f" — `{d['file']}`" if d.get("file") else "")
                st.markdown(f"{ic} [{d['desc'][:160]}]({d['url']}){extra}")
