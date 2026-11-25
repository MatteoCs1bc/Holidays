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


# ---------------------------------------------------------------------
# ATTIVITA
# ---------------------------------------------------------------------
"""Classificazione per TIPOLOGIA DI ATTIVITA'.

cross  = voli di cross: decolli e atterraggi ufficiali, si arriva in auto o con impianto
hef    = hike & fly: si sale a piedi, terreno escursionistico
pa_est = paralpinismo estivo: cima alpina, terreno da alpinismo, si vola in discesa
pa_inv = paralpinismo invernale: scialpinismo o neve, si vola in discesa

Un punto puo' avere piu' attivita'. La classificazione dei due paralpinismi e' una
PROPOSTA basata sul carattere della cima, non su relazioni di volo verificate.
"""

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
    if tipo in ("decollo","atterraggio","parcheggio","impianto"): a.append("cross")
    if tipo == "hike&fly": a.append("hef")
    if k in PARALP_ESTIVO:    a.append("pa_est")
    if k in PARALP_INVERNALE: a.append("pa_inv")
    # un hike & fly molto alto e' quasi sempre anche terreno alpino
    if tipo == "hike&fly" and quota and quota >= 2000 and "pa_est" not in a:
        a.append("pa_est")
    return a or ["cross"]


# ---------------------------------------------------------------------
# MOTORE METEO
# ---------------------------------------------------------------------
"""Analisi meteo orientata al volo: instabilita', quota massima, inversioni,
turbolenza, gradiente termico. Dati Open-Meteo (modello ICON/ECMWF)."""
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
)
GIORNALIERE = ["temperature_2m_max","temperature_2m_min","precipitation_sum",
               "precipitation_probability_max","wind_speed_10m_max"]

def _get(la, lo, orarie):
    p = urllib.parse.urlencode({"latitude": la, "longitude": lo, "timezone": "auto",
                                "forecast_days": 10, "daily": ",".join(GIORNALIERE),
                                "hourly": ",".join(orarie)})
    with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?" + p, timeout=25) as f:
        return json.load(f)

def scarica(la, lo):
    """Prova i nomi moderni, ripiega su quelli vecchi se l'API li rifiuta."""
    try:
        return _get(la, lo, ORARIE)
    except Exception:
        vecchi = [v.replace("dew_point_2m","dewpoint_2m").replace("wind_speed","windspeed")
                   .replace("wind_direction","winddirection").replace("wind_gusts","windgusts")
                   .replace("cloud_cover","cloudcover") for v in ORARIE]
        return _get(la, lo, vecchi)

def _c(h, nome):
    """Colonna, qualunque sia la convenzione di nomi."""
    for n in (nome, nome.replace("dew_point_2m","dewpoint_2m").replace("wind_speed","windspeed")
                        .replace("wind_direction","winddirection").replace("wind_gusts","windgusts")
                        .replace("cloud_cover","cloudcover")):
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
        r["base_nubi"] = quota_staz + 125*(t2-td2) if pd.notna(t2) and pd.notna(td2) else float("nan")
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
            prof.append(dict(hPa=l, t=t, z=z, v=v, d=dr_))
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

# ======================================================================
# APP
# ======================================================================
import json, math, os
import pandas as pd
import streamlit as st
import pydeck as pdk
import sys as _sys
M = _sys.modules[__name__]   # le funzioni meteo sono qui sopra

st.set_page_config(page_title="Nordest — volo e montagna", page_icon="\U0001FA82", layout="centered")
BASE = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def carica():
    return pd.DataFrame(json.load(open(os.path.join(BASE, "siti_ne.json"), encoding="utf-8")))

df = carica()
PRIORITA = ["pa_inv", "pa_est", "hef", "cross"]
TIPI_ETI = {"decollo":"Decollo","hike&fly":"Hike & Fly","atterraggio":"Atterraggio",
            "impianto":"Impianto","parcheggio":"Parcheggio","zona":"Regole"}
