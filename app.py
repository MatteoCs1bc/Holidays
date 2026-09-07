# -*- coding: utf-8 -*-
import json, math, os
import pandas as pd
import streamlit as st
import pydeck as pdk
from curati import GIORNI, TAPPE, COSTI, COORD_TAPPE, MATERIALE, FONTI, GITE

st.set_page_config(page_title="Viaggio set 2026", page_icon="🪂", layout="centered")
BASE = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def carica():
    with open(os.path.join(BASE, "siti.json"), encoding="utf-8") as f:
        return pd.DataFrame(json.load(f))

df = carica()

# Gli stessi numeri RGB vanno sulla mappa E nella legenda: non possono divergere.
STILI = {
    "decollo":     dict(rgb=[230,  57,  70], eti="Decollo ufficiale"),
    "hike&fly":    dict(rgb=[255, 183,   3], eti="Hike & Fly"),
    "atterraggio": dict(rgb=[ 42, 157, 143], eti="Atterraggio"),
    "cima":        dict(rgb=[ 38,  70,  83], eti="Cima"),
    "rifugio":     dict(rgb=[231, 111,  81], eti="Rifugio"),
    "parcheggio":  dict(rgb=[168, 162, 158], eti="Parcheggio"),
    "impianto":    dict(rgb=[157,  78, 221], eti="Impianto"),
    "zona":        dict(rgb=[  0,   0,   0], eti="Zona / regola"),
    "logistica":   dict(rgb=[  0, 119, 255], eti="Logistica"),
}
GRIGIO = [136, 136, 136]
CAMPI_TESTO = ["nome", "note", "vento", "difficolta", "partenza", "categoria", "fonte", "zona"]

def rgb(t):  return STILI.get(t, {}).get("rgb", GRIGIO)
def hexa(t): return "#%02x%02x%02x" % tuple(rgb(t))
def eti(t):  return STILI.get(t, {}).get("eti", t)

def dist_km(la1, lo1, la2, lo2):
    return math.hypot((la1 - la2) * 111,
                      (lo1 - lo2) * 111 * math.cos(math.radians((la1 + la2) / 2)))

def val(r, c):
    v = r[c] if c in r.index else None
    return "" if v is None or (isinstance(v, float) and pd.isna(v)) else v

def riassunto(r):
    p = []
    if val(r, "quota"): p.append(f"{int(r['quota'])} m")
    if val(r, "vento"): p.append(f"🧭 {r['vento']}")
    if val(r, "disl"):  p.append(f"↗ {int(r['disl'])} m")
    if val(r, "difficolta"): p.append(str(r["difficolta"])[:34])
    return " · ".join(p)

def pallino(t):
    return (f"<span style='display:inline-block;width:11px;height:11px;border-radius:50%;"
            f"background:{hexa(t)};border:1px solid #bbb;margin-right:6px'></span>")

def scheda(r):
    st.markdown(pallino(r["tipo"]) + f"<b>{r['nome']}</b> <small>· {eti(r['tipo'])}</small>",
                unsafe_allow_html=True)
    riga = riassunto(r)
    if riga: st.markdown(f"**{riga}**")
    if val(r, "partenza"):  st.markdown(f"**Partenza:** {r['partenza']}")
    if val(r, "categoria"): st.caption(r["categoria"])
    if val(r, "note"):      st.write(r["note"])
    aff = {"V": "✅ verificato", "L": "🧑 da un pilota che c'è stato",
           "K": "🟡 solo KML", "?": "❓ da verificare"}.get(val(r, "aff"), "")
    st.caption(f"{aff} — fonte: {val(r,'fonte')}  ·  `{r['lat']:.5f}, {r['lon']:.5f}`")
    st.markdown(
        f"[Google Maps](https://www.google.com/maps/search/?api=1&query={r['lat']},{r['lon']}) · "
        f"[Organic Maps](om://map?v=1&ll={r['lat']},{r['lon']}&n={r['nome']}) · "
        f"[meteo-parapente](https://meteo-parapente.com/#/{r['lat']},{r['lon']},11)")

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### Filtri")
    zone = sorted(df["zona"].unique())
    z_sel = st.multiselect("Zona", zone, default=zone)
    tipi = sorted(df["tipo"].unique())
    dflt = [t for t in ["decollo", "hike&fly", "cima", "atterraggio", "zona", "rifugio", "logistica"]
            if t in tipi]
    t_sel = st.multiselect("Tipo", tipi, default=dflt, format_func=eti)
    solo_note = st.checkbox("Solo punti con note vere", value=True)
    st.markdown("---")
    disl_max = st.slider("Dislivello massimo a piedi (m)", 400, 2600, 2400, 100)
    st.caption("Cross ≤1200 · Alpinismo ≤2400")
    st.markdown("---")
    pos = st.text_input("La tua posizione — lat, lon", placeholder="46.65, 8.27")

