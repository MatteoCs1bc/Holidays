# Nordest — volo e montagna

Friuli, Carnia, Alpi Giulie, Slovenia di confine, Alpago, bellunese, feltrino.
543 punti, divisi per **tipologia di attività**. Le 107 uscite di
[Cammina e Vola](https://camminaevola.it/elenco-uscite/) sono dentro, con difficoltà
di decollo, direzione del vento, atterraggio, parcheggio e via di salita.

## File

- `app.py` — interfaccia, dati, classificazione e motore meteo in un file solo
- `montagna.py` — schede Neve per zona, Rotte di volo e Documenti
- `documenti.json` — bibliografia meteo FVG con stato dei download
- `siti_ne.json` — i punti
- `build_ne.py` — rigenera `siti_ne.json` incrociando dati curati, Cammina e Vola e KML
- `cev_ne.py` + `cev.json` — le 107 relazioni di Cammina e Vola e la lettura delle esposizioni
- `mk.py` — riassembla `app.py` dai moduli di lavoro
- `requirements.txt`

## Le quattro attività

| | | Punti |
|---|---|---|
| 🪂 | **Voli di cross** — decolli e atterraggi ufficiali, auto o impianto, club e regolamento | 409 |
| 🥾 | **Hike & Fly** — si sale a piedi su terreno escursionistico | 347 |
| ⛰️ | **Paralpinismo estivo** — cime alpine, si vola in discesa | 285 |
| ❄️ | **Paralpinismo invernale** — scialpinismo e volo | 308 |

Un punto può valere per più attività. Sulla mappa prende il colore di quella più
impegnativa fra quelle selezionate.

**Cross e hike & fly** vengono dalle cartelle del KML, dalle fonti dei club e dalle
relazioni di Cammina e Vola.
**I due paralpinismi sono una proposta**: classificati sul carattere della cima,
non su relazioni di volo verificate. Vanno confermati.

## Schede

Tre schede in alto.

**🌤️ Meteo** — si apre sul **colpo d'occhio regionale**: dieci zone fra Friuli,
Carnia, Giulie, Slovenia di confine, Dolomiti friulane, Alpago, bellunese e feltrino,
ognuna con un punteggio da 0 a 100 calcolato **con criteri diversi per ogni attività**.
In cima quattro card dicono dove conviene andare oggi per cross, hike & fly,
alpinismo estivo e invernale, con il motivo e le due alternative. Sotto, tutte le zone
in ordine, e una mappa regionale con i punteggi.

Poi l'**approfondimento** su una località, scelta fra zona, singolo decollo o coordinate libere.
Sintesi del giorno a card colorate (instabilità, gradiente, inversioni, turbolenza,
copertura nuvolosa), quote di lavoro, analisi delle nubi per fascia e per strato,
gradiente strato per strato, profilo verticale, andamento sui giorni.
In fondo: mappa dei siti volabili con quel meteo, Windy, carte sinottiche e il
capitolo sul tempo in Friuli.

**🪂 Siti di volo** — selettore di attività, mappa della sola attività scelta,
poi **decolli e atterraggi separati**, con esposizione, difficoltà di decollo,
dislivello e via di salita dove ci sono. Filtro per grado di difficoltà e legenda
della scala Cammina e Vola.

**❄️ Neve per zona** — 16 zone (Dolomiti Friulane, Prealpi Maniago–Aviano, Val Pesarina,
Sappada, Zoncolan, Gemonese, Val Tagliamento, Avostanis/Monte Croce, Amariana/Verzegnis,
Tramontina, Sernio/Grauzaria, Zuc dal Bôr/Cjavals, Val Resia, Val Raccolana,
Pontebba–Tarvisio, Mangart). Diario giornaliero dal 1° novembre, letto da Open-Meteo alla
quota di riferimento della zona: neve fresca 24/72 h, pioggia, zero termico, vento al suolo
e a 700 hPa, notti serene; più la previsione a 7 giorni. Regole semplici segnalano pioggia
su neve, accumuli da vento (con i versanti sottovento), fusione e rigelo, rialzi termici,
brina/sfaccettamento. Non sostituisce il bollettino valanghe. Zone e quote si correggono
in `ZONE` dentro `montagna.py`.

**🧭 Rotte di volo** — mappa con gli strati di thermal.kk7.ch (skyways e termiche,
CC BY-NC-SA 4.0), le ipotesi di rotta e i decolli; per ogni rotta il ragionamento e il
verdetto dei prossimi 3 giorni (strato limite, vento 850/700 hPa, nord in quota, pioggia).

**🔧 Info** — documenti meteo FVG (Drive e bibliografia), le quattro attività, stato della documentazione zona per zona,
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

## Come viene calcolato il punteggio

Pesa vento a 700 hPa, gradiente termico, tetto delle termiche, nuvole basse,
instabilità e pioggia — ma li pesa in modo diverso a seconda dell'attività:

- **cross e hike & fly** vogliono gradiente e quota, vento fra i 12 e i 22 km/h,
  cumuli come segnalatori; penalizzano l'aria stabile, il coperto basso e il CAPE
  sopra 1500 per rischio sovrasviluppi. L'hike & fly perdona condizioni più magre
  ma penalizza le raffiche al suolo.
- **i due alpinismi** vogliono aria calma e cielo pulito; penalizzano forte
  l'instabilità, perché il problema non è volare male ma prendersi un temporale
  in cresta. L'estivo vuole lo zero termico alto, l'invernale basso — e penalizza
  il gradiente molto forte per il rischio sul manto nevoso.

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

## Cammina e Vola

Tutte e 107 le uscite di `camminaevola.it` sono dentro: nome del sito, difficoltà di
decollo sulla scala dell'autore (1, 2-, 2, 2+, 3), possibili decolli con l'esposizione,
possibili atterraggi, parcheggio, quota minima e massima, via di salita e coordinate
sia del decollo sia dell'atterraggio. 166 punti nuovi; altri 41 si sono fusi su punti
che c'erano già (il Cuarnan, il San Simeone e compagnia) completandoli.

Le esposizioni sono ricavate dal testo della relazione: 63 decolli su 107 la dichiarano,
gli altri descrivono il prato senza dire da che parte guarda e restano senza.
Ogni scheda ha il link alla relazione originale.

Per rileggere il sito serve un browser sulla tua macchina: dal sandbox il dominio è
bloccato dal proxy, e questo mi aveva fatto dire, a torto, che il sito fosse morto.
