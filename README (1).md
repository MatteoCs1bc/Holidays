# Nordest — volo e montagna

Friuli (area principale), Alpi Giulie, Slovenia di confine, Alpago, bellunese, feltrino.

Ramo separato dall'app del viaggio di settembre 2026: dati e codice non hanno niente in comune.

## File

- `app.py` — interfaccia **e** dati insieme, un file solo
- `siti_ne.json` — i 257 punti
- `build_ne.py` — rigenera `siti_ne.json` incrociando i dati curati dentro `app.py` con il KML
- `requirements.txt`

## Avvio

```bash
pip install -r requirements.txt
streamlit run app.py
```

Online: carica la cartella su GitHub e collegala a share.streamlit.io, main file `app.py`.

## Sezioni

Menu a tendina in cima, non schede: su telefono le schede finiscono fuori schermo.

| Sezione | Cosa c'è |
|---|---|
| Friuli | Cuarnan, San Simeone, Prealpi, Carnia, più Alpi Giulie e Pordenonese |
| Slovenia | i 10 decolli del Posočje con esposizione, difficoltà, club, tasse e regole |
| Alpago e bellunese | Dolada, Nevegal, Visentin, Pizzoc, Monte Avena, le 25 gite di Flytherapy |
| Mappa | tutti i punti filtrati |
| Elenco | ricerca libera nelle note |
| Gite | itinerari curati + schede Flytherapy |
| Meteo | Windy, semaforo per decollo, previsioni a 14 giorni |
| Info | stato della documentazione zona per zona, fonti, legenda |

## Rigenerare i dati

I dati curati stanno nella prima metà di `app.py`, sopra il marcatore `# APP`.
Modifichi lì e poi:

```bash
python3 build_ne.py
```

`build_ne.py` legge il KML da `/mnt/user-data/uploads/Paragliding_Sites.kml`:
cambia quel percorso se tieni il file altrove.

## Affidabilità

- ✅ verificato con fonte scritta: club, federazioni, guide locali
- 🟡 solo KML — presente nella mappa di Lorenzo Delbene ma senza note
- ❓ da verificare prima di andarci

## Nota su Cammina e Vola

`camminaevola.it` è morto: a settembre 2026 rispondeva un clone commerciale su https,
adesso il dominio non risolve più. I circa 25 hike & fly carnici che trovi nel KML
(Clapsavon, Tinisa, Pleros, Raut, Lovinzola, Creta di Mimoias…) sono quasi certamente
quelli che stavano lì. Il KML è il fossile superstite di quel sito.