sel = df[df["zona"].isin(z_sel) & df["tipo"].isin(t_sel)].copy()
if solo_note:
    sel = sel[(sel["origine"] == "curato") | (sel["note"].astype(str).str.len() > 20)]

qui = None
if pos.strip():
    try:
        a, b = [float(x) for x in pos.replace(";", ",").split(",")[:2]]
        qui = (a, b)
        if len(sel):
            sel["dist"] = [dist_km(a, b, la, lo) for la, lo in zip(sel["lat"], sel["lon"])]
            sel = sel.sort_values("dist")
    except Exception:
        st.sidebar.error("Formato: 46.65, 8.27")
sel = sel.reset_index(drop=True)

t1, t2, t3, t4, t5, t6, t7 = st.tabs(
    ["🗺️ Mappa", "📋 Elenco", "🥾 Gite", "📅 Giorni", "🚗 Viaggio", "🌤️ Meteo", "🔧 Info"])

# ---------------------------------------------------------------- mappa
with t1:
    st.caption(f"{len(sel)} punti — tocca un punto per aprirne la scheda")
    m = sel.dropna(subset=["lat", "lon"]).copy()
    if len(m):
        m["col"] = [rgb(t) for t in m["tipo"]]
        m["rad"] = [{"cima": 420, "decollo": 380, "hike&fly": 380,
                     "zona": 460}.get(t, 240) for t in m["tipo"]]
        m["etichetta"] = [eti(t) for t in m["tipo"]]
        m["sotto"] = [riassunto(r) or "—" for _, r in m.iterrows()]

        livelli = [pdk.Layer(
            "ScatterplotLayer", data=m[["lat", "lon", "col", "rad", "nome", "etichetta", "sotto"]],
            get_position=["lon", "lat"], get_fill_color="col", get_radius="rad",
            radius_min_pixels=6, radius_max_pixels=20, pickable=True, auto_highlight=True,
            stroked=True, get_line_color=[255, 255, 255], line_width_min_pixels=1)]
        if qui:
            livelli.append(pdk.Layer(
                "ScatterplotLayer",
                data=pd.DataFrame([{"lat": qui[0], "lon": qui[1]}]),
                get_position=["lon", "lat"], get_fill_color=[0, 119, 255],
                get_radius=700, radius_min_pixels=9, pickable=False))

        ev = st.pydeck_chart(
            pdk.Deck(layers=livelli, map_style=None,
                     initial_view_state=pdk.ViewState(
                         latitude=float(m["lat"].mean()), longitude=float(m["lon"].mean()),
                         zoom=5 if len(z_sel) > 2 else 9),
                     tooltip={"html": "<b>{nome}</b><br/>{etichetta}<br/>{sotto}"}),
            on_select="rerun", selection_mode="single-object", key="mappa")

        scelto = None
        try:
            for _, lista in (ev.selection.get("objects") or {}).items():
                if lista:
                    scelto = lista[0]
                    break
        except Exception:
            pass
        st.divider()
        if scelto and scelto.get("nome"):
            r = m[m["nome"] == scelto["nome"]]
            if len(r):
                scheda(r.iloc[0])
        else:
            st.caption("Nessun punto selezionato. Tocca un pallino sulla mappa.")
    else:
        st.info("Nessun punto con questi filtri.")

    st.divider()
    st.markdown("**Legenda**")
    presenti = [t for t in STILI if t in set(sel["tipo"])] or list(STILI)
    cols = st.columns(3)
    for i, t in enumerate(presenti):
        cols[i % 3].markdown(pallino(t) + f"<small>{eti(t)}</small>", unsafe_allow_html=True)

