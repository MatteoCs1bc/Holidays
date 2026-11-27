# -*- coding: utf-8 -*-
"""Lettura dello stato del manto nevoso: sci o picca e ramponi?

Regole costruite sui manuali AINEVA in cartella (Le valanghe, Il bollettino valanghe e la
scala di pericolo, La neve) e sugli appunti CAI di meteorologia alpina:
 - metamorfismo distruttivo (T vicino a 0 °C): la neve fresca si assesta e si arrotonda;
 - metamorfismo costruttivo (freddo intenso, manto sottile, notti serene): cristalli
   sfaccettati e brina di profondità, strati deboli persistenti;
 - metamorfismo da fusione: di giorno fonde, se di notte rigela il manto si consolida
   (crosta portante, firn); dopo una notte calda e coperta resta bagnato dal mattino;
 - dopo una nevicata, se resta freddo, il freddo "conserva l'instabilità";
 - il vento trasporta la neve fresca sui versanti sottovento (accumuli, lastroni) e la
   indurisce sopravento e in cresta.
I dati sono del modello (Open-Meteo) alla quota di riferimento della zona: la diagnosi è
un punto di partenza da confrontare con bollettino e osservazioni sul campo."""
import json, urllib.request
from datetime import date, timedelta
import pandas as pd

# ------------------------------------------------------------------ MICROZONE BOLLETTINO
# Microzone del bollettino valanghe FVG (AINEVA / ALBINA, regione IT-36).
MICRO = {
    "IT-36-UD-01": "Alpi Carniche occidentali",
    "IT-36-UD-02": "Alpi Carniche orientali",
    "IT-36-UD-03": "Alpi Giulie (senza Canin)",
    "IT-36-UD-04": "Canin",
    "IT-36-UD-05": "Prealpi Giulie",
    "IT-36-PN-01": "Prealpi Carniche occidentali",
    "IT-36-PN-02": "Prealpi Carniche orientali",
}
GRADI = {"low": 1, "moderate": 2, "considerable": 3, "high": 4, "very_high": 5}
NOME_GRADO = {1: "1 debole", 2: "2 moderato", 3: "3 marcato", 4: "4 forte", 5: "5 molto forte"}
COL_GRADO = {1: [204, 255, 102], 2: [255, 255, 0], 3: [255, 153, 0], 4: [255, 0, 0],
             5: [120, 0, 0]}
PROBLEMI = {"new_snow": "neve fresca", "wind_slab": "neve ventata", "persistent_weak_layers":
            "strati deboli persistenti", "wet_snow": "neve bagnata", "gliding_snow":
            "valanghe da slittamento", "cornices": "cornici", "no_distinct_avalanche_problem":
            "nessun problema evidente", "favourable_situation": "situazione favorevole"}


def bollettino(giorno: date):
    """Bollettino valanghe FVG del giorno (formato aperto CAAMLv6 su avalanche.report).
    Ritorna {regionID: dict(grado, gradi, problemi, testo, pubblicato)} o {} se non c'è."""
    for g in (giorno, giorno - timedelta(days=1)):
        url = (f"https://static.avalanche.report/eaws_bulletins/{g:%Y-%m-%d}/"
               f"{g:%Y-%m-%d}-IT-36.json")
        try:
            with urllib.request.urlopen(url, timeout=20) as f:
                js = json.load(f)
        except Exception:
            continue
        out = {}
        for b in js.get("bulletins", []):
            gradi = []
            for dr in b.get("dangerRatings", []):
                el = dr.get("elevation", {}) or {}
                gradi.append((GRADI.get(dr.get("mainValue"), 0),
                              el.get("lowerBound"), el.get("upperBound"),
                              dr.get("validTimePeriod", "all_day")))
            prob = []
            for p in b.get("avalancheProblems", []):
                el = p.get("elevation", {}) or {}
                quota = (f"sopra {el['lowerBound']} m" if el.get("lowerBound") else "") + \
                        (f" sotto {el['upperBound']} m" if el.get("upperBound") else "")
                prob.append(dict(tipo=PROBLEMI.get(p.get("problemType"), p.get("problemType")),
                                 esposizioni=p.get("aspects", []), quota=quota.strip(),
                                 periodo=p.get("validTimePeriod", "")))
            testo = " ".join(x for x in [
                (b.get("avalancheActivity") or {}).get("highlights", ""),
                (b.get("avalancheActivity") or {}).get("comment", ""),
                (b.get("snowpackStructure") or {}).get("comment", "")] if x)
            info = dict(grado=max([x[0] for x in gradi] or [0]), gradi=gradi, problemi=prob,
                        testo=testo.replace("<br/>", " "), pubblicato=b.get("publicationTime", ""),
                        valido=f"{g:%d/%m/%Y}")
            for reg in b.get("regions", []):
                out[reg.get("regionID")] = info
        if out:
            return out
    return {}