ORDINE = ["1 Friuli","2 Alpi Giulie","6 Pordenonese / Carnia ovest","3 Slovenia",
          "4 Alpago","5 Feltrino","10 Cadore / Dolomiti","11 Dolomiti / Agordino",
          "8 Austria / Carinzia","9 Slovenia centrale / Austria est",
          "7 Veneto (Bassano/Marostica)"]
CAMPI = ["nome","note","vento","difficolta","partenza","categoria","fonte","zona"]
VIN_FLAT = {v["sito"]: v for vs in VINCOLI.values() for v in vs}

def att_prim(lista, ammesse=None):
    for a in PRIORITA:
        if a in lista and (ammesse is None or a in ammesse): return a
    return lista[0] if lista else "cross"

def rgb(a):  return ATTIVITA.get(a, {}).get("rgb", [136,136,136])
def hexa(a): return "#%02x%02x%02x" % tuple(rgb(a))
def eti(a):  return ATTIVITA.get(a, {}).get("eti", a)
def ico(a):  return ATTIVITA.get(a, {}).get("ico", "\U0001F4CD")

def dist_km(a,b,c,d):
    return math.hypot((a-c)*111, (b-d)*111*math.cos(math.radians((a+c)/2)))

def val(r,c):
    v = r[c] if c in r.index else None
    return "" if v is None or (isinstance(v,float) and pd.isna(v)) else v

def riassunto(r):
    p = []
    if val(r,"quota"): p.append(f"{int(r['quota'])} m")
    if val(r,"vento"): p.append(f"\U0001F9ED {r['vento']}")
    if val(r,"disl"):  p.append(f"↗ {int(r['disl'])} m")
    if val(r,"difficolta"): p.append(str(r["difficolta"])[:30])
    return " · ".join(p)

def pallino(a):
    return (f"<span style='display:inline-block;width:11px;height:11px;border-radius:50%;"
            f"background:{hexa(a)};border:1px solid #bbb;margin-right:6px'></span>")

def scheda(r):
    atts = r["att"] if isinstance(r["att"], list) else []
    st.markdown(pallino(att_prim(atts)) + f"<b>{r['nome']}</b> "
                f"<small>· {TIPI_ETI.get(r['tipo'], r['tipo'])}</small>", unsafe_allow_html=True)
    if atts:
        st.markdown(" ".join(f"{ico(a)} {eti(a)}" for a in atts))
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
    for a,b in settori:
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

def mappa(blocco, zoom=8, colora_per="att", ammesse=None, verdetti=None):
    m = blocco.dropna(subset=["lat","lon"]).copy()
    if not len(m):
        st.info("Nessun punto con questi filtri."); return
    if colora_per == "verdetto" and verdetti is not None:
        COL = {"\U0001F7E2":[34,160,70], "\U0001F7E1":[235,180,20],
               "\U0001F534":[200,40,40], "⚪":[150,150,150], "":[150,150,150]}
        m["_v"] = [verdetti.get(n, "⚪") for n in m["nome"]]
        m["col"] = [COL.get(v, [150,150,150]) for v in m["_v"]]
        m["etichetta"] = m["_v"]
    else:
        m["_a"] = [att_prim(a if isinstance(a, list) else [], ammesse) for a in m["att"]]
        m["col"] = [rgb(a) for a in m["_a"]]
        m["etichetta"] = [eti(a) for a in m["_a"]]
    m["rad"] = [{"decollo":420,"hike&fly":400,"zona":460}.get(t, 230) for t in m["tipo"]]
    m["sotto"] = [riassunto(r) or TIPI_ETI.get(r["tipo"], "") for _, r in m.iterrows()]
    st.pydeck_chart(pdk.Deck(
        layers=[pdk.Layer("ScatterplotLayer",
                          data=m[["lat","lon","col","rad","nome","etichetta","sotto"]],
                          get_position=["lon","lat"], get_fill_color="col", get_radius="rad",
                          radius_min_pixels=5, radius_max_pixels=18, pickable=True,
                          auto_highlight=True, stroked=True, get_line_color=[255,255,255],
                          line_width_min_pixels=1)],
        map_style=None,
        initial_view_state=pdk.ViewState(latitude=float(m["lat"].mean()),
                                         longitude=float(m["lon"].mean()), zoom=zoom),
        tooltip={"html": "<b>{nome}</b><br/>{etichetta}<br/>{sotto}"}))

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### Filtri")
    zone_d = [z for z in ORDINE if z in set(df["zona"])]
    z_sel = st.multiselect("Zona", zone_d,
                           default=[z for z in zone_d if not z.startswith(("7 ","8 ","9 ","11 "))])
    aff_sel = st.multiselect("Affidabilità", ["V","K","?"], default=["V","K","?"],
                             format_func=lambda a: {"V":"✅ verificato","K":"\U0001F7E1 solo KML",
                                                    "?":"❓ da verificare"}[a])
    mostra_servizi = st.checkbox("Mostra parcheggi e impianti", value=False)
    st.markdown("---")
    pos = st.text_input("La tua posizione — lat, lon", placeholder="46.27, 13.14")