# ---------------------------------------------------------------- elenco
with t2:
    q = st.text_input("Cerca", placeholder="lorenzo, crepaccia, rotore, navetta, cavi, doppia...")
    vis = sel
    if q and len(vis):
        ql = q.lower()
        vis = vis[[any(ql in str(r[c]).lower() for c in CAMPI_TESTO if c in vis.columns)
                   for _, r in vis.iterrows()]]
    if len(vis):
        vis = vis[vis["disl"].isna() | (vis["disl"] <= disl_max)]
    st.caption(f"{len(vis)} risultati")
    for zona in sorted(vis["zona"].unique()):
        st.markdown(f"#### {zona}")
        for _, r in vis[vis["zona"] == zona].iterrows():
            coda = riassunto(r)
            if "dist" in r.index and pd.notna(r["dist"]):
                coda = (coda + " · " if coda else "") + f"{r['dist']:.0f} km"
            with st.expander(f"{r['nome']}" + (f"  ·  {coda}" if coda else "")):
                scheda(r)

# ---------------------------------------------------------------- gite
with t3:
    cats = sorted({g["cat"] for g in GITE})
    cat = st.multiselect("Categoria", cats, default=cats)
    gz = [g for g in GITE if g["cat"] in cat and g["zona"] in z_sel
          and (not g["disl"] or g["disl"] <= disl_max)]
    st.caption(f"{len(gz)} gite")
    for g in gz:
        meta = [g["zona"], g["cat"]]
        if g["disl"]: meta.append(f"↗ {g['disl']} m")
        if g["ore"]:  meta.append(g["ore"])
        with st.expander(f"{g['nome']}  ·  {g['giorni']}"):
            st.caption(" · ".join(meta))
            st.write(g["testo"])
            st.markdown("**Punti collegati**")
            for p in g["punti"]:
                riga = df[df["nome"] == p]
                if len(riga):
                    r = riga.iloc[0]
                    st.markdown(
                        pallino(r["tipo"]) +
                        f"**{r['nome']}** <small>{eti(r['tipo'])}</small> — {riassunto(r)} "
                        f"<a href='https://www.google.com/maps/search/?api=1"
                        f"&query={r['lat']},{r['lon']}'>↗</a>", unsafe_allow_html=True)
                else:
                    st.markdown(f"• {p}")

# ---------------------------------------------------------------- giorni
with t4:
    for giorno, zona, nota in GIORNI:
        st.markdown(f"**{giorno}** — {zona if zona else '—'}")
        if nota: st.caption(nota)
        gg = [g["nome"] for g in GITE if giorno in g["giorni"]]
        if gg:
            st.markdown(" ".join(f"🥾 {x}  " for x in gg))
    st.markdown("---")
    st.caption("Gli spostamenti sono nel tab Viaggio.")

