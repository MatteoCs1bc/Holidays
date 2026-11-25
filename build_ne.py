# -*- coding: utf-8 -*-
"""Unisce i punti curati con quelli del KML di Delbene, filtrati sul nordest."""
import xml.etree.ElementTree as ET, math, re, json, html, unicodedata, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
MARCATORE = "# ======================================================================\n# APP"

def _curati_da(path):
    """Esegue solo la parte DATI del file (prima del marcatore APP): niente streamlit."""
    testo = open(path, encoding="utf-8").read()
    dati = testo.split(MARCATORE)[0]
    ns_ = {}
    exec(compile(dati, path, "exec"), ns_)
    if "CURATI" not in ns_:
        raise SystemExit(f"CURATI non trovato in {path}")
    return ns_["CURATI"]

_qui = os.path.dirname(os.path.abspath(__file__))
_src = os.path.join(_qui, "app.py")
if not os.path.exists(_src):
    _src = os.path.join(_qui, "dati_ne.py")
CURATI = _curati_da(_src)

ns = {'k': 'http://www.opengis.net/kml/2.2'}
KML = '/mnt/user-data/uploads/Paragliding_Sites.kml'
doc = ET.parse(KML).getroot().find('k:Document', ns)

TIPO = {'Takeoffs':'decollo','Landings':'atterraggio','Parkings':'parcheggio',
        'Cablecars':'impianto','Hike & Fly':'hike&fly'}

def zona(la, lo):
    if lo >= 13.80:                      return "8 Austria / Carinzia"
    if lo >= 13.55 and la <= 46.45:      return "3 Slovenia"
    if lo >= 13.30 and la >= 46.35:      return "2 Alpi Giulie"
    if lo >= 12.95:                      return "1 Friuli"
    if lo >= 12.55:                      return "6 Pordenonese / Carnia ovest"
    if lo >= 12.10:                      return "4 Alpago"
    if lo >= 11.95:                      return "5 Feltrino"
    return "7 Veneto (Bassano/Marostica)"

def chiave(n):
    n = str(n)
    for sp_ in (" "," "," "," ","\t"): n = n.replace(sp_," ")
    n = n.lower()
    for p in ("takeoff ","hike & fly ","hike and fly ","landing ","parking ","cablecar "):
        n = n.replace(p, "")
    n = unicodedata.normalize("NFKD", n).encode("ascii","ignore").decode()
    for ch in "'`’-/()": n = n.replace(ch, " ")
    return " ".join(n.split())

rows = []
for r in CURATI:
    r = dict(r)
    r.setdefault('disl', None); r.setdefault('partenza',''); r.setdefault('vento','')
    r['difficolta'] = r.pop('diff','') or ''
    r['categoria']  = r.pop('cat','') or ''
    r['origine'] = 'curato'
    rows.append(r)

chiavi_cur = {(r['zona'], chiave(r['nome'])) for r in rows}
coord_cur  = [(r['lat'], r['lon'], r['tipo']) for r in rows]
n_kml = 0
for f in doc.findall('k:Folder', ns):
    fn = f.find('k:name', ns).text
    if fn not in TIPO: continue
    for p in f.findall('k:Placemark', ns):
        co = p.find('.//k:coordinates', ns)
        if co is None: continue
        lon, lat, *_ = co.text.strip().split(','); lat = float(lat); lon = float(lon)
        if not (45.55 <= lat <= 46.80 and 11.55 <= lon <= 14.40): continue
        nm = (p.find('k:name', ns).text or '').strip()
        if not nm or nm[0].isdigit(): continue
        z = zona(lat, lon)
        if (z, chiave(nm)) in chiavi_cur: continue
        if any(t == TIPO[fn] and abs(a-lat) < 0.004 and abs(b-lon) < 0.005 for a,b,t in coord_cur):
            continue
        de = p.find('k:description', ns)
        d = re.sub('<[^>]+>', ' ', de.text).strip() if de is not None and de.text else ''
        d = html.unescape(' '.join(d.split()))
        if d.replace('WIND:','').replace('SEASONS:','').replace('VOTE:','').replace('NOTES:','').strip() == '':
            d = ''
        rows.append(dict(zona=z, tipo=TIPO[fn], nome=nm, lat=lat, lon=lon, quota=None,
                         vento='', difficolta='', aff='K',
                         categoria='Hike & Fly' if fn=='Hike & Fly' else 'Dal KML',
                         note=d, fonte='KML Delbene', disl=None, partenza='', origine='kml'))
        n_kml += 1

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'siti_ne.json')
json.dump(rows, open(out,'w'), ensure_ascii=False)
import collections
print(f"curati {len(CURATI)}  +  kml {n_kml}  =  {len(rows)} punti")
print(dict(collections.Counter(r['zona'] for r in rows)))
print(dict(collections.Counter(r['tipo'] for r in rows)))