base = df[df["zona"].isin(z_sel) & df["aff"].isin(aff_sel)].copy()
if not mostra_servizi:
    base = base[~base["tipo"].isin(["parcheggio","impianto"])]
qui = None
if pos.strip():
    try:
        a, b = [float(x) for x in pos.replace(";", ",").split(",")[:2]]
        qui = (a, b)
        base["dist"] = [dist_km(a,b,la,lo) for la,lo in zip(base["lat"], base["lon"])]
        base = base.sort_values("dist")
    except Exception:
        st.sidebar.error("Formato: 46.27, 13.14")
base = base.reset_index(drop=True)

def solo(att):
    return base[[att in (a if isinstance(a,list) else []) for a in base["att"]]]

SEZ = ["\U0001F5FA️ Mappa unica", "\U0001FA82 Voli di cross", "\U0001F97E Hike & Fly",
       "⛰️ Paralpinismo estivo", "❄️ Paralpinismo invernale",
       "\U0001F324️ Meteo", "✅ Siti volabili", "\U0001F527 Info"]
sezione = st.selectbox("Sezione", SEZ, index=0, key="nav")
st.caption("Friuli · Carnia · Alpi Giulie · Slovenia di confine · Alpago · bellunese")
st.divider()

def elenco(blocco, vuoto="Nessun punto con questi filtri."):
    if not len(blocco): st.info(vuoto); return
    for z in [z for z in ORDINE if z in set(blocco["zona"])]:
        st.markdown(f"**{z}**")
        for _, r in blocco[blocco["zona"]==z].sort_values("nome").iterrows():
            coda = riassunto(r)
            if "dist" in r.index and pd.notna(r["dist"]):
                coda = (coda + " · " if coda else "") + f"{r['dist']:.0f} km"
            with st.expander(f"{r['nome']}" + (f"  ·  {coda}" if coda else "")):
                scheda(r)

def sezione_attivita(chiave, titolo, intro, tipi=None):
    st.markdown(f"### {ico(chiave)} {titolo}")
    st.caption(intro)
    B = solo(chiave)
    if tipi: B = B[B["tipo"].isin(tipi)]
    c = st.columns(4)
    for i, t in enumerate(["decollo","hike&fly","atterraggio","zona"]):
        n = len(B[B["tipo"]==t])
        if n: c[i].metric(TIPI_ETI[t], n)
    mappa(B, zoom=8.3, ammesse={chiave})
    st.divider()
    q = st.text_input("Cerca", key=f"q_{chiave}",
                      placeholder="bora, cavi, vietato, navetta, biglietto…")
    V = B
    if q and len(V):
        ql = q.lower()
        V = V[[any(ql in str(r[c_]).lower() for c_ in CAMPI if c_ in V.columns)
               for _, r in V.iterrows()]]
    st.caption(f"{len(V)} punti")
    elenco(V)