# ------------------------------------------------------------------ DIAGNOSI
TIPI = {
    # chiave: (emoji, titolo, colore mappa, attrezzatura)
    "scarsa":     ("\U0001FAA8", "Neve scarsa o assente", [150, 150, 150],
                   "\U0001F97E a piedi; ramponcini per ghiaccio residuo nei tratti in ombra"),
    "polvere":    ("❄️", "Neve fresca polverosa", [90, 160, 255],
                   "\U0001F3BF sci o ciaspole; picca e ramponi solo in cresta"),
    "assesta":    ("\U0001F328️", "Neve fresca che si assesta", [130, 190, 255],
                   "\U0001F3BF sci o ciaspole"),
    "ventata":    ("\U0001F32C️", "Neve fresca ventata: accumuli e croste da vento",
                   [150, 90, 220],
                   "\U0001F3BF sci con attenzione ai pendii sottovento; in cresta neve dura: "
                   "ramponi"),
    "fredda":     ("\U0001F9CA", "Neve fredda non trasformata", [70, 110, 200],
                   "\U0001F3BF sci (polvere vecchia in ombra); croste da vento e tratti duri "
                   "esposti: ramponi e picca"),
    "rigelo":     ("\U0001F9CA", "Trasformata con rigelo (crosta portante / firn)",
                   [34, 160, 70],
                   "⛏️ picca e ramponi al mattino sul ripido; \U0001F3BF firn a metà "
                   "mattina sui versanti al sole, scendere prima che molli"),
    "bagnata":    ("\U0001F4A7", "Bagnata, senza rigelo notturno", [226, 116, 28],
                   "\U0001F6AB sprofondamento e valanghe bagnate: partire molto presto o "
                   "rinunciare; ciaspole se proprio"),
    "crosta":     ("\U0001F9CA", "Crosta da pioggia / ghiaccio", [200, 45, 45],
                   "⛏️ ramponi e picca; sci su neve dura o vetrata, scivolate pericolose"),
}


def _v(x, d=0.0):
    return d if x is None or pd.isna(x) else float(x)


