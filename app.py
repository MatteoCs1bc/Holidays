# -*- coding: utf-8 -*-
import json, math, os
import pandas as pd
import streamlit as st
from curati import GIORNI, TRATTE, MATERIALE, FONTI

st.set_page_config(page_title="Viaggio set 2026", page_icon="🪂", layout="centered")

BASE = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def carica():
    with open(os.path.join(BASE, "siti.json"), encoding="utf-8") as f:
        return pd.DataFrame(json.load(f))

df = carica()

COLORI = {"decollo": "#e63946", "atterraggio": "#2a9d8f", "cima": "#264653",
          "rifugio": "#e76f51", "parcheggio": "#f4a261", "impianto": "#9d4edd",
          "zona": "#000000", "logistica": "#0077ff"}
ICONE = {"decollo": "🪂", "atterraggio": "🎯", "cima": "⛰️", "rifugio": "🏠",
         "parcheggio": "🅿️", "impianto": "🚡", "zona": "⚠️", "logistica": "🚐"}
CAMPI_TESTO = ["nome", "note", "vento", "difficolta", "partenza", "categoria", "fonte"]

def dist_km(la1, lo1, la2, lo2):
    return math.hypot((la1 - la2) * 111,
                      (lo1 - lo2) * 111 * math.cos(math.radians((la1 + la2) / 2)))

def val(riga, campo):
    """Lettura sicura: mai attributi, pandas ha .cat .diff .size .name ecc."""
    v = riga[campo] if campo in riga.index else None
    return "" if v is None or (isinstance(v, float) and pd.isna(v)) else v

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### Filtri")
    zone = sorted(df["zona"].unique())
    z_sel = st.multiselect("Zona", zone, default=zone)
    tipi = sorted(df["tipo"].unique())
    default_tipi = [t for t in ["decollo", "cima", "atterraggio", "zona", "rifugio", "logistica"]
                    if t in tipi]
    t_sel = st.multiselect("Tipo", tipi, default=default_tipi)
    solo_note = st.checkbox("Solo punti con note vere", value=True,
                            help="Esclude i punti del KML senza descrizione")
    st.markdown("---")
    st.markdown("### Soglie")
    disl_max = st.slider("Dislivello massimo a piedi (m)", 400, 2600, 2400, 100)
    st.caption("Cross ≤1200 · Alpinismo ≤2400")
    st.markdown("---")
    st.markdown("### Posizione")
    pos = st.text_input("lat, lon (opzionale)", placeholder="46.65, 8.27",
                        help="Incolla le coordinate dal telefono per ordinare per distanza")

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

# ---------------------------------------------------------------- tabs
t1, t2, t3, t4 = st.tabs(["🗺️ Mappa", "📋 Elenco", "📅 Giorni", "🔧 Info"])

with t1:
    st.caption(f"{len(sel)} punti")
    m = sel.dropna(subset=["lat", "lon"]).copy()
    if len(m) or qui:
        m["color"] = m["tipo"].map(COLORI).fillna("#888888")
        m["size"] = m["tipo"].map({"cima": 260, "decollo": 200, "zona": 300}).fillna(130)
        if qui:
            m = pd.concat([m[["lat", "lon", "color", "size"]],
                           pd.DataFrame([{"lat": qui[0], "lon": qui[1],
                                          "color": "#0077ff", "size": 400}])],
                          ignore_index=True)
        st.map(m, latitude="lat", longitude="lon", color="color", size="size")
    else:
        st.info("Nessun punto con questi filtri.")
    c = st.columns(4)
    for i, (k, v) in enumerate(ICONE.items()):
        c[i % 4].markdown(f"<small>{v} {k}</small>", unsafe_allow_html=True)

with t2:
    q = st.text_input("Cerca", placeholder="lorenzo, crepaccia, rotore, navetta, cavi, doppia...")
    vis = sel
    if q and len(vis):
        ql = q.lower()
        tieni = [any(ql in str(r[c]).lower() for c in CAMPI_TESTO if c in vis.columns)
                 for _, r in vis.iterrows()]
        vis = vis[tieni]
    if len(vis):
        vis = vis[vis["disl"].isna() | (vis["disl"] <= disl_max)]
    st.caption(f"{len(vis)} risultati")

    for zona in sorted(vis["zona"].unique()):
        st.markdown(f"#### {zona}")
        for _, r in vis[vis["zona"] == zona].iterrows():
            coda = []
            if val(r, "quota"):
                coda.append(f"{int(r['quota'])} m")
            if val(r, "disl"):
                coda.append(f"D+{int(r['disl'])}")
            if val(r, "vento"):
                coda.append(f"vento {r['vento']}")
            if "dist" in r.index and pd.notna(r["dist"]):
                coda.append(f"{r['dist']:.0f} km")
            testa = f"{ICONE.get(r['tipo'], '📍')} **{r['nome']}**"
            with st.expander(testa + ("  ·  " + " · ".join(coda) if coda else "")):
                if val(r, "partenza"):
                    st.markdown(f"**Partenza:** {r['partenza']}")
                if val(r, "difficolta"):
                    st.markdown(f"**Difficoltà:** {r['difficolta']}")
                if val(r, "categoria"):
                    st.markdown(f"**Categoria:** {r['categoria']}")
                if val(r, "note"):
                    st.write(r["note"])
                aff = {"V": "✅ verificato", "K": "🟡 solo KML",
                       "?": "❓ da verificare"}.get(val(r, "aff"), "")
                st.caption(f"{aff} — fonte: {val(r, 'fonte')}")
                st.markdown(
                    f"[Google Maps](https://www.google.com/maps/search/?api=1"
                    f"&query={r['lat']},{r['lon']}) · "
                    f"[Organic Maps](om://map?v=1&ll={r['lat']},{r['lon']}&n={r['nome']}) · "
                    f"`{r['lat']:.5f}, {r['lon']:.5f}`")

with t3:
    for giorno, zona, nota in GIORNI:
        st.markdown(f"**{giorno}** — {zona if zona else '—'}")
        if nota:
            st.caption(nota)
    st.markdown("---")
    st.markdown("#### Tratte")
    st.dataframe(pd.DataFrame(TRATTE, columns=["Da", "A", "km", "ore"]), hide_index=True)

with t4:
    st.markdown("#### Materiale")
    for k, v in MATERIALE:
        st.markdown(f"**{k}** — {v}")
    st.markdown("---")
    st.markdown("#### Fonti")
    st.dataframe(pd.DataFrame(FONTI, columns=["Fonte", "Cosa dà", "Area"]), hide_index=True)
    st.markdown("---")
    st.caption("✅ verificato con fonte · 🧑 raccontato da un pilota che c'è stato · "
               "🟡 presente solo nel KML di Lorenzo Delbene, senza note · ❓ da verificare prima di "
               "andarci. Condizioni di ghiacciaio e decolli non ufficiali vanno sempre confermati "
               "sul posto.")