# ---------------------------------------------------------------- sezioni
if sezione == SEZ[0]:
    att_sel = st.multiselect("Attività", list(ATTIVITA), default=list(ATTIVITA),
                             format_func=lambda a: f"{ico(a)} {eti(a)}")
    B = base[[any(x in (a if isinstance(a,list) else []) for x in att_sel) for a in base["att"]]]
    st.caption(f"{len(B)} punti su {len(df)} totali")
    mappa(B, zoom=7.6, ammesse=set(att_sel))
    cols = st.columns(2)
    for i, a in enumerate(att_sel):
        n = len(solo(a))
        cols[i % 2].markdown(pallino(a) + f"<small>{eti(a)} — {n} punti</small>",
                             unsafe_allow_html=True)
    st.caption("Un punto può valere per più attività: sulla mappa prende il colore "
               "di quella più impegnativa fra quelle selezionate.")

elif sezione == SEZ[1]:
    sezione_attivita("cross", "Voli di cross",
                     "Decolli e atterraggi ufficiali: ci si arriva in auto o con impianto, "
                     "c'è un club dietro e di solito un regolamento.")

elif sezione == SEZ[2]:
    sezione_attivita("hef", "Hike & Fly",
                     "Si sale a piedi su terreno escursionistico. Molti vengono dal KML senza "
                     "note: il punto c'è, l'esposizione va ricavata da carta, camptocamp o "
                     "dai tracciati XContest.")

elif sezione == SEZ[3]:
    sezione_attivita("pa_est", "Paralpinismo estivo",
                     "Cime alpine: terreno da alpinismo, roccia o neve residua, si vola in discesa. "
                     "La classificazione è una PROPOSTA basata sul carattere della cima, "
                     "non su relazioni di volo verificate.")

elif sezione == SEZ[4]:
    sezione_attivita("pa_inv", "Paralpinismo invernale",
                     "Cime da scialpinismo: si sale con le pelli e si vola giù. "
                     "Anche qui la classificazione è una proposta da confermare. "
                     "D'inverno valgono valanghe, vento di quota e giornate corte: "
                     "il semaforo guarda solo il vento.")