# ---------------------------------------------------------------- viaggio
with t5:
    tipi_t = ["base", "locale", "opzionale"]
    nomi_t = {"base": "Giro principale", "locale": "Spostamenti in zona",
              "opzionale": "Deviazioni possibili"}
    scelti = st.multiselect("Cosa conteggiare", tipi_t, default=["base", "locale"],
                            format_func=lambda x: nomi_t[x])
    ar = st.checkbox("Conta gli spostamenti in zona andata e ritorno", value=True)

    def km_eff(t):
        return t["km"] * 2 if (ar and t["tipo"] == "locale") else t["km"]

    att = [t for t in TAPPE if t["tipo"] in scelti]
    tot_km = sum(km_eff(t) for t in att)
    tot_ore = sum(t["ore"] * (2 if (ar and t["tipo"] == "locale") else 1) for t in att)

    c1, c2, c3 = st.columns(3)
    c1.metric("Chilometri", f"{tot_km:,.0f}".replace(",", "."))
    c2.metric("Ore di guida", f"{tot_ore:.1f}")
    c3.metric("Tappe", len(att))

    st.markdown("---")
    st.markdown("#### Mappa degli spostamenti")

    COL_T = {"base": [200, 30, 45], "locale": [42, 157, 143], "opzionale": [245, 158, 11]}
    seg = []
    for t in att:
        a, b = COORD_TAPPE.get(t["da"]), COORD_TAPPE.get(t["a"])
        if not a or not b:
            continue
        seg.append(dict(da=t["da"], a_=t["a"], tipo=t["tipo"], g=t["g"], km=km_eff(t),
                        lat1=a[0], lon1=a[1], lat2=b[0], lon2=b[1],
                        col=COL_T[t["tipo"]],
                        larg={"base": 5, "locale": 3, "opzionale": 2}[t["tipo"]],
                        eti=f"{t['da']} → {t['a']}"))
    if seg:
        S = pd.DataFrame(seg)
        nodi = {}
        for t in att:
            for k in (t["da"], t["a"]):
                c = COORD_TAPPE.get(k)
                if c:
                    nodi.setdefault(k, dict(nome=k, lat=c[0], lon=c[1], base=False))
                    if t["tipo"] == "base":
                        nodi[k]["base"] = True
        N = pd.DataFrame(nodi.values())
        N["col"] = [[200, 30, 45] if b else [90, 90, 90] for b in N["base"]]
        N["rad"] = [7000 if b else 3500 for b in N["base"]]

        livelli_v = []
        dritte = S[S["tipo"] != "opzionale"]
        if len(dritte):
            livelli_v.append(pdk.Layer(
                "LineLayer", data=dritte,
                get_source_position=["lon1", "lat1"], get_target_position=["lon2", "lat2"],
                get_color="col", get_width="larg", width_min_pixels=2,
                pickable=True, auto_highlight=True))
        archi = S[S["tipo"] == "opzionale"]
        if len(archi):
            livelli_v.append(pdk.Layer(
                "ArcLayer", data=archi,
                get_source_position=["lon1", "lat1"], get_target_position=["lon2", "lat2"],
                get_source_color=[245, 158, 11], get_target_color=[245, 158, 11],
                get_width=2, get_height=0.35, pickable=True, auto_highlight=True))
        livelli_v.append(pdk.Layer(
            "ScatterplotLayer", data=N,
            get_position=["lon", "lat"], get_fill_color="col", get_radius="rad",
            radius_min_pixels=5, radius_max_pixels=14, pickable=True,
            stroked=True, get_line_color=[255, 255, 255], line_width_min_pixels=1))
        livelli_v.append(pdk.Layer(
            "TextLayer", data=N, get_position=["lon", "lat"], get_text="nome",
            get_size=12, get_color=[40, 40, 40], get_alignment_baseline="'top'",
            get_pixel_offset=[0, 10], size_units="'pixels'"))

        st.pydeck_chart(pdk.Deck(
            layers=livelli_v, map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=float(N["lat"].mean()), longitude=float(N["lon"].mean()), zoom=5.6),
            tooltip={"html": "<b>{eti}</b><br/>{g} · {km} km"}))

        lg = st.columns(3)
        for i, (k, v) in enumerate(COL_T.items()):
            if k in scelti:
                lg[i % 3].markdown(
                    f"<span style='display:inline-block;width:22px;height:4px;"
                    f"background:rgb({v[0]},{v[1]},{v[2]});vertical-align:middle;"
                    f"margin-right:6px'></span><small>{nomi_t[k]}</small>",
                    unsafe_allow_html=True)
        st.caption("Le deviazioni sono disegnate ad arco. Le linee sono in linea d'aria, "
                   "i chilometri in tabella sono quelli reali su strada.")
    else:
        st.info("Seleziona almeno una categoria di spostamenti.")

    st.markdown("---")
    st.markdown("#### Costo indicativo")
    k1, k2 = st.columns(2)
    cons = k1.number_input("Consumo l/100 km", 4.0, 20.0, float(COSTI["consumo"]), 0.5)
    prezzo = k2.number_input("€/litro", 1.0, 3.0, float(COSTI["prezzo_gasolio"]), 0.05)
    carb = tot_km / 100 * cons * prezzo
    vign = COSTI["vignetta_chf"] * 1.05 + COSTI.get("vignetta_at", 0)
    ped = COSTI["pedaggi_stimati"]
    d1, d2, d3, d4 = st.columns(4)
    d1.metric("Carburante", f"{carb:.0f} €")
    d2.metric("Vignette", f"{vign:.0f} €")
    d3.metric("Pedaggi", f"{ped:.0f} €")
    d4.metric("Totale", f"{carb + vign + ped:.0f} €")
    st.caption(COSTI["nota"])

    st.markdown("---")
    st.markdown("#### Tappe")
    tab = pd.DataFrame([{
        "Giorno": t["g"], "Da": t["da"], "A": t["a"],
        "km": km_eff(t),
        "ore": round(t["ore"] * (2 if (ar and t["tipo"] == "locale") else 1), 1),
        "Tipo": nomi_t[t["tipo"]],
    } for t in att])
    st.dataframe(tab, hide_index=True)

    st.markdown("#### Note per tappa")
    for t in att:
        if t["nota"]:
            with st.expander(f"{t['g']} · {t['da']} → {t['a']}  ·  {km_eff(t)} km"):
                st.write(t["nota"])
                st.markdown(
                    "[Percorso su Google Maps](https://www.google.com/maps/dir/?api=1"
                    f"&origin={t['da'].replace(' ', '+')}"
                    f"&destination={t['a'].replace(' ', '+')})")

    st.markdown("---")
    st.markdown("#### Chilometri accumulati")
    base_ord = [t for t in TAPPE if t["tipo"] == "base"]
    cum, acc = [], 0
    for t in base_ord:
        acc += t["km"]
        cum.append({"tappa": t["a"], "km": acc})
    st.line_chart(pd.DataFrame(cum).set_index("tappa"))
    st.caption(f"Solo il giro principale: {sum(t['km'] for t in base_ord)} km. "
               "Gli spostamenti in zona e le deviazioni si aggiungono a questi.")

    st.markdown("---")
    st.markdown("#### Se aggiungi una deviazione")
    for t in TAPPE:
        if t["tipo"] == "opzionale":
            st.markdown(f"**{t['da']} → {t['a']}** — {t['km']} km sola andata, "
                        f"{t['km']*2} km a/r, ~{t['ore']*2:.1f} h totali")
    st.caption("La Dibona da sola costa 220 km e 4 ore di guida: con tre giorni negli Écrins "
               "esclude la Barre.")

