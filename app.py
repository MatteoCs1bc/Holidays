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

# Le zone del colpo d'occhio regionale. Ordine da est a ovest.
PUNTI_METEO = {
 "Prealpi Giulie \u2014 Gemona, Cuarnan":   (46.27, 13.16),
 "Carnia \u2014 Tolmezzo, Zoncolan":        (46.40, 13.02),
 "Alpi Giulie \u2014 Tarvisio, Lussari":    (46.46, 13.53),
 "Valli del Natisone \u2014 Matajur":       (46.18, 13.52),
 "Poso\u010dje \u2014 Tolmin, Kobala":       (46.19, 13.74),
 "Kobarid \u2014 Stol, Livek":              (46.25, 13.58),
 "Dolomiti friulane \u2014 Piancavallo":    (46.12, 12.52),
 "Alpago \u2014 Dolada, Cansiglio":         (46.15, 12.35),
 "Bellunese \u2014 Nevegal, Visentin":      (46.10, 12.28),
 "Feltrino \u2014 Monte Avena":             (46.03, 11.83),
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
 ("camminaevola.it","107 relazioni di hike & fly con difficolta' di decollo, direzione del "
  "vento, atterraggi, parcheggio, via di salita e coordinate di decollo e atterraggio",
  "Friuli, Carnia, Dolomiti friulane, Slovenia"),
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

# Fonti meteo locali del Friuli. Quelle con (drive) vengono dal materiale del
# comitato sul Tagliamento che mi hai indicato.
FONTI_METEO_FVG = [
 ("ARPA FVG — OSMER", "Il servizio meteo regionale: previsioni, allerte, radar e dati delle "
  "stazioni. meteo.fvg.it. Nota emersa dal materiale sul Drive: anche loro ogni tanto scivolano "
  "nel linguaggio da clickbait — 27-29 °C descritti come 'temperature quasi estive'. "
  "I dati restano i migliori che ci sono in regione."),
 ("Pazzi per il Meteo Goriziano", "Pagina di Daniel Tescari (Dantex), cacciatore di tempeste, "
  "attiva da 11 anni e vicina ai 100.000 follower su Facebook. Mappe temporalesche, radarate a "
  "bassa quota e una mano sulle allerte. È il canale social meteo di riferimento in regione. (drive)"),
 ("Società Meteorologica Alpino-Adriatica", "Ex Unione Meteorologica del FVG. "
  "Convegni e divulgazione tecnica sul clima regionale. (drive)"),
 ("Radar Protezione Civile", "radar.protezionecivile.it. 26 radar in Italia, scansione completa "
  "ogni 5-15 minuti, ciechi nei primi 5 km e nel cono sopra l'antenna, portata 150-200 km. (drive)"),
 ("meteo-parapente.com", "Vento di gradiente per quota, top termico, spessore dello strato "
  "limite. È il modello tarato sul volo libero, non sul meteo generale."),
 ("Wetterzentrale / Meteociel", "Carte sinottiche GFS ed ECMWF: geopotenziale a 500 hPa, "
  "fronti, pressione al suolo. Per capire la configurazione, non la giornata."),
]

# Fenomeni locali del Friuli emersi dal materiale sul Drive.
FENOMENI_FVG = [
 ("Alte pressioni persistenti", "Il maltempo non è solo il ciclone. Nell'estate 2026 la "
  "LUNGHEZZA delle fasi calde, più che le punte, è stata superiore al 2003 nella zona "
  "morenica. Per il volo vuol dire inversioni tenaci e termiche che si spengono presto."),
 ("Temporali meno numerosi ma più violenti", "Con le alte pressioni più presenti i "
  "temporali diminuiscono di numero ma aumentano di intensità, perché c'è molta "
  "più energia accumulata in atmosfera."),
 ("Fasi siccitose lunghe", "Dal 2010 in poi, in regione: una pioggia da 200 mm a Lignano e poi "
  "altri 30 giorni di sole. Il pattern si è allungato."),
 ("Vaia, ottobre 2018", "Mediterraneo caldissimo più ingresso di aria fredda. 204 km/h di "
  "scirocco registrati a Monte Rest, ma con l'incanalamento vallivo in Val Visdende "
  "probabilmente di più. Il dato che conta per chi vola: IL GROSSO DELLE PRECIPITAZIONI "
  "FU NELLE ALPI INTERNE E NON NELLE PREALPI, al contrario del solito."),
 ("Eventi recenti da ricordare", "La grandinata di Santa Maria la Longa e Mortegliano, "
  "il bow echo che ha divelto alberi e pali tra Carlino e Torviscosa, una supercella tornadica "
  "uscita sul mare. Tutti in regione, tutti negli ultimi anni."),
 ("Tempi di ritorno che si accorciano", "Eventi che sembravano secolari 'si cominciano un po' "
  "ad avvicinare'. Le statistiche storiche valgono meno di una volta."),
]

DESCR_ATT = {
 "cross": "Decolli e atterraggi ufficiali: ci si arriva in auto o con un impianto, c'e' un club "
          "dietro e di solito un regolamento da rispettare.",
 "hef": "Si sale a piedi su terreno escursionistico. Le 107 uscite di Cammina e Vola portano "
        "difficolta' di decollo, direzione del vento, via di salita e atterraggio; sui punti che "
        "vengono solo dal KML l'esposizione va ricavata dalla carta o dai tracciati XContest.",
 "pa_est": "Cime alpine: terreno da alpinismo, roccia o neve residua, si vola in discesa. "
           "La classificazione e' una proposta basata sul carattere della cima.",
 "pa_inv": "Cime da scialpinismo: si sale con le pelli e si vola giu'. Valgono valanghe, vento "
           "di quota e giornate corte: il semaforo guarda solo il vento.",
}

# Scala della difficolta' di decollo usata da Cammina e Vola (camminaevola.it).
SCALA_CEV = [
 ("1", "Spazi ampi: ci stanno piu' vele stese, gonfiaggio e corsa in sicurezza anche senza vento "
       "e con la possibilita' di fermare il decollo. Pendenza ottimale, sufficiente anche per una "
       "vela da montagna e non eccessiva. Terreno regolare, niente pietre acuminate, vegetazione o "
       "intoppi dove cordini e vela possano impigliarsi, niente dirupi o ostacoli vicini. "
       "La direzione di decollo non e' vincolata: tollera angoli ampi rispetto alla massima pendenza."),
 ("2", "Serve buona esperienza e ottimo controllo della vela in gonfiaggio. Gli spazi bastano per "
       "stendere la vela e per gonfiare, controllare e decollare se le condizioni aerologiche sono "
       "adeguate. Il terreno puo' essere irregolare e richiedere attenzione nella rincorsa; pietre "
       "acuminate, vegetazione o altri intoppi chiedono cura per non impigliare cordini e vela. "
       "Possibili dirupi o ostacoli nelle vicinanze."),
 ("2-", "Le difficolta' del grado 2 sono presenti solo in parte."),
 ("2+", "Le condizioni del grado 2 si presentano in forma particolarmente severa."),
 ("3", "Spazi angusti, appena sufficienti a stendere la vela: si decolla solo con condizioni "
       "aerologiche perfette. Serve ottima capacita' di valutare aria e attrezzatura e controllo "
       "perfetto in gonfiaggio, senza errori ne' esitazioni. Terreno estremamente impegnativo per "
       "irregolarita' e pietre acuminate, dirupi o ostacoli nelle immediate vicinanze. "
       "Ogni leggerezza qui comporta un rischio molto elevato."),
]

# Dagli "Appunti di meteorologia per il Friuli Venezia Giulia", ARPA FVG, III edizione 2010.
METEO_FVG = [
 ("Stau e foehn — perche' piove tanto sulle Prealpi",
  "Sul versante sopravvento l'aria e' costretta a salire: si espande, si raffredda e da una certa "
  "quota in su il vapore condensa, con nuvole e precipitazioni TANTO PIU' INTENSE QUANTO PIU' SI "
  "E' VICINI ALLE MONTAGNE. Ma condensando il vapore emette calore, quindi da li' in su l'aria si "
  "raffredda meno del normale e arriva sullo spartiacque meno fredda di quanto sarebbe. "
  "Sul versante sottovento torna a scendere, ha perso quasi tutto il vapore, si comprime e si "
  "riscalda: la nuvolosita' scompare subito e l'aria arriva in pianura ben piu' calda che "
  "sull'altro versante alla stessa quota. Tempo bello, ventoso e secco: e' il foehn."),
 ("Dove piove in Friuli",
  "Dai trent'anni di dati del Servizio Idrografico: a causa dello stau LE PREALPI, che sono le "
  "prime montagne a sbarrare il passo alle masse d'aria umide meridionali, ricevono le quantita' "
  "piu' elevate di pioggia e neve. A seconda dei casi risultano favorite le Prealpi Carniche o le "
  "Giulie. Allontanandosi dalle Prealpi le precipitazioni diminuiscono: nelle Alpi perche' sono "
  "riparate dalle Prealpi, sulla pianura perche' lo stau si fa via via meno intenso. "
  "Il Friuli e' fortunato: riceve piogge e nevicate con venti sia da sud-ovest (Libeccio), "
  "sia da sud, sia da sud-est (Scirocco)."),
 ("Bora chiara",
  "Generata da un forte anticiclone sull'Europa nord-orientale, che spinge aria secca e "
  "d'inverno molto fredda verso il Mediterraneo centrale. Il vento sulle Venezie e' IMPETUOSO, "
  "MOLTO FORTE MA DISCONTINUO, A RAFFICHE. Tempo bello e secco, d'inverno freddo. "
  "Puo' essere brutto sui versanti sopravvento di Slovenia e Croazia per effetto stau."),
 ("Bora scura",
  "Generata da una profonda depressione sul Tirreno, a volte sull'Adriatico, che richiama aria "
  "dall'Europa orientale. Il vento da nord-est e' FORTE E ABBASTANZA CONTINUO, con raffiche meno "
  "marcate della chiara. Poiche' la depressione richiama in quota aria calda e umida da sud, su "
  "buona parte d'Italia il tempo e' brutto, ma SUL FRIULI LE PIOGGE NON SONO MOLTO INTENSE. "
  "D'inverno e' una delle poche situazioni che portano la neve in regione."),
 ("Dove nasce la Bora e perche' e' cosi' forte",
  "E' particolarmente forte sulle Venezie perche' prima di arrivarci una gran massa d'aria deve "
  "passare per una ZONA RISTRETTA FRA LE ALPI GIULIE E I DINARI, sul Carso, nel retroterra "
  "triestino. Chiara o scura, quando c'e' Bora la pressione e' piu' alta su Austria, entroterra "
  "sloveno e croato che sull'area padano-veneta. Il gradiente e' massimo proprio sulle Alpi "
  "Giulie, sul Carso fra Lubiana e Trieste e sulle Dinariche. "
  "E' comunque un VENTO DI CADUTA, DEL TIPO FOEHN: arriva sull'Adriatico piu' calda di quando e' "
  "partita, anche di diversi gradi. Ma fra wind-chill e aria preesistente piu' calda, la "
  "sensazione e' di freddo."),
 ("Le brezze: il respiro della montagna",
  "Le valli friulane sono rivolte all'incirca VERSO SUD, verso la pianura e l'Adriatico. Questo "
  "determina sia l'incanalamento dei venti sia lo sviluppo delle brezze. "
  "La brezza di MONTE e' notturna: i versanti in quota si raffreddano, l'aria a contatto diventa "
  "piu' pesante e scende lungo i pendii fino al fondovalle. La brezza di VALLE e' diurna ed e' "
  "l'inverso: i versanti si scaldano, l'aria sale lungo i pendii e richiama aria dal fondovalle. "
  "Quando la situazione le favorisce le brezze possono diventare anche forti."),
 ("La giornata tipo in una valle friulana",
  "DI BUON MATTINO soffia la brezza di monte: alle alte quote cielo sereno e buona visibilita', "
  "sul fondovalle ristagna un cuscinetto di aria fredda che genera INVERSIONE TERMICA, con "
  "foschie o nebbie. Se l'inversione e' forte ed e' a meta' altezza nella vallata, la nebbia puo' "
  "sollevarsi fin sotto l'inversione formando STRATOCUMULI anche compatti, che da sotto danno "
  "l'impressione di cielo coperto.\\n\\n"
  "A META' MATTINATA il sole scalda i versanti e poi il fondovalle: l'aria sale, prima ROMPE "
  "L'INVERSIONE e poi comincia a risalire il fondovalle. Nuvole, foschia e nebbia si dissolvono. "
  "La visibilita' migliora in basso e PEGGIORA IN QUOTA, perche' l'umidita' viene portata in alto.\\n\\n"
  "VERSO META' GIORNATA e' piena brezza di valle: l'aria porta su l'umidita', si espande, si "
  "raffredda e condensa nei CUMULI DI BEL TEMPO sopra i versanti. Lo sviluppo e' piu' facile con "
  "atmosfera instabile, ostacolato con atmosfera stabile.\\n\\n"
  "D'INVERNO tutto questo avviene con molta minore intensita'. A volte l'inversione, con nebbia o "
  "nuvole, PUO' PERMANERE TUTTO IL GIORNO."),
 ("Il temporale di calore pomeridiano",
  "Favorito da instabilita', umidita' elevata e ASSENZA DI VENTO FORTE IN QUOTA. Uno dei cumuli "
  "diventa sempre piu' grande, torreggiante, con molte protuberanze; la sommita' si allarga e si "
  "appiattisce nell'INCUDINE. Se la base e' grigia e frastagliata e' facile che ci siano pioggia "
  "o grandine. IL TEMPORALE ROMPE IL SISTEMA DEI VENTI DI BREZZA: correnti di aria fredda "
  "arrivano fino al suolo con raffiche disordinate. Si sposta nella direzione del vento dominante "
  "in quota. "
  "Sulle Alpi non e' raro che PIU' TEMPORALI FORMATISI IN VALLATE VICINE SI UNISCANO nel tardo "
  "pomeriggio, per esempio in Carnia o nelle Dolomiti, e che il gruppo poi si sposti sulla "
  "pianura friulana."),
 ("Di sera: come si legge il giorno dopo",
  "Quando il temporale si allontana o si esaurisce, nella vallata non ci sono venti ben "
  "individuabili e le nuvole vanno diminuendo; quelle che restano tendono a diventare "
  "STRATIFORMI. SE SCOMPAIONO DEL TUTTO il tempo probabilmente non sta cambiando e restera' "
  "bello, e l'indomani il ciclo ricomincia. SE INVECE SI ESTENDONO E SI ALLARGANO, e' possibile "
  "che si prospetti un peggioramento."),
 ("Il vento trasversale alla valle",
  "Quando il vento sinottico soffia a circa 90 gradi rispetto alla valle, e' difficile che venga "
  "incanalato. TANTO PIU' LA VALLE E' STRETTA E PROFONDA, TANTO PIU' IL VENTO ARRIVA SUL "
  "FONDOVALLE INALTERATO. Puo' succedere che l'aria, dopo aver sorvolato la valle, venga riflessa "
  "dal versante opposto e torni indietro sul fondovalle in verso opposto al vento dominante. "
  "In generale si forma TURBOLENZA, che pero' dissipa foschie e nebbie e rimescola l'atmosfera. "
  "Sul fondovalle i venti trasversali sono comunque rari."),
]

# A quali zone del dataset corrisponde ogni punto meteo, per contare i siti.
ZONE_SITI = {
 "Gemona / Cuarnan":        ["1 Friuli"],
 "Tolmezzo / Carnia":       ["6 Pordenonese / Carnia ovest"],
 "Tarvisio / Alpi Giulie":  ["2 Alpi Giulie"],
 "Tolmin / Kobala":         ["3 Slovenia"],
 "Kobarid / Stol":          ["3 Slovenia"],
 "Alpago / Dolada":         ["4 Alpago"],
 "Belluno / Nevegal":       ["4 Alpago", "10 Cadore / Dolomiti"],
 "Feltre / Monte Avena":    ["5 Feltrino"],
}


# --------------------------------------------------------------------
# ATTIVITA
# --------------------------------------------------------------------
# Classificazione per TIPOLOGIA DI ATTIVITA'.
# 
# cross  = voli di cross: decolli e atterraggi ufficiali, si arriva in auto o con impianto
# hef    = hike & fly: si sale a piedi, terreno escursionistico
# pa_est = paralpinismo estivo: cima alpina, terreno da alpinismo, si vola in discesa
# pa_inv = paralpinismo invernale: scialpinismo o neve, si vola in discesa
# 
# Un punto puo' avere piu' attivita'. La classificazione dei due paralpinismi e' una
# PROPOSTA basata sul carattere della cima, non su relazioni di volo verificate.

ATTIVITA = {
 "cross":  dict(eti="Voli di cross",          rgb=[214,  40,  40], ico="\U0001FA82"),
 "hef":    dict(eti="Hike & Fly",             rgb=[255, 170,   0], ico="\U0001F97E"),
 "pa_est": dict(eti="Paralpinismo estivo",    rgb=[ 45, 106,  79], ico="⛰️"),
 "pa_inv": dict(eti="Paralpinismo invernale", rgb=[ 60, 145, 230], ico="❄️"),
}

# Cime alpine del nordest: terreno da alpinismo estivo.
PARALP_ESTIVO = {
 # Alpi Giulie
 "montasio","jof di montasio","jof fuart","canin","monte canin","monte jama",
 "mangart","prestreljenik","due pizzi","cima del cacciatore","monte lussari",
 # Prealpi Giulie e Carniche orientali
 "monte plauris","monte amariana","musi","monte cretis","monte dobis","monte brancot",
 "monte cucco","costa cavallo","cima somp selve","postuncicco","matajur","stol",
 # Carnia
 "monte clapsavon","monte tinisa","monte pleros","creta di mimoias","monte lovinzola",
 "monte tersadia","monte oberkovel","creton di culzei","monte teglara","monte taront",
 "monte rossa e taiet","croce di micottis","casera davass","cuel di montof","rancolin",
 "monte rua","colle dei larici","missione cormolina","bivacco brollo","passo pura",
 # Dolomiti friulane e bellunesi
 "monte raut","monte borga","val montanaia","forcella di giais","il portellin",
 "cima vallon scuro","moon lander - cima postegae","bivacco spagnolli","col mat",
 "tre cime","monte piana","monte serva","monte dolada","rit",
}

# Cime classiche da scialpinismo: si sale con le pelli e si vola giu'.
PARALP_INVERNALE = {
 "monte zoncolan","zoncolan","val secca","monte tersadia","monte dobis","monte cucco",
 "monte cretis","croce di micottis","casera davass","passo pura","monte amariana",
 "cuel di montof","rancolin","monte rua","colle dei larici","monte teglara",
 "monte lussari","monte jama","canin","monte canin","montasio",
 "cima somp selve","costa cavallo","monte brancot","sattelnock","golzentipp",
 "emberger alm","helm","monte piana","tre cime","col mat","rit","sorica","vogel","gozd",
}

# Override espliciti: nome esatto -> lista attivita'
OVERRIDE = {
 "Monte Cuarnan": ["cross","hef"],
 "Monte San Simeone": ["cross","hef"],
 "Monte Dolada": ["cross","hef","pa_est"],
 "Revine": ["cross"],
 "Nevegal": ["cross","hef"],
 "Col Visentin": ["cross","hef"],
 "Pizzoc": ["cross"],
 "Monte Serva": ["cross","hef","pa_est"],
 "Bernadia": ["cross"], "Porzus": ["cross"], "Karcos": ["cross"],
 "Monte Avena — Decollo Sud": ["cross"], "Monte Avena — Decollo Ovest": ["cross"],
 "Monte Avena — Decollo Est": ["cross"],
 "Monte Lussari": ["cross","pa_inv"],
 "Canin": ["cross","pa_est","pa_inv"],
 "Stol (versante italiano)": ["cross","hef","pa_est"],
 "Mittagskogel": ["cross"],
 "Hike & Fly Montasio": ["hef","pa_est","pa_inv"],
 "Hike & Fly Monte Plauris": ["hef","pa_est"],
 "Hike & Fly Monte Amariana": ["hef","pa_est","pa_inv"],
 "Hike & Fly Musi": ["hef","pa_est"],
 "Hike & Fly Matajur": ["hef","pa_est"],
 # Slovenia
 "Kobala (Tolmin)": ["cross"], "Kobariski Stol": ["cross"], "Livski Kuk": ["cross"],
 "Mrzli vrh — Matajur": ["cross"], "Ozben": ["cross"], "Vrse": ["cross"],
 "Mangart — Sedlo": ["cross","pa_est","pa_inv"],
 "Mangart — Tunel (Prhodci)": ["cross","pa_inv"],
 "Kanin — Skripi": ["cross","pa_est","pa_inv"],
 "Planja": ["hef","pa_est"],
}

def _norm(n):
    import unicodedata
    n = str(n)
    for p in ("Takeoff ","Hike & Fly ","Hike and Fly ","Landing ","Parking ","Cablecar "):
        n = n.replace(p, "")
    n = unicodedata.normalize("NFKD", n.lower()).encode("ascii","ignore").decode()
    for ch in "'`’": n = n.replace(ch, " ")
    return " ".join(n.split())

def attivita_di(nome, tipo, cartella_kml=None, quota=None):
    """Ritorna la lista di attivita' per un punto."""
    if nome in OVERRIDE:
        return list(OVERRIDE[nome])
    k = _norm(nome)
    a = []
    # si atterra e si parcheggia qualunque sia l'attivita': valgono per tutte
    if tipo in ("atterraggio", "parcheggio"):
        return ["cross", "hef", "pa_est", "pa_inv"]
    if tipo == "impianto":
        return ["cross", "pa_inv"]
    if tipo == "decollo": a.append("cross")
    if tipo == "hike&fly": a.append("hef")
    if k in PARALP_ESTIVO:    a.append("pa_est")
    if k in PARALP_INVERNALE: a.append("pa_inv")
    # un hike & fly molto alto e' quasi sempre anche terreno alpino
    if tipo == "hike&fly" and quota and quota >= 2000 and "pa_est" not in a:
        a.append("pa_est")
    return a or ["cross"]


# --------------------------------------------------------------------
# MOTORE METEO
# --------------------------------------------------------------------
# Analisi meteo orientata al volo: instabilita', quota massima, inversioni,
# turbolenza, gradiente termico. Dati Open-Meteo (modello ICON/ECMWF).
import json, urllib.request, urllib.parse, math
import pandas as pd

LIVELLI = [925, 850, 800, 700, 600, 500]

ORARIE = (
    ["temperature_2m","dew_point_2m","cape","lifted_index","convective_inhibition",
     "boundary_layer_height","freezing_level_height","cloud_cover","cloud_cover_low",
     "cloud_cover_mid","cloud_cover_high","wind_speed_10m","wind_direction_10m",
     "wind_gusts_10m","precipitation_probability"]
    + [f"temperature_{l}hPa" for l in LIVELLI]
    + [f"wind_speed_{l}hPa" for l in LIVELLI]
    + [f"wind_direction_{l}hPa" for l in LIVELLI]
    + [f"geopotential_height_{l}hPa" for l in LIVELLI]
    + [f"relative_humidity_{l}hPa" for l in LIVELLI]
    + [f"cloud_cover_{l}hPa" for l in LIVELLI]
)
GIORNALIERE = ["temperature_2m_max","temperature_2m_min","precipitation_sum",
               "precipitation_probability_max","wind_speed_10m_max"]

# Modello preferito per i primi giorni: ICON-2I di ItaliaMeteo-ARPAE (~2 km, 3 giorni,
# aggiornato ogni 12 h). Dove non c'e' (oltre i 3 giorni, o variabili che non calcola come
# lo strato limite e i livelli 800/600 hPa) si usa la scelta automatica di Open-Meteo.
MODELLO_PREF = "italia_meteo_arpae_icon_2i"

def _famiglia(nome):
    """Raggruppa i livelli di pressione: temperature_850hPa -> temperature_hPa."""
    import re as _re
    return _re.sub(r"_\d+hPa$", "_hPa", nome)

def _interpola_livelli(h, orarie, suf):
    """ICON-2I ha 1000/925/850/700/500/250 hPa: i livelli mancanti (800, 600) si
    ricavano interpolando in log(p) tra i due livelli vicini; le direzioni del vento
    lungo l'arco piu' corto."""
    import re as _re
    for v in orarie:
        m = _re.match(r"(.+)_(\d+)hPa$", v)
        if not m or any(x is not None for x in (h.get(v + suf) or [])):
            continue
        base, lv = m.group(1), int(m.group(2))
        sotto = [l for l in (1000, 925, 850, 700, 500, 250) if l > lv]
        sopra = [l for l in (1000, 925, 850, 700, 500, 250) if l < lv]
        if not sotto or not sopra:
            continue
        l1, l2 = min(sotto), max(sopra)
        a, b = h.get(f"{base}_{l1}hPa{suf}"), h.get(f"{base}_{l2}hPa{suf}")
        if not a or not b:
            continue
        w = (math.log(l1) - math.log(lv)) / (math.log(l1) - math.log(l2))
        out = []
        for x, y in zip(a, b):
            if x is None or y is None:
                out.append(None)
            elif "direction" in base:
                d = ((y - x + 180) % 360) - 180
                out.append((x + w * d) % 360)
            else:
                out.append(x + w * (y - x))
        h[v + suf] = out

def _fondi(js, orarie):
    """Unisce le due risposte: per ogni famiglia di variabili prende ICON-2I solo se ha
    tutti i livelli, cosi' un profilo verticale non mescola due modelli."""
    h = js.get("hourly", {})
    suf_p, suf_b = "_" + MODELLO_PREF, "_best_match"
    _interpola_livelli(h, orarie, suf_p)
    fam = {}
    for v in orarie:
        fam.setdefault(_famiglia(v), []).append(v)
    out = {"time": h["time"]}
    usato = []
    for f, vs in fam.items():
        ok = all(any(x is not None for x in (h.get(v + suf_p) or [])) for v in vs)
        for v in vs:
            b = h.get(v + suf_b) or h.get(v) or [None] * len(h["time"])
            if ok:
                p_ = h.get(v + suf_p)
                out[v] = [pv if pv is not None else bv for pv, bv in zip(p_, b)]
            else:
                out[v] = b
        if ok: usato.append(f)
    js["hourly"] = out
    d = js.get("daily", {})
    if d:
        nd = {"time": d["time"]}
        for k in GIORNALIERE:
            b = d.get(k + suf_b) or d.get(k) or [None] * len(d["time"])
            p_ = d.get(k + suf_p)
            nd[k] = [pv if pv is not None else bv for pv, bv in zip(p_, b)] if p_ else b
        js["daily"] = nd
    js["_modello"] = f"ICON-2I per i primi giorni ({len(usato)}/{len(fam)} grandezze), poi automatico"
    return js

def _get(la, lo, orarie):
    base = {"latitude": la, "longitude": lo, "timezone": "auto", "forecast_days": 10,
            "daily": ",".join(GIORNALIERE), "hourly": ",".join(orarie)}
    try:
        p = urllib.parse.urlencode({**base, "models": MODELLO_PREF + ",best_match"})
        with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?" + p, timeout=25) as f:
            return _fondi(json.load(f), orarie)
    except Exception:
        p = urllib.parse.urlencode(base)
        with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?" + p, timeout=25) as f:
            return json.load(f)

def scarica(la, lo):
    """Prova i nomi moderni, ripiega su quelli vecchi se l'API li rifiuta."""
    try:
        return _get(la, lo, ORARIE)
    except Exception:
        vecchi = [v.replace("dew_point_2m","dewpoint_2m").replace("wind_speed","windspeed")
                   .replace("wind_direction","winddirection").replace("wind_gusts","windgusts")
                   .replace("cloud_cover","cloudcover")
                   .replace("relative_humidity","relativehumidity") for v in ORARIE]
        return _get(la, lo, vecchi)

def _c(h, nome):
    """Colonna, qualunque sia la convenzione di nomi."""
    for n in (nome, nome.replace("dew_point_2m","dewpoint_2m").replace("wind_speed","windspeed")
                        .replace("wind_direction","winddirection").replace("wind_gusts","windgusts")
                        .replace("cloud_cover","cloudcover")
                        .replace("relative_humidity","relativehumidity")):
        if n in h.columns: return h[n]
    return pd.Series([float("nan")] * len(h), index=h.index)

def _vento_medio(vs, ds):
    """Media vettoriale di vento e direzione."""
    u = sum(-v*math.sin(math.radians(d)) for v,d in zip(vs,ds) if pd.notna(v) and pd.notna(d))
    w = sum(-v*math.cos(math.radians(d)) for v,d in zip(vs,ds) if pd.notna(v) and pd.notna(d))
    n = sum(1 for v,d in zip(vs,ds) if pd.notna(v) and pd.notna(d))
    if not n: return float("nan"), float("nan")
    u, w = u/n, w/n
    return math.hypot(u,w), (math.degrees(math.atan2(-u,-w)) % 360)

def _shear(v1,d1,v2,d2):
    if any(pd.isna(x) for x in (v1,d1,v2,d2)): return float("nan")
    u1,w1 = -v1*math.sin(math.radians(d1)), -v1*math.cos(math.radians(d1))
    u2,w2 = -v2*math.sin(math.radians(d2)), -v2*math.cos(math.radians(d2))
    return math.hypot(u2-u1, w2-w1)

def analizza(la, lo):
    """Ritorna (DataFrame per giorno, quota stazione, orario scaricamento)."""
    from datetime import datetime
    d = scarica(la, lo)
    quota_staz = d.get("elevation", 0) or 0
    h = pd.DataFrame(d["hourly"]); h["time"] = pd.to_datetime(h["time"])
    f = h[h["time"].dt.hour.between(11, 16)].copy()
    f["g"] = f["time"].dt.date
    dd = pd.DataFrame(d["daily"]); dd["time"] = pd.to_datetime(dd["time"]); dd["g"] = dd["time"].dt.date

    righe = []
    for g, b in f.groupby("g"):
        r = {"g": g}
        r["cape"] = _c(b,"cape").mean()
        r["cape_max"] = _c(b,"cape").max()
        r["li"]  = _c(b,"lifted_index").mean()
        r["cin"] = _c(b,"convective_inhibition").mean()
        blh = _c(b,"boundary_layer_height").max()
        r["blh"] = blh
        r["quota_termica"] = quota_staz + blh if pd.notna(blh) else float("nan")
        r["zero_term"] = _c(b,"freezing_level_height").mean()
        t2, td2 = _c(b,"temperature_2m").mean(), _c(b,"dew_point_2m").mean()
        r["spread"] = t2 - td2 if pd.notna(t2) and pd.notna(td2) else float("nan")
        r["base_nubi"] = (max(quota_staz + 50, quota_staz + 125*(t2-td2))
                          if pd.notna(t2) and pd.notna(td2) else float("nan"))
        r["nuv_bassa"] = _c(b,"cloud_cover_low").mean()
        r["nuv_tot"]   = _c(b,"cloud_cover").mean()
        r["pioggia"]   = _c(b,"precipitation_probability").max()
        r["raffiche"]  = _c(b,"wind_gusts_10m").max()
        v10 = _c(b,"wind_speed_10m").mean()
        r["v10"] = v10
        r["raff_ratio"] = (r["raffiche"]/v10) if pd.notna(v10) and v10 > 1 else float("nan")

        # profilo verticale
        prof = []
        for l in LIVELLI:
            t = _c(b,f"temperature_{l}hPa").mean()
            z = _c(b,f"geopotential_height_{l}hPa").mean()
            v = _c(b,f"wind_speed_{l}hPa").mean()
            dr_ = _vento_medio(_c(b,f"wind_speed_{l}hPa"), _c(b,f"wind_direction_{l}hPa"))[1]
            rh = _c(b,f"relative_humidity_{l}hPa").mean()
            nb = _c(b,f"cloud_cover_{l}hPa").mean()
            prof.append(dict(hPa=l, t=t, z=z, v=v, d=dr_, rh=rh, nub=nb))
        r["profilo"] = prof
        P = {p["hPa"]: p for p in prof}
        r["v700"], r["d700"] = P[700]["v"], P[700]["d"]
        r["v850"], r["d850"] = P[850]["v"], P[850]["d"]
        r["t850"], r["t700"] = P[850]["t"], P[700]["t"]

        # gradiente termico (lapse rate) in gradi ogni 100 m
        def lapse(a, b_):
            pa, pb = P[a], P[b_]
            if any(pd.isna(x) for x in (pa["t"],pb["t"],pa["z"],pb["z"])) or pb["z"]==pa["z"]:
                return float("nan")
            return (pa["t"]-pb["t"]) / (pb["z"]-pa["z"]) * 100
        r["lapse_925_850"] = lapse(925, 850)
        r["lapse_850_700"] = lapse(850, 700)
        r["lapse_700_500"] = lapse(700, 500)

        # inversioni: temperatura che sale salendo di quota
        inv = []
        ordinati = sorted([p for p in prof if pd.notna(p["t"]) and pd.notna(p["z"])],
                          key=lambda p: p["z"])
        for a_, b_ in zip(ordinati, ordinati[1:]):
            if b_["t"] > a_["t"] + 0.2:
                inv.append((a_["z"], b_["z"], b_["t"]-a_["t"]))
        # inversione bassa: suolo piu' freddo del 925
        if pd.notna(t2) and pd.notna(P[925]["t"]) and P[925]["t"] > t2 + 0.2 \
           and pd.notna(P[925]["z"]) and P[925]["z"] > quota_staz:
            inv.insert(0, (quota_staz, P[925]["z"], P[925]["t"]-t2))
        r["inversioni"] = inv
        r["tappo"] = inv[0][0] if inv else float("nan")

        # strati di nubi: quota e copertura
        strati = []
        for p in sorted([x for x in prof if pd.notna(x["z"])], key=lambda x: x["z"]):
            cop = p["nub"] if pd.notna(p["nub"]) else (
                  max(0.0, (p["rh"]-70)*3.3) if pd.notna(p["rh"]) else float("nan"))
            if pd.notna(cop) and cop >= 25:
                strati.append(dict(z=p["z"], cop=cop, rh=p["rh"], hPa=p["hPa"]))
        r["strati_nubi"] = strati
        r["nuv_media"] = _c(b,"cloud_cover_mid").mean()
        r["nuv_alta"]  = _c(b,"cloud_cover_high").mean()
        # la base dei cumuli e' sopra o sotto il tetto delle termiche?
        bn, qt = r["base_nubi"], r["quota_termica"]
        r["cumuli"] = (pd.notna(bn) and pd.notna(qt) and bn <= qt + 150)

        # shear = turbolenza potenziale
        r["shear_925_700"] = _shear(P[925]["v"],P[925]["d"],P[700]["v"],P[700]["d"])
        r["shear_850_700"] = _shear(P[850]["v"],P[850]["d"],P[700]["v"],P[700]["d"])
        righe.append(r)

    out = dd.merge(pd.DataFrame(righe), on="g", how="left")
    return out, quota_staz, datetime.now().strftime("%d/%m %H:%M")

# ---------------- interpretazioni ----------------
def giudica_instabilita(cape, li):
    if pd.isna(cape) and pd.isna(li): return "—", "dati mancanti"
    c = 0 if pd.isna(cape) else cape
    if c < 150:   lv, t = 0, "stabile"
    elif c < 500: lv, t = 1, "instabilità debole"
    elif c < 1200: lv, t = 2, "instabilità moderata"
    elif c < 2000: lv, t = 3, "instabilità forte"
    else:          lv, t = 4, "instabilità molto forte"
    if pd.notna(li):
        if li <= -5 and lv < 3: lv, t = 3, "instabilità forte (LI)"
        elif li <= -2 and lv < 2: lv, t = 2, "instabilità moderata (LI)"
    ic = ["\U0001F7E2","\U0001F7E2","\U0001F7E1","\U0001F7E0","\U0001F534"][lv]
    return ic, t

def giudica_gradiente(l):
    if pd.isna(l): return "—", "dati mancanti"
    if l < 0.45: return "\U0001F535", "stabile, termiche deboli o assenti"
    if l < 0.65: return "\U0001F7E2", "gradiente modesto, termiche dolci"
    if l < 0.80: return "\U0001F7E2", "buon gradiente, termiche efficienti"
    if l < 0.92: return "\U0001F7E1", "gradiente forte, termiche vigorose"
    return "\U0001F534", "quasi adiabatico secco, termiche violente"

def giudica_turbolenza(shear, raff_ratio, v700):
    pt = 0
    if pd.notna(shear):
        pt += 0 if shear < 15 else (1 if shear < 30 else (2 if shear < 45 else 3))
    if pd.notna(raff_ratio):
        pt += 0 if raff_ratio < 1.6 else (1 if raff_ratio < 2.2 else 2)
    if pd.notna(v700) and v700 > 35: pt += 1
    lv = min(pt, 3)
    return (["\U0001F7E2","\U0001F7E1","\U0001F7E0","\U0001F534"][lv],
            ["turbolenza bassa","turbolenza moderata","turbolenza marcata",
             "turbolenza forte"][lv])

def descrivi_inversioni(inv, quota_staz):
    if not inv: return "\U0001F7E2", "nessuna inversione nel profilo"
    base, cima, dt = inv[0]
    rel = base - quota_staz
    if rel < 300:
        return "\U0001F534", (f"inversione al suolo, tappo a {base:.0f} m "
                              f"(+{dt:.1f}°C fino a {cima:.0f} m)")
    if rel < 1200:
        return "\U0001F7E0", (f"inversione bassa, tappo a {base:.0f} m "
                              f"(+{dt:.1f}°C fino a {cima:.0f} m)")
    return "\U0001F7E1", f"inversione in quota a {base:.0f} m (+{dt:.1f}°C)"


def giudica_nuvole(nuv_bassa, nuv_media, nuv_alta, base, quota_term, cumuli):
    """Lettura operativa della copertura: cosa vuol dire per chi vola."""
    nb = 0 if pd.isna(nuv_bassa) else nuv_bassa
    nm = 0 if pd.isna(nuv_media) else nuv_media
    na = 0 if pd.isna(nuv_alta) else nuv_alta
    frasi, ic = [], "\U0001F7E2"
    if nb >= 70:
        ic = "\U0001F534"
        frasi.append(f"nubi basse al {nb:.0f}%: sole schermato, termiche spente")
    elif nb >= 35:
        ic = "\U0001F7E1"
        frasi.append(f"nubi basse al {nb:.0f}%: termiche a intermittenza")
    elif nb > 10:
        frasi.append(f"poche nubi basse ({nb:.0f}%)")
    if nm >= 50:
        if ic == "\U0001F7E2": ic = "\U0001F7E1"
        frasi.append(f"strato medio al {nm:.0f}%: scalda meno, attenzione al peggioramento")
    if na >= 50:
        frasi.append(f"velature al {na:.0f}%: riducono l'irraggiamento ma lasciano volare")
    if cumuli:
        frasi.append(f"cumuli attesi, base intorno a {base:.0f} m")
    elif pd.notna(base) and pd.notna(quota_term) and base > quota_term + 150:
        frasi.append("aria troppo secca per i cumuli: termiche blu, niente riferimenti visivi")
    if not frasi:
        frasi.append("cielo sereno o quasi")
    return ic, " \u00b7 ".join(frasi)


# ---------------- punteggi per attivita' ----------------
def _p(v, buono, limite):
    """100 se <= buono, 0 se >= limite, lineare in mezzo."""
    if pd.isna(v): return 55.0
    if v <= buono: return 100.0
    if v >= limite: return 0.0
    return 100.0 * (limite - v) / (limite - buono)

def _combina(s):
    """Il fattore peggiore pesa piu' della media: una sola cosa storta basta a
    rovinare la giornata, e fare la media la nasconderebbe."""
    return 0.6 * min(s.values()) + 0.4 * (sum(s.values()) / len(s))

def punteggi(r):
    """Per ogni attivita': (voto 0-100, motivo in una riga)."""
    v700 = r.get("v700"); cape = r.get("cape"); li = r.get("li")
    lapse = r.get("lapse_850_700"); nb = r.get("nuv_bassa"); pio = r.get("pioggia")
    shear = r.get("shear_925_700"); zt = r.get("zero_term"); qt = r.get("quota_termica")
    out = {}

    def comune(lim_vento):
        s = {}
        s["vento"] = _p(v700, lim_vento * 0.6, lim_vento * 1.7)
        s["pioggia"] = _p(pio, 10, 70)
        s["nubi"] = _p(nb, 25, 85)
        s["turb"] = _p(shear, 15, 55)
        return s

    # CROSS: vuole termiche efficienti, vento gestibile, niente temporali
    s = comune(25)
    s["grad"] = 100.0 if pd.isna(lapse) else (
        100.0 if 0.62 <= lapse <= 0.90 else (65.0 if 0.5 <= lapse < 0.62 else
        (55.0 if 0.90 < lapse <= 0.96 else 25.0)))
    s["inst"] = 100.0 if pd.isna(cape) else (
        55.0 if cape < 150 else (100.0 if cape < 700 else
        (70.0 if cape < 1200 else (35.0 if cape < 2000 else 10.0))))
    out["cross"] = (_combina(s), _motivo("cross", min(s, key=s.get), s, r))

    # HIKE & FLY: tollera meno vento, non gli serve la termica forte
    s = comune(20)
    s["grad"] = 100.0 if pd.isna(lapse) else (100.0 if lapse <= 0.92 else 45.0)
    s["inst"] = 100.0 if pd.isna(cape) else (100.0 if cape < 900 else
                (55.0 if cape < 1600 else 15.0))
    out["hef"] = (_combina(s), _motivo("hef", min(s, key=s.get), s, r))

    # PARALPINISMO ESTIVO: aria calma, niente temporali, zero termico alto
    s = comune(16)
    s["inst"] = 100.0 if pd.isna(cape) else (100.0 if cape < 300 else
                (55.0 if cape < 800 else 10.0))
    s["zero"] = 100.0 if pd.isna(zt) else (100.0 if zt >= 3200 else
                (70.0 if zt >= 2600 else 40.0))
    out["pa_est"] = (_combina(s), _motivo("pa_est", min(s, key=s.get), s, r))

    # PARALPINISMO INVERNALE: aria calma, poca neve nuova, zero termico basso
    s = comune(16)
    s["inst"] = 100.0 if pd.isna(cape) else (100.0 if cape < 300 else 40.0)
    s["zero"] = 100.0 if pd.isna(zt) else (100.0 if zt <= 2200 else
                (65.0 if zt <= 2900 else 35.0))
    out["pa_inv"] = (_combina(s), _motivo("pa_inv", min(s, key=s.get), s, r))
    return out

def _motivo(att, peggio, s, r):
    if s[peggio] >= 80:
        if att in ("cross","hef"):
            g = r.get("lapse_850_700")
            if pd.notna(g) and g >= 0.62: return "termiche efficienti e vento gestibile"
            return "condizioni tranquille, termiche dolci"
        return "aria calma, giornata pulita"
    testi = {
     "vento": lambda: f"vento a 700 hPa {r['v700']:.0f} km/h",
     "pioggia": lambda: f"pioggia al {r['pioggia']:.0f}%",
     "nubi": lambda: f"nubi basse al {r['nuv_bassa']:.0f}%",
     "turb": lambda: f"shear {r['shear_925_700']:.0f} km/h, aria mossa",
     "grad": lambda: (f"gradiente {r['lapse_850_700']:.2f}, aria stabile"
                      if pd.notna(r.get('lapse_850_700')) and r['lapse_850_700'] < 0.6
                      else f"gradiente {r['lapse_850_700']:.2f}, termiche dure"),
     "inst": lambda: f"CAPE {r['cape']:.0f}, rischio sviluppi",
     "zero": lambda: f"zero termico {r['zero_term']:.0f} m",
    }
    try: return testi[peggio]()
    except Exception: return "condizioni marginali"

def voto_icona(v):
    if pd.isna(v): return "—"
    if v >= 78: return "\U0001F7E2"
    if v >= 62: return "\U0001F7E1"
    if v >= 45: return "\U0001F7E0"
    return "\U0001F534"


# ---------------- punteggio per attivita' ----------------
def _fascia(x, soglie):
    """Ritorna 0..len(soglie) in base a dove cade x."""
    if pd.isna(x): return 0
    n = 0
    for s in soglie:
        if x >= s: n += 1
    return n

def punteggio(r, att):
    """0-100 e una frase. Ogni attivita' vuole cose diverse dal tempo."""
    v700 = r.get("v700"); cape = r.get("cape"); grad = r.get("lapse_850_700")
    qt = r.get("quota_termica"); nb = r.get("nuv_bassa"); pio = r.get("pioggia")
    zt = r.get("zero_term"); raf = r.get("raffiche"); cum = r.get("cumuli")
    p, note = 50, []

    pio_ = 0 if pd.isna(pio) else pio
    if pio_ >= 60: p -= 40; note.append("pioggia probabile")
    elif pio_ >= 30: p -= 18; note.append("qualche rovescio")

    nb_ = 0 if pd.isna(nb) else nb
    v_ = 0 if pd.isna(v700) else v700

    if att in ("cross", "hef"):
        # vento: ne serve poco ma non zero
        if v_ <= 12: p += 12
        elif v_ <= 22: p += 18
        elif v_ <= 30: p += 2; note.append("vento sostenuto")
        elif v_ <= 40: p -= 22; note.append("vento forte in quota")
        else: p -= 40; note.append("troppo vento")
        # gradiente
        if pd.notna(grad):
            if grad >= 0.80: p += 18; note.append("gradiente ottimo")
            elif grad >= 0.65: p += 14; note.append("buon gradiente")
            elif grad >= 0.50: p += 5
            else: p -= 14; note.append("aria stabile")
        # quota di lavoro
        if pd.notna(qt):
            if qt >= 2500: p += 14; note.append("termiche alte")
            elif qt >= 1800: p += 9
            elif qt >= 1200: p += 3
            else: p -= 10; note.append("tetto basso")
        if nb_ >= 70: p -= 22; note.append("coperto basso")
        elif nb_ >= 40: p -= 8
        if cum: p += 6; note.append("cumuli segnalatori")
        c_ = 0 if pd.isna(cape) else cape
        if c_ >= 1500: p -= 18; note.append("rischio sovrasviluppi")
        elif c_ >= 800: p -= 6
        if att == "hef":
            p += 6   # perdona condizioni piu' magre: tanto si sale a piedi
            if pd.notna(raf) and raf >= 45: p -= 14; note.append("raffiche al suolo")
    else:
        # paralpinismo: conta salire in sicurezza e volare giu' in aria calma
        if v_ <= 12: p += 24; note.append("aria calma")
        elif v_ <= 20: p += 12
        elif v_ <= 28: p -= 8; note.append("vento in quota")
        else: p -= 35; note.append("troppo vento in cresta")
        c_ = 0 if pd.isna(cape) else cape
        if c_ >= 800: p -= 25; note.append("instabilità: temporali")
        elif c_ >= 400: p -= 10
        if nb_ >= 60: p -= 18; note.append("visibilità scarsa")
        elif nb_ <= 20: p += 10; note.append("cielo pulito")
        if pd.notna(raf) and raf >= 50: p -= 12
        if att == "pa_est":
            if pd.notna(zt):
                if zt >= 3200: p += 8
                elif zt <= 2000: p -= 8; note.append("zero termico basso")
        else:  # pa_inv
            if pd.notna(zt):
                if zt <= 1800: p += 10; note.append("neve fredda")
                elif zt >= 2800: p -= 12; note.append("zero termico alto, neve molle")
            if pd.notna(grad) and grad >= 0.85:
                p -= 6; note.append("rischio instabilità del manto")
    p = max(0, min(100, p))
    return p, (", ".join(note[:3]) if note else "condizioni ordinarie")

def colore_punteggio(p):
    if p >= 72: return "\U0001F7E2"
    if p >= 55: return "\U0001F7E1"
    if p >= 38: return "\U0001F7E0"
    return "\U0001F534"

# ======================================================================
# APP
# ======================================================================
import json, math, os
import pandas as pd
import streamlit as st
import pydeck as pdk
import streamlit.components.v1 as components
import sys as _sys
M = _sys.modules[__name__]   # il motore meteo e' definito qui sopra

st.set_page_config(page_title="Nordest — volo", page_icon="\U0001FA82", layout="centered")
BASE = os.path.dirname(os.path.abspath(__file__))

st.markdown("""<style>
.block-container{padding-top:1.4rem;padding-bottom:3rem;max-width:860px}
h1,h2,h3{letter-spacing:-.02em}
div[data-testid="stMetricValue"]{font-size:1.35rem;font-weight:650}
div[data-testid="stMetricLabel"] p{font-size:.72rem;opacity:.72;text-transform:uppercase;
  letter-spacing:.06em}
.card{border:1px solid rgba(128,128,128,.25);border-radius:14px;padding:.9rem 1.05rem;
  margin:.45rem 0;background:rgba(128,128,128,.045)}
.card.g{border-left:4px solid #22a046}.card.y{border-left:4px solid #e0a500}
.card.o{border-left:4px solid #e2741c}.card.r{border-left:4px solid #cc2b2b}
.card.b{border-left:4px solid #3c91e6}.card.n{border-left:4px solid #8a8a8a}
.card h4{margin:0 0 .3rem 0;font-size:1rem;font-weight:650}
.card .sub{font-size:.82rem;opacity:.75;line-height:1.45}
.chip{display:inline-block;padding:.12rem .55rem;border-radius:999px;font-size:.72rem;
  border:1px solid rgba(128,128,128,.35);margin:.1rem .25rem .1rem 0;white-space:nowrap}
.kv{display:flex;justify-content:space-between;gap:1rem;padding:.3rem 0;
  border-bottom:1px dashed rgba(128,128,128,.22);font-size:.87rem}
.kv:last-child{border-bottom:none}
.kv .k{opacity:.7}.kv .v{font-weight:600;font-variant-numeric:tabular-nums;text-align:right}
.kv.lunga{display:block}
.kv.lunga .k{display:block;font-size:.76rem;text-transform:uppercase;letter-spacing:.05em}
.kv.lunga .v{display:block;text-align:left;font-weight:450;line-height:1.5;margin-top:.15rem}
.bar{height:7px;border-radius:4px;background:rgba(128,128,128,.2);overflow:hidden}
.bar>i{display:block;height:100%}
.stTabs [data-baseweb="tab"]{font-size:.95rem;font-weight:600}
</style>""", unsafe_allow_html=True)

@st.cache_data
def carica():
    return pd.DataFrame(json.load(open(os.path.join(BASE, "siti_ne.json"), encoding="utf-8")))

df = carica()
PRIORITA = ["pa_inv", "pa_est", "hef", "cross"]
ORDINE = ["1 Friuli","2 Alpi Giulie","6 Pordenonese / Carnia ovest","3 Slovenia",
          "4 Alpago","5 Feltrino","10 Cadore / Dolomiti","11 Dolomiti / Agordino",
          "8 Austria / Carinzia","9 Slovenia centrale / Austria est",
          "7 Veneto (Bassano/Marostica)"]
CAMPI = ["nome","note","vento","difficolta","partenza","categoria","fonte","zona"]
VIN_FLAT = {v["sito"]: v for vs in VINCOLI.values() for v in vs}

# Per i decolli senza scheda vincoli scritta a mano, i settori si ricavano
# dall'esposizione: quella dichiarata dalla fonte (campo "vento") oppure, se manca,
# quella stimata dal pendio sul modello del terreno (campo "vento_stimato").
_DIR = {"N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90, "ESE": 112.5, "SE": 135,
        "SSE": 157.5, "S": 180, "SSW": 202.5, "SSO": 202.5, "SW": 225, "SO": 225,
        "WSW": 247.5, "OSO": 247.5, "W": 270, "O": 270, "WNW": 292.5, "ONO": 292.5,
        "NW": 315, "NO": 315, "NNW": 337.5, "NNO": 337.5}

def settori_da_testo(s, ampiezza=30):
    import re as _re
    gradi = [_DIR[x] for x in _re.split(r"[^A-Z]+", str(s or "").upper()) if x in _DIR]
    if not gradi: return None
    if len(set(gradi)) >= 7: return [(0, 360)]
    out = []
    for g in gradi:
        a, b = (g - ampiezza) % 360, (g + ampiezza) % 360
        out += [(a, b)] if a < b else [(a, 360), (0, b)]
    return out

for _, _r in df[df["tipo"].isin(["decollo", "hike&fly"])].iterrows():
    if _r["nome"] in VIN_FLAT: continue
    _v = _r.get("vento") if isinstance(_r.get("vento"), str) else ""
    _st = _r.get("vento_stimato") if isinstance(_r.get("vento_stimato"), str) else ""
    _s = settori_da_testo(_v) if _v else settori_da_testo(_st, 35) if _st else None
    if not _s: continue
    VIN_FLAT[_r["nome"]] = dict(
        sito=_r["nome"], settori=_s, vietati=[], max_v=22 if _v else 20,
        max_giallo=30 if _v else 26, auto=True, stimata=not _v,
        nota=(f"Esposizione {_v} (dalla fonte). Settori automatici: da verificare." if _v else
              f"Esposizione STIMATA dal pendio: {_st}. Da verificare sul posto."))
CL = {"\U0001F7E2":"g","\U0001F7E1":"y","\U0001F7E0":"o","\U0001F534":"r",
      "\U0001F535":"b","⚪":"n","—":"n","·":"n"}

def rgb(a):  return ATTIVITA.get(a, {}).get("rgb", [136,136,136])
def hexa(a): return "#%02x%02x%02x" % tuple(rgb(a))
def eti(a):  return ATTIVITA.get(a, {}).get("eti", a)
def ico(a):  return ATTIVITA.get(a, {}).get("ico", "\U0001F4CD")

def att_prim(l, am=None):
    for a in PRIORITA:
        if a in l and (am is None or a in am): return a
    return l[0] if l else "cross"

def dist_km(a,b,c,d):
    return math.hypot((a-c)*111, (b-d)*111*math.cos(math.radians((a+c)/2)))

def val(r,c):
    v = r[c] if c in r.index else None
    return "" if v is None or (isinstance(v,float) and pd.isna(v)) else v

def cardinale(v):
    p = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return p[int((v % 360)/22.5 + 0.5) % 16] if pd.notna(v) else "—"

def card(titolo, sotto="", stato="n"):
    st.markdown(f"<div class='card {stato}'><h4>{titolo}</h4>"
                + (f"<div class='sub'>{sotto}</div>" if sotto else "") + "</div>",
                unsafe_allow_html=True)

def kv(righe):
    def riga(k, v):
        # i valori lunghi vanno a capo sotto l'etichetta, se no la colonna si strozza
        cl = "kv lunga" if len(str(v)) > 44 else "kv"
        return f"<div class='{cl}'><span class='k'>{k}</span><span class='v'>{v}</span></div>"
    st.markdown("<div class='card'>" + "".join(riga(k, v) for k, v in righe) + "</div>",
                unsafe_allow_html=True)

def barra(perc, colore="#3c91e6"):
    p = 0 if pd.isna(perc) else max(0, min(100, perc))
    return f"<div class='bar'><i style='width:{p:.0f}%;background:{colore}'></i></div>"

def in_settore(deg, s):
    if pd.isna(deg): return False
    d = deg % 360
    for a,b in s:
        if a <= b and a <= d <= b: return True
        if a > b and (d >= a or d <= b): return True
    return False

def giudizio(v, deg, s):
    if pd.isna(v): return "·", "dati mancanti"
    if in_settore(deg, s["vietati"]):     return "\U0001F534", "direzione vietata"
    if not in_settore(deg, s["settori"]): return "\U0001F534", "fuori settore"
    if v <= s["max_v"]:      return "\U0001F7E2", f"{v:.0f} km/h, in settore"
    if v <= s["max_giallo"]: return "\U0001F7E1", f"{v:.0f} km/h, al limite"
    return "\U0001F534", f"{v:.0f} km/h, troppo vento"

@st.cache_data(ttl=900, show_spinner="Scarico il meteo…")
def analisi(la, lo):
    return M.analizza(la, lo)

def mappa(b, zoom=8, ammesse=None, verdetti=None, h=420, key=None, spiega=None):
    """Mappa dei punti. Con key= diventa cliccabile e ritorna il nome del punto scelto."""
    m = b.dropna(subset=["lat","lon"]).copy()
    if not len(m):
        st.info("Nessun punto con questi filtri."); return None
    if verdetti is not None:
        COL = {"\U0001F7E2":[34,160,70],"\U0001F7E1":[225,170,20],
               "\U0001F534":[200,45,45],"⚪":[150,150,150]}
        m["_e"] = [verdetti.get(n,"⚪") for n in m["nome"]]
        m["col"] = [COL.get(v,[150,150,150]) for v in m["_e"]]
        m["etichetta"] = m["_e"]
    else:
        m["_a"] = [att_prim(a if isinstance(a,list) else [], ammesse) for a in m["att"]]
        m["col"] = [rgb(a) for a in m["_a"]]
        m["etichetta"] = [eti(a) for a in m["_a"]]
    m["rad"] = [460 if t=="decollo" else (380 if t=="hike&fly" else 240) for t in m["tipo"]]
    m["sotto"] = [(f"{int(r['quota'])} m · " if val(r,'quota') else "")
                  + (str(r["vento"]) if val(r,"vento") else
                     (f"{r['vento_stimato']} (stimata)" if val(r,"vento_stimato") else r["tipo"]))
                  for _, r in m.iterrows()]
    m["salita"] = ["\U0001F97E via di salita descritta" if val(r,"partenza") else ""
                   for _, r in m.iterrows()]
    deck = pdk.Deck(
        layers=[pdk.Layer("ScatterplotLayer", id="punti",
                data=m[["lat","lon","col","rad","nome","etichetta","sotto","tipo","salita"]],
                get_position=["lon","lat"], get_fill_color="col", get_radius="rad",
                radius_min_pixels=5, radius_max_pixels=18, pickable=True, auto_highlight=True,
                stroked=True, get_line_color=[255,255,255], line_width_min_pixels=1)],
        map_style=None,
        initial_view_state=pdk.ViewState(latitude=float(m["lat"].mean()),
                                         longitude=float(m["lon"].mean()), zoom=zoom),
        tooltip={"html": "<b>{nome}</b><br/>{tipo} · {etichetta}<br/>{sotto}<br/>{salita}"
                         + ("<br/><i>clic per aprire la scheda e la salita</i>" if key else ""),
                 "style": {"fontSize": "12px"}})
    scelto = None
    if key:
        ev = st.pydeck_chart(deck, height=h, on_select="rerun",
                             selection_mode="single-object", key=key)
        try:
            ogg = ev.selection["objects"].get("punti") or []
            if ogg: scelto = ogg[0]["nome"]
        except Exception:
            scelto = None
    else:
        st.pydeck_chart(deck, height=h)
    with st.expander("ℹ️ Come leggere la mappa"):
        if verdetti is not None:
            st.markdown("Ogni punto è un decollo. 🟢 si vola con il vento previsto, "
                        "🟡 al limite (o esposizione solo stimata dal pendio), 🔴 vento "
                        "sbagliato per quel decollo, ⚪ esposizione "
                        "non nota. Passa sopra un punto per nome, quota ed esposizione.")
        else:
            st.markdown("Colore = attività principale del punto. Punti grandi = decolli, "
                        "medi = hike & fly, piccoli = atterraggi e servizi. Passa sopra un "
                        "punto per nome, quota ed esposizione; \U0001F97E indica che c'è la "
                        "via di salita descritta."
                        + (" **Clicca** un decollo per aprire sotto la sua scheda con la "
                           "via di salita." if key else ""))
            st.markdown("  ".join(f"<span class='chip' style='border-color:{hexa(a)}'>"
                                  f"{ico(a)} {eti(a)}</span>" for a in ATTIVITA),
                        unsafe_allow_html=True)
        if spiega: st.markdown(spiega)
    return scelto

def scheda_sito(r, verdetto=None, motivo=None):
    a = r["att"] if isinstance(r["att"], list) else []
    chips = "".join(f"<span class='chip'>{ico(x)} {eti(x)}</span>" for x in a)
    aff = {"V":"✅ verificato","K":"\U0001F7E1 solo KML","C":"\U0001F4D7 relazione Cammina e Vola",
           "?":"❓ da verificare"}.get(val(r,"aff"), "")
    if verdetto: st.markdown(f"**{verdetto} {motivo or ''}**")
    st.markdown(chips, unsafe_allow_html=True)
    righe = []
    if val(r,"quota"):      righe.append(("Quota", f"{int(r['quota'])} m"))
    if val(r,"vento"):      righe.append(("Esposizione", str(r["vento"])))
    elif val(r,"vento_stimato"): righe.append(("Esposizione (stimata dal pendio)", str(r["vento_stimato"])))
    if val(r,"difficolta"):
        d_ = str(r["difficolta"])
        righe.append(("Difficoltà decollo", d_[4:]) if d_.startswith("H&F ")
                     else ("Valutazione sito", d_))
    if val(r,"disl"):       righe.append(("Dislivello", f"{int(r['disl'])} m"))
    if val(r,"partenza"):   righe.append(("Via di salita", str(r["partenza"])))
    righe.append(("Zona", r["zona"]))
    righe.append(("Affidabilità", aff))
    if "dist" in r.index and pd.notna(r["dist"]): righe.append(("Distanza", f"{r['dist']:.0f} km"))
    kv(righe)
    if val(r,"note"): st.write(r["note"])
    st.caption(f"Fonte: {val(r,'fonte')}  ·  `{r['lat']:.5f}, {r['lon']:.5f}`")
    link = [f"[Maps](https://www.google.com/maps/search/?api=1&query={r['lat']},{r['lon']})",
            f"[Organic Maps](om://map?v=1&ll={r['lat']},{r['lon']}&n={r['nome']})",
            f"[meteo-parapente](https://meteo-parapente.com/#/{r['lat']},{r['lon']},11)"]
    if "url" in r.index and val(r, "url"):
        link.append(f"[relazione](https://{str(r['url']).lstrip('/')})")
    st.markdown(" · ".join(link))


def _accesso(note):
    """Estrae dalle note il pezzo che parla di come si arriva al decollo."""
    import re
    s = str(note or "")
    m = re.search(r"(ACCESSO|SALITA|AVVICINAMENTO)\s*:\s*(.+?)(?=\s[A-Z]{4,}[ A-Z']*:|$)", s)
    return m.group(2).strip() if m else ""

def vie_di_salita(B, cliccato, att):
    """Sezione 'Vie di salita': si apre sul decollo cliccato in mappa."""
    dec = B[B["tipo"].isin(["decollo","hike&fly"])].sort_values("nome")
    if not len(dec): return
    st.markdown("<div id='vie-di-salita'></div>", unsafe_allow_html=True)
    st.markdown("#### \U0001F97E Vie di salita")
    nomi = list(dec["nome"])
    con_via = set(dec[[bool(val(r,"partenza")) or bool(_accesso(r["note"]))
                       for _, r in dec.iterrows()]]["nome"])
    k = f"via_{att}"
    if cliccato in nomi and st.session_state.get(f"{k}_ultimo") != cliccato:
        st.session_state[k] = cliccato
        st.session_state[f"{k}_ultimo"] = cliccato
        components.html("<script>const e=window.parent.document.getElementById('vie-di-salita');"
                        "if(e) e.scrollIntoView({behavior:'smooth', block:'start'});</script>",
                        height=0)
    scelta = st.selectbox("Decollo", nomi, key=k, index=None,
                          placeholder="clicca un decollo sulla mappa o sceglilo qui",
                          format_func=lambda n: ("\U0001F97E " if n in con_via else "") + n)
    st.caption(f"{len(con_via)} decolli su {len(nomi)} hanno la salita descritta (\U0001F97E).")
    if not scelta: return
    r = dec[dec["nome"] == scelta].iloc[0]
    via = str(val(r,"partenza") or "") or _accesso(r["note"])
    righe = []
    if val(r,"quota"): righe.append(("Quota decollo", f"{int(r['quota'])} m"))
    if val(r,"disl"):  righe.append(("Dislivello a piedi", f"{int(r['disl'])} m"))
    if val(r,"vento"): righe.append(("Esposizione", str(r["vento"])))
    elif val(r,"vento_stimato"): righe.append(("Esposizione (stimata dal pendio)", str(r["vento_stimato"])))
    if val(r,"difficolta"):
        d_ = str(r["difficolta"])
        righe.append(("Difficoltà decollo", d_[4:] if d_.startswith("H&F ") else d_))
    card(f"\U0001F97E {r['nome']}",
         via if via else "Via di salita non ancora descritta per questo decollo: "
                         "se la conosci, segnalala nella scheda Neve → Osservazioni.",
         "g" if via else "n")
    if righe: kv(righe)
    zv = montagna.zona_vicina(float(r["lat"]), float(r["lon"]))
    if zv:
        try:
            import manto
            from datetime import date as _d
            _tab, _dia = montagna.dati_neve(_d.today())
            g_ = _dia.get(zv["id"])
            if g_:
                card(f"{g_['emoji']} Neve oggi nella zona {zv['nome']} ({zv['q']} m)",
                     f"{g_['titolo']} — {g_['attrezzatura']}<br>"
                     f"<span style='opacity:.7'>Dettagli nella scheda Neve per zona.</span>",
                     "b")
        except Exception:
            st.caption(f"Zona neve: {zv['nome']} (dati non disponibili ora).")
    st.markdown(f"[Termiche e skyways su kk7]({montagna.link_kk7(float(r['lat']), float(r['lon']), 13)})"
                f" · [Decollo su burnair](https://map.burnair.cloud/#14/{float(r['lat']):.4f}/{float(r['lon']):.4f})")
    if not val(r, "vento") and isinstance(r.get("vento_stimato"), str) and r.get("vento_stimato"):
        st.caption(f"Esposizione stimata dal pendio: {r['vento_stimato']} "
                   f"(pendenza ~{r.get('pendenza', '?')}°). Da verificare.")
    with st.expander("Scheda completa del decollo"):
        scheda_sito(r)

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### Filtri")
    zone_d = [z for z in ORDINE if z in set(df["zona"])]
    z_sel = st.multiselect("Zona", zone_d,
                           default=[z for z in zone_d if not z.startswith(("7 ","8 ","9 ","11 "))])
    aff_sel = st.multiselect("Affidabilità", ["V","C","K","?"], default=["V","C","K","?"],
                             format_func=lambda a: {"V":"✅ verificato",
                                                    "C":"\U0001F4D7 Cammina e Vola",
                                                    "K":"\U0001F7E1 solo KML",
                                                    "?":"❓ da verificare"}[a])
    serv = st.checkbox("Mostra parcheggi e impianti", value=False)
    pos = st.text_input("La tua posizione — lat, lon", placeholder="46.27, 13.14")

base = df[df["zona"].isin(z_sel) & df["aff"].isin(aff_sel)].copy()
if not serv: base = base[~base["tipo"].isin(["parcheggio","impianto"])]
if pos.strip():
    try:
        a_, b_ = [float(x) for x in pos.replace(";",",").split(",")[:2]]
        base["dist"] = [dist_km(a_,b_,la,lo) for la,lo in zip(base["lat"], base["lon"])]
        base = base.sort_values("dist")
    except Exception:
        st.sidebar.error("Formato: 46.27, 13.14")
base = base.reset_index(drop=True)

def solo(a):
    return base[[a in (x if isinstance(x,list) else []) for x in base["att"]]]

st.markdown("## \U0001FA82 Nordest")
st.caption("Friuli · Carnia · Alpi Giulie · Slovenia di confine · Alpago · bellunese")

import montagna
import osservazioni
T_METEO, T_SITI, T_NEVE, T_ROTTE, T_OSS, T_INFO = st.tabs(
    ["\U0001F324️  Meteo", "\U0001FA82  Attività", "❄️  Neve per zona",
     "\U0001F9ED  Rotte di volo", "\U0001F4DD  Osservazioni", "\U0001F527  Info"])

# ======================================================= METEO
with T_METEO:
    # ---------------- panoramica regionale ----------------
    @st.cache_data(ttl=900, show_spinner="Guardo tutta la regione\u2026")
    def panoramica():
        from concurrent.futures import ThreadPoolExecutor
        def uno(kv_):
            nome, (a_, b_) = kv_
            try:
                return nome, M.analizza(a_, b_)
            except Exception:
                return nome, None
        out = {}
        with ThreadPoolExecutor(max_workers=6) as ex:
            for nome, res in ex.map(uno, list(PUNTI_METEO.items())):
                if res: out[nome] = res
        return out

    st.markdown("### Colpo d'occhio sulla regione")
    pano = panoramica()
    if not pano:
        st.warning("Non riesco a raggiungere Open-Meteo adesso: la panoramica resta vuota.")
        giorni_comuni = []
    else:
        giorni_comuni = sorted(set.intersection(*[set(t_["g"]) for t_, _, _ in pano.values()]))

    if giorni_comuni:
        gsel = st.select_slider(
            "Giorno", giorni_comuni, value=giorni_comuni[0],
            format_func=lambda x: pd.Timestamp(x).strftime("%a %d/%m"), key="gpano")

        righe = []
        for nome, (t_, qs_, qd_) in pano.items():
            sub = t_[t_["g"] == gsel]
            if not len(sub): continue
            rr = sub.iloc[0]
            d_ = {"zona": nome, "r": rr, "quota": qs_}
            for a_ in ATTIVITA:
                d_[a_] = M.punteggio(rr, a_)
            righe.append(d_)

        # --- mappa regionale (in cima)
        att_p = st.segmented_control(
            "Attività", list(ATTIVITA), default="cross",
            format_func=lambda a: f"{ico(a)} {eti(a)}", key="pano_att") or "cross"
        # --- mappa regionale
        st.markdown("#### La regione a colpo d'occhio")
        COLP = {"\U0001F7E2":[34,160,70],"\U0001F7E1":[225,180,20],
                "\U0001F7E0":[226,116,28],"\U0001F534":[200,45,45]}
        mp = pd.DataFrame([{
            "nome": x["zona"], "lat": PUNTI_METEO[x["zona"]][0],
            "lon": PUNTI_METEO[x["zona"]][1], "p": x[att_p][0],
            "col": COLP[M.colore_punteggio(x[att_p][0])],
            "rad": 3000 + x[att_p][0]*90, "perche": x[att_p][1],
            "vento": (f"{x['r']['v700']:.0f} km/h {cardinale(x['r']['d700'])}"
                      if pd.notna(x["r"]["v700"]) else "—"),
            "tetto": (f"{x['r']['quota_termica']:.0f} m"
                      if pd.notna(x["r"]["quota_termica"]) else "—")} for x in righe])
        st.pydeck_chart(pdk.Deck(
            layers=[
                pdk.Layer("ScatterplotLayer", data=mp, get_position=["lon","lat"],
                          get_fill_color="col", get_radius="rad", opacity=0.55,
                          radius_min_pixels=14, radius_max_pixels=54, pickable=True,
                          stroked=True, get_line_color=[255,255,255], line_width_min_pixels=1),
                pdk.Layer("TextLayer", data=mp, get_position=["lon","lat"], get_text="p",
                          get_size=13, get_color=[20,20,20], size_units="'pixels'")],
            map_style=None,
            initial_view_state=pdk.ViewState(latitude=46.2, longitude=13.0, zoom=7.4),
            tooltip={"html": "<b>{nome}</b><br/>{p}/100 · {perche}<br/>vento 700 hPa {vento} · tetto termiche {tetto}"}), height=420)
        with st.expander("ℹ️ Come leggere la mappa"):
            st.markdown("Ogni cerchio è una zona meteo. **Colore** = punteggio dell'attività "
                        "scelta (🟢 buono, 🟡 discreto, 🟠 scarso, 🔴 no); **grandezza** e "
                        "**numero** = punteggio su 100. Passa sopra un cerchio per il motivo, "
                        "il vento a 700 hPa (~3000 m) e il tetto delle termiche. Il giorno si "
                        "cambia con il cursore qui sopra.")
        st.caption("Il punteggio pesa vento in quota, gradiente, tetto delle termiche, nuvole "
                   "basse, instabilit\u00e0 e pioggia, con criteri diversi per ogni attivit\u00e0: "
                   "il cross vuole gradiente e quota, il paralpinismo vuole aria calma e "
                   "cielo pulito.")


        # --- siti volabili (vento a 700 hPa della zona meteo piu' vicina, giorno scelto)
        st.markdown(f"#### Siti volabili — {pd.Timestamp(gsel).strftime('%a %d/%m')}")
        vz = {}
        for nome_, (t_, _, _) in pano.items():
            sub = t_[t_["g"] == gsel]
            if len(sub): vz[nome_] = (sub.iloc[0]["v700"], sub.iloc[0]["d700"])
        B = solo(att_p); B = B[B["tipo"].isin(["decollo","hike&fly"])]
        verdetti, motivi = {}, {}
        for _, x in B.iterrows():
            vk = VIN_FLAT.get(x["nome"])
            if vk and vz:
                zn = min(vz, key=lambda n: dist_km(float(x["lat"]), float(x["lon"]),
                                                    *PUNTI_METEO[n]))
                ic2, why = giudizio(vz[zn][0], vz[zn][1], vk)
                if vk.get("stimata") and ic2 == "\U0001F7E2":
                    ic2, why = "\U0001F7E1", why + " — esposizione solo stimata dal pendio"
                verdetti[x["nome"]] = ic2; motivi[x["nome"]] = (why, vk["nota"], zn)
            else:
                verdetti[x["nome"]] = "⚪"
        cnt = {k: sum(1 for z in verdetti.values() if z==k)
               for k in ["\U0001F7E2","\U0001F7E1","\U0001F534","⚪"]}
        s1,s2_,s3,s4 = st.columns(4)
        s1.metric("\U0001F7E2 Si vola", cnt["\U0001F7E2"])
        s2_.metric("\U0001F7E1 Al limite", cnt["\U0001F7E1"])
        s3.metric("\U0001F534 No", cnt["\U0001F534"])
        s4.metric("⚪ Ignoto", cnt["⚪"])
        mappa(B, zoom=7.8, verdetti=verdetti, h=430,
              spiega="Il vento usato per ogni decollo è quello a 700 hPa (~3000 m) della "
                     "zona meteo più vicina, nel giorno scelto sopra. Il semaforo confronta "
                     "solo quel vento con l'esposizione del decollo: brezza di valle, "
                     "inversioni e stato del terreno li valuti tu.")
        for stato, tit in [("\U0001F7E2","Si vola"),("\U0001F7E1","Al limite"),
                           ("\U0001F534","Da escludere")]:
            bl = B[[verdetti.get(n)==stato for n in B["nome"]]]
            if not len(bl): continue
            with st.expander(f"{stato} {tit} — {len(bl)}"):
                for _, x in bl.sort_values("nome").iterrows():
                    w = motivi.get(x["nome"])
                    st.markdown(f"**{x['nome']}** — {w[0] if w else ''}"
                                + (f" *(meteo: {w[2]})*" if w else ""))
                    if w and w[1]: st.caption(w[1])

        # --- carte e mappe (Windy ecc.)
        st.markdown("#### Carte e mappe")
        LIV = {"Superficie":"surface","850 hPa (~1500 m)":"850h","700 hPa (~3000 m)":"700h",
               "600 hPa (~4200 m)":"600h","500 hPa (~5500 m)":"500h"}
        STR = {"Vento":"wind","Raffiche":"gust","Nuvole":"clouds","Base nubi":"cbase",
               "CAPE":"cape","Pioggia":"rain","Temperatura":"temp","Pressione":"pressure",
               "Isoterma zero":"deg0"}
        # Modelli della carta Windy incorporata. ALADIN (CHMI, "czeAladin") su windy.com
        # c'e' ma la carta incorporata non lo accetta: si apre col pulsante qui sotto.
        MODELLI_W = {"AROME (Météo-France, famiglia ALADIN, ~1,3 km)": "arome",
                     "ICON-D2 (DWD, ~2,2 km)": "iconD2", "ICON-EU (DWD, ~7 km)": "iconEu",
                     "ECMWF (~9 km)": "ecmwf", "GFS (~22 km)": "gfs"}
        fonte_c = st.radio("Carta", ["Windy", "Paragliding Map (volabilità dei siti)"],
                           horizontal=True, key="w_fonte")
        cw0, cw1 = st.columns([2,2])
        zw = cw0.selectbox("Centro della carta", list(PUNTI_METEO), key="w_zona")
        wla, wlo = PUNTI_METEO[zw]
        if fonte_c == "Windy":
            mod = cw1.selectbox("Modello", list(MODELLI_W), key="w_mod")
            cw2, cw3 = st.columns(2)
            strato = cw2.selectbox("Strato", list(STR), key="w_ov")
            livw = cw3.selectbox("Quota", list(LIV), index=2, key="w_lv")
            components.iframe(
                f"https://embed.windy.com/embed2.html?lat={wla}&lon={wlo}"
                f"&detailLat={wla}&detailLon={wlo}&zoom=8&level={LIV[livw]}"
                f"&overlay={STR[strato]}&product={MODELLI_W[mod]}&menu=&message=true&marker=true"
                "&calendar=now&pressure=true&type=map&location=coordinates&detail=true"
                "&metricWind=km%2Fh&metricTemp=%C2%B0C&radarRange=-1", height=480)
            st.link_button("Apri su Windy con il modello ALADIN",
                           f"https://www.windy.com/?czeAladin,{wla:.3f},{wlo:.3f},9",
                           width="stretch")
            with st.expander("ℹ️ Come leggere la carta"):
                st.markdown("Carta Windy col **modello** scelto: di base AROME, il modello ad "
                            "alta risoluzione della famiglia ALADIN, che vede meglio valli e "
                            "brezze; ICON-D2 è l'alternativa ad alta risoluzione; ECMWF e GFS "
                            "sono globali, più lisci. ALADIN vero e proprio Windy lo mostra solo "
                            "sul suo sito: pulsante sopra. Scegli lo **strato** (vento, raffiche, "
                            "nuvole, base nubi, CAPE, pioggia, temperatura, pressione, zero "
                            "termico) e la **quota**: 850 hPa ≈ 1500 m, 700 hPa ≈ 3000 m. "
                            "In basso scorri le ore; clicca un punto per il meteogramma. "
                            "Non tutti gli strati esistono per tutti i modelli.")
        else:
            components.iframe(f"https://www.paraglidingmap.com/thirdpartywidget.aspx?"
                              f"lat={wla}&lng={wlo}&zoom=9", height=480)
            with st.expander("ℹ️ Come leggere la carta"):
                st.markdown("Widget ufficiale di Paragliding Map: ogni decollo è colorato "
                            "secondo la volabilità prevista (vento rispetto all'esposizione "
                            "del decollo) e ci sono le stazioni meteo in tempo reale. Trascina "
                            "e ingrandisci; clicca un decollo per i dettagli. Alcune funzioni "
                            "sono solo per abbonati sul loro sito.")
            st.caption("Paragliding Map permette di incorporare il widget; i suoi dati non "
                       "vengono copiati nell'app.")
        st.markdown("[Wetterzentrale](https://www.wetterzentrale.de/en/topkarten.php?model=ecm&var=1) "
                    "· [Meteociel](https://www.meteociel.fr/modeles/ecmwf_cartes.php) "
                    "· [ARPA FVG OSMER](https://www.meteo.fvg.it/) "
                    "· [Radar Protezione Civile](https://radar.protezionecivile.it/) "
                    f"· [meteo-parapente](https://meteo-parapente.com/#/{wla},{wlo},11)")
        st.divider()

        # --- le zone migliori, attivita' per attivita'
        st.markdown("#### Dove conviene andare")
        cc = st.columns(2)
        for i, (a_, cfg) in enumerate(ATTIVITA.items()):
            ord_ = sorted(righe, key=lambda x: -x[a_][0])
            if not ord_: continue
            top = ord_[0]
            p_, why = top[a_]
            ic_ = M.colore_punteggio(p_)
            secondi = ", ".join(x["zona"].split("\u2014")[0].strip() for x in ord_[1:3])
            with cc[i % 2]:
                card(f"{cfg['ico']} {cfg['eti']}",
                     f"<b>{ic_} {top['zona']}</b> \u2014 {p_}/100<br>"
                     f"<span style='opacity:.8'>{why}</span><br>"
                     f"<span style='font-size:.78rem;opacity:.65'>poi: {secondi}</span>",
                     CL.get(ic_, "n"))

        # --- tabella di tutte le zone
        st.markdown(f"#### Tutte le zone \u2014 {eti(att_p)}")
        for x in sorted(righe, key=lambda z: -z[att_p][0]):
            rr, p_, why = x["r"], x[att_p][0], x[att_p][1]
            ic_ = M.colore_punteggio(p_)
            v_ = (f"{rr['v700']:.0f} km/h {cardinale(rr['d700'])}"
                  if pd.notna(rr["v700"]) else "\u2014")
            qt_ = f"{rr['quota_termica']:.0f} m" if pd.notna(rr["quota_termica"]) else "\u2014"
            nb_ = f"{rr['nuv_bassa']:.0f}%" if pd.notna(rr["nuv_bassa"]) else "\u2014"
            pi_ = f"{rr['pioggia']:.0f}%" if pd.notna(rr["pioggia"]) else "\u2014"
            st.markdown(
                f"<div class='card {CL.get(ic_,'n')}'>"
                f"<h4>{ic_} {x['zona']} <span style='float:right;opacity:.6'>{p_}/100</span></h4>"
                f"<div class='sub'>{why}</div>"
                f"<div class='kv'><span class='k'>Vento 700 hPa</span><span class='v'>{v_}</span></div>"
                f"<div class='kv'><span class='k'>Tetto termiche</span><span class='v'>{qt_}</span></div>"
                f"<div class='kv'><span class='k'>Nubi basse</span><span class='v'>{nb_}</span></div>"
                f"<div class='kv'><span class='k'>Pioggia</span><span class='v'>{pi_}</span></div>"
                f"</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("### Approfondimento su una localit\u00e0")
    modo = st.radio("Riferimento", ["Zona", "Da un sito", "Coordinate"],
                    horizontal=True, label_visibility="collapsed")
    if modo == "Zona":
        luogo = st.selectbox("Zona di riferimento", list(PUNTI_METEO))
        la, lo = PUNTI_METEO[luogo]
    elif modo == "Da un sito":
        dec = base[base["tipo"].isin(["decollo","hike&fly"])].sort_values("nome")
        nomi = list(dec["nome"])
        if nomi:
            scelto = st.selectbox("Decollo", nomi)
            rr = dec[dec["nome"]==scelto].iloc[0]
            la, lo, luogo = rr["lat"], rr["lon"], scelto
        else:
            luogo = list(PUNTI_METEO)[0]; la, lo = PUNTI_METEO[luogo]
    else:
        c1, c2 = st.columns(2)
        la = c1.number_input("Latitudine", 44.5, 47.5, 46.27, 0.01, format="%.4f")
        lo = c2.number_input("Longitudine", 10.5, 16.0, 13.16, 0.01, format="%.4f")
        luogo = f"{la:.3f}, {lo:.3f}"
    cga, cgb = st.columns([3,1])
    if cgb.button("\U0001F504 Aggiorna", use_container_width=True):
        analisi.clear(); panoramica.clear(); st.rerun()

    try:
        t, qstaz, quando = analisi(float(la), float(lo))
        gg = list(t["g"])
        dflt = gsel if giorni_comuni and gsel in gg else gg[0]
        g = cga.select_slider("Giorno", gg, value=dflt,
                              format_func=lambda x: pd.Timestamp(x).strftime("%a %d/%m"), key="mg")
        r = t[t["g"]==g].iloc[0]

        st.markdown(f"### {luogo} — {pd.Timestamp(g).strftime('%A %d/%m')}")
        i_ic,i_tx = M.giudica_instabilita(r["cape"], r["li"])
        g_ic,g_tx = M.giudica_gradiente(r["lapse_850_700"])
        tb_ic,tb_tx = M.giudica_turbolenza(r["shear_925_700"], r["raff_ratio"], r["v700"])
        in_ic,in_tx = M.descrivi_inversioni(r["inversioni"], qstaz)
        nu_ic,nu_tx = M.giudica_nuvole(r["nuv_bassa"], r["nuv_media"], r["nuv_alta"],
                                       r["base_nubi"], r["quota_termica"], r["cumuli"])
        for ic_, tx_, tit in [(i_ic,i_tx,"Instabilità"), (g_ic,g_tx,"Gradiente termico"),
                              (in_ic,in_tx,"Inversioni"), (tb_ic,tb_tx,"Turbolenza"),
                              (nu_ic,nu_tx,"Copertura nuvolosa")]:
            card(f"{ic_} {tit}", tx_, CL.get(ic_,"n"))

        st.markdown("#### Quote di lavoro")
        q1,q2,q3,q4 = st.columns(4)
        q1.metric("Tetto termiche",
                  f"{r['quota_termica']:.0f}" if pd.notna(r["quota_termica"]) else "—")
        q2.metric("Base cumuli",
                  f"{r['base_nubi']:.0f}" if pd.notna(r["base_nubi"]) else "—")
        q3.metric("Zero termico",
                  f"{r['zero_term']:.0f}" if pd.notna(r["zero_term"]) else "—")
        q4.metric("Stazione", f"{qstaz:.0f}")
        st.caption("Metri sul livello del mare. Il tetto delle termiche è la cima dello "
                   "strato rimescolato; la base dei cumuli viene dallo spread temperatura/rugiada.")

        st.markdown("#### Copertura nuvolosa")
        n1,n2,n3 = st.columns(3)
        for col, et, vv, cc in [(n1,"Basse < 2 km",r["nuv_bassa"],"#cc2b2b"),
                                (n2,"Medie 2-7 km",r["nuv_media"],"#e0a500"),
                                (n3,"Alte > 7 km",r["nuv_alta"],"#3c91e6")]:
            col.markdown(f"<div class='card'><h4>{vv:.0f}%</h4>"
                         f"<div class='sub'>{et}</div>{barra(vv, cc)}</div>"
                         if pd.notna(vv) else f"<div class='card'><h4>—</h4>"
                         f"<div class='sub'>{et}</div></div>", unsafe_allow_html=True)
        strati = r["strati_nubi"]
        if strati:
            st.markdown("**Strati individuati nel profilo**")
            kv([(f"{s['z']:.0f} m ({int(s['hPa'])} hPa)",
                 f"{s['cop']:.0f}% · UR {s['rh']:.0f}%" if pd.notna(s["rh"])
                 else f"{s['cop']:.0f}%") for s in strati])
        else:
            st.caption("Nessuno strato significativo nel profilo verticale.")
        if r["cumuli"]:
            st.success(f"Cumuli attesi con base intorno a {r['base_nubi']:.0f} m: "
                       "hai riferimenti visivi per trovare le termiche.")
        elif pd.notna(r["base_nubi"]) and pd.notna(r["quota_termica"]) \
             and r["base_nubi"] > r["quota_termica"] + 150:
            st.info("Aria secca: termiche blu, nessun cumulo a segnalarle.")

        with st.expander("Gradiente termico, strato per strato"):
            for k, et in [("lapse_925_850","925→850 hPa, il basso"),
                          ("lapse_850_700","850→700 hPa, il medio"),
                          ("lapse_700_500","700→500 hPa, l'alto")]:
                ic_, tx_ = M.giudica_gradiente(r[k])
                v_ = f"{r[k]:.2f} °C/100 m" if pd.notna(r[k]) else "—"
                card(f"{ic_} {et} — {v_}", tx_, CL.get(ic_,"n"))
            st.caption("0,98 °C/100 m è l'adiabatica secca: più ci si avvicina, "
                       "più le termiche sono forti. Sotto 0,45 l'aria è stabile.")

        with st.expander("Profilo verticale e inversioni"):
            prof = pd.DataFrame(r["profilo"]); prof = prof[prof["z"].notna()]
            if len(prof):
                kv([(f"{int(p.hPa)} hPa — {p.z:.0f} m",
                     (f"{p.t:.1f}°" if pd.notna(p.t) else "—") + "  ·  "
                     + (f"{p.v:.0f} km/h {cardinale(p.d)}" if pd.notna(p.v) else "—")
                     + (f"  ·  UR {p.rh:.0f}%" if pd.notna(p.rh) else ""))
                    for p in prof.itertuples()])
                ch = prof[["z","t"]].dropna().set_index("z").sort_index()
                if len(ch):
                    ch.columns = ["temperatura °C"]; st.line_chart(ch, height=200)
                    st.caption("Dove la linea torna a salire andando verso quote maggiori, "
                               "c'è un'inversione.")
            if r["inversioni"]:
                for b2, c2_, dt in r["inversioni"]:
                    st.markdown(f"• inversione da **{b2:.0f} m** a **{c2_:.0f} m**, "
                                f"+{dt:.1f} °C")

        with st.expander("Instabilità, vento e numeri"):
            kv([("CAPE medio", f"{r['cape']:.0f} J/kg" if pd.notna(r["cape"]) else "—"),
                ("CAPE massimo", f"{r['cape_max']:.0f} J/kg" if pd.notna(r["cape_max"]) else "—"),
                ("Lifted index", f"{r['li']:.1f}" if pd.notna(r["li"]) else "—"),
                ("CIN", f"{r['cin']:.0f} J/kg" if pd.notna(r["cin"]) else "—"),
                ("Vento 700 hPa", f"{r['v700']:.0f} km/h {cardinale(r['d700'])}"
                 if pd.notna(r["v700"]) else "—"),
                ("Vento 850 hPa", f"{r['v850']:.0f} km/h {cardinale(r['d850'])}"
                 if pd.notna(r["v850"]) else "—"),
                ("Shear 925→700", f"{r['shear_925_700']:.0f} km/h"
                 if pd.notna(r["shear_925_700"]) else "—"),
                ("Raffiche al suolo", f"{r['raffiche']:.0f} km/h"
                 if pd.notna(r["raffiche"]) else "—"),
                ("Pioggia", f"{r['pioggia']:.0f}%" if pd.notna(r["pioggia"]) else "—")])

        with st.expander("Andamento sui prossimi giorni"):
            s_ = t[["time","quota_termica","base_nubi"]].dropna(subset=["time"]).set_index("time")
            st.line_chart(s_.rename(columns={"quota_termica":"tetto termiche m",
                                             "base_nubi":"base cumuli m"}), height=210)
            s2 = t[["time","cape","v700"]].dropna(subset=["time"]).set_index("time")
            st.line_chart(s2.rename(columns={"cape":"CAPE J/kg","v700":"vento 700 hPa km/h"}),
                          height=210)
        st.caption(f"Medie della fascia 11-16. Ultimo scaricamento: {quando}.")

    except Exception as e:
        st.warning("Non riesco a raggiungere Open-Meteo adesso.")
        st.caption(f"({type(e).__name__}) Serve connessione internet.")

    st.divider()
    st.markdown("#### Come funziona il tempo in Friuli")
    st.caption("Dagli *Appunti di meteorologia per il Friuli Venezia Giulia*, ARPA FVG.")
    for n_, d_ in METEO_FVG:
        with st.expander(n_):
            st.write(d_)
    st.markdown("#### Fonti locali")
    for n_, d_ in FONTI_METEO_FVG:
        st.markdown(f"**{n_}** — {d_}")

# ======================================================= SITI
with T_SITI:
    att = st.segmented_control("Attività", list(ATTIVITA), default="cross",
                               format_func=lambda a: f"{ico(a)} {eti(a)}", key="att") or "cross"
    B = solo(att)
    st.markdown(f"### {ico(att)} {eti(att)}")
    st.caption(DESCR_ATT[att])
    dec = B[B["tipo"].isin(["decollo","hike&fly"])]
    att_l = B[B["tipo"]=="atterraggio"]
    altro = B[B["tipo"].isin(["zona","parcheggio","impianto"])]
    n_esp = int((dec["vento"].astype(str).str.len() > 0).sum())
    n_gr  = int(dec["difficolta"].astype(str).str.startswith("H&F ").sum())
    st.markdown("".join(f"<span class='chip'>{t}</span>" for t in (
        f"\U0001FA82 {len(dec)} decolli", f"\U0001F3AF {len(att_l)} atterraggi",
        f"\U0001F9ED {n_esp} con esposizione",
        *( [f"\U0001F4D0 {n_gr} con difficoltà"] if n_gr else [] ))),
        unsafe_allow_html=True)
    cliccato = mappa(B, zoom=8.1, ammesse={att}, h=430, key=f"mappa_{att}")
    vie_di_salita(B, cliccato, att)
    q = st.text_input("Cerca", key=f"q_{att}",
                      placeholder="bora, cavi, vietato, navetta, biglietto…")
    gradi_pres = [g for g in ("1","2-","2","2+","3")
                  if (dec["difficolta"].astype(str) == "H&F " + g).any()]
    if gradi_pres:
        scelti = st.multiselect("Difficoltà di decollo (scala Cammina e Vola)", gradi_pres,
                                key=f"g_{att}", placeholder="tutti i gradi",
                                help="Vuoto = tutti, compresi i punti senza valutazione")
        if scelti:
            dec = dec[dec["difficolta"].astype(str).isin(["H&F " + g for g in scelti])]
        with st.expander("Cosa vogliono dire i gradi"):
            for g, testo in SCALA_CEV:
                st.markdown(f"**Grado {g}** — {testo}")
            st.caption("Scala di camminaevola.it. Riguarda il decollo, non la salita.")
    def filtra(b):
        if not q or not len(b): return b
        ql = q.lower()
        return b[[any(ql in str(x[c]).lower() for c in CAMPI if c in b.columns)
                  for _, x in b.iterrows()]]
    dec, att_l, altro = filtra(dec), filtra(att_l), filtra(altro)

    st.markdown(f"#### \U0001FA82 Decolli — {len(dec)}")
    if not len(dec): st.info("Nessun decollo con questi filtri.")
    for z in [z for z in ORDINE if z in set(dec["zona"])]:
        st.markdown(f"*{z}*")
        for _, r in dec[dec["zona"]==z].sort_values("nome").iterrows():
            e_ = val(r,"vento") or "esposizione da verificare"
            qt = f" · {int(r['quota'])} m" if val(r,"quota") else ""
            d_ = str(val(r,"difficolta") or "")
            gr = f" · dec. {d_[4:]}" if d_.startswith("H&F ") else ""
            with st.expander(f"{r['nome']} — \U0001F9ED {e_}{qt}{gr}"):
                scheda_sito(r)
    if len(att_l):
        st.markdown(f"#### \U0001F3AF Atterraggi — {len(att_l)}")
        for z in [z for z in ORDINE if z in set(att_l["zona"])]:
            st.markdown(f"*{z}*")
            for _, r in att_l[att_l["zona"]==z].sort_values("nome").iterrows():
                with st.expander(r["nome"]):
                    scheda_sito(r)
    if len(altro):
        st.markdown(f"#### ⚠️ Regole e servizi — {len(altro)}")
        for _, r in altro.sort_values("nome").iterrows():
            with st.expander(r["nome"]):
                scheda_sito(r)

# ======================================================= NEVE
with T_NEVE:
    montagna.scheda_neve(card, kv)

# ======================================================= ROTTE
with T_ROTTE:
    montagna.scheda_rotte(card, kv, df)

# ======================================================= OSSERVAZIONI
with T_OSS:
    osservazioni.scheda_osservazioni(card, kv, df)

# ======================================================= INFO
with T_INFO:
    montagna.scheda_documenti(card)
    st.divider()
    st.markdown("#### Le quattro attività")
    for a, cfg in ATTIVITA.items():
        b = solo(a)
        card(f"{cfg['ico']} {cfg['eti']} — {len(b)} punti",
             f"{len(b[b['tipo'].isin(['decollo','hike&fly'])])} decolli · "
             f"{len(b[b['tipo']=='atterraggio'])} atterraggi<br>{DESCR_ATT[a]}")
    st.caption("Un punto può valere per più attività. Cross e hike & fly vengono "
               "dalle cartelle del KML e dalle fonti dei club. I due alpinismi sono una "
               "PROPOSTA basata sul carattere della cima: vanno confermati.")
    st.divider()
    st.markdown("#### Com'è messa ogni zona")
    for k, v in NOTE_AREA:
        with st.expander(k): st.write(v)
    st.divider()
    st.markdown("#### Gite curate")
    for g in GITE:
        with st.expander(f"{g['nome']} · {g['zona']}"):
            st.caption(" · ".join([g["cat"]] + ([f"↗ {g['disl']} m"] if g["disl"] else [])
                                       + ([g["ore"]] if g["ore"] else [])))
            st.write(g["testo"])
    st.markdown("#### Flytherapy — 25 gite bellunesi")
    st.markdown("  ·  ".join(
        f"[{n}](https://www.flytherapy.it/portfolio_page/{s}/)" for n, _, s in GITE_FLYTHERAPY))
    st.divider()
    st.markdown("#### Fonti")
    st.dataframe(pd.DataFrame(FONTI, columns=["Fonte","Cosa dà","Area"]), hide_index=True)
    st.divider()
    st.markdown("#### Affidabilità")
    card("✅ Verificato", "fonte scritta: club, federazioni, guide locali, ARPA FVG", "g")
    card("\U0001F4D7 Relazione Cammina e Vola",
         "uscita raccontata da chi l'ha fatta, con difficoltà di decollo, vento, "
         "via di salita e coordinate", "b")
    card("\U0001F7E1 Solo KML", "nella mappa di Lorenzo Delbene ma senza note dell'autore", "y")
    card("❓ Da verificare", "prima di andarci", "n")
    st.divider()
    st.markdown("#### Difficoltà di decollo")
    st.caption(f"Scala di camminaevola.it, applicata a "
               f"{int(df['difficolta'].astype(str).str.startswith('H&F ').sum())} decolli. "
               "Valuta lo spazio, la pendenza e il terreno del decollo, non la salita.")
    for g, testo in SCALA_CEV:
        card(f"Grado {g}", testo, "g" if g == "1" else "y" if g.startswith("2") else "r")
