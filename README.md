# Viaggio 12-28 settembre 2026

App per consultare decolli, cime, vie e regole del viaggio, da telefono.

## Avvio

```bash
pip install -r requirements.txt
streamlit run app.py
```

Si apre su http://localhost:8501. Dal telefono, sulla stessa rete wifi:

```bash
streamlit run app.py --server.address 0.0.0.0
```

poi apri `http://IP-DEL-PC:8501` dal cellulare.

## Per averla sempre in tasca

Carica la cartella su GitHub e collegala a **share.streamlit.io** (gratis).
Ottieni un URL pubblico che funziona ovunque, anche in valle.

## File

- `app.py` — interfaccia
- `curati.py` — dati scritti a mano (decolli con orientamento, cime, vie, rifugi, giorni)
- `siti.json` — dataset generato
- `build.py` — rigenera `siti.json` unendo `curati.py` con il KML

Per rigenerare dopo aver modificato `curati.py`:

```bash
python3 build.py
```

## Uso

- **Mappa** — tutti i punti filtrati, colorati per tipo
- **Elenco** — ricerca libera nelle note. Cerca "crepaccia", "rotore", "navetta", "cavi"
- **Giorni** — lo scheletro del viaggio con le tratte
- **Info** — materiale e fonti

Nella sidebar, il campo *lat, lon* accetta le coordinate copiate dal telefono
e riordina tutto per distanza.

## Affidabilità

- ✅ verificato con fonte (pannelli SHV/FGA, paraglidingearth, FFCAM, camptocamp, blog di relazioni)
- 🟡 presente solo nel KML di Lorenzo Delbene, senza note dell'autore
- ❓ da verificare prima di andarci
