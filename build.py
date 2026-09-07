# Unisce i punti curati con quelli del KML di Delbene, filtrati sulle zone del viaggio
import xml.etree.ElementTree as ET, math, re, json, html
from curati import CURATI

ns={'k':'http://www.opengis.net/kml/2.2'}
doc=ET.parse('/mnt/user-data/uploads/Paragliding_Sites.kml').getroot().find('k:Document',ns)

ZONE=[("1 Alpstein",47.28,9.35,32),("2 Zurigo",47.10,8.60,55),("3 Oberland",46.66,7.95,38),
      ("4 Annecy",45.87,6.20,32),("5 Saint-Hilaire",45.31,5.86,35),("6 Ecrins",44.92,6.45,50),
      ("7 Val Susa/Chisone",44.98,7.00,45)]
TIPO={'Takeoffs':'decollo','Landings':'atterraggio','Parkings':'parcheggio',
      'Cablecars':'impianto','Hike & Fly':'decollo'}

def dist(a,b,c,d): return math.hypot((a-c)*111,(b-d)*111*math.cos(math.radians((a+c)/2)))

rows=[]
for r in CURATI:
    r=dict(r); r.setdefault('disl',None); r.setdefault('partenza',''); r.setdefault('vento','')
    r.setdefault('diff',''); r.setdefault('cat',''); r['origine']='curato'
    rows.append(r)

# nomi gia curati, per non duplicare
seen={(r['zona'], r['nome'].lower()[:12]) for r in rows}
n_kml=0
for f in doc.findall('k:Folder',ns):
    fn=f.find('k:name',ns).text
    if fn not in TIPO: continue
    for p in f.findall('k:Placemark',ns):
        co=p.find('.//k:coordinates',ns)
        if co is None: continue
        lon,lat,*_=co.text.strip().split(','); lat=float(lat); lon=float(lon)
        z=next((zn for zn,la,lo,rad in ZONE if dist(la,lo,lat,lon)<rad), None)
        if not z: continue
        nm=(p.find('k:name',ns).text or '').strip()
        if not nm or nm[0].isdigit(): continue          # scarta i punti senza nome vero
        if (z, nm.lower()[:12]) in seen: continue
        de=p.find('k:description',ns)
        d=re.sub('<[^>]+>',' ',de.text).strip() if de is not None and de.text else ''
        rows.append(dict(zona=z, tipo=TIPO[fn], nome=nm, lat=lat, lon=lon, quota=None,
                         vento='', diff='', aff='K', cat='Hike & Fly' if fn=='Hike & Fly' else '',
                         note=html.unescape(d), fonte='KML Delbene', disl=None, partenza='',
                         origine='kml'))
        n_kml+=1

json.dump(rows, open('siti.json','w'), ensure_ascii=False)
print(f"curati {len(CURATI)}  +  kml {n_kml}  =  {len(rows)} punti")
