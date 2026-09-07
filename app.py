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

COLORI = {
    "decollo":    "#e63946",
    "atterraggio":"#2a9d8f",
    "cima":       "#264653",
    "rifugio":    "#e76f51",
    "parcheggio": "#f4a261",
    "impianto":   "#9d4edd",
    "zona":       "#000000",
}
ICONE = {
    "decollo": "🪂", "atterraggio": "🎯", "cima": "⛰️", "rifugio": "🏠",
    "parcheggio": "🅿️", "impianto": "🚡", "zona": "⚠️",
}

def dist_km(la1, lo1, la2, lo2):
    return math.hypot((la1-la2)*111, (lo1-lo2)*111*math.cos(math.radians((la1+la2)/2)))

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### Filtri")
    zone = sorted(df.zona.unique())
    z_sel = st.multiselect("Zona", zone, default=zone)
    t_sel = st.multiselect("Tipo", sorted(df.tipo.unique()),
                           default=["decollo", "cima", "atterraggio", "zona", "rifugio"])
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

sel = df[df.zona.isin(z_sel) & df.tipo.isin(t_sel)].copy()
if solo_note:
    sel = sel[(sel.origine == "curato") | (sel.note.astype(str).str.len() > 20)]

qui = None
if pos.strip():
    try:
        a, b = [float(x) for x in pos.replace(";", ",").split(",")[:2]]
        qui = (a, b)
        sel["dist"] = sel.apply(lambda r: dist_km(a, b, r.lat, r.lon), axis=1)
        sel = sel.sort_values("dist")
    except Exception:
        st.sidebar.error("Formato: 46.65, 8.27")

# ---------------------------------------------------------------- tabs
t1, t2, t3, t4 = st.tabs(["🗺️ Mappa", "📋 Elenco", "📅 Giorni", "🔧 Info"])

with t1:
    st.caption(f"{len(sel)} punti")
    m = sel.dropna(subset=["lat", "lon"]).copy()
    m["color"] = m.tipo.map(COLORI).fillna("#888888")
    m["size"] = m.tipo.map({"cima": 260, "decollo": 200, "zona": 300}).fillna(130)
    if qui:
        m = pd.concat([m, pd.DataFrame([{"lat": qui[0], "lon": qui[1],
                                         "color": "#0077ff", "size": 400}])], ignore_index=True)
    st.map(m, latitude="lat", longitude="lon", color="color", size="size")
    c = st.columns(4)
    for i, (k, v) in enumerate(ICONE.items()):
        c[i % 4].markdown(f"<small>{v} {k}</small>", unsafe_allow_html=True)

with t2:
    q = st.text_input("Cerca", placeholder="crepaccia, rotore, navetta, corda...")
    vis = sel
    if q:
        m_ = vis.apply(lambda r: q.lower() in " ".join(
            str(r[c]) for c in ["nome", "note", "vento", "diff", "partenza"]).lower(), axis=1)
        vis = vis[m_]
    vis = vis[(vis.disl.isna()) | (vis.disl <= disl_max)]
    st.caption(f"{len(vis)} risultati")

    for zona in sorted(vis.zona.unique()):
        blocco = vis[vis.zona == zona]
        st.markdown(f"#### {zona}")
        for _, r in blocco.iterrows():
            testa = f"{ICONE.get(r.tipo,'📍')} **{r.nome}**"
            coda = []
            if pd.notna(r.quota) and r.quota: coda.append(f"{int(r.quota)} m")
            if pd.notna(r.disl) and r.disl:   coda.append(f"D+{int(r.disl)}")
            if r.vento:                        coda.append(f"vento {r.vento}")
            if qui is not None and "dist" in r: coda.append(f"{r.dist:.0f} km")
            with st.expander(testa + ("  ·  " + " · ".join(coda) if coda else "")):
                if r.partenza: st.markdown(f"**Partenza:** {r.partenza}")
                if r.diff:     st.markdown(f"**Difficolta:** {r.diff}")
                if r.cat:      st.markdown(f"**Categoria:** {r.cat}")
                if r.note:     st.write(r.note)
                aff = {"V": "✅ verificato", "K": "🟡 solo KML", "?": "❓ da verificare"}.get(r.aff, "")
                st.caption(f"{aff} — fonte: {r.fonte}")
                st.markdown(
                    f"[Google Maps](https://www.google.com/maps/search/?api=1&query={r.lat},{r.lon}) · "
                    f"[Organic Maps](om://map?v=1&ll={r.lat},{r.lon}&n={r.nome}) · "
                    f"`{r.lat:.5f}, {r.lon:.5f}`")

with t3:
    for giorno, zona, nota in GIORNI:
        st.markdown(f"**{giorno}** — {zona if zona else '—'}")
        if nota:
            st.caption(nota)
    st.markdown("---")
    st.markdown("#### Tratte")
    st.dataframe(pd.DataFrame(TRATTE, columns=["Da", "A", "km", "ore"]),
                 hide_index=True, use_container_width=True)

with t4:
    st.markdown("#### Materiale")
    for k, v in MATERIALE:
        st.markdown(f"**{k}** — {v}")
    st.markdown("---")
    st.markdown("#### Fonti")
    st.dataframe(pd.DataFrame(FONTI, columns=["Fonte", "Cosa da", "Area"]),
                 hide_index=True, use_container_width=True)
    st.markdown("---")
    st.caption(
        "✅ verificato con fonte · 🟡 presente solo nel KML di Lorenzo Delbene, senza note "
        "· ❓ da verificare prima di andarci. Le condizioni di ghiacciaio e i "
        "decolli non ufficiali vanno sempre confermati sul posto."
    )