elif sezione == SEZ[5]:
    st.markdown("### Analisi meteo per il volo")
    ca, cb = st.columns([3,1])
    luogo = ca.selectbox("Località", list(PUNTI_METEO))
    if cb.button("\U0001F504 Aggiorna", use_container_width=True):
        analisi.clear(); st.rerun()
    la, lo = PUNTI_METEO[luogo]
    try:
        t, quota_staz, quando = analisi(la, lo)
        gg = list(t["g"])
        g = st.select_slider("Giorno", gg, value=gg[0],
                             format_func=lambda x: pd.Timestamp(x).strftime("%a %d/%m"), key="mg")
        r = t[t["g"]==g].iloc[0]

        st.markdown("#### Sintesi")
        i_ic, i_tx = M.giudica_instabilita(r["cape"], r["li"])
        g_ic, g_tx = M.giudica_gradiente(r["lapse_850_700"])
        tb_ic, tb_tx = M.giudica_turbolenza(r["shear_925_700"], r["raff_ratio"], r["v700"])
        inv_ic, inv_tx = M.descrivi_inversioni(r["inversioni"], quota_staz)
        for icn, txt in [(i_ic,i_tx),(g_ic,g_tx),(tb_ic,tb_tx),(inv_ic,inv_tx)]:
            st.markdown(f"{icn} **{txt}**")

        st.markdown("#### Quote")
        q1,q2,q3 = st.columns(3)
        q1.metric("Quota massima termica",
                  f"{r['quota_termica']:.0f} m" if pd.notna(r["quota_termica"]) else "—",
                  help="Cima dello strato rimescolato: in pratica il tetto delle termiche.")
        q2.metric("Base dei cumuli",
                  f"{r['base_nubi']:.0f} m" if pd.notna(r["base_nubi"]) else "—",
                  help="Stimata dallo spread temperatura/rugiada al suolo.")
        q3.metric("Zero termico",
                  f"{r['zero_term']:.0f} m" if pd.notna(r["zero_term"]) else "—")

        st.markdown("#### Instabilità e vento")
        w1,w2,w3,w4 = st.columns(4)
        w1.metric("CAPE", f"{r['cape']:.0f}" if pd.notna(r["cape"]) else "—",
                  help="Energia convettiva disponibile, J/kg. Sopra 1200 sono temporali.")
        w2.metric("Lifted index", f"{r['li']:.1f}" if pd.notna(r["li"]) else "—",
                  help="Negativo = instabile. Sotto -5 molto instabile.")
        w3.metric("Vento 700 hPa",
                  f"{r['v700']:.0f} {cardinale(r['d700'])}" if pd.notna(r["v700"]) else "—")
        w4.metric("Raffiche", f"{r['raffiche']:.0f} km/h" if pd.notna(r["raffiche"]) else "—")

        st.markdown("#### Gradiente termico")
        grad = pd.DataFrame({
            "Strato": ["925→850 hPa (basso)","850→700 hPa (medio)","700→500 hPa (alto)"],
            "°C / 100 m": [f"{r[k]:.2f}" if pd.notna(r[k]) else "—"
                                for k in ["lapse_925_850","lapse_850_700","lapse_700_500"]],
            "Lettura": [M.giudica_gradiente(r[k])[1]
                        for k in ["lapse_925_850","lapse_850_700","lapse_700_500"]]})
        st.dataframe(grad, hide_index=True)
        st.caption("0,98 °C/100 m è l'adiabatica secca: più ci si avvicina, "
                   "più le termiche sono forti. Sotto 0,45 l'aria è stabile.")

        st.markdown("#### Profilo verticale")
        prof = pd.DataFrame(r["profilo"])
        prof = prof[prof["z"].notna()]
        if len(prof):
            st.dataframe(pd.DataFrame({
                "Livello": [f"{int(p)} hPa" for p in prof["hPa"]],
                "Quota": [f"{z:.0f} m" for z in prof["z"]],
                "Temp": [f"{x:.1f}°" if pd.notna(x) else "—" for x in prof["t"]],
                "Vento": [f"{v:.0f} km/h {cardinale(d)}" if pd.notna(v) else "—"
                          for v,d in zip(prof["v"], prof["d"])]}), hide_index=True)
            ch = prof[["z","t"]].dropna().set_index("z").sort_index()
            if len(ch):
                ch.columns = ["temperatura °C"]
                st.line_chart(ch)
                st.caption("Se la linea torna a salire andando verso quote maggiori, "
                           "lì c'è un'inversione.")
        if r["inversioni"]:
            st.markdown("**Inversioni trovate**")
            for b_, c_, dt in r["inversioni"]:
                st.markdown(f"• da {b_:.0f} m a {c_:.0f} m, +{dt:.1f} °C")

        st.markdown("#### Andamento sui giorni")
        serie = t[["time","cape","quota_termica","v700"]].dropna(subset=["time"]).set_index("time")
        st.line_chart(serie[["quota_termica"]].rename(columns={"quota_termica":"quota termica m"}))
        st.line_chart(serie[["cape","v700"]].rename(
            columns={"cape":"CAPE J/kg","v700":"vento 700 hPa km/h"}))
        st.caption(f"Medie della fascia 11-16. Quota stazione {quota_staz:.0f} m. "
                   f"Ultimo scaricamento: {quando}.")
    except Exception as e:
        st.warning("Non riesco a raggiungere Open-Meteo adesso.")
        st.caption(f"({type(e).__name__}) Serve connessione internet.")

    st.divider()
    st.markdown("#### Carte sinottiche e mappe")
    import streamlit.components.v1 as components
    LIV = {"Superficie":"surface","850 hPa (~1500 m)":"850h","700 hPa (~3000 m)":"700h",
           "600 hPa (~4200 m)":"600h","500 hPa (~5500 m)":"500h"}
    STR = {"Vento":"wind","Raffiche":"gust","CAPE":"cape","Base nubi":"cbase",
           "Nuvole":"clouds","Pioggia":"rain","Temperatura":"temp","Pressione":"pressure",
           "Isoterma zero":"deg0","Inversione":"deg0"}
    c1,c2 = st.columns(2)
    strato = c1.selectbox("Strato", list(STR), key="w_ov")
    liv = c2.selectbox("Quota", list(LIV), index=2, key="w_lv")
    wla, wlo = PUNTI_METEO[luogo]
    components.iframe(
        f"https://embed.windy.com/embed2.html?lat={wla}&lon={wlo}&detailLat={wla}"
        f"&detailLon={wlo}&zoom=7&level={LIV[liv]}&overlay={STR[strato]}&product=ecmwf"
        "&menu=&message=true&marker=true&calendar=now&pressure=true&type=map"
        "&location=coordinates&detail=true&metricWind=km%2Fh&metricTemp=%C2%B0C&radarRange=-1",
        height=500)
    st.markdown(
        "**Carte vere:** "
        "[Wetterzentrale GFS/ECMWF](https://www.wetterzentrale.de/en/topkarten.php?model=ecm&var=1) · "
        "[Meteociel ECMWF](https://www.meteociel.fr/modeles/ecmwf_cartes.php) · "
        "[ARPA FVG OSMER](https://www.meteo.fvg.it/) · "
        "[Radar Protezione Civile](https://radar.protezionecivile.it/) · "
        f"[meteo-parapente](https://meteo-parapente.com/#/{wla},{wlo},11)")
    st.divider()
    st.markdown("#### Fonti locali del Friuli")
    for n_, d_ in FONTI_METEO_FVG:
        st.markdown(f"**{n_}** — {d_}")