def diagnosi(d: pd.DataFrame, giorno: date, q: int):
    """Stato del manto alla quota q il giorno indicato (passato o previsto)."""
    s = d[d["data"] <= giorno].reset_index(drop=True)
    if not len(s):
        return None
    r = s.iloc[-1]
    hs = _v(r["neve_suolo"])
    tmin, tmax = _v(r["temperature_2m_min"]), _v(r["temperature_2m_max"])
    zt = _v(r["zt_max"], -1)
    nuv_n = _v(r["nuv_notte"], 100)
    rigelo_oggi = tmin <= -1.5 or (tmin <= 0 and nuv_n < 40)
    fonde_oggi = tmax >= 0.5 or zt >= q + 150

    # ultimo episodio nevoso (giorni contigui con neve)
    i_last = None
    for i in range(len(s) - 1, -1, -1):
        if _v(s.loc[i, "snowfall_sum"]) >= 3:
            i_last = i; break
    if i_last is not None:
        j = i_last
        while j - 1 >= 0 and _v(s.loc[j - 1, "snowfall_sum"]) >= 1:
            j -= 1
        evento = s.loc[j:i_last]
        hn_ev = float(evento["snowfall_sum"].sum())
        data_ev = s.loc[i_last, "data"]
        giorni_da = (giorno - data_ev).days
        dopo = s.loc[i_last + 1:]                         # giorni dopo la nevicata
        durante_dopo = s.loc[j:]
    else:
        hn_ev, data_ev, giorni_da = 0.0, None, 999
        dopo = s.iloc[-30:]; durante_dopo = s.iloc[-30:]

    # cicli fusione-rigelo dopo la nevicata (giorno k fonde, mattina k+1 rigela)
    cicli = 0; fusi = 0
    dopo = dopo[dopo["data"] < giorno]               # solo i giorni prima di oggi
    idx = list(dopo.index)
    for a, b in zip(idx, idx[1:] + [None]):
        fonde = _v(s.loc[a, "temperature_2m_max"]) >= 0.5 or _v(s.loc[a, "zt_max"], -1) >= q + 150
        if fonde:
            fusi += 1
            if b is not None and _v(s.loc[b, "temperature_2m_min"]) <= -1:
                cicli += 1
    giorni_freddi = int(sum(1 for k in dopo.index
                            if _v(s.loc[k, "temperature_2m_max"]) < -1
                            and _v(s.loc[k, "zt_max"], -1) < q))
    pioggia = float(durante_dopo["rain_sum"].fillna(0).sum())
    pioggia_oggi = _v(r["rain_sum"])
    # vento con neve trasportabile: entro 4 giorni dalla nevicata e prima che fonda
    trasp = durante_dopo[(durante_dopo["data"] <= (data_ev + timedelta(days=4)
                                                   if data_ev else giorno))]
    if fusi and len(dopo):
        prima_fusione = next((s.loc[k, "data"] for k in dopo.index
                              if _v(s.loc[k, "temperature_2m_max"]) >= 0.5), None)
        if prima_fusione is not None:
            trasp = trasp[trasp["data"] <= prima_fusione]
    v7max = float(trasp["v700_max"].max()) if len(trasp) else 0.0
    rafmax = float(trasp["wind_gusts_10m_max"].max()) if len(trasp) else 0.0
    ventato = hn_ev >= 5 and (v7max >= 35 or rafmax >= 45)
    dir_v = None
    if ventato:
        k = trasp["v700_max"].idxmax()
        dir_v = trasp.loc[k, "v700_dir"]
    # notti serene e fredde dopo la nevicata: metamorfismo costruttivo
    notti_fredde = int(sum(1 for k in dopo.index
                           if _v(s.loc[k, "temperature_2m_min"]) <= -8
                           and _v(s.loc[k, "nuv_notte"], 100) < 35))
    hn72 = _v(r["hn72"])

    # ---- classificazione della superficie
    if hs < 10 and hn72 < 10:
        tipo = "scarsa"
    elif pioggia_oggi >= 2 and hs >= 10:
        tipo = "bagnata"
    elif giorni_da <= 1 and hn_ev >= 5 and fusi == 0:
        tipo = "ventata" if ventato else "polvere"
    elif giorni_da <= 4 and fusi == 0:
        tipo = "ventata" if ventato else "assesta"
    elif fusi >= 1:
        if not rigelo_oggi:
            tipo = "bagnata"
        elif pioggia >= 2 and hs >= 10:
            tipo = "crosta"
        else:
            tipo = "rigelo"
    else:
        tipo = "fredda"

    # ---- versanti al sole e in ombra
    if tipo in ("rigelo", "bagnata", "crosta"):
        if zt >= q + 600 or tmax >= 4:
            ombra = "anche a nord la neve si scalda: trasformata, bagnata nel pomeriggio"
        else:
            ombra = ("a nord la neve resta fredda: dura o ghiacciata se ha già trasformato, "
                     "polverosa se no")
        sole = ("al sole dura al mattino presto, poi firn, poi molle e marcia nel pomeriggio"
                if rigelo_oggi else "al sole marcia già dal mattino")
    elif tipo in ("polvere", "assesta", "ventata", "fredda"):
        sole = ("oggi al sole comincia a trasformare: umida nelle ore calde, crosta "
                "domattina se la notte è serena" if fonde_oggi else "anche al sole resta fredda")
        ombra = "in ombra resta polverosa" if tipo != "ventata" else \
                "in ombra polverosa, ma con accumuli sottovento"
    else:
        sole = ombra = ""

    # ---- problemi tipici (scala EAWS, dai manuali AINEVA)
    prob = []
    if hn72 >= 20 or (giorni_da <= 2 and hn_ev >= 20):
        prob.append("neve fresca")
    if ventato and giorni_da <= 5:
        prob.append("neve ventata")
    if tipo == "bagnata" or (fonde_oggi and not rigelo_oggi and hs >= 10):
        prob.append("neve bagnata")
    if notti_fredde >= 3 and hs < 80:
        prob.append("strati deboli persistenti (brina e cristalli sfaccettati)")

    # ---- perché, in parole
    perche = []
    if data_ev is not None and giorni_da < 999:
        perche.append(f"ultima nevicata {data_ev:%d/%m} ({hn_ev:.0f} cm), {giorni_da} giorni fa"
                      if giorni_da else f"nevicata in corso o di oggi: {hn_ev:.0f} cm")
    if fusi:
        perche.append(f"{fusi} giorni con fusione dopo la nevicata, {cicli} con rigelo notturno")
    if giorni_freddi and not fusi:
        perche.append(f"{giorni_freddi} giorni freddi senza fusione: il freddo conserva la "
                      "neve fresca e la sua instabilità")
    if ventato:
        from montagna import card8, sottovento
        perche.append(f"vento fino a {v7max:.0f} km/h in quota da {card8(dir_v)} con neve "
                      f"fresca: accumuli sui versanti {sottovento(dir_v)}")
    if pioggia >= 2:
        perche.append(f"{pioggia:.0f} mm di pioggia sulla neve")
    perche.append(f"stanotte minima {tmin:.0f} °C, nuvole {nuv_n:.0f}%: "
                  + ("rigelo" if rigelo_oggi else "niente rigelo"))
    perche.append(f"zero termico fino a {zt:.0f} m (zona a {q} m)")
    if notti_fredde >= 3:
        perche.append(f"{notti_fredde} notti serene sotto −8 °C: gradiente forte nel manto")

    e, tit, col, att = TIPI[tipo]
    return dict(tipo=tipo, emoji=e, titolo=tit, colore=col, attrezzatura=att, hs=hs,
                hn_evento=hn_ev, data_evento=data_ev, giorni_da=giorni_da, cicli=cicli,
                rigelo=rigelo_oggi, fonde=fonde_oggi, ventato=ventato,
                sottovento=dir_v, problemi=prob, perche=perche, sole=sole, ombra=ombra)


