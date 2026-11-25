# -*- coding: utf-8 -*-
"""Dati curati nordest: Friuli (specialita'), Alpi Giulie, Slovenia, Alpago, Bellunese.
Fonti: vololiberofriuli.it, paragliding-bovec.com, paradeltafeltre.it, flytherapy.it,
KML Paragliding Sites di Lorenzo Delbene."""

# aff: V = verificato con fonte | K = solo nel KML | ? = da verificare
CURATI = [

# ===================== 1 FRIULI =====================
dict(zona="1 Friuli", tipo="decollo", nome="Monte Cuarnan", lat=46.2741, lon=13.1758, quota=1200,
     vento="SW-S-SE", diff="4,5/5", aff="V", cat="Decollo ufficiale",
     note="IL SITO DI CASA. Prato ampio, bello e grande. Circa 1000 m di dislivello sulla pianura. "
          "VOLI CONSENTITI CON VENTO DA SUD. Buona attivita' termica ed esposizione: possibili voli "
          "cross in quasi tutte le direzioni. "
          "ACCESSO: da Gemona si sale lungo la STRADA DI FOREDOR fino a Malga Cuarnan, poi a piedi "
          "per un sentiero nel bosco di faggi fino al prato di decollo. "
          "PANORAMA: pianura friulana, il mare nelle giornate limpide, la Carnia verso Tolmezzo, "
          "il San Simeone e la catena dei Musi. "
          "Qui si e' volata la Paragliding World Cup.",
     fonte="vololiberofriuli.it + KML Delbene"),
dict(zona="1 Friuli", tipo="decollo", nome="Monte San Simeone", lat=46.3301, lon=13.1016, quota=1180,
     vento="S", diff="Da principianti a esperti", aff="V", cat="Decollo ufficiale",
     note="Prato ampio che parte da un pianoro e AUMENTA GRADUALMENTE DI PENDENZA. Circa 1000 m di "
          "dislivello sulla pianura. VOLI CONSENTITI CON VENTO DA SUD. "
          "CONDIZIONI: prevalentemente DINAMICA (soaring su pendio), con attivita' termica nei mesi "
          "piu' caldi. Per questo e' adatto a tutti i livelli. "
          "ACCESSO: strada forestale INTERAMENTE ASFALTATA che parte da Bordano. "
          "ATTERRAGGIO di dimensioni considerevoli e libero da ostacoli. "
          "PANORAMA: Bordano, piana del Tagliamento, valle del Lago dei Tre Comuni, Gemona.",
     fonte="vololiberofriuli.it"),
dict(zona="1 Friuli", tipo="atterraggio", nome="Atterraggio Bordano", lat=46.3220, lon=13.1050, quota=230,
     vento="", diff="", aff="V", cat="Atterraggio ufficiale",
     note="REGOLAMENTO ASD VOLO LIBERO FRIULI, v1.0 settembre 2024. "
          "Uso consentito a parapendio, deltaplano, VDS-VL e VDS-VM e alla scuola di volo. "
          "GROUND-HANDLING VIETATO nelle zone 'Atterraggio' e 'Ripiegamento', solo per il tempo "
          "necessario. Vietate altre attivita': picnic, campeggio, giochi con la palla, altri sport. "
          "NON SORVOLARE L'ABITATO DI BORDANO SOTTO I 300 m AGL. "
          "Vietate acrobazie, simulazioni di emergenza e manovre non prudenti sopra centri abitati, "
          "edifici o installazioni. Rispettare le precedenze in atterraggio. "
          "Dopo l'atterraggio ripiegare la vela nella zona 'Ripiegamento'. "
          "Servono attestato, visita medica valida, assicurazione e CASCO. "
          "Corsi, raduni e iniziative di gruppo richiedono autorizzazione preventiva dell'ASD. "
          "Gli incidenti vanno segnalati subito all'ASD. Il soccorso ha priorita' e l'area va sgomberata. "
          "Coordinate approssimative.",
     fonte="vololiberofriuli.it"),
dict(zona="1 Friuli", tipo="atterraggio", nome="Atterraggio Gemona", lat=46.2688, lon=13.1410, quota=200,
     vento="", diff="4/5", aff="V", cat="Atterraggio ufficiale",
     note="Campo grande e bello. In primavera ed estate, NELLE ORE CENTRALI, attenzione alle bolle.",
     fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="decollo", nome="Bernadia", lat=46.2253, lon=13.2638, quota=850,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Esposizione da verificare. Ha il suo atterraggio dedicato.", fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="decollo", nome="Porzus", lat=46.1839, lon=13.3327, quota=700,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Prealpi Giulie meridionali, sopra Attimis. Esposizione da verificare.", fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="decollo", nome="Karcos", lat=46.1046, lon=13.4866, quota=600,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Valli del Natisone, vicino al confine. Esposizione da verificare.", fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="decollo", nome="Stol (versante italiano)", lat=46.2726, lon=13.4731, quota=1400,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Sul confine. Dal lato sloveno e' il Kobariski Stol, molto meglio documentato: "
          "vedi quella scheda per esposizione e accesso.", fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="hike&fly", nome="Hike & Fly Monte Plauris", lat=46.3400, lon=13.1900, quota=1958,
     vento="", diff="", aff="K", cat="Hike & Fly",
     note="Una delle cime grosse delle Prealpi Giulie sopra Venzone. Esposizione da verificare.",
     fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="hike&fly", nome="Hike & Fly Monte Amariana", lat=46.3998, lon=13.0858, quota=1906,
     vento="", diff="", aff="K", cat="Hike & Fly",
     note="La piramide sopra Tolmezzo. Esposizione da verificare.", fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="hike&fly", nome="Hike & Fly Musi", lat=46.3301, lon=13.2603, quota=1600,
     vento="", diff="", aff="K", cat="Hike & Fly",
     note="Catena dei Musi. Ha un atterraggio dedicato nel KML. Esposizione da verificare.",
     fonte="KML Delbene"),
dict(zona="1 Friuli", tipo="hike&fly", nome="Hike & Fly Matajur", lat=46.1750, lon=13.5700, quota=1641,
     vento="", diff="", aff="K", cat="Hike & Fly",
     note="Sul confine sopra Cividale. Dal lato sloveno c'e' il decollo Mrzli vrh-Matajur, "
          "documentato: N-NE, difficolta' 2/5. Esposizione lato italiano da verificare.",
     fonte="KML Delbene"),

# ===================== 2 ALPI GIULIE / TARVISIANO =====================
dict(zona="2 Alpi Giulie", tipo="decollo", nome="Monte Lussari", lat=46.4650, lon=13.5300, quota=1760,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Servito da cabinovia da Camporosso. Ha il suo atterraggio. Esposizione da verificare.",
     fonte="KML Delbene"),
dict(zona="2 Alpi Giulie", tipo="decollo", nome="Canin", lat=46.3600, lon=13.4300, quota=1800,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Lato italiano del Canin, sopra Sella Nevea. Dal lato sloveno c'e' Kanin-Skripi, "
          "documentato. Esposizione lato italiano da verificare.", fonte="KML Delbene"),
dict(zona="2 Alpi Giulie", tipo="hike&fly", nome="Hike & Fly Montasio", lat=46.4214, lon=13.4257, quota=2000,
     vento="", diff="", aff="K", cat="Hike & Fly",
     note="Altopiano del Montasio. Esposizione da verificare.", fonte="KML Delbene"),
dict(zona="2 Alpi Giulie", tipo="decollo", nome="Mittagskogel", lat=46.5065, lon=13.9527, quota=1700,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Lato austriaco, sopra il Worthersee. Esposizione da verificare.", fonte="KML Delbene"),

# ===================== 3 SLOVENIA / POSOCJE =====================
dict(zona="3 Slovenia", tipo="zona", nome="Posocje — regole, tasse e pericoli", lat=46.1800, lon=13.7300,
     quota=0, vento="", diff="", aff="V", cat="Note generali",
     note="TASSE: solo i piloti singoli comprano il biglietto. Giornaliero 4 euro, 3 giorni 11, "
          "10 giorni 20, stagionale 35. Voli organizzati (tandem, scuole, gare) richiedono accordo "
          "con il club che gestisce il decollo. "
          "PUNTI VENDITA a Tolmin: Camp Gabrje, Kobala center, FlyZone Ciginj, Camp Siber, Bar Pri Noni. "
          "A Kobarid: TIC Kobarid, Jazbec Idrsko, Bar Teja. "
          "SPAZIO AEREO: solo classe G, regole VFR. NELLA VALLE DELL'ISONZO IL LIMITE E' 2900 m MSL. "
          "Volo locale non supervisionato: serve livello 4 IPP; per l'XC serve il 5. "
          "FREQUENZA volo libero: 147.800 MHz. Rispettare gli avvisi di arrivo degli elicotteri. "
          "EMERGENZE: 112. Segnalare anche riserve aperte o atterraggi su albero, pure senza bisogno "
          "di aiuto. "
          "PARCO NAZIONALE DEL TRIGLAV: vietato volare sotto i 300 m dal terreno; decollo e atterraggio "
          "vietati tranne che al Mangart (Bovec), a Vogel e a Vogar (Bohinj). "
          "AEROPORTO DI BOVEC: zona di divieto. Il paracadutismo rende la zona molto pericolosa: "
          "PRIMA DI OGNI DECOLLO MANDARE UN SMS AL +386 51 661 003. "
          "BORA: catabatico da nord-est, puo' superare i 150 km/h. Con nuvole alte e 'belle' il decollo "
          "puo' sembrare buono mentre la valle e' molto turbolenta. "
          "VENTO DI VALLE: con forte termica o vento generale forte, evitare voli bassi nelle valli "
          "strette; puo' superare i 10 m/s. Non decollare a Log pod Mangartom dopo le 10 con forte termica. "
          "CAVI: linee elettriche, di trasporto e di carico lungo tutta la valle, soprattutto a bassa "
          "quota. Vicino al Kanin e a ovest di Planja c'e' anche una tirolese. "
          "Esiste un database dei cavi dell'associazione aeronautica slovena.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Kobala (Tolmin)", lat=46.1850, lon=13.7450, quota=1080,
     vento="E, SE, SW, W", diff="2/5", aff="V", cat="Decollo ufficiale",
     note="IL DECOLLO PIU' POPOLARE DELLA VALLE. Si arriva in auto. Club DPL Posocje. "
          "CON VENTO FORTE IL DECOLLO E' RIPIDO E C'E' IL RISCHIO DI ESSERE TRASCINATI OLTRE IL CRINALE. "
          "Ad aprile la strada per Kobala puo' essere ghiacciata in cima. "
          "Atterraggi: Tolmin (ampio, valle larga, il vento di valle di solito non e' un problema), "
          "Camp Gabrje e Camp Siber accanto ai campeggi.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Kobariski Stol", lat=46.2800, lon=13.5200, quota=1414,
     vento="SE, S, SW", diff="1/5", aff="V", cat="Decollo ufficiale",
     note="Prato ampio che ha ospitato molte gare XC. Club Drustvo Adrenalin. "
          "LA STRADA E' DISSESTATA: serve un fuoristrada o il servizio navetta. "
          "Essendo alto, permette voli locali anche in autunno con termiche deboli. "
          "Atterraggio a Kobarid, ampio.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Livski Kuk", lat=46.2450, lon=13.5100, quota=1240,
     vento="N, SE, S, SW", diff="Sud 3/5, Nord 5/5", aff="V", cat="Decollo ufficiale",
     note="Auto o bus piu' 15 min a piedi. Club Drustvo Adrenalin. "
          "NON ATTERRARE A SUD DEL DECOLLO. Attraversare verso OVEST con quota sufficiente per "
          "raggiungere atterraggi sicuri. SE SI PERDE QUOTA, VOLARE VERSO NORD-OVEST SULLA VALLE. "
          "Il lato nord e' 5/5 di difficolta': non e' un decollo da prendere alla leggera.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Mrzli vrh — Matajur", lat=46.1900, lon=13.5900, quota=1320,
     vento="N, NE", diff="2/5", aff="V", cat="Decollo ufficiale",
     note="IL DECOLLO DA VENTO DA NORD della zona. Fuoristrada piu' 5 min a piedi. "
          "Club Drustvo Adrenalin. Valutare il meteo SIA AL DECOLLO SIA IN VALLE. "
          "E' il versante sloveno del Matajur, che dal lato italiano sta sopra Cividale.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Ozben", lat=46.2350, lon=13.6100, quota=750,
     vento="S, SW", diff="1/5", aff="V", cat="Decollo ufficiale",
     note="ACCESSIBILE TUTTO L'ANNO per la bassa quota: e' il ripiego invernale. Fuoristrada. "
          "Club Drustvo Adrenalin. Ha ospitato una Coppa del Mondo e un Campionato europeo di "
          "atterraggio di precisione.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Mangart — Sedlo", lat=46.4350, lon=13.6500, quota=1990,
     vento="E-W", diff="1/5", aff="V", cat="Decollo ufficiale",
     note="Auto o bus piu' 5 min a piedi. Club JPD Kanin. Adatto ai principianti. "
          "MA: con vento forte di valle c'e' un RISCHIO SERIO se si finisce a terra in condizioni "
          "termiche. Atterraggio a Log pod Mangartom, valle stretta in fondo al sistema: "
          "CON VENTO FORTE D'ESTATE E' PERICOLOSO, non decollare dopo le 10 con forte termica. "
          "LA STRADA PER IL MANGART E' SPESSO COPERTA DI NEVE FINO A GIUGNO. "
          "E' una delle tre eccezioni al divieto di decollo nel Parco del Triglav.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Mangart — Tunel (Prhodci)", lat=46.4300, lon=13.6400, quota=1870,
     vento="S-SW", diff="4/5", aff="V", cat="Decollo ufficiale",
     note="Auto o bus. Club JPD Kanin. SI USA QUANDO IL VENTO IN QUOTA E' TROPPO FORTE o quando il "
          "sedlo non e' accessibile per la neve. SOTTO IL DECOLLO C'E' UNA STRADA. "
          "SCONSIGLIATO DECOLLARE CON VENTO NULLO O NEGATIVO.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Kanin — Skripi", lat=46.3580, lon=13.4750, quota=1717,
     vento="SE-SW", diff="3/5", aff="V", cat="Decollo ufficiale",
     note="Funivia piu' 15 min a piedi. Club JPD Kanin. VIETATO DECOLLARE E ATTERRARE NELLA ZONA "
          "DELL'AEROPORTO. Ci sono reti protettive. "
          "AGGIORNAMENTO 1.7.2024: LA FUNIVIA NON FUNZIONA. Per il decollo 'Tee' si sale con la "
          "funivia fino alla stazione B e poi si cammina per circa 600 m di dislivello. "
          "Vicino al Kanin c'e' anche una TIROLESE.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="hike&fly", nome="Planja", lat=46.3450, lon=13.4600, quota=1070,
     vento="E-W", diff="2/5", aff="V", cat="Hike & Fly",
     note="SOLO A PIEDI, almeno 20 minuti. Club JPD Kanin. Usato soprattutto FUORI STAGIONE per voli "
          "XC e per hike & fly. VIETATO DECOLLARE E ATTERRARE NELLA ZONA DELL'AEROPORTO. "
          "A ovest di Planja c'e' una tirolese.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="decollo", nome="Vrse", lat=46.3300, lon=13.5500, quota=580,
     vento="E-W", diff="4/5", aff="V", cat="Decollo ufficiale",
     note="Nato come decollo scuola, ma OGGI E' IN PARTE INVASO DALLA VEGETAZIONE. "
          "Lo usano i piloti esperti quando Kobala e' troppo ventosa. Auto o bus piu' 5 min a piedi. "
          "Club DPL Posocje.",
     fonte="paragliding-bovec.com"),
dict(zona="3 Slovenia", tipo="atterraggio", nome="Bovec (atterraggio)", lat=46.3380, lon=13.5520, quota=440,
     vento="", diff="", aff="V", cat="Atterraggio",
     note="PIU' COMPLICATO degli altri: sta a est della valle, con ostacoli intorno. "
          "Da non confondere con l'aeroporto di Bovec, che e' zona di divieto.",
     fonte="paragliding-bovec.com"),

# ===================== 4 ALPAGO / BELLUNESE =====================
dict(zona="4 Alpago", tipo="decollo", nome="Monte Dolada", lat=46.1917, lon=12.3527, quota=1500,
     vento="SW-S-SE", diff="4/5", aff="V", cat="Decollo ufficiale",
     note="Decollo erboso molto bello, al Rifugio Dolada, base comune dei parapendisti della zona: "
          "si decolla facilmente. Sopra il lago di Santa Croce. "
          "COME HIKE & FLY: si parte dall'atterraggio del DeltaClub Monte Dolada, si attraversa Villa, "
          "poi Pieve e Torres per strade e piste ciclabili; da Torres si prende la vecchia strada "
          "verso Plois e poco dopo il paese il sentiero ben segnato per il Rifugio Dolada. "
          "900 m di dislivello, 6 km, circa 1h45. Decollo S / SW.",
     fonte="KML Delbene + flytherapy.it"),
dict(zona="4 Alpago", tipo="decollo", nome="Nevegal", lat=46.0705, lon=12.2984, quota=1000,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Zona storica di volo sopra Belluno. Flytherapy documenta il Monte Faverghera come hike & fly. "
          "Esposizione da verificare.", fonte="KML Delbene"),
dict(zona="4 Alpago", tipo="decollo", nome="Col Visentin", lat=46.0535, lon=12.2822, quota=1763,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Cima panoramica tra Belluno e il Quartier del Piave. Esposizione da verificare.",
     fonte="KML Delbene"),
dict(zona="4 Alpago", tipo="decollo", nome="Pizzoc", lat=46.0200, lon=12.3700, quota=1565,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="Sopra il Cansiglio. Esposizione da verificare.", fonte="KML Delbene"),
dict(zona="4 Alpago", tipo="decollo", nome="Revine", lat=46.0024, lon=12.2083, quota=900,
     vento="SW-S-SE", diff="4/5", aff="V", cat="Decollo ufficiale",
     note="Decollo erboso molto bello, sopra i laghi di Revine.", fonte="KML Delbene"),
dict(zona="4 Alpago", tipo="decollo", nome="Monte Serva", lat=46.1750, lon=12.2250, quota=2130,
     vento="", diff="", aff="K", cat="Decollo ufficiale",
     note="La montagna di Belluno. Flytherapy la documenta come hike & fly in due versioni "
          "(Monte Serva e Croce Monte Serva). Esposizione da verificare.", fonte="KML Delbene"),

# ===================== 5 VALBELLUNA / FELTRINO =====================
dict(zona="5 Feltrino", tipo="decollo", nome="Monte Avena — Decollo Sud", lat=46.02987, lon=11.82615,
     quota=1417, vento="S / SE", diff="Adatto ai neo-brevettati", aff="V", cat="Decollo ufficiale",
     note="Pascolo MOLTO AMPIO, circa 11.500 m2, senza ostacoli e leggermente inclinato verso valle. "
          "Manica a vento e bacheca. Niente servizi igienici. "
          "CON VENTO DA NORD IL DECOLLO E' SEMPRE VIETATO. Con vento sostenuto da est o ovest, "
          "cambiare decollo secondo la direzione. "
          "In genere non ha turbolenze significative perche' e' SOPRAVENTO rispetto al vento di valle, "
          "che di solito soffia da nord-est verso sud-ovest. Ottimo per i voli mattutini. "
          "IL TOP LANDING E' VIETATO IN ZONA DECOLLO. "
          "Dislivello ~1067 m sull'atterraggio Boscherai. "
          "ACCESSO: direzione Passo Croce d'Aune - Monte Avena, ~15 km da Feltre. "
          "CI SONO POSTI AUTO MA NON SI PARCHEGGIA LUNGO LA STRADA.",
     fonte="paradeltafeltre.it"),
dict(zona="5 Feltrino", tipo="decollo", nome="Monte Avena — Decollo Ovest", lat=46.02961, lon=11.81738,
     quota=1438, vento="S / SW", diff="Primavera: solo esperti", aff="V", cat="Decollo ufficiale",
     note="Vasto prato in leggera pendenza. Manica a vento e bacheca. "
          "CON VENTO DA NORD SEMPRE VIETATO. Con vento sostenuto da sud o ovest, cambiare decollo. "
          "SPESSO SOTTOVENTO rispetto al vento di valle che scorre da Feltre: nelle tipiche condizioni "
          "primaverili E' ADATTO SOLO A PILOTI ESPERTI. "
          "VERSO SERA, DOPO LE 17, diventa piu' tranquillo: si veleggia in dinamica o si trovano "
          "termiche di restituzione sopra la piana tra Fonzaso e Arten. "
          "CON AEROMODELLI IN ZONA e' vietato usare e sorvolare il decollo a loro dedicato. "
          "Dal Decollo Sud, circa 1 km su strada sterrata. Dislivello ~1088 m.",
     fonte="paradeltafeltre.it"),
dict(zona="5 Feltrino", tipo="decollo", nome="Monte Avena — Decollo Est", lat=46.03386, lon=11.83082,
     quota=1351, vento="E", diff="", aff="V", cat="Decollo ufficiale",
     note="Prato in leggera pendenza, SPAZIO PER APRIRE 5 O 6 VELE. Manica a vento. "
          "Con vento sostenuto da sud o ovest, cambiare decollo secondo la direzione. "
          "Sta circa 500 m prima del Decollo Sud; posti auto al Decollo Sud. Dislivello ~1084 m.",
     fonte="paradeltafeltre.it"),
dict(zona="5 Feltrino", tipo="atterraggio", nome="Boscherai (Pedavena)", lat=46.03145, lon=11.87945,
     quota=350, vento="", diff="", aff="V", cat="Atterraggio ufficiale",
     note="L'ATTERRAGGIO UFFICIALE. Rettangolo di circa 20.000 m2 senza ostacoli, nell'area sportiva "
          "del Boscherai a Pedavena. PERMETTE ATTERRAGGI SICURI CON QUALSIASI DIREZIONE DI VENTO. "
          "Posti auto, SERVIZI IGIENICI E DOCCIA, tre maniche a vento, bacheca. "
          "Dal KML: campo grande e bello, su una collina piatta alta 20 m rispetto alla piana "
          "circostante; in primavera ed estate attenzione alle bolle nelle ore centrali.",
     fonte="paradeltafeltre.it + KML Delbene"),
dict(zona="5 Feltrino", tipo="atterraggio", nome="Arten", lat=46.00419, lon=11.82416, quota=311,
     vento="E / SE", diff="", aff="V", cat="Atterraggio",
     note="30 m di larghezza per 200 m di lunghezza, orientato est-ovest, con ampie possibilita' di fuga. "
          "Zona artigianale di Arten, posti auto, manica a vento, niente servizi. "
          "Il vento di solito soffia da est o sud-est. NEL POMERIGGIO PUO' ESSERE MOLTO SOSTENUTO: "
          "attenzione per i principianti. "
          "I deltaplanisti devono verificare le condizioni di atterraggio prima di andare in volo.",
     fonte="paradeltafeltre.it"),
]

# ---- VINCOLI DI VOLO: settori in cui il sito funziona, in gradi ----
VINCOLI = {
 "1 Friuli": [
   dict(sito="Monte Cuarnan", settori=[(135,247)], vietati=[(315,360),(0,45)], max_v=25, max_giallo=33,
        nota="Voli consentiti con vento da sud. Cross in quasi tutte le direzioni"),
   dict(sito="Monte San Simeone", settori=[(135,225)], vietati=[(315,360),(0,45)], max_v=25, max_giallo=33,
        nota="Vento da sud. Prevalentemente dinamica, termica nei mesi caldi"),
   dict(sito="Bernadia", settori=[(0,360)], vietati=[], max_v=25, max_giallo=33,
        nota="Esposizione non documentata: verifica sul posto"),
   dict(sito="Porzus", settori=[(0,360)], vietati=[], max_v=25, max_giallo=33,
        nota="Esposizione non documentata"),
 ],
 "3 Slovenia": [
   dict(sito="Kobala (Tolmin)", settori=[(45,157),(202,292)], vietati=[], max_v=22, max_giallo=30,
        nota="Con vento forte il decollo e' ripido: rischio di essere trascinati oltre il crinale"),
   dict(sito="Kobariski Stol", settori=[(112,247)], vietati=[], max_v=25, max_giallo=35,
        nota="Prato ampio da gara. Strada dissestata, serve fuoristrada"),
   dict(sito="Mrzli vrh — Matajur", settori=[(315,360),(0,67)], vietati=[], max_v=22, max_giallo=30,
        nota="IL decollo da nord della zona"),
   dict(sito="Ozben", settori=[(157,247)], vietati=[], max_v=22, max_giallo=30,
        nota="Basso: il ripiego di tutto l'anno"),
   dict(sito="Livski Kuk", settori=[(315,360),(0,45),(112,247)], vietati=[], max_v=22, max_giallo=28,
        nota="Lato nord 5/5. Non atterrare a sud del decollo"),
   dict(sito="Mangart — Sedlo", settori=[(45,135),(225,315)], vietati=[], max_v=20, max_giallo=27,
        nota="Rischio serio se finisci a terra in termica. Strada innevata fino a giugno"),
   dict(sito="Kanin — Skripi", settori=[(112,247)], vietati=[], max_v=22, max_giallo=30,
        nota="Funivia ferma dal 2024: 600 m a piedi dalla stazione B"),
 ],
 "4 Alpago": [
   dict(sito="Monte Dolada", settori=[(135,247)], vietati=[], max_v=25, max_giallo=33,
        nota="Decollo al Rifugio Dolada, facile"),
   dict(sito="Revine", settori=[(135,247)], vietati=[], max_v=25, max_giallo=33, nota=""),
   dict(sito="Col Visentin", settori=[(0,360)], vietati=[], max_v=25, max_giallo=33,
        nota="Esposizione non documentata"),
 ],
 "5 Feltrino": [
   dict(sito="Monte Avena — Decollo Sud", settori=[(135,202)], vietati=[(315,360),(0,45)],
        max_v=25, max_giallo=33, nota="Con nord SEMPRE VIETATO. Sopravento al vento di valle"),
   dict(sito="Monte Avena — Decollo Ovest", settori=[(180,247)], vietati=[(315,360),(0,45)],
        max_v=22, max_giallo=30, nota="Con nord SEMPRE VIETATO. Spesso sottovento: in primavera solo esperti"),
   dict(sito="Monte Avena — Decollo Est", settori=[(45,135)], vietati=[], max_v=22, max_giallo=30,
        nota="Spazio per 5-6 vele"),
 ],
}

# ---- GITE ----
GITE = [
 dict(nome="Cuarnan da Gemona", zona="1 Friuli", cat="Hike & Fly", disl=1000, ore="2h30",
      punti=["Monte Cuarnan","Atterraggio Gemona"],
      testo="Il giro di casa. Si sale per la Strada di Foredor fino a Malga Cuarnan e poi a piedi "
            "nel bosco di faggi fino al prato. Circa 1000 m di dislivello sulla pianura. "
            "Si vola con vento da sud e si atterra a Gemona, dove hai lasciato l'auto. "
            "Attenzione alle bolle nelle ore centrali in primavera ed estate."),
 dict(nome="San Simeone da Bordano", zona="1 Friuli", cat="Cross", disl=950, ore="2h",
      punti=["Monte San Simeone","Atterraggio Bordano"],
      testo="Strada forestale interamente asfaltata da Bordano, quindi ci arrivi anche in auto. "
            "Il decollo e' dinamico prima ancora che termico, quindi regge anche le giornate magre. "
            "All'atterraggio vale il regolamento ASD: niente ground-handling nelle zone atterraggio e "
            "ripiegamento, e non si sorvola Bordano sotto i 300 m."),
 dict(nome="Dolada in hike & fly", zona="4 Alpago", cat="Hike & Fly", disl=900, ore="1h45",
      punti=["Monte Dolada"],
      testo="Si parte dall'atterraggio del DeltaClub Monte Dolada, si attraversa Villa, poi Pieve e "
            "Torres per strade e ciclabili, da Torres la vecchia strada verso Plois e poi il sentiero "
            "segnato per il Rifugio Dolada. 6 km, 900 m, circa un'ora e tre quarti. Decollo S/SW. "
            "Chiudi il cerchio atterrando dove hai lasciato l'auto."),
 dict(nome="Kobala, il classico di Tolmin", zona="3 Slovenia", cat="Cross", disl=0, ore="",
      punti=["Kobala (Tolmin)","Posocje — regole, tasse e pericoli"],
      testo="Il decollo piu' popolare della valle dell'Isonzo, ci si arriva in auto. "
            "Biglietto giornaliero 4 euro, si compra al Camp Gabrje, al Kobala center, a FlyZone Ciginj, "
            "al Camp Siber o al Bar Pri Noni. Tetto di spazio aereo a 2900 m MSL. "
            "Con vento forte il decollo e' ripido e si rischia di essere trascinati oltre il crinale."),
 dict(nome="Stol di Kobarid", zona="3 Slovenia", cat="Cross", disl=0, ore="",
      punti=["Kobariski Stol","Posocje — regole, tasse e pericoli"],
      testo="Prato ampio che ha ospitato molte gare XC, esposto SE-S-SW. "
            "La strada e' dissestata: fuoristrada o navetta. Essendo alto regge anche in autunno, "
            "quando le termiche si fanno deboli. Biglietto a Kobarid: TIC, Jazbec Idrsko o Bar Teja."),
 dict(nome="Mangart, quando c'e' la neve in basso", zona="3 Slovenia", cat="Cross", disl=0, ore="",
      punti=["Mangart — Sedlo","Mangart — Tunel (Prhodci)"],
      testo="Il Sedlo a 1990 m e' facile e adatto anche ai principianti, ma con vento forte di valle "
            "il rischio e' serio se finisci a terra in termica. Non decollare dopo le 10 con forte "
            "attivita'. Se il vento in quota e' troppo o la neve chiude il sedlo, si ripiega sul Tunel "
            "a 1870, S-SW, ma li' sotto il decollo c'e' una strada e col vento nullo meglio lasciar perdere. "
            "La strada e' spesso innevata fino a giugno."),
 dict(nome="Monte Avena, tre decolli per tre venti", zona="5 Feltrino", cat="Cross", disl=0, ore="",
      punti=["Monte Avena — Decollo Sud","Monte Avena — Decollo Ovest","Monte Avena — Decollo Est",
             "Boscherai (Pedavena)"],
      testo="Sud per il mattino e per chi e' agli inizi, Ovest dopo le 17 quando si calma e si veleggia "
            "sopra la piana tra Fonzaso e Arten, Est quando gira. "
            "CON VENTO DA NORD SUD E OVEST SONO SEMPRE VIETATI. "
            "Si atterra al Boscherai, 20.000 m2 che accettano qualsiasi direzione, con docce."),
]

# gite di flytherapy.it, lato bellunese: nome, zona, link
GITE_FLYTHERAPY = [
 ("Monte Serva","Valbelluna","monte-serva-parapendio"), ("Montanel","Cadore","montanel"),
 ("Monte Terne","Valbelluna","monte-terne"), ("Monte Guslon","Alpago","monte-guslon"),
 ("Monte Talvena","Valbelluna","monte-talvena"), ("Monte Dolada","Alpago","monte-dolada"),
 ("Monte Antelao","Cadore","monte-antelao"), ("Monte Tranego","Cadore","tranego"),
 ("Monte Palmar","Valbelluna","monte-palmar"), ("Bivacco Spagnolli","Cadore","bivacco-spagnolli"),
 ("Monte Grave","Valbelluna","monte-grave"), ("Casera Zervoi","Valbelluna","casera-zervoi"),
 ("Casera Busnich","Longarone-Zoldo","casera-busnich"), ("Rifugio Scarpa","Agordino","rifugio-scarpa"),
 ("Bivacco Toffolon","Alpago","bivacco-toffolon"), ("Cima Coldai","Longarone-Zoldo","cima-coldai"),
 ("Monte Rite","Longarone-Zoldo","monte-ritte"), ("Col Rosson","Comelico-Sappada","col-rosson"),
 ("Monte Porgeit","Longarone-Zoldo","monte-porgeit"),
 ("Monte Faverghera Nevegal","Alpago / Valbelluna","monte-faverghera-nevegal"),
 ("Croce Monte Serva","Valbelluna","croce-monte-serva"), ("Sappada 2000","Comelico-Sappada","sappada-2000"),
 ("Casera Colon","Longarone-Zoldo","casera-colon"), ("Monte Simone","Cadore","monte-simone"),
 ("Monte Avena","Valbelluna","monte-avena"),
]

PUNTI_METEO = {
 "Gemona / Cuarnan": (46.27, 13.16),
 "Tolmezzo / Carnia": (46.40, 13.02),
 "Tarvisio / Alpi Giulie": (46.46, 13.53),
 "Tolmin / Kobala": (46.19, 13.74),
 "Kobarid / Stol": (46.25, 13.58),
 "Alpago / Dolada": (46.15, 12.35),
 "Belluno / Nevegal": (46.10, 12.28),
 "Feltre / Monte Avena": (46.03, 11.83),
}

FONTI = [
 ("vololiberofriuli.it","Cuarnan e San Simeone, regolamento atterraggio Bordano","Friuli"),
 ("visitgemona.com","Pagina volo del comune di Gemona","Friuli"),
 ("paragliding-bovec.com","Guida completa Posocje: 10 decolli, tasse, regole, pericoli","Slovenia"),
 ("drustvo-adrenalin.si","Club di Kobarid: Stol, Ozben, Livski Kuk, Mrzli vrh","Slovenia"),
 ("paraglidingmap.com","Schede siti Kobarid e Tolmin","Slovenia"),
 ("paradeltafeltre.it","Monte Avena: tre decolli e due atterraggi con coordinate","Feltrino"),
 ("flytherapy.it","25 schede hike & fly bellunesi con dislivello e tempi","Bellunese"),
 ("komoot","Collection 'Hike&Fly Val Belluna, Alpago e Prealpi Venete'","Bellunese"),
 ("fivl.it","Federazione Italiana Volo Libero, tag hike-fly","Italia"),
 ("camptocamp.org","Waypoint tipo Decollage, copre anche Alpi Giulie e Slovenia","Tutto"),
 ("XContest","Decolli reali estratti dai tracciati","Tutto"),
 ("thermal.kk7.ch","Termiche e traiettorie aggregate","Tutto"),
 ("paraglidingearth.com","Database collaborativo, export solo GPX, max 99 siti","Tutto"),
 ("meteo-parapente.com","Vento di gradiente per quota, top termico, strato limite","Meteo"),
 ("ARPA FVG OSMER","Previsioni e radar regionali","Meteo"),
 ("camminaevola.it","MORTO: il dominio non risolve piu' dal 2026. Gli hike & fly carnici "
  "sopravvivono dentro il KML di Lorenzo Delbene","Friuli"),
]

NOTE_AREA = [
 ("Friuli", "Due decolli ufficiali principali, Cuarnan e San Simeone, entrambi esposti a sud e con "
            "circa 1000 m di dislivello sulla pianura. Il grosso del potenziale non ufficiale sta nei "
            "25 hike & fly carnici che trovi nel KML: Clapsavon, Tinisa, Pleros, Raut, Lovinzola, "
            "Creta di Mimoias, Amariana, Plauris, Musi. Di quelli non esiste documentazione pubblica "
            "di esposizione: vanno ricavati dalla carta, da camptocamp o dai tracciati XContest."),
 ("Slovenia", "La zona meglio documentata di tutte. Dieci decolli ufficiali con esposizione, "
              "difficolta' da 1 a 5, club di riferimento e tariffe. Occhio al tetto di spazio aereo "
              "a 2900 m, al Parco del Triglav e all'SMS obbligatorio per l'aeroporto di Bovec."),
 ("Alpago e bellunese", "Dolada e Revine hanno esposizione nota, il resto no. "
                        "Flytherapy copre 25 gite hike & fly con dislivello e tempi, ma solo lato "
                        "bellunese: in Friuli non ha niente."),
 ("Feltrino", "Il Para&Delta Club Feltre e' l'unico ad avere pubblicato tutto: tre decolli e due "
              "atterraggi con coordinate al quinto decimale, regole e condizioni. "
              "Il modello di come dovrebbero essere documentati tutti gli altri."),
]

# ======================================================================
# APP
# ======================================================================
import json, math, os, urllib.request, urllib.parse
from datetime import datetime
import pandas as pd
import streamlit as st
import pydeck as pdk

st.set_page_config(page_title="Nordest — volo e montagna", page_icon="\U0001FA82", layout="centered")
BASE = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def carica():
    with open(os.path.join(BASE, "siti_ne.json"), encoding="utf-8") as f:
        return pd.DataFrame(json.load(f))

df = carica()

STILI = {
    "decollo":     dict(rgb=[230,  57,  70], eti="Decollo ufficiale"),
    "hike&fly":    dict(rgb=[255, 183,   3], eti="Hike & Fly"),
    "atterraggio": dict(rgb=[ 42, 157, 143], eti="Atterraggio"),
    "impianto":    dict(rgb=[157,  78, 221], eti="Impianto"),
    "parcheggio":  dict(rgb=[168, 162, 158], eti="Parcheggio"),
    "zona":        dict(rgb=[  0,   0,   0], eti="Regole / spazio aereo"),
}
CAMPI = ["nome","note","vento","difficolta","partenza","categoria","fonte","zona"]
ORDINE = ["1 Friuli","2 Alpi Giulie","3 Slovenia","4 Alpago","5 Feltrino",
          "6 Pordenonese / Carnia ovest","7 Veneto (Bassano/Marostica)","8 Austria / Carinzia"]

def rgb(t):  return STILI.get(t, {}).get("rgb", [136,136,136])
def hexa(t): return "#%02x%02x%02x" % tuple(rgb(t))
def eti(t):  return STILI.get(t, {}).get("eti", t)

def dist_km(a, b, c, d):
    return math.hypot((a-c)*111, (b-d)*111*math.cos(math.radians((a+c)/2)))

def val(r, c):
    v = r[c] if c in r.index else None
    return "" if v is None or (isinstance(v, float) and pd.isna(v)) else v

def riassunto(r):
    p = []
    if val(r,"quota"): p.append(f"{int(r['quota'])} m")
    if val(r,"vento"): p.append(f"\U0001F9ED {r['vento']}")
    if val(r,"disl"):  p.append(f"↗ {int(r['disl'])} m")
    if val(r,"difficolta"): p.append(str(r["difficolta"])[:34])
    return " · ".join(p)

def pallino(t):
    return (f"<span style='display:inline-block;width:11px;height:11px;border-radius:50%;"
            f"background:{hexa(t)};border:1px solid #bbb;margin-right:6px'></span>")

def scheda(r):
    st.markdown(pallino(r["tipo"]) + f"<b>{r['nome']}</b> <small>· {eti(r['tipo'])}</small>",
                unsafe_allow_html=True)
    riga = riassunto(r)
    if riga: st.markdown(f"**{riga}**")
    if val(r,"partenza"):  st.markdown(f"**Partenza:** {r['partenza']}")
    if val(r,"categoria"): st.caption(r["categoria"])
    if val(r,"note"):      st.write(r["note"])
    aff = {"V":"✅ verificato con fonte","K":"\U0001F7E1 solo KML",
           "?":"❓ da verificare"}.get(val(r,"aff"), "")
    st.caption(f"{aff} — fonte: {val(r,'fonte')}  ·  `{r['lat']:.5f}, {r['lon']:.5f}`")
    st.markdown(
        f"[Maps](https://www.google.com/maps/search/?api=1&query={r['lat']},{r['lon']}) · "
        f"[Organic Maps](om://map?v=1&ll={r['lat']},{r['lon']}&n={r['nome']}) · "
        f"[meteo-parapente](https://meteo-parapente.com/#/{r['lat']},{r['lon']},11)")

def cardinale(v):
    pts = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return pts[int((v % 360)/22.5 + 0.5) % 16] if pd.notna(v) else "—"

def in_settore(deg, settori):
    if pd.isna(deg): return False
    d = deg % 360
    for a, b in settori:
        if a <= b and a <= d <= b: return True
        if a > b and (d >= a or d <= b): return True
    return False

def giudizio(v, deg, s):
    if pd.isna(v): return "·", "dati mancanti"
    if in_settore(deg, s["vietati"]):  return "\U0001F534", "direzione vietata"
    if not in_settore(deg, s["settori"]): return "\U0001F534", "fuori settore"
    if v <= s["max_v"]:      return "\U0001F7E2", f"{v:.0f} km/h, in settore"
    if v <= s["max_giallo"]: return "\U0001F7E1", f"{v:.0f} km/h, al limite"
    return "\U0001F534", f"{v:.0f} km/h, troppo vento"

@st.cache_data(ttl=900, show_spinner=False)
def meteo(la, lo):
    p = urllib.parse.urlencode({
        "latitude": la, "longitude": lo, "timezone": "auto", "forecast_days": 14,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,"
                 "precipitation_probability_max,windspeed_10m_max",
        "hourly": "windspeed_700hPa,winddirection_700hPa,freezing_level_height,cloudcover",
    })
    with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?" + p, timeout=20) as f:
        d = json.load(f)
    d["_scaricato"] = datetime.now().strftime("%d/%m %H:%M")
    return d

def meteo_giorno(la, lo):
    """Ritorna (df_giorni, quando) con media 12-16 del vento a 700 hPa."""
    d = meteo(la, lo)
    hh = pd.DataFrame(d["hourly"]); hh["time"] = pd.to_datetime(hh["time"])
    h = hh[hh["time"].dt.hour.between(12, 16)].copy(); h["g"] = h["time"].dt.date
    ag = h.groupby("g").agg(v=("windspeed_700hPa","mean"), dr=("winddirection_700hPa","mean"),
                            zt=("freezing_level_height","mean"), nuv=("cloudcover","mean")).reset_index()
    dd = pd.DataFrame(d["daily"]); dd["time"] = pd.to_datetime(dd["time"]); dd["g"] = dd["time"].dt.date
    return dd.merge(ag, on="g", how="left"), d.get("_scaricato")

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### Filtri")
    zone_d = [z for z in ORDINE if z in set(df["zona"])]
    z_sel = st.multiselect("Zona", zone_d,
                           default=[z for z in zone_d if not z.startswith(("7 ","8 "))])
    tipi = sorted(df["tipo"].unique())
    t_sel = st.multiselect("Tipo", tipi, format_func=eti,
                           default=[t for t in ["decollo","hike&fly","atterraggio","zona"] if t in tipi])
    solo_note = st.checkbox("Solo punti con note vere", value=False)
    st.markdown("---")
    disl_max = st.slider("Dislivello massimo a piedi (m)", 300, 2600, 2600, 100)
    st.caption("Cross ≤1200 · Alpinismo ≤2400")
    st.markdown("---")
    pos = st.text_input("La tua posizione — lat, lon", placeholder="46.27, 13.14")

sel = df[df["zona"].isin(z_sel) & df["tipo"].isin(t_sel)].copy()
if solo_note:
    sel = sel[(sel["origine"]=="curato") | (sel["note"].astype(str).str.len() > 20)]
qui = None
if pos.strip():
    try:
        a, b = [float(x) for x in pos.replace(";", ",").split(",")[:2]]
        qui = (a, b)
        if len(sel):
            sel["dist"] = [dist_km(a,b,la,lo) for la,lo in zip(sel["lat"], sel["lon"])]
            sel = sel.sort_values("dist")
    except Exception:
        st.sidebar.error("Formato: 46.27, 13.14")
sel = sel.reset_index(drop=True)

# ---------------------------------------------------------------- nav
SEZIONI = ["\U0001F1EE\U0001F1F9 Friuli", "\U0001F1F8\U0001F1EE Slovenia",
           "\U0001F3D4️ Alpago e bellunese", "\U0001F5FA️ Mappa", "\U0001F4CB Elenco",
           "\U0001F97E Gite", "\U0001F324️ Meteo", "\U0001F527 Info"]
sezione = st.selectbox("Sezione", SEZIONI, index=0, key="nav")
st.caption("Friuli · Alpago · bellunese · Slovenia di confine — volo, hike & fly, montagna")
st.divider()

def mappa_di(blocco, zoom=8.5):
    m = blocco.dropna(subset=["lat","lon"]).copy()
    if not len(m):
        st.info("Nessun punto con questi filtri."); return
    m["col"] = [rgb(t) for t in m["tipo"]]
    m["rad"] = [{"decollo":420,"hike&fly":400,"zona":460}.get(t, 240) for t in m["tipo"]]
    m["etichetta"] = [eti(t) for t in m["tipo"]]
    m["sotto"] = [riassunto(r) or "—" for _, r in m.iterrows()]
    st.pydeck_chart(pdk.Deck(
        layers=[pdk.Layer("ScatterplotLayer",
                          data=m[["lat","lon","col","rad","nome","etichetta","sotto"]],
                          get_position=["lon","lat"], get_fill_color="col", get_radius="rad",
                          radius_min_pixels=6, radius_max_pixels=20, pickable=True,
                          auto_highlight=True, stroked=True, get_line_color=[255,255,255],
                          line_width_min_pixels=1)],
        map_style=None,
        initial_view_state=pdk.ViewState(latitude=float(m["lat"].mean()),
                                         longitude=float(m["lon"].mean()), zoom=zoom),
        tooltip={"html": "<b>{nome}</b><br/>{etichetta}<br/>{sotto}"}))
    cols = st.columns(3)
    for i, t in enumerate([t for t in STILI if t in set(m["tipo"])]):
        cols[i % 3].markdown(pallino(t) + f"<small>{eti(t)}</small>", unsafe_allow_html=True)

def sezione_zona(nome_zona, punto_meteo, intro=""):
    B = sel[sel["zona"] == nome_zona]
    if intro: st.caption(intro)
    vin = {v["sito"]: v for v in VINCOLI.get(nome_zona, [])}

    def vincolo_per(n):
        from_k = " ".join(str(n).lower().split())
        for k, v in vin.items():
            kk = " ".join(k.lower().split())
            if kk == from_k or kk in from_k or from_k in kk: return v
        return None

    ok, vs, ds = False, None, None
    try:
        t, quando = meteo_giorno(*punto_meteo)
        gg = list(t["g"])[:12]
        gsel = st.select_slider("Giorno (meteo live)", gg, value=gg[0],
                                format_func=lambda x: pd.Timestamp(x).strftime("%a %d/%m"),
                                key=f"g_{nome_zona}")
        rg = t[t["g"] == gsel].iloc[0]
        vs, ds = rg["v"], rg["dr"]; ok = pd.notna(vs)
        c1, c2, c3 = st.columns(3)
        c1.metric("Vento 700 hPa", f"{vs:.0f} km/h" if ok else "—")
        c2.metric("Direzione", cardinale(ds))
        c3.metric("Pioggia", f"{rg['precipitation_probability_max']:.0f}%"
                  if pd.notna(rg["precipitation_probability_max"]) else "—")
        st.caption(f"Media 12-16. Ultimo scaricamento: {quando}")
    except Exception:
        st.caption("Meteo non raggiungibile: i semafori restano spenti.")

    def badge(n):
        if not ok: return ""
        v = vincolo_per(n)
        return giudizio(vs, ds, v)[0] if v else "⚪"

    st.divider()
    m1, m2, m3 = st.columns(3)
    dec = B[B["tipo"]=="decollo"]; hef = B[B["tipo"]=="hike&fly"]; att = B[B["tipo"]=="atterraggio"]
    m1.metric("Decolli", len(dec)); m2.metric("Hike & Fly", len(hef)); m3.metric("Atterraggi", len(att))
    mappa_di(B, zoom=9)

    for titolo, blocco, nota in [
        ("\U0001FA82 Decolli ufficiali", dec, "Siti censiti da club e federazioni."),
        ("\U0001F97E Hike & Fly", hef, "Molti vengono dal KML senza note: il punto c'è, "
                                        "l'esposizione va ricavata da carta, camptocamp o XContest."),
        ("\U0001F3AF Atterraggi", att, ""),
        ("⚠️ Regole e spazio aereo", B[B["tipo"]=="zona"], "")]:
        if not len(blocco): continue
        st.divider(); st.markdown(f"#### {titolo}")
        if nota: st.caption(nota)
        for _, r in blocco.sort_values("nome").iterrows():
            v = val(r,"vento") or "esposizione da verificare"
            q = f" · {int(r['quota'])} m" if val(r,"quota") else ""
            cap = f"{badge(r['nome'])} {r['nome']}"
            if r["tipo"] in ("decollo","hike&fly"): cap += f" — \U0001F9ED {v}{q}"
            with st.expander(cap):
                vk = vincolo_per(r["nome"])
                if ok and vk:
                    ic, why = giudizio(vs, ds, vk)
                    st.markdown(f"{ic} **giorno scelto:** {why}" + (f". {vk['nota']}" if vk["nota"] else ""))
                scheda(r)

    gz = [g for g in GITE if g["zona"] == nome_zona]
    if gz:
        st.divider(); st.markdown("#### \U0001F97E Gite della zona")
        for g in gz:
            meta = [g["cat"]] + ([f"↗ {g['disl']} m"] if g["disl"] else []) + ([g["ore"]] if g["ore"] else [])
            with st.expander(g["nome"]):
                st.caption(" · ".join(meta)); st.write(g["testo"])
                for p in g["punti"]:
                    riga = df[df["nome"] == p]
                    if len(riga):
                        rr = riga.iloc[0]
                        st.markdown(pallino(rr["tipo"]) + f"**{rr['nome']}** "
                                    f"<small>{eti(rr['tipo'])}</small> — {riassunto(rr)}",
                                    unsafe_allow_html=True)

# ---------------------------------------------------------------- sezioni
if sezione == SEZIONI[0]:
    st.markdown("### Friuli — Prealpi Giulie e Carnia")
    sezione_zona("1 Friuli", PUNTI_METEO["Gemona / Cuarnan"],
                 "Cuarnan e San Simeone sono i due decolli ufficiali: entrambi sud, entrambi "
                 "circa 1000 m sulla pianura. Il resto è potenziale da verificare.")
    st.divider()
    st.markdown("#### ⛰️ Alpi Giulie e Tarvisiano")
    B2 = sel[sel["zona"] == "2 Alpi Giulie"]
    if len(B2):
        mappa_di(B2, zoom=10)
        for _, r in B2.sort_values("nome").iterrows():
            with st.expander(f"{r['nome']}" + (f" — {int(r['quota'])} m" if val(r,"quota") else "")):
                scheda(r)
    st.divider()
    st.markdown("#### \U0001F332 Pordenonese e Carnia ovest")
    B6 = sel[sel["zona"] == "6 Pordenonese / Carnia ovest"]
    st.caption(f"{len(B6)} punti, quasi tutti hike & fly dal KML. È il giacimento più grosso "
               "di decolli non ufficiali di tutto il nordest.")
    if len(B6):
        mappa_di(B6, zoom=9.5)
        for _, r in B6.sort_values("nome").iterrows():
            with st.expander(f"{eti(r['tipo'])} — {r['nome']}"):
                scheda(r)

elif sezione == SEZIONI[1]:
    st.markdown("### Slovenia — Posočje, valle dell'Isonzo")
    sezione_zona("3 Slovenia", PUNTI_METEO["Tolmin / Kobala"],
                 "La zona meglio documentata: dieci decolli con esposizione, difficoltà da 1 a 5 "
                 "e club di riferimento. Leggi prima la scheda delle regole.")

elif sezione == SEZIONI[2]:
    st.markdown("### Alpago, bellunese e feltrino")
    sezione_zona("4 Alpago", PUNTI_METEO["Alpago / Dolada"])
    st.divider()
    st.markdown("### Feltrino — Monte Avena")
    sezione_zona("5 Feltrino", PUNTI_METEO["Feltre / Monte Avena"],
                 "Il Para&Delta Club Feltre è l'unico ad aver pubblicato tutto con le coordinate.")
    st.divider()
    st.markdown("#### \U0001F97E Le 25 gite di Flytherapy")
    st.caption("Schede con dislivello e tempi, lato bellunese. In Friuli non hanno niente.")
    for nome_g, zona_g, slug in GITE_FLYTHERAPY:
        st.markdown(f"• **{nome_g}** <small>{zona_g}</small> — "
                    f"[scheda](https://www.flytherapy.it/portfolio_page/{slug}/)",
                    unsafe_allow_html=True)

elif sezione == SEZIONI[3]:
    st.caption(f"{len(sel)} punti")
    mappa_di(sel, zoom=7.6)

elif sezione == SEZIONI[4]:
    q = st.text_input("Cerca", placeholder="bora, cavi, tirolese, navetta, biglietto, vietato...")
    vis = sel
    if q and len(vis):
        ql = q.lower()
        vis = vis[[any(ql in str(r[c]).lower() for c in CAMPI if c in vis.columns)
                   for _, r in vis.iterrows()]]
    if len(vis): vis = vis[vis["disl"].isna() | (vis["disl"] <= disl_max)]
    st.caption(f"{len(vis)} risultati")
    for z in [z for z in ORDINE if z in set(vis["zona"])]:
        st.markdown(f"#### {z}")
        for _, r in vis[vis["zona"] == z].sort_values("nome").iterrows():
            coda = riassunto(r)
            if "dist" in r.index and pd.notna(r["dist"]):
                coda = (coda + " · " if coda else "") + f"{r['dist']:.0f} km"
            with st.expander(f"{r['nome']}" + (f"  ·  {coda}" if coda else "")):
                scheda(r)

elif sezione == SEZIONI[5]:
    cats = sorted({g["cat"] for g in GITE})
    cat = st.multiselect("Categoria", cats, default=cats)
    gz = [g for g in GITE if g["cat"] in cat and (not g["disl"] or g["disl"] <= disl_max)]
    st.caption(f"{len(gz)} gite curate")
    for g in gz:
        meta = [g["zona"], g["cat"]] + ([f"↗ {g['disl']} m"] if g["disl"] else []) \
               + ([g["ore"]] if g["ore"] else [])
        with st.expander(g["nome"]):
            st.caption(" · ".join(meta)); st.write(g["testo"])
            for p in g["punti"]:
                riga = df[df["nome"] == p]
                if len(riga):
                    rr = riga.iloc[0]
                    st.markdown(pallino(rr["tipo"]) + f"**{rr['nome']}** "
                                f"<small>{eti(rr['tipo'])}</small> — {riassunto(rr)}",
                                unsafe_allow_html=True)
    st.divider()
    st.markdown("#### Flytherapy — 25 gite bellunesi")
    for nome_g, zona_g, slug in GITE_FLYTHERAPY:
        st.markdown(f"• **{nome_g}** <small>{zona_g}</small> — "
                    f"[scheda](https://www.flytherapy.it/portfolio_page/{slug}/)",
                    unsafe_allow_html=True)

elif sezione == SEZIONI[6]:
    ca, cb = st.columns([3,1])
    ca.caption("Dati Open-Meteo, si riscaricano ogni 15 minuti.")
    if cb.button("\U0001F504 Aggiorna", use_container_width=True):
        meteo.clear(); st.rerun()
    modo = st.radio("Vista", ["Windy", "Semaforo", "Una località"], horizontal=True,
                    label_visibility="collapsed")
    if modo == "Windy":
        import streamlit.components.v1 as components
        LIV = {"Superficie":"surface","850 hPa (~1500 m)":"850h","700 hPa (~3000 m)":"700h",
               "600 hPa (~4200 m)":"600h","500 hPa (~5500 m)":"500h"}
        STR = {"Vento":"wind","Raffiche":"gust","Nuvole":"clouds","Pioggia":"rain",
               "Temperatura":"temp","CAPE":"cape","Neve fresca":"snowAccu","Isoterma zero":"deg0"}
        c1, c2 = st.columns(2)
        luogo = c1.selectbox("Centro mappa", list(PUNTI_METEO))
        strato = c2.selectbox("Strato", list(STR))
        liv = st.select_slider("Quota", list(LIV), value="700 hPa (~3000 m)")
        wla, wlo = PUNTI_METEO[luogo]
        components.iframe(
            f"https://embed.windy.com/embed2.html?lat={wla}&lon={wlo}&detailLat={wla}"
            f"&detailLon={wlo}&zoom=8&level={LIV[liv]}&overlay={STR[strato]}&product=ecmwf"
            "&menu=&message=true&marker=true&calendar=now&pressure=&type=map"
            "&location=coordinates&detail=true&metricWind=km%2Fh&metricTemp=%C2%B0C&radarRange=-1",
            height=520)
        st.markdown(f"[Schermo intero](https://www.windy.com/{wla}/{wlo}?{STR[strato]},{wla},{wlo},8) "
                    f"· [meteo-parapente](https://meteo-parapente.com/#/{wla},{wlo},11)")
    elif modo == "Semaforo":
        st.caption("Ogni decollo confrontato con le sue regole di vento, sul gradiente 700 hPa "
                   "della fascia 12-16.")
        MAPPA_Z = {"1 Friuli":"Gemona / Cuarnan", "3 Slovenia":"Tolmin / Kobala",
                   "4 Alpago":"Alpago / Dolada", "5 Feltrino":"Feltre / Monte Avena"}
        try:
            for z in [z for z in MAPPA_Z if z in z_sel]:
                t, quando = meteo_giorno(*PUNTI_METEO[MAPPA_Z[z]])
                ag = t.head(10)
                st.markdown(f"##### {z}")
                col = {"Decollo": [s["sito"] for s in VINCOLI[z]]}
                for _, riga in ag.iterrows():
                    col[pd.Timestamp(riga["g"]).strftime("%a %d")] = [
                        giudizio(riga["v"], riga["dr"], s)[0] for s in VINCOLI[z]]
                st.dataframe(pd.DataFrame(col), hide_index=True)
                og = ag.iloc[0]
                with st.expander(f"Perché — {pd.Timestamp(og['g']).strftime('%a %d/%m')}, "
                                 f"{og['v']:.0f} km/h da {cardinale(og['dr'])}"):
                    for s in VINCOLI[z]:
                        ic, why = giudizio(og["v"], og["dr"], s)
                        st.markdown(f"{ic} **{s['sito']}** — {why}"
                                    + (f". {s['nota']}" if s["nota"] else ""))
            st.caption("\U0001F7E2 si vola · \U0001F7E1 al limite · \U0001F534 no. "
                       "Guarda solo il gradiente in quota: brezza, inversione e stato del terreno "
                       "li vedi tu sul posto.")
        except Exception as e:
            st.warning("Non riesco a raggiungere Open-Meteo adesso.")
            st.caption(f"({type(e).__name__}) Serve connessione internet.")
    else:
        luogo = st.selectbox("Località", list(PUNTI_METEO))
        try:
            t, quando = meteo_giorno(*PUNTI_METEO[luogo])
            st.dataframe(pd.DataFrame({
                "Giorno": t["time"].dt.strftime("%a %d/%m"),
                "Min/Max": [f"{a:.0f}/{b:.0f}°" for a,b in
                            zip(t["temperature_2m_min"], t["temperature_2m_max"])],
                "Pioggia": [f"{p:.0f}% · {s:.0f}mm" for p,s in
                            zip(t["precipitation_probability_max"].fillna(0),
                                t["precipitation_sum"].fillna(0))],
                "Vento 700hPa": [f"{v:.0f} km/h {cardinale(x)}" if pd.notna(v) else "—"
                                 for v,x in zip(t["v"], t["dr"])],
                "Zero term.": [f"{z:.0f} m" if pd.notna(z) else "—" for z in t["zt"]],
            }), hide_index=True)
            g = t[["time","v"]].dropna().set_index("time"); g.columns = ["vento 700 hPa km/h"]
            if len(g): st.line_chart(g)
            st.caption(f"Ultimo scaricamento: {quando}. Sopra i 25-30 km/h a 700 hPa i decolli "
                       "esposti diventano difficili.")
        except Exception as e:
            st.warning("Non riesco a raggiungere Open-Meteo adesso.")
            st.caption(f"({type(e).__name__})")

else:
    st.markdown("#### Com'è messa ogni zona")
    for k, v in NOTE_AREA:
        st.markdown(f"**{k}**"); st.write(v)
    st.divider()
    st.markdown("#### Fonti")
    st.dataframe(pd.DataFrame(FONTI, columns=["Fonte","Cosa dà","Area"]), hide_index=True)
    st.divider()
    st.markdown("#### Affidabilità")
    st.markdown("✅ **verificato** con fonte scritta: club, federazioni, guide locali")
    st.markdown("\U0001F7E1 **solo KML** — nella mappa di Lorenzo Delbene ma senza note")
    st.markdown("❓ **da verificare** prima di andarci")
    st.caption("Esposizioni non documentate e decolli non ufficiali vanno sempre confermati sul posto.")