elif sezione == SEZ[6]:
    st.markdown("### Siti volabili")
    st.caption("Incrocia il vento a 700 hPa previsto con le regole di ogni decollo. "
               "Verde si vola, giallo al limite, rosso no, grigio esposizione sconosciuta.")
    ca, cb = st.columns([3,1])
    luogo = ca.selectbox("Meteo di riferimento", list(PUNTI_METEO), key="sv_l")
    att_f = cb.selectbox("Attività", list(ATTIVITA), key="sv_a",
                         format_func=lambda a: eti(a))
    la, lo = PUNTI_METEO[luogo]
    try:
        t, quota_staz, quando = analisi(la, lo)
        gg = list(t["g"])
        g = st.select_slider("Giorno", gg, value=gg[0],
                             format_func=lambda x: pd.Timestamp(x).strftime("%a %d/%m"), key="svg")
        r = t[t["g"]==g].iloc[0]
        v, d = r["v700"], r["d700"]
        k1,k2,k3,k4 = st.columns(4)
        k1.metric("Vento 700 hPa", f"{v:.0f} km/h" if pd.notna(v) else "—")
        k2.metric("Direzione", cardinale(d))
        k3.metric("Quota termica",
                  f"{r['quota_termica']:.0f} m" if pd.notna(r["quota_termica"]) else "—")
        k4.metric("CAPE", f"{r['cape']:.0f}" if pd.notna(r["cape"]) else "—")
        i_ic,i_tx = M.giudica_instabilita(r["cape"], r["li"])
        tb_ic,tb_tx = M.giudica_turbolenza(r["shear_925_700"], r["raff_ratio"], r["v700"])
        inv_ic,inv_tx = M.descrivi_inversioni(r["inversioni"], quota_staz)
        st.markdown(f"{i_ic} {i_tx} · {tb_ic} {tb_tx} · {inv_ic} {inv_tx}")

        B = solo(att_f)
        B = B[B["tipo"].isin(["decollo","hike&fly"])]
        verdetti, motivi = {}, {}
        for _, x in B.iterrows():
            vk = VIN_FLAT.get(x["nome"])
            if vk:
                ic, why = giudizio(v, d, vk)
                verdetti[x["nome"]] = ic; motivi[x["nome"]] = (why, vk["nota"])
            else:
                verdetti[x["nome"]] = "⚪"
        n_ok = sum(1 for x in verdetti.values() if x == "\U0001F7E2")
        n_gi = sum(1 for x in verdetti.values() if x == "\U0001F7E1")
        n_no = sum(1 for x in verdetti.values() if x == "\U0001F534")
        n_bo = sum(1 for x in verdetti.values() if x == "⚪")
        s1,s2,s3,s4 = st.columns(4)
        s1.metric("\U0001F7E2 Si vola", n_ok); s2.metric("\U0001F7E1 Al limite", n_gi)
        s3.metric("\U0001F534 No", n_no); s4.metric("⚪ Da verificare", n_bo)
        mappa(B, zoom=8, colora_per="verdetto", verdetti=verdetti)
        st.divider()
        for stato, titolo in [("\U0001F7E2","Si vola"),("\U0001F7E1","Al limite"),
                              ("\U0001F534","Da escludere"),("⚪","Esposizione sconosciuta")]:
            blocco = B[[verdetti.get(n)==stato for n in B["nome"]]]
            if not len(blocco): continue
            st.markdown(f"#### {stato} {titolo} — {len(blocco)}")
            for _, x in blocco.sort_values("nome").iterrows():
                why = motivi.get(x["nome"])
                sub = f" — {why[0]}" if why else ""
                with st.expander(f"{x['nome']}{sub}"):
                    if why and why[1]: st.caption(why[1])
                    scheda(x)
        st.caption(f"Ultimo scaricamento: {quando}. Il semaforo guarda solo il gradiente in "
                   "quota: brezza di valle, inversione locale e stato del terreno li vedi tu.")
    except Exception as e:
        st.warning("Non riesco a raggiungere Open-Meteo adesso.")
        st.caption(f"({type(e).__name__}) Serve connessione internet.")