# ------------------------------------------------------------------ SAPERE DAI MANUALI
DRV = "https://drive.google.com/file/d/"
SAPERE = [
    ("I tre metamorfismi",
     "**Distruttivo** — con aria vicina a 0 °C i cristalli si arrotondano e la neve si "
     "assesta: la neve fresca si stabilizza in pochi giorni. **Costruttivo** — con freddo "
     "intenso e manto sottile (notti serene) si forma un forte gradiente: cristalli "
     "sfaccettati, a calice e brina di profondità, strati deboli che durano settimane. "
     "**Da fusione** — a 0 °C i grani fondono; se di notte rigela, l'acqua salda i grani e "
     "il manto si consolida (crosta portante, firn).",
     "AINEVA, Le valanghe (2021)", DRV + "1z9i_VPx7VP2GBoIAjAQ0ELcTY0SOJSJw"),
    ("Dopo una nevicata",
     "Se dopo una nevicata intensa resta freddo, il freddo conserva l'instabilità e ritarda "
     "l'assestamento. Con escursione termica giornaliera il manto si consolida perché "
     "l'acqua di fusione rigela legando i cristalli.",
     "AINEVA, Le valanghe (2021)", DRV + "1z9i_VPx7VP2GBoIAjAQ0ELcTY0SOJSJw"),
    ("Neve bagnata e tempistica",
     "Dopo una notte fredda e serena il rigelo rende favorevole il mattino e la stabilità si "
     "perde nelle ore calde; dopo una notte calda e coperta il problema c'è già dal mattino; "
     "la pioggia su neve fresca lo crea quasi subito. Lo sprofondamento dello scarpone è un "
     "segnale di inumidimento.",
     "AINEVA, Il bollettino valanghe e la scala di pericolo",
     DRV + "1WTyOVoCaI96pED2pCLqPw29Z05jBndb5"),
    ("Neve ventata",
     "Il vento sposta la neve con o senza nevicata: accumuli sul lato sottovento di creste, "
     "canali, conche e cambi di pendenza, soprattutto sopra il bosco. Dura da durante "
     "l'episodio a pochi giorni dopo. Evitare gli accumuli sul ripido, soprattutto dove il "
     "manto passa da sottile a spesso o da duro a soffice.",
     "AINEVA, Il bollettino valanghe e la scala di pericolo",
     DRV + "1WTyOVoCaI96pED2pCLqPw29Z05jBndb5"),
    ("Strati deboli persistenti",
     "Brina di superficie sepolta, brina di profondità, cristalli sfaccettati: più frequenti "
     "in ombra e al riparo dal vento, durano settimane o mesi, difficili da riconoscere "
     "(whumpf). Sono la causa della maggior parte degli incidenti: pendii ampi e ripidi da "
     "evitare, attenzione ai passaggi da manto sottile a spesso.",
     "AINEVA, Il bollettino valanghe e la scala di pericolo",
     DRV + "1WTyOVoCaI96pED2pCLqPw29Z05jBndb5"),
    ("Pendenza e sovraccarico",
     "Ripido 30–35°, molto ripido 35–40°, estremamente ripido oltre 40°. Sovraccarico debole: "
     "un singolo scialpinista, gruppo distanziato, ciaspole; forte: escursionista a piedi, "
     "gruppo senza distanze, caduta. Togliere gli sci per salire a piedi in cresta trasforma "
     "un sovraccarico debole in forte.",
     "AINEVA, Il bollettino valanghe e la scala di pericolo",
     DRV + "1WTyOVoCaI96pED2pCLqPw29Z05jBndb5"),
    ("Meteorologia alpina",
     "Manuale AINEVA di meteorologia alpina (Micheletti, OSMER) — situazioni sinottiche, "
     "föhn, inversioni, previsione in montagna.",
     "AINEVA, Manuale meteo 2021", DRV + "1AB1oZJAh6nT8JTUJFGRAkkrJ_uoB_SA_"),
]
