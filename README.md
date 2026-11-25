# Nordest — volo e montagna

Friuli, Carnia, Alpi Giulie, Slovenia di confine, Alpago, bellunese, feltrino.
420 punti, divisi per **tipologia di attività**.

## File

- `app.py` — interfaccia, dati, classificazione e motore meteo in un file solo
- `siti_ne.json` — i punti
- `build_ne.py` — rigenera `siti_ne.json` incrociando i dati curati con il KML
- `requirements.txt`

## Le quattro attività

| | | Punti |
|---|---|---|
| 🪂 | **Voli di cross** — decolli e atterraggi ufficiali, auto o impianto, club e regolamento | 342 |
| 🥾 | **Hike & Fly** — si sale a piedi su terreno escursionistico | 85 |
| ⛰️ | **Paralpinismo estivo** — cime alpine, si vola in discesa | 43 |
| ❄️ | **Paralpinismo invernale** — scialpinismo e volo | 37 |

Un punto può valere per più attività. Sulla mappa prende il colore di quella più
impegnativa fra quelle selezionate.

**Cross e hike & fly** vengono dalle cartelle del KML e dalle fonti dei club.
**I due paralpinismi sono una proposta**: classificati sul carattere della cima,
non su relazioni di volo verificate. Vanno confermati.

## Schede

Tre schede in alto.

**🌤️ Meteo** — riferimento scelto fra zona, singolo decollo o coordinate libere.
Sintesi del giorno a card colorate (instabilità, gradiente, inversioni, turbolenza,
copertura nuvolosa), quote di lavoro, analisi delle nubi per fascia e per strato,
gradiente strato per strato, profilo verticale, andamento sui giorni.
In fondo: mappa dei siti volabili con quel meteo, Windy, carte sinottiche e il
capitolo sul tempo in Friuli.

**🪂 Siti di volo** — selettore di attività, mappa della sola attività scelta,
poi **decolli e atterraggi separati**, con esposizione, difficoltà, dislivello e
via di salita dove ci sono.

**🔧 Info** — le quattro attività, stato della documentazione zona per zona,
gite, fonti, legenda.

## Cosa calcola il motore meteo

Da Open-Meteo, medie della fascia 11-16:

- **Instabilità** da CAPE e lifted index
- **Quota massima di volo** = quota stazione + altezza dello strato limite
- **Base dei cumuli** dallo spread temperatura/rugiada, con il confronto
  base-contro-tetto per sapere se avrai cumuli o termiche blu
- **Copertura nuvolosa** per fascia (basse, medie, alte) e **strati veri** individuati
  nel profilo con quota, copertura e umidità relativa a sei livelli
- **Inversioni** cercate nel profilo: dove la temperatura torna a salire con la quota
- **Gradiente termico** su tre strati (925→850, 850→700, 700→500) in °C/100 m,
  confrontato con l'adiabatica secca di 0,98
- **Turbolenza potenziale** da shear vettoriale 925→700, rapporto raffiche/vento medio
  e intensità a 700 hPa
- **Profilo verticale** su sei livelli con quota, temperatura, vento e umidità

## Il tempo in Friuli

Dieci capitoli tratti dagli *Appunti di meteorologia per il Friuli Venezia Giulia*
(ARPA FVG, III edizione): stau e föhn, dove piove e perché, bora chiara e scura,
le brezze di monte e di valle, la giornata tipo in una valle friulana, il temporale
di calore pomeridiano, come si legge la sera per il giorno dopo, il vento trasversale.

## Avvio

```bash
pip install -r requirements.txt
streamlit run app.py
```

Online: carica su GitHub e collega a share.streamlit.io, main file `app.py`.

## Rigenerare i dati

I dati curati e la classificazione stanno nella prima metà di `app.py`,
sopra il marcatore `# APP`. Modifichi lì e poi:

```bash
python3 build_ne.py
```

Legge il KML da `/mnt/user-data/uploads/Paragliding_Sites.kml`: cambia il percorso
in cima al file se lo tieni altrove.

## Nota sulla mappa Google

Il KML usato è l'export di settembre 2026 della tua My Maps. Non posso riscaricarlo
da qui: il proxy blocca `google.com/maps/d/kml`. Se hai aggiunto punti dopo settembre,
riesporta il KML e sostituiscilo.

## Nota su Cammina e Vola

`camminaevola.it` non risolve più. I circa 25 hike & fly carnici nel KML
(Clapsavon, Tinisa, Pleros, Raut, Lovinzola, Creta di Mimoias…) sono quasi
certamente quelli che stavano lì.