else:
    st.markdown("#### Le quattro attività")
    for a, cfg in ATTIVITA.items():
        st.markdown(pallino(a) + f"**{cfg['ico']} {cfg['eti']}** — {len(solo(a))} punti",
                    unsafe_allow_html=True)
    st.caption("Un punto può valere per più attività. Cross e hike & fly vengono "
               "dalle cartelle del KML e dalle fonti dei club. I due paralpinismi sono una "
               "PROPOSTA basata sul carattere della cima: vanno confermati.")
    st.divider()
    st.markdown("#### Com'è messa ogni zona")
    for k, v in NOTE_AREA:
        st.markdown(f"**{k}**"); st.write(v)
    st.divider()
    st.markdown("#### Fonti")
    st.dataframe(pd.DataFrame(FONTI, columns=["Fonte","Cosa dà","Area"]), hide_index=True)
    st.divider()
    st.markdown("#### Gite curate")
    for g in GITE:
        with st.expander(f"{g['nome']} · {g['zona']}"):
            st.caption(" · ".join([g["cat"]] + ([f"↗ {g['disl']} m"] if g["disl"] else [])
                                       + ([g["ore"]] if g["ore"] else [])))
            st.write(g["testo"])
    st.markdown("#### Flytherapy — 25 gite bellunesi")
    for nome_g, zona_g, slug in GITE_FLYTHERAPY:
        st.markdown(f"• **{nome_g}** <small>{zona_g}</small> — "
                    f"[scheda](https://www.flytherapy.it/portfolio_page/{slug}/)",
                    unsafe_allow_html=True)
    st.divider()
    st.markdown("#### Affidabilità")
    st.markdown("✅ **verificato** con fonte scritta: club, federazioni, guide locali")
    st.markdown("\U0001F7E1 **solo KML** — nella mappa di Lorenzo Delbene ma senza note")
    st.markdown("❓ **da verificare** prima di andarci")