# ---------------------------------------------------------------- meteo
PUNTI_METEO = {
    "Gemona del Friuli": (46.28, 13.14),
    "Appenzell / Alpstein": (47.28, 9.35),
    "Rigi / Svizzera centrale": (47.05, 8.48),
    "Interlaken / Oberland": (46.69, 7.86),
    "Annecy": (45.90, 6.13),
    "Saint-Hilaire": (45.31, 5.89),
    "Briançon / Écrins": (44.90, 6.45),
}

@st.cache_data(ttl=1800, show_spinner=False)
def meteo(la, lo):
    import urllib.request, urllib.parse
    p = urllib.parse.urlencode({
        "latitude": la, "longitude": lo, "timezone": "auto", "forecast_days": 16,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,"
                 "precipitation_probability_max,windspeed_10m_max",
        "hourly": "windspeed_700hPa,winddirection_700hPa,freezing_level_height,cloudcover",
    })
    with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?" + p, timeout=20) as f:
        return json.load(f)

def cardinale(v):
    pts = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return pts[int((v % 360) / 22.5 + 0.5) % 16] if pd.notna(v) else "—"

with t6:
    st.caption("Il vento a 700 hPa (~3000 m) è il gradiente che decide se voli. "
               "Lo zero termico serve per i ghiacciai. Medie della fascia 12-16.")
    modo = st.radio("Vista", ["Windy", "Una località, 16 giorni", "Confronto fra tutte, un giorno"],
                    horizontal=True, label_visibility="collapsed")

    if modo == "Windy":
        import streamlit.components.v1 as components
        LIVELLI = {
            "Superficie (10 m)": "surface",
            "850 hPa (~1500 m)": "850h",
            "700 hPa (~3000 m)": "700h",
            "600 hPa (~4200 m)": "600h",
            "500 hPa (~5500 m)": "500h",
        }
        STRATI = {
            "Vento": "wind", "Raffiche": "gust", "Nuvole": "clouds", "Pioggia": "rain",
            "Temperatura": "temp", "CAPE (instabilità)": "cape",
            "Neve fresca": "snowAccu", "Isoterma zero": "deg0",
        }
        c1, c2 = st.columns(2)
        luogo = c1.selectbox("Centro mappa", list(PUNTI_METEO), key="windy_loc")
        strato = c2.selectbox("Strato", list(STRATI), key="windy_ov")
        liv = st.select_slider("Quota", list(LIVELLI), value="700 hPa (~3000 m)")
        wla, wlo = PUNTI_METEO[luogo]
        url = (f"https://embed.windy.com/embed2.html?lat={wla}&lon={wlo}"
               f"&detailLat={wla}&detailLon={wlo}&zoom=8"
               f"&level={LIVELLI[liv]}&overlay={STRATI[strato]}"
               "&product=ecmwf&menu=&message=true&marker=true&calendar=now"
               "&pressure=&type=map&location=coordinates&detail=true"
               "&metricWind=km%2Fh&metricTemp=%C2%B0C&radarRange=-1")
        components.iframe(url, height=520, scrolling=False)
        st.caption("Modello ECMWF. Il livello **700 hPa** è il gradiente che decide la giornata; "
                   "**isoterma zero** e **neve fresca** servono per i ghiacciai degli Écrins.")
        st.markdown(
            f"[Apri a schermo intero su windy.com](https://www.windy.com/{wla}/{wlo}"
            f"?{STRATI[strato]},{wla},{wlo},8) · "
            f"[meteo-parapente](https://meteo-parapente.com/#/{wla},{wlo},11)")
        with st.expander("I vincoli di vento sito per sito"):
            st.markdown("- **Ebenalp** — con W forte: pericolo di rotore")
            st.markdown("- **Kronberg** — nessuno: 4 decolli coprono tutte le direzioni")
            st.markdown("- **Säntis** — solo W-SW **deboli**, e non si parte dalla funivia")
            st.markdown("- **Rigi Staffelhöhe** — dalle 14 a sera; con bise vai a Rigi Scheidegg (NE)")
            st.markdown("- **Rotenflue** — non ideale con W; quota massima 2750 m (aerovia A9)")
            st.markdown("- **Schynige Platte** — no con vento di valle a Lehn, no con NW, "
                        "no con bise forte")
            st.markdown("- **Saint-Hilaire** — attenzione al vento da sud; **tetto 3000 m** "
                        "(aeroporto di Lione)")
            st.markdown("- **Dôme / Roche Faurio** — si decolla presto: la neve troppo scaldata "
                        "fa sprofondare mentre corri")
        st.stop()

    if modo.startswith("Confronto"):
        try:
            righe = []
            for nome, (a, b) in PUNTI_METEO.items():
                d = meteo(a, b)
                dd = pd.DataFrame(d["daily"]); dd["time"] = pd.to_datetime(dd["time"])
                hh = pd.DataFrame(d["hourly"]); hh["time"] = pd.to_datetime(hh["time"])
                h = hh[hh["time"].dt.hour.between(12, 16)].copy(); h["g"] = h["time"].dt.date
                ag = h.groupby("g").agg(v700=("windspeed_700hPa", "mean"),
                                        d700=("winddirection_700hPa", "mean"),
                                        zt=("freezing_level_height", "mean")).reset_index()
                dd["g"] = dd["time"].dt.date
                for _, x in dd.merge(ag, on="g", how="left").iterrows():
                    righe.append(dict(Localita=nome, g=x["g"],
                                      tmax=x["temperature_2m_max"],
                                      pioggia=x["precipitation_probability_max"],
                                      v700=x["v700"], d700=x["d700"], zt=x["zt"]))
            R = pd.DataFrame(righe)
            giorni_d = sorted(R["g"].unique())
            gsel = st.select_slider("Giorno", giorni_d, value=giorni_d[0],
                                    format_func=lambda d: d.strftime("%a %d/%m"))
            q = R[R["g"] == gsel].copy()
            st.dataframe(pd.DataFrame({
                "Località": q["Localita"],
                "Max": [f"{v:.0f}°" for v in q["tmax"]],
                "Pioggia": [f"{v:.0f}%" for v in q["pioggia"].fillna(0)],
                "Vento 700hPa": [f"{v:.0f} km/h {cardinale(x)}" if pd.notna(v) else "—"
                                 for v, x in zip(q["v700"], q["d700"])],
                "Zero term.": [f"{z:.0f} m" if pd.notna(z) else "—" for z in q["zt"]],
            }), hide_index=True)
            st.caption("Il gradiente piu debole e quasi sempre la localita dove si vola meglio.")
        except Exception as e:
            st.warning("Non riesco a raggiungere Open-Meteo adesso.")
            st.caption(f"({type(e).__name__}) Serve connessione internet.")
        st.stop()

    scelta = st.selectbox("Località", list(PUNTI_METEO))
    la, lo = PUNTI_METEO[scelta]
    try:
        d = meteo(la, lo)
        dd = pd.DataFrame(d["daily"]); dd["time"] = pd.to_datetime(dd["time"])
        hh = pd.DataFrame(d["hourly"]); hh["time"] = pd.to_datetime(hh["time"])
        h = hh[hh["time"].dt.hour.between(12, 16)].copy()
        h["g"] = h["time"].dt.date
        agg = h.groupby("g").agg(v700=("windspeed_700hPa", "mean"),
                                 d700=("winddirection_700hPa", "mean"),
                                 zt=("freezing_level_height", "mean"),
                                 nuv=("cloudcover", "mean")).reset_index()
        dd["g"] = dd["time"].dt.date
        t = dd.merge(agg, on="g", how="left")

        st.dataframe(pd.DataFrame({
            "Giorno": t["time"].dt.strftime("%a %d/%m"),
            "Min/Max": [f"{a:.0f}/{b:.0f}°" for a, b in
                        zip(t["temperature_2m_min"], t["temperature_2m_max"])],
            "Pioggia": [f"{p:.0f}% · {s:.0f}mm" for p, s in
                        zip(t["precipitation_probability_max"].fillna(0),
                            t["precipitation_sum"].fillna(0))],
            "Vento 700hPa": [f"{v:.0f} km/h {cardinale(x)}" if pd.notna(v) else "—"
                             for v, x in zip(t["v700"], t["d700"])],
            "Zero term.": [f"{z:.0f} m" if pd.notna(z) else "—" for z in t["zt"]],
            "Nuvole": [f"{n:.0f}%" if pd.notna(n) else "—" for n in t["nuv"]],
        }), hide_index=True)

        g = t[["time", "v700"]].dropna().set_index("time")
        if len(g):
            g.columns = ["vento 700 hPa km/h"]
            st.line_chart(g)
            st.caption("Sopra i 25-30 km/h a 700 hPa i decolli esposti diventano difficili.")
        with st.expander("I vincoli di vento sito per sito"):
            st.markdown("- **Ebenalp** — con W forte: pericolo di rotore")
            st.markdown("- **Kronberg** — nessuno: 4 decolli coprono tutte le direzioni")
            st.markdown("- **Säntis** — solo W-SW **deboli**, e non si parte dalla funivia")
            st.markdown("- **Rigi Staffelhöhe** — dalle 14 a sera; con bise vai a Rigi Scheidegg (NE)")
            st.markdown("- **Rotenflue** — non ideale con W; quota massima 2750 m (aerovia A9)")
            st.markdown("- **Schynige Platte** — no con vento di valle a Lehn, no con NW, "
                        "no con bise forte")
            st.markdown("- **Saint-Hilaire** — attenzione al vento da sud; **tetto 3000 m** "
                        "(aeroporto di Lione)")
            st.markdown("- **Dôme / Roche Faurio** — si decolla presto: la neve troppo scaldata "
                        "fa sprofondare mentre corri")
    except Exception as e:
        st.warning("Non riesco a raggiungere Open-Meteo adesso.")
        st.caption(f"({type(e).__name__}) Serve connessione internet. Su Streamlit Cloud funziona.")
    st.markdown(
        f"[meteo-parapente su {scelta}](https://meteo-parapente.com/#/{la},{lo},11) · "
        "[MeteoSwiss](https://www.meteoswiss.admin.ch) · "
        "[Météo-France montagne](https://meteofrance.com/meteo-montagne) · "
        "[gipfelbuch.ch](https://www.gipfelbuch.ch)")

# ---------------------------------------------------------------- info
with t7:
    st.markdown("#### Materiale")
    for k, v in MATERIALE:
        st.markdown(f"**{k}** — {v}")
    st.markdown("---")
    st.markdown("#### Fonti")
    st.dataframe(pd.DataFrame(FONTI, columns=["Fonte", "Cosa dà", "Area"]), hide_index=True)
    st.markdown("---")
    st.markdown("#### Affidabilità")
    st.markdown("✅ **verificato** con fonte scritta — pannelli SHV/FGA, paraglidingearth, "
                "FFCAM, camptocamp, blog di relazioni")
    st.markdown("🧑 **da un pilota che c'è stato** — racconto diretto, non pubblicato da nessuna parte")
    st.markdown("🟡 **solo KML** — nella mappa di Lorenzo Delbene ma senza note dell'autore")
    st.markdown("❓ **da verificare** prima di andarci")
    st.caption("Condizioni di ghiacciaio e decolli non ufficiali vanno sempre confermati sul posto.")
