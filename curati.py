# -*- coding: utf-8 -*-
"""Dati curati: tutto quello che ha note vere (orientamento, pericoli, dislivelli).
Fonti: pannelli SHV/FGA, paraglidingearth, lespiedssurterre.blog, paragliding.ch,
FFCAM, camptocamp, refuges-ecrins, KML di Lorenzo Delbene."""

# tipo: decollo | atterraggio | cima | rifugio | zona | parcheggio
# aff:  V = verificato con fonte  |  K = solo nel KML  |  ? = da verificare

CURATI = [

# ============ 1. ALPSTEIN ============
dict(zona="1 Alpstein", tipo="decollo", nome="Ebenalp NW (1.1)", lat=47.2844, lon=9.4110, quota=1600,
     vento="NW-NNE", diff="Facile", aff="V", cat="Parapendio",
     note="Decollo standard. Accesso con Ebenalpbahn da Wasserauen, sta sopra la stazione a monte. "
          "Prato prima piatto poi piu inclinato. CON VENTO DA OVEST: pericolo di rotore. "
          "Finestra pomeridiana 15-18, tira fino alle 19:30. Prima di mezzogiorno solo giornate rare.",
     fonte="SHV/FGA Fluggebiet Alpstein"),
dict(zona="1 Alpstein", tipo="decollo", nome="Ebenalp NO (1.2)", lat=47.2849, lon=9.4117, quota=1600,
     vento="N-NE", diff="Facile", aff="V", cat="Parapendio/Delta",
     note="Direttamente sotto la stazione a monte. Delta e scuole hanno la precedenza.",
     fonte="SHV/FGA Fluggebiet Alpstein"),
dict(zona="1 Alpstein", tipo="decollo", nome="Ebenalp SO (1.3)", lat=47.2838, lon=9.4136, quota=1600,
     vento="NE-SE", diff="DIFFICILE", aff="V", cat="Delta (Parapendio)",
     note="Salita al ristorante poi discesa a est. Decollo da scogliera per i delta sopra il muro. "
          "PER PARAPENDIO: prato piccolo, MOLTO TURBOLENTO.",
     fonte="SHV/FGA Fluggebiet Alpstein"),
dict(zona="1 Alpstein", tipo="decollo", nome="Hoher Kasten W (2.1)", lat=47.2859, lon=9.4864, quota=1730,
     vento="W-NW", diff="Medio", aff="V", cat="Parapendio",
     note="Dalla stazione a monte si scende al Kastensattel (~10 min, discesa ripida). "
          "Nella parte nord le scuole hanno la precedenza.",
     fonte="SHV/FGA Fluggebiet Alpstein"),
dict(zona="1 Alpstein", tipo="decollo", nome="Hoher Kasten Starkwind (2.2)", lat=47.2877, lon=9.4847, quota=1830,
     vento="W-NW", diff="Medio", aff="V", cat="Parapendio",
     note="Decollo di ripiego quando il vento nella sella e troppo forte. "
          "Segui il sentiero fino alla 2a curva a sinistra.",
     fonte="SHV/FGA Fluggebiet Alpstein"),
dict(zona="1 Alpstein", tipo="decollo", nome="Hoher Kasten Ost (2.3)", lat=47.2885, lon=9.4883, quota=1750,
     vento="E", diff="Facile", aff="V", cat="Parapendio",
     note="Dalla stazione a monte al lato opposto della sella. Per voli di planata nel Rheintal.",
     fonte="SHV/FGA Fluggebiet Alpstein"),
dict(zona="1 Alpstein", tipo="decollo", nome="Kronberg Sud", lat=47.2758, lon=9.2811, quota=1640,
     vento="S-SW", diff="Medio", aff="V", cat="Parapendio",
     note="UNICO DECOLLO DELL'ALPSTEIN PER VENTO DA SUD/SUDOVEST. Stendere sotto il cavo dello skilift. "
          "Appena staccato virata 90 gradi a destra per passare tra gli alberi. "
          "Se non sei abbastanza alto, atterri dritto sulla selletta.",
     fonte="fga.ch"),
dict(zona="1 Alpstein", tipo="decollo", nome="Kronberg Ovest", lat=47.2760, lon=9.2805, quota=1640,
     vento="W-WNW", diff="Facile", aff="V", cat="Parapendio",
     note="Prato lungo e progressivamente piu ripido, ottimo. A destra strapiombo, a sinistra abeti. "
          "Scuole prioritarie. NON BRUCIARE QUOTA davanti al decollo: l'atterraggio e lontano.",
     fonte="fga.ch"),
dict(zona="1 Alpstein", tipo="decollo", nome="Kronberg Nord", lat=47.2765, lon=9.2812, quota=1640,
     vento="NW-NE", diff="Difficile", aff="V", cat="Parapendio",
     note="Solo per chi parte sicuro e solo con vento sufficiente. Spazio giusto per stendere sul sentiero: "
          "quando le funi sono in tensione sei gia sul pendio ripido.",
     fonte="fga.ch"),
dict(zona="1 Alpstein", tipo="decollo", nome="Kronberg Nord 2", lat=47.2768, lon=9.2840, quota=1620,
     vento="NW-NE", diff="Medio", aff="V", cat="Parapendio",
     note="5 minuti a piedi verso est dal Nord. Piu facile.",
     fonte="fga.ch"),
dict(zona="1 Alpstein", tipo="decollo", nome="Saentis", lat=47.2494, lon=9.3428, quota=2502,
     vento="W-SW deboli", diff="ALPINISTICO", aff="V", cat="Parapendio",
     note="NON SI PUO DECOLLARE ALLA STAZIONE DELLA FUNIVIA. Esposizione W-SW, molto sensibile al vento: "
          "solo con W-SW DEBOLI. Terreno di decollo relativamente facile ma servono passo sicuro ed "
          "esperienza alpina. ATTERRAGGIO A UNTERWASSER (Toggenburg): a nord c'e la zona di protezione "
          "Falalp-Saentis con quota minima 3000 m. Stagione migliore: da fine estate alla prima neve di ottobre. "
          "Con vento da sud esiste il Chalbersaentis: sentire prima un local del Toggenburg.",
     fonte="fga.ch"),
dict(zona="1 Alpstein", tipo="atterraggio", nome="A1 Wasserauen (parapendio)", lat=47.2835, lon=9.4277, quota=870,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Delta e parapendii atterrano su campi SEPARATI. SEMPRE CIRCUITO A SINISTRA (Linksvolte). "
          "Non atterrare mai nell'erba alta. Cammina lungo il recinto con la vela raccolta. "
          "Ripiega SOLO sull'area blu segnata. Non e campo scuola ne area picnic. Parcheggi alla stazione a valle.",
     fonte="SHV Gleitschirmlandeplatz Wasserauen"),
dict(zona="1 Alpstein", tipo="atterraggio", nome="A2 Wasserauen (delta)", lat=47.2874, lon=9.4288, quota=870,
     vento="", diff="", aff="V", cat="Delta", note="Campo separato per i delta.",
     fonte="SHV Gleitschirmlandeplatz Wasserauen"),
dict(zona="1 Alpstein", tipo="atterraggio", nome="B Bruelisau (parapendio)", lat=47.2975, lon=9.4570, quota=920,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Subito accanto a quello dei delta. Osserva attentamente lo spazio aereo. Mai atterrare nell'erba alta. "
          "Ripiega solo sull'area blu.",
     fonte="SHV Gleitschirmlandeplatz Bruelisau"),
dict(zona="1 Alpstein", tipo="zona", nome="ZONA VIETATA Heliport Trogen (LSXT)", lat=47.4067, lon=9.4611, quota=811,
     vento="", diff="", aff="V", cat="Spazio aereo",
     note="DIVIETO DI VOLO SOTTO I 1200 m nella zona rossa. Nella zona di 2.5 km si puo volare con "
          "cautela aumentata. Attivo TUTTI I GIORNI 07:00-19:00, chiuso domenica e festivi. "
          "Fuori orario tutto lo spazio aereo e libero. Liberazione temporanea richiedibile per telefono: "
          "+41 71 343 71 71. Consigliato volare con FLARM. I piloti in difetto vengono segnalati alle autorita.",
     fonte="SHV Sonderregelung LSXT"),
dict(zona="1 Alpstein", tipo="zona", nome="Zone a quota minima Alpstein", lat=47.2494, lon=9.3428, quota=0,
     vento="", diff="", aff="V", cat="Spazio aereo",
     note="Le zone rosse della carta FGA si sorvolano solo sopra la quota indicata: "
          "min 3000 m sul massiccio del Saentis, min 2000 m in piu settori (Marwees, Hundstein, Sammtis), "
          "min 1800 m a ovest, min 1500 m nella zona Ebenalp/Schaefler. "
          "CAVI E TELEFERICHE: uno poco visibile dalla cima dello Schaefler verso nord (Lehmental): "
          "chi vola sotto la cresta sulla linea Saentis-Ebenalp deve passarci SOPRA o intorno, mai sotto. "
          "Altro cavo elettrico sotto il decollo Ebenalp dopo il salto di pendio. "
          "Vietato volare sotto i cavi della funivia.",
     fonte="SHV/FGA + fga.ch"),
dict(zona="1 Alpstein", tipo="cima", nome="Saentis via Rotsteinpass e Lisengrat", lat=47.2494, lon=9.3428, quota=2502,
     disl=1634, partenza="Wasserauen 868 m", diff="Cresta esposta e attrezzata, 5 h", aff="V", cat="Alpinismo",
     note="Via Seealpsee, Meglisalp, Rotsteinpass, poi il Lisengrat. La traversata classica dell'Alpstein. "
          "Dalla Schwaegalp (1352 m) sono solo 1150 m e 3h30.", fonte="ricerca web"),
dict(zona="1 Alpstein", tipo="cima", nome="Ebenalp a piedi", lat=47.2844, lon=9.4110, quota=1600,
     disl=770, partenza="Wasserauen 868 m", diff="Sentiero", aff="V", cat="Cross",
     note="Via Seealpsee. Rientra nel budget cross.", fonte="ricerca web"),
dict(zona="1 Alpstein", tipo="cima", nome="Kronberg a piedi", lat=47.2758, lon=9.2811, quota=1640,
     disl=770, partenza="Jakobsbad 870 m", diff="Sentiero", aff="V", cat="Cross",
     note="4 decolli in cima: qualunque vento trovi, uno funziona. Atterraggio alla stazione a valle, "
          "dietro il parco avventura: recupero a piedi.", fonte="fga.ch"),
dict(zona="1 Alpstein", tipo="cima", nome="Hoher Kasten a piedi", lat=47.2859, lon=9.4864, quota=1794,
     disl=810, partenza="Bruelisau 920 m", diff="Sentiero", aff="V", cat="Cross",
     note="3 decolli (W, Starkwind, Est).", fonte="ricerca web"),
dict(zona="1 Alpstein", tipo="cima", nome="Kreuzberge (arrampicata)", lat=47.2200, lon=9.4000, quota=2065,
     disl=None, partenza="Bruelisau / Saemtisersee", diff="Placche e spigoli, calcare", aff="?", cat="Arrampicata",
     note="Il gruppo di arrampicata piu frequentato dell'Alpstein. Nessun decollo documentato: "
          "salita e discesa a piedi.", fonte="conoscenza generale, da verificare"),
dict(zona="1 Alpstein", tipo="cima", nome="Altmann", lat=47.2394, lon=9.3697, quota=2435,
     disl=None, partenza="Meglisalp / Saemtisersee", diff="Via normale con passaggi di III", aff="?", cat="Alpinismo",
     note="Seconda cima del massiccio. Nessun decollo documentato.", fonte="conoscenza generale, da verificare"),

# ============ 2. ZURIGO / SVIZZERA CENTRALE ============
dict(zona="2 Zurigo", tipo="decollo", nome="Rigi Staffelhoehe", lat=47.0570, lon=8.4750, quota=1550,
     vento="W-NW", diff="Piccolo", aff="V", cat="Parapendio",
     note="3 minuti a piedi dalla stazione verso il Chaenzeli. FUNZIONA DALLE 14 FINO A SERA, "
          "buono per i voli lunghi serali. Esiste anche una variante sud verso Weggis, non sempre "
          "praticabile secondo l'erba. Atterraggi: Kuessnacht, Arth, Goldau, Weggis. "
          "Salita da Weggis/Vitznau (435 m) = 1115 m.", fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Rigi Kulm", lat=47.0570, lon=8.4853, quota=1798,
     vento="S/SE-SW", diff="", aff="V", cat="Parapendio",
     note="Considerato meno affidabile di Staffelhoehe. Salita da Weggis = 1360 m.", fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Rigi Scheidegg", lat=47.0430, lon=8.5250, quota=1665,
     vento="NE", diff="", aff="V", cat="Parapendio",
     note="IL DECOLLO DA BISE. Utile quando l'alta si riforma sul Mittelland. Meno affidabile degli altri.",
     fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Rigi Rotstoeckli", lat=47.0600, lon=8.4700, quota=1600,
     vento="N-NW", diff="", aff="V", cat="Parapendio", note="", fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Rotenflue", lat=47.0330, lon=8.6800, quota=1571,
     vento="N e S (no W)", diff="", aff="V", cat="Parapendio",
     note="Sopra Svitto, funivia riaperta. Due decolli, nord e sud. Non ideale con vento da ovest. "
          "ATTERRAGGIO RICKENBACH: accesso e piazzale di ripiegatura sul LATO EST, il vecchio accesso non "
          "si usa piu, i campi a nord e sud non si calpestano. Sotto l'aerovia A9: QUOTA MASSIMA 2750 m.",
     fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Hoch Ybrig - Sternen", lat=47.0180, lon=8.7800, quota=1820,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Atterraggio Weglosen 1035 m, ~800 m di dislivello. Start e landing accanto agli impianti. "
          "Funivia da Weglosen a Seebli 1460 m, poi seggiovia.", fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Niederbauen", lat=46.9450, lon=8.5200, quota=1575,
     vento="", diff="Facile", aff="V", cat="Parapendio",
     note="Sopra Emmetten. Decollo grande e progressivamente piu ripido, 850 m. Funivia ogni 30 minuti "
          "da Emmetten (8 min). Atterraggio leggermente inclinato, buono se il vento da ovest non e forte. "
          "Buone condizioni anche nel tardo pomeriggio. Il piu facile del gruppo.", fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Schrina / Walenstadtberg", lat=47.1200, lon=9.3200, quota=1290,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Ai piedi delle Churfirsten sopra il Walensee. NIENTE IMPIANTO: si sale con servizio taxi. "
          "Si soara spesso sulle pareti e poi si fa cross lungo la Seeztal.", fonte="ricerca web"),
dict(zona="2 Zurigo", tipo="decollo", nome="Alp Scheidegg", lat=47.2700, lon=8.9200, quota=1200,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Sopra Wald nel Toesstal, 40 min da Zurigo. Buono per soaring.", fonte="ricerca web"),
# cime Svizzera centrale (touch and go)
dict(zona="2 Zurigo", tipo="cima", nome="Chaiserstuel", lat=46.8300, lon=8.4000, quota=2400, disl=690,
     partenza="", diff="T2, ~2 h", aff="V", cat="Cross",
     note="Miglior rapporto quota/fatica del gruppo.", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Niederbauen-Kulm", lat=46.9450, lon=8.5200, quota=1920, disl=400,
     partenza="", diff="T2, ~1h30", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Hagelstock", lat=46.9000, lon=8.5500, quota=2182, disl=460,
     partenza="", diff="T2, ~1h30", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Arvigrat", lat=46.8600, lon=8.3200, quota=2013, disl=600,
     partenza="", diff="T2, ~2 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Buochserhorn", lat=46.9500, lon=8.4200, quota=1800, disl=650,
     partenza="", diff="T2, ~2 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Halgeren", lat=46.9000, lon=8.4500, quota=1950, disl=800,
     partenza="", diff="T2, ~2h30", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Bockmattli", lat=47.0700, lon=8.9200, quota=1932, disl=1000,
     partenza="", diff="T2, ~3 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Rossberg-Gnipen", lat=47.0700, lon=8.5600, quota=1570, disl=1020,
     partenza="", diff="T2, ~3 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Waengihorn", lat=46.9500, lon=8.8000, quota=2150, disl=1060,
     partenza="", diff="T3, ~3 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Forstberg", lat=46.9900, lon=8.8500, quota=2215, disl=1189,
     partenza="", diff="T3, ~3 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="2 Zurigo", tipo="cima", nome="Fluebrig-Diethelm", lat=47.0200, lon=8.8700, quota=2090, disl=1160,
     partenza="", diff="T2-T5, ~3h30", aff="V", cat="Alpinismo",
     note="Arriva a T5: alpinismo vero.", fonte="paragliding.ch"),

# ============ 3. OBERLAND / EIGER ============
dict(zona="3 Oberland", tipo="decollo", nome="Schynige Platte", lat=46.6560, lon=7.9060, quota=1967,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Decollo parapendio A EST DELLA STAZIONE A MONTE (quello delta e vicino all'antenna). Piatto, "
          "spesso aria discendente all'inizio della termica. FINESTRA: DA MEZZOGIORNO AL TRAMONTO. "
          "NO-GO: con vento di valle a Lehn il decollo e sottovento, non si parte; con NW e turbolento; "
          "con bise forte di nuovo sottovento, non si parte. "
          "Ferrovia a cremagliera da Wilderswil (7 km, 1420 m, 40 min), maggio-ottobre. L'ultima corsa in "
          "salita prende solo parapendisti. ATTENZIONE agli spazi aerei della base REGA di Wilderswil.",
     fonte="SHV Infotafel / deltaclub-interlaken"),
dict(zona="3 Oberland", tipo="decollo", nome="Breitlauenen", lat=46.6480, lon=7.8940, quota=1542,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Stazione intermedia della ferrovia della Schynige Platte. Decollo mosso, stessa finestra "
          "pomeridiana. ~958 m a piedi da Wilderswil.", fonte="ricerca web"),
dict(zona="3 Oberland", tipo="decollo", nome="Grindelwald-First", lat=46.6650, lon=8.0540, quota=2150,
     vento="S", diff="", aff="V", cat="Parapendio",
     note="Esposto a sud, cabinovia da Grindelwald in 25 min. Vista su Grosse Scheidegg, Wetterhorn, "
          "Schreckhorn e parete nord dell'Eiger. Si vedono spesso le aquile. "
          "Il ripiego quando la Schynige Platte non va per vento.", fonte="ricerca web"),
dict(zona="3 Oberland", tipo="decollo", nome="Beatenberg-Amisbuehl", lat=46.6900, lon=7.7700, quota=1350,
     vento="", diff="Facile", aff="V", cat="Parapendio",
     note="Bus da Interlaken ~20 min. Il piu semplice della zona. Si fa akro sopra il Thunersee "
          "da qui e da Luegibrueggli.", fonte="ricerca web"),
dict(zona="3 Oberland", tipo="decollo", nome="Morgenberghorn", lat=46.6560, lon=7.7500, quota=2190,
     vento="S, SW, W", diff="", aff="V", cat="Parapendio",
     note="Partenza MUELENEN, 1498 m di salita, atterraggio a INTERLAKEN, 1622 m di volo. "
          "Via alternativa da AESCHIRIED (fermata postale Schulhaus) lungo la cresta: alla stazione a monte "
          "dello skilift superiore c'e gia il STARTPLATZ SPITZ, utile per chiudere prima se in alto non va.",
     fonte="hikeandfly.com / baern-gliders.ch"),
dict(zona="3 Oberland", tipo="atterraggio", nome="Lehn (Interlaken)", lat=46.6830, lon=7.8550, quota=565,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Il centro dell'attivita parapendio della zona. NUOVA REGOLA: virata a destra con vento di valle.",
     fonte="SHV Infotafel"),
dict(zona="3 Oberland", tipo="atterraggio", nome="Hoehematte (Interlaken)", lat=46.6860, lon=7.8620, quota=568,
     vento="", diff="", aff="V", cat="Parapendio", note="In mezzo a Interlaken.", fonte="SHV Infotafel"),
dict(zona="3 Oberland", tipo="cima", nome="Faulhorn", lat=46.6710, lon=8.0250, quota=2680, disl=516,
     partenza="First (cabinovia)", diff="T2, ~2 h", aff="V", cat="Cross",
     note="I 516 m sono da First. Da Grindelwald per il Bachalpsee sono 1660 m. "
          "Traversata integrale Wilderswil-Schynige Platte-Faulhorn: 2330 m su 25 km, ~10 h.",
     fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Hoeji Sulegg", lat=46.6100, lon=7.8100, quota=2413, disl=900,
     partenza="Saxeten / Sulwald", diff="T2, ~3 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Elsighorn", lat=46.5100, lon=7.6300, quota=2341, disl=545,
     partenza="", diff="T2, ~1h30", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Bluemlisalphuette", lat=46.4950, lon=7.7500, quota=2834, disl=1420,
     partenza="", diff="T2, ~4h30", aff="V", cat="Alpinismo", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Hohgant", lat=46.7800, lon=7.8900, quota=2146, disl=1190,
     partenza="", diff="T2/T3, ~4 h", aff="V", cat="Cross", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Glecksteinhuette", lat=46.6300, lon=8.1100, quota=2316, disl=760,
     partenza="Grindelwald", diff="T3, ~2h30", aff="V", cat="Alpinismo", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Bunderspitz", lat=46.4700, lon=7.6200, quota=2546, disl=823,
     partenza="", diff="T3, ~2h30", aff="V", cat="Alpinismo", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Albristhorn", lat=46.4400, lon=7.5300, quota=2762, disl=810,
     partenza="", diff="T3, ~3 h", aff="V", cat="Alpinismo", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Wildstrubel", lat=46.4100, lon=7.5300, quota=3244, disl=1195,
     partenza="", diff="T3, ~4 h", aff="V", cat="Alpinismo", note="", fonte="paragliding.ch"),
dict(zona="3 Oberland", tipo="cima", nome="Schynige Platte a piedi", lat=46.6560, lon=7.9060, quota=1967,
     disl=1383, partenza="Wilderswil 584 m", diff="4-4h30", aff="V", cat="Cross",
     note="Poco sopra la soglia cross. Sali in mattinata, decolli nella finestra pomeridiana, "
          "atterri a Lehn: 3 km dal parcheggio di Wilderswil, treno e bus ogni pochi minuti.",
     fonte="ricerca web"),
dict(zona="3 Oberland", tipo="cima", nome="Eiger (nota)", lat=46.5775, lon=8.0053, quota=3967,
     disl=None, partenza="Grindelwald", diff="Mittellegi D / pilastro ovest AD", aff="V", cat="Alpinismo",
     note="La Mittellegi vuole la notte alla Mittellegihuette e una giornata piena. Il pilastro ovest e "
          "lungo e serio. Nessuna delle due sta in una giornata singola dal fondovalle. "
          "Anche Moench e Jungfrau hanno lo stesso vincolo di rifugio.", fonte="ricerca web"),

# ============ 4. ANNECY ============
dict(zona="4 Annecy", tipo="decollo", nome="Planfait", lat=45.8532, lon=6.2230, quota=1250,
     vento="W-NW", diff="4/5", aff="V", cat="Parapendio",
     note="Tutto l'anno. Prato sintetico molto bello, quasi sempre affollato. "
          "LORENZO: e' il decollo a meta' lago, piu' BASSO della Forclaz. "
          "SI ARRIVA IN DECOLLO IN AUTO e si parcheggia bene. Alcuni giorni della settimana ci sono "
          "anche bus gratuiti che partono dall'atterraggio. "
          "Per partire in XC meglio la Forclaz.", fonte="KML Delbene + Lorenzo"),
dict(zona="4 Annecy", tipo="decollo", nome="La Forclaz", lat=45.8142, lon=6.2468, quota=1240,
     vento="SW-W-NW", diff="4/5", aff="V", cat="Parapendio",
     note="Tutto l'anno. Stesse caratteristiche di Planfait, quasi sempre affollato. "
          "Salita da Doussard (490 m) = ~750 m. "
          "LORENZO: e' a SUD e piu' ALTO di Planfait. PER PARTIRE IN XC VAI QUI. "
          "MA non ci arrivi in auto: la strada e' privata, devi parcheggiare un bel pezzo prima. "
          "In compenso dall'atterraggio a sud del lago partono navette organizzate benissimo.",
     fonte="KML Delbene + Lorenzo"),
dict(zona="4 Annecy", tipo="hike&fly", nome="Col des Fretes", lat=45.8564, lon=6.2466, quota=1584,
     vento="S-SW / W-SW", diff="4/5", aff="V", cat="Hike & Fly",
     note="Pendio erboso grande e bello. Dall'atterraggio ufficiale di Perroix (550 m) sono D+ 1030. "
          "La prima parte della salita e quella che porta al decollo di Planfait. "
          "LORENZO: L'HIKE & FLY BELLO DELLA ZONA. Il punto di partenza e' il PARCHEGGIO ALTO DEL "
          "DECOLLO PLANFAIT (45.8526, 6.2237): puoi arrivare li' con navetta o bus e camminare solo "
          "l'ultimo pezzo, oppure farla tutta a piedi da sotto. Da li' a piedi si raggiungono "
          "comunque tutti i decolli della zona.",
     fonte="KML Delbene + lespiedssurterre + Lorenzo"),
dict(zona="4 Annecy", tipo="decollo", nome="Sambuy", lat=45.7500, lon=6.2800, quota=2100,
     vento="N / NE-E", diff="", aff="V", cat="Parapendio",
     note="Pendio erboso. Dall'atterraggio del Val de Tamie (780 m): D+ 1420 per la cima 2198 m, "
          "1300 per il decollo al colle verso la Petite Sambuy.", fonte="KML Delbene + lespiedssurterre"),
dict(zona="4 Annecy", tipo="atterraggio", nome="Doussard", lat=45.7880, lon=6.2200, quota=490,
     vento="", diff="5/5", aff="V", cat="Parapendio",
     note="Grande e bello. In primavera ed estate attenzione alle bolle nelle ore centrali. "
          "NAVETTA MOLTO BEN ORGANIZZATA: punto d'attesa dove il parcheggio incontra l'atterraggio, "
          "massimo 8 persone per corsa, la fila si fa con gli zaini.", fonte="KML Delbene"),
dict(zona="4 Annecy", tipo="atterraggio", nome="Planfait (atterraggio)", lat=45.8486, lon=6.2138, quota=460,
     vento="", diff="5/5", aff="V", cat="Parapendio",
     note="Stesse note sulle bolle. Navette solo bus urbani nei weekend estivi, gratuiti. "
          "MOLTO BUONO PER L'AUTOSTOP.", fonte="KML Delbene"),
dict(zona="4 Annecy", tipo="cima", nome="La Tournette / Pointe de la Bajulaz", lat=45.8180, lon=6.2650, quota=2250,
     disl=1600, partenza="Tornante dopo Verel, tra Perroix e col de la Forclaz",
     diff="", aff="V", cat="Alpinismo",
     note="Decollo nei pendii della Bajulaz, SUD/SUD-OVEST. Atterraggio a RIANT DESSUS (plateau sotto la "
          "Talamarche). Concatenabile con la Pointe de Talamarche (+250 m, decollo sud, atterraggio nel "
          "prato vicino a Verel).", fonte="lespiedssurterre.blog"),
dict(zona="4 Annecy", tipo="cima", nome="Pointe des Fretes", lat=45.8250, lon=6.2450, quota=2019,
     disl=1000, partenza="Montmin 1020 m", diff="", aff="V", cat="Cross",
     note="Decollo OVEST, possibile anche est risalendo dall'altro versante. Atterraggio vicino al "
          "cimitero di Montmin. In primavera serve la piccozza per i passaggi su neve.",
     fonte="lespiedssurterre.blog"),
dict(zona="4 Annecy", tipo="cima", nome="Tardevant", lat=45.9100, lon=6.4300, quota=2501,
     disl=1090, partenza="Les Confins", diff="", aff="V", cat="Alpinismo",
     note="Decollo dall'Ambrevetta, OVEST.", fonte="lespiedssurterre.blog"),
dict(zona="4 Annecy", tipo="cima", nome="Croisse Baulet", lat=45.8800, lon=6.5100, quota=2236,
     disl=1000, partenza="Le Plan, dopo La Giettaz", diff="", aff="V", cat="Cross",
     note="Decollo EST o OVEST.", fonte="lespiedssurterre.blog"),
dict(zona="4 Annecy", tipo="cima", nome="Mont Colombier", lat=45.6500, lon=6.0600, quota=2045,
     disl=1125, partenza="La Bottiere 920 m", diff="", aff="V", cat="Cross",
     note="Decollo OVEST 50 m sotto la cima. ATTENZIONE a una linea elettrica all'atterraggio.",
     fonte="lespiedssurterre.blog"),
dict(zona="4 Annecy", tipo="cima", nome="Mont Trelod", lat=45.6900, lon=6.1300, quota=2181,
     disl=None, partenza="", diff="", aff="K", cat="Cross", note="", fonte="parapenterando.free.fr"),

# ============ 5. CHARTREUSE / SAINT-HILAIRE ============
dict(zona="5 Saint-Hilaire", tipo="decollo", nome="Saint-Hilaire NORD", lat=45.3069, lon=5.88806, quota=906,
     vento="tutte", diff="", aff="V", cat="Parapendio",
     note="Grande tappeto comodo, ma PUO TROVARSI SOTTOVENTO alla termica che soffia davanti. "
          "REGOLA D'ARIA: NON SI SALE SOPRA I 3000 m, per la vicinanza dell'aeroporto di Lione. "
          "Attenzione al vento da sud. In primavera condizioni dure vicino alla falesia. "
          "Il 19-20 settembre e occupato dall'Icarnaval.", fonte="paraglidingearth"),
dict(zona="5 Saint-Hilaire", tipo="decollo", nome="Saint-Hilaire SUD", lat=45.3104, lon=5.89052, quota=953,
     vento="tutte", diff="", aff="V", cat="Parapendio",
     note="In erba, ci trovi piu spesso brezza di fronte. L'USCITA PUO ESSERE MOSSA, resta all'erta. "
          "Accesso: NON svoltare dopo la caserma dei pompieri, parcheggia 100 m piu avanti a destra, "
          "poi 5 minuti di pista, decollo sulla destra.", fonte="paraglidingearth"),
dict(zona="5 Saint-Hilaire", tipo="decollo", nome="Saint-Hilaire EST (il segreto)", lat=45.3084, lon=5.88795, quota=935,
     vento="", diff="", aff="V", cat="Parapendio",
     note="PICCOLO DECOLLO NASCOSTO E PULITO per quando il tappeto e troppo affollato. Attenzione alle "
          "vele che arrivano di lato. LA TUA CARTA PER VOLARE DURANTE LA COUPE ICARE.",
     fonte="paraglidingearth"),
dict(zona="5 Saint-Hilaire", tipo="atterraggio", nome="Lumbin", lat=45.302, lon=5.90612, quota=229,
     vento="", diff="", aff="V", cat="Parapendio",
     note="All'ingresso del paese venendo da Grenoble. Top landing con vento o brezza da nord vicino alla "
          "strada principale, al syndicat d'initiative, vicino al parcheggio grande. "
          "PARCHEGGIO UFFICIALE: non lasciare oggetti in vista in auto. "
          "Da 906 a 229 sono solo 680 m: il sito vive di termica, non di quota.", fonte="paraglidingearth"),
dict(zona="5 Saint-Hilaire", tipo="atterraggio", nome="Top landing ufficio turismo", lat=45.3107, lon=5.88863, quota=963,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Sul plateau. Utile se hai parcheggiato in decollo.", fonte="paraglidingearth"),
dict(zona="5 Saint-Hilaire", tipo="atterraggio", nome="Saint-Nazaire", lat=45.2653, lon=5.84198, quota=446,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Utile se lasci l'auto li e sali in autostop. DELICATO: area autorizzata stretta, di traverso "
          "alla brezza, alberi intorno.", fonte="paraglidingearth"),
dict(zona="5 Saint-Hilaire", tipo="parcheggio", nome="Parcheggio decollo St-Hilaire", lat=45.3076, lon=5.8855, quota=940,
     vento="", diff="", aff="V", cat="",
     note="Consiglio della scheda: lasciare l'auto all'ATTERRAGGIO e salire con la funicolare. "
          "Durante la Coupe Icare navette gratuite Saint-Hilaire-Lumbin.", fonte="paraglidingearth"),
dict(zona="5 Saint-Hilaire", tipo="cima", nome="Dent de Crolles", lat=45.3010, lon=5.8570, quota=2062,
     disl=650, partenza="Col du Coq (la scorciatoia)", diff="", aff="V", cat="Cross",
     note="Decollo nel pendio sommitale, SUD oppure NORD. Attenzione a un effetto di COMPRESSIONE sulla cima. "
          "Altre vie: da Saint-Hilaire 1100 m, da Saint-Nazaire-les-Eymes (460 m) 1700 m, da Lumbin 1800 m. "
          "E' la linea di cross classica del sito: dopo il Manival si sale alla Dent de Crolles e si segue "
          "la grande cresta a nord fino al Granier.", fonte="lespiedssurterre + infos-parapente"),
dict(zona="5 Saint-Hilaire", tipo="cima", nome="Chamechaude", lat=45.2880, lon=5.7700, quota=2082,
     disl=1050, partenza="Le Sappey-en-Chartreuse 1050 m", diff="", aff="V", cat="Cross",
     note="Decollo pendio sommitale OVEST. Atterraggio nel prato vicino al cimitero o al Bruchet. "
          "IDEALE IN VOLO SERALE, con soaring.", fonte="lespiedssurterre.blog"),
dict(zona="5 Saint-Hilaire", tipo="cima", nome="Grand Som", lat=45.3600, lon=5.8000, quota=2026,
     disl=900, partenza="Col du Cucheron 1139 m", diff="", aff="V", cat="Cross",
     note="Decollo NE/E/SE, atterraggio ufficiale di Saint-Hugues. Si puo atterrare sotto il colle ma e "
          "delicato: poco spazio e in pendenza. Concatenabile con il Charmant Som.",
     fonte="lespiedssurterre.blog"),
dict(zona="5 Saint-Hilaire", tipo="cima", nome="Charmant Som", lat=45.3080, lon=5.7500, quota=1867,
     disl=1000, partenza="Saint-Hugues 880 m", diff="", aff="V", cat="Cross",
     note="Decollo nel pendio PRIMA DELLA CROCE, EST.", fonte="lespiedssurterre.blog"),
dict(zona="5 Saint-Hilaire", tipo="cima", nome="Saint-Eynard (linea di cross)", lat=45.2400, lon=5.7800, quota=1359,
     disl=None, partenza="", diff="", aff="V", cat="Cross",
     note="LINEA DI CROSS CLASSICA: dal decollo verso sud lungo la falesia, attraversare il Manival, "
          "lavorare la prima termica, salire alla cresta del Saint-Eynard, seguirla a sud fino a un "
          "vecchio forte, ritorno per la stessa via.", fonte="paraglidingearth"),

# ============ 6. ECRINS / BRIANCON ============
dict(zona="6 Ecrins", tipo="cima", nome="Dome de Neige des Ecrins", lat=44.9200, lon=6.3500, quota=4015,
     disl=2141, partenza="Pre de Madame Carle 1874 m", diff="Ghiacciaio, ~11 km", aff="V", cat="Alpinismo",
     note="TRE OPZIONI DI VOLO: verso La Berarde per il col des Ecrins; sorvolo del Glacier Blanc; "
          "scavalco del col de Barre Noire per uscire sul Glacier Noir. "
          "IL DECOLLO SI FA SOTTO LA CREPACCIA TERMINALE. Attenzione alla NEVE TROPPO SCALDATA in cui "
          "sprofondi mentre corri: si parte presto. Chi l'ha fatto: in cima verso le 8, vento nullo, "
          "spazio giusto per due vele; variante Glacier Noir per non farsi schiacciare dal catabatico in "
          "fondo al Glacier Blanc; parcheggio in meno di 30 minuti. "
          "La Barre des Ecrins (4102 m) sono 2230 m. A fine settembre il ghiacciaio e scoperto e "
          "crepacciato, la crepaccia sotto la Barre e la crux.", fonte="FFCAM + relazioni"),
dict(zona="6 Ecrins", tipo="cima", nome="Roche Faurio", lat=44.9350, lon=6.3800, quota=3730,
     disl=1850, partenza="Pre de Madame Carle 1874 m", diff="Misto neve e roccia, senza grandi difficolta",
     aff="V", cat="Alpinismo",
     note="DECOLLO EST/SUD-EST, funziona bene. Due piazzali: uno a OVEST poco pendente con spazio per "
          "correre, uno a SUD sopra la fine del ghiacciaio, grande e piatto. "
          "PORTARE PICCHETTI da piantare nella neve perche la vela non scivoli. "
          "Volo sopra il Glacier Blanc con Barre e Dome di fronte, fino al Pre de Madame Carle.",
     fonte="FFCAM + relazioni"),
dict(zona="6 Ecrins", tipo="cima", nome="Mont Pelvoux", lat=44.9200, lon=6.4100, quota=3946,
     disl=2435, partenza="Ailefroide 1512 m (parcheggio dietro il campeggio)", diff="", aff="V", cat="Alpinismo",
     note="Decollo dalle pendici sommitali, TUTTE LE ORIENTAZIONI TRANNE OVEST (scheda 'vue d'ensemble des "
          "decos' su camptocamp). Chi l'ha fatto non e riuscito a partire dalla cima e ha decollato in "
          "discesa sotto il COULOIR COOLIDGE. Atterraggi: Vallouise, Ailefroide, Pre de Madame Carle - "
          "ha scelto Ailefroide ma i local dicono che e spesso caotico. Notte al refuge du Pelvoux. "
          "35 m oltre la tua soglia dei 2400.", fonte="lespiedssurterre + camptocamp"),
dict(zona="6 Ecrins", tipo="cima", nome="Pic du Glacier d'Arsine", lat=44.9800, lon=6.3900, quota=3364,
     disl=1500, partenza="Pre de Madame Carle 1874 m", diff="", aff="V", cat="Alpinismo",
     note="Decollo su ripiano sotto la cima, OVEST e SUD. Complementare alla Roche Faurio (est/sud-est): "
          "con qualsiasi vento uno dei due funziona. Possibile atterrare sul Glacier Blanc per concatenare.",
     fonte="lespiedssurterre.blog"),
dict(zona="6 Ecrins", tipo="cima", nome="Pointe des Cerces", lat=45.0800, lon=6.4700, quota=3098,
     disl=1150, partenza="Plan Lachat 1960 m (sulla sinistra salendo al Galibier)", diff="", aff="V", cat="Cross",
     note="Decollo su ripiano sotto la cima seguendo la cresta verso ovest, NORD/NORD-OVEST. "
          "Atterraggio a Plan Lachat, grandi spazi. Rientra nel budget cross.", fonte="lespiedssurterre.blog"),
dict(zona="6 Ecrins", tipo="cima", nome="Mont Thabor", lat=45.1400, lon=6.5700, quota=3178,
     disl=1400, partenza="Le Lavoir, dopo Valfrejus, 1925 m", diff="", aff="V", cat="Alpinismo",
     note="Decollo nel pendio sommitale, SUD-EST a SUD-OVEST (scheda su camptocamp). Atterraggio al piano "
          "sopra il Lavoir, vicino alla piccola presa d'acqua, ci si passa salendo, spazio grande. "
          "Con la Pointe des Cerces copri regimi opposti (NW e SW).", fonte="lespiedssurterre.blog"),
dict(zona="6 Ecrins", tipo="cima", nome="Aiguille Dibona", lat=44.9600, lon=6.2100, quota=3131,
     disl=1150, partenza="Les Etages 1590 m (Vallee du Veneon)", diff="Normale III / Voie du Nain AD 5a / Madier TD VII-",
     aff="V", cat="Arrampicata",
     note="LA CIMA E UNA GUGLIA AFFILATA: NON SI DECOLLA. "
          "VIE: Normale cresta nord (III) - dal rifugio si traversa la pietraia a ovest, canale di rocce "
          "facili, nevaio del Colle occidentale, Breche des Clochetons, cengia fino alla Breche Gunneng. "
          "Voie du Nain (AD, 6L max 5a, IV obbligatorio, + traverso 50 m di II + 2L in comune con la "
          "normale) tutta a spit, roccia splendida, ~150 m. Madier (TD, VII-) classicissima della sud. "
          "Visite Obligatoire (fino a 6a+) fix da 10 mm, soste con catena e maillon per calarsi sui primi "
          "5 tiri, poi si esce dalla normale, utile qualche nut, attacco a 5 min dal rifugio. "
          "Lady Bona sportiva, fix 10 e 12 mm, 14 rinvii. "
          "DISCESE IN DOPPIA: dalla normale una doppia da 50 m, frazionabile in due da 25 con una singola "
          "da 50. Dalla Voie du Nain due doppie da 30 m, fattibili con una singola da 60. "
          "ACCESSO: dal 1 settembre 2026 la D530 e pienamente aperta alle auto fino a Les Etages, ultima "
          "zona di sosta li. La Berarde resta CHIUSA al pubblico, perimetro di esclusione da rispettare.",
     fonte="vienormali + camptocamp + parc national"),
dict(zona="6 Ecrins", tipo="rifugio", nome="Refuge des Ecrins", lat=44.9280, lon=6.3620, quota=3175,
     vento="", diff="", aff="V", cat="Rifugio",
     note="Custodito fino al 27 SETTEMBRE (verificare telefonando). Prenotazione obbligatoria. "
          "Dal Pre de Madame Carle: 1300 m. Il gardien e la fonte migliore per lo stato della crepaccia.",
     fonte="CAF / refuges-ecrins"),
dict(zona="6 Ecrins", tipo="rifugio", nome="Refuge du Glacier Blanc", lat=44.9420, lon=6.3830, quota=2542,
     vento="", diff="", aff="V", cat="Rifugio",
     note="Custodito fino al 20 SETTEMBRE, poi resta il LOCALE INVERNALE. "
          "Dormirci senza prenotazione dimezza la giornata verso il Dome (restano 1470 m) e ti da "
          "una notte di acclimatamento. Dal Pre de Madame Carle: 670 m.", fonte="CAF"),
dict(zona="6 Ecrins", tipo="rifugio", nome="Refuge du Soreiller", lat=44.9650, lon=6.2000, quota=2719,
     vento="", diff="", aff="V", cat="Rifugio",
     note="DATE DISCORDANTI: la scheda del parco da aperto dal 6 giugno al 10 ottobre 2026, il CAF Isere "
          "dice custodito fino al 13 settembre e oltre solo se ci sono le navette (a settembre non ci sono). "
          "TELEFONA: 04 76 79 08 32. Mezza pensione 57 euro, notte semplice 22 euro. "
          "Da Les Etages: 1150 m, 2-3 h.", fonte="CAF / parc national des Ecrins"),
dict(zona="6 Ecrins", tipo="zona", nome="Regola volo parco Ecrins", lat=44.9200, lon=6.3500, quota=0,
     vento="", diff="", aff="V", cat="Spazio aereo",
     note="Il volo libero sopra il CUORE del parco degli Ecrins e autorizzato dal 1 LUGLIO al 31 OTTOBRE. "
          "Il 21-23 settembre sei dentro. Bivacco tollerato in prossimita dei rifugi, da confermare con "
          "i gardien.", fonte="Parc national des Ecrins"),
dict(zona="6 Ecrins", tipo="decollo", nome="Col d'Izoard High", lat=44.8143, lon=6.7224, quota=2360,
     vento="SW-S-SE", diff="4/5", aff="V", cat="Parapendio",
     note="Tutto l'anno. Prato bello. "
          "LORENZO: la zona dell'Izoard e' bellissima (parco del Queyras) MA e' LA RAMPA DI LANCIO "
          "PER I VOLI DA 300 KM. D'estate e' davvero forte forte; A SETTEMBRE MOLTO MEGLIO. "
          "C'e' anche una scuola di volo, quindi puo' essere un posto tranquillo oppure il delirio.",
     fonte="KML Delbene + Lorenzo"),
dict(zona="6 Ecrins", tipo="decollo", nome="Col d'Izoard 2", lat=44.8036, lon=6.7472, quota=2300,
     vento="NW-W-SW-S-SE", diff="3/5", aff="V", cat="Parapendio",
     note="Prato ripido sul lato NW. IL LATO SUD E ROCCIOSO CON SASSI PICCOLI CHE TAGLIANO FACILMENTE "
          "LE FUNI.", fonte="KML Delbene"),
dict(zona="6 Ecrins", tipo="decollo", nome="Col d'Izoard (basso)", lat=44.8191, lon=6.7288, quota=2250,
     vento="SE", diff="2,5/5", aff="V", cat="Parapendio",
     note="Piccolo. Serve solo a evitare di camminare fino a quello bello.", fonte="KML Delbene"),
dict(zona="6 Ecrins", tipo="decollo", nome="Puy Aillaud", lat=44.8503, lon=6.4791, quota=1650,
     vento="SE-E", diff="4/5", aff="V", cat="Parapendio",
     note="Tutto l'anno. Prato non enorme ma con spazio. "
          "E' IL DECOLLO UFFICIALE DI VALLOUISE. "
          "LORENZO: Vallouise e' uno dei due posti che consiglia vivamente nel Brianconnese. "
          "Dal decollo ufficiale SI PUO SALIRE ANCORA PIU SU per hike & fly molto belli. "
          "Dietro c'e il parco nazionale degli Ecrins con i ghiacciai. "
          "Hike & fly Puy Aillaud a 44.8526, 6.4556. Atterraggio a 44.8416, 6.4888.",
     fonte="KML Delbene + Lorenzo"),
dict(zona="6 Ecrins", tipo="decollo", nome="Puy Aillaud 2", lat=44.8503, lon=6.4781, quota=1680,
     vento="S", diff="3,5/5", aff="V", cat="Parapendio",
     note="Bello ma stretto.", fonte="KML Delbene"),
dict(zona="6 Ecrins", tipo="decollo", nome="Prorel", lat=44.8900, lon=6.6100, quota=2566,
     vento="", diff="", aff="K", cat="Parapendio",
     note="Cabinovia da Briancon, 5 km dal centro.", fonte="KML Delbene"),
dict(zona="6 Ecrins", tipo="decollo", nome="Col de Granon", lat=44.9600, lon=6.6000, quota=2404,
     vento="", diff="", aff="K", cat="Parapendio", note="", fonte="KML Delbene"),
# Val di Susa / Val Chisone (rientro)
dict(zona="7 Val Susa/Chisone", tipo="decollo", nome="Condotte", lat=45.0500, lon=6.9500, quota=1600,
     vento="E", diff="4,5/5", aff="V", cat="Parapendio",
     note="Bello e grande. IL VENTO DI VALLE E TROPPO FORTE DALLE 10 ALLE 17 in primavera ed estate. "
          "In estate il posto migliore per lunghi voli serali. Atterraggio Condotte 3,5/5, grande.",
     fonte="KML Delbene"),
dict(zona="7 Val Susa/Chisone", tipo="decollo", nome="Colle Azzara", lat=45.0300, lon=6.9800, quota=1700,
     vento="S-SE", diff="5/5", aff="V", cat="Parapendio",
     note="Campo molto grande, ottimo per il groundhandling. SE NON RIESCI A GUADAGNARE QUOTA DEVI "
          "TOPLANDARE: l'atterraggio e troppo lontano e non ci sono atterraggi di fortuna in mezzo. "
          "Quasi sempre vento forte.", fonte="KML Delbene"),
dict(zona="7 Val Susa/Chisone", tipo="hike&fly", nome="Monte Vandalino", lat=44.8600, lon=7.1700, quota=2121,
     vento="SW-S-SE", diff="5/5", aff="V", cat="Hike & Fly",
     note="Bel decollo alpino, buono anche per groundhandling.", fonte="KML Delbene"),
dict(zona="7 Val Susa/Chisone", tipo="hike&fly", nome="Punta Curbasiri", lat=44.9500, lon=7.0500, quota=1800,
     vento="SE-S-SW-W", diff="4/5", aff="V", cat="Hike & Fly", note="", fonte="KML Delbene"),
dict(zona="7 Val Susa/Chisone", tipo="hike&fly", nome="Pian dell'Alpe", lat=45.0100, lon=6.9900, quota=1980,
     vento="SW-S-SE", diff="4/5", aff="V", cat="Hike & Fly",
     note="Usato dalle scuole per i voli intermedi.", fonte="KML Delbene"),
dict(zona="7 Val Susa/Chisone", tipo="atterraggio", nome="Riposa", lat=45.0400, lon=6.9300, quota=1100,
     vento="", diff="4/5", aff="V", cat="Parapendio",
     note="Grande. NELLA PARTE OVEST attenzione a TONDINI DI FERRO E CAVI ALTI 1 m.", fonte="KML Delbene"),
dict(zona="7 Val Susa/Chisone", tipo="atterraggio", nome="Fenestrelle", lat=45.0400, lon=7.0500, quota=1150,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Bello. ATTENZIONE AI CAVI ELETTRICI.", fonte="KML Delbene"),
dict(zona="7 Val Susa/Chisone", tipo="atterraggio", nome="Prali", lat=44.8900, lon=7.0500, quota=1400,
     vento="", diff="", aff="V", cat="Parapendio",
     note="Stretto ma lungo. NAVETTE: raramente organizzate in Val di Susa. Chiedere ai local di "
          "'BICIO', il tizio che gestisce le navette dei decolli della valle.", fonte="KML Delbene"),
# ---- aggiunte da Lorenzo (pilota, c'e stato) ----
dict(zona="6 Ecrins", tipo="decollo", nome="Ceillac", lat=44.6670, lon=6.7854, quota=1900,
     vento="", diff="", aff="L", cat="Parapendio",
     note="LORENZO: proprio PARADISO VAN LIFE. Valle alpina con mega pianoro e paesino super "
          "caratteristico. DECOLLO A 200 m DALL'ATTERRAGGIO, con SEMPRE DINAMICA che stai su. "
          "Ci sono anche hike & fly belli alti con viste spettacolari. "
          "UNICO CONTRO: partire per fare XC da li NON E NIENTE FACILE. Sei molto in alto e giri in "
          "valli alpine. Pero anche solo un giretto e bellissimo. "
          "Atterraggio a 44.6636, 6.7809, parcheggio atterraggio a 44.6650, 6.7761.",
     fonte="Lorenzo"),
dict(zona="6 Ecrins", tipo="atterraggio", nome="Ceillac (atterraggio)", lat=44.6636, lon=6.7809, quota=1640,
     vento="", diff="", aff="L", cat="Parapendio",
     note="A 200 m dal decollo. Parcheggio a 44.6650, 6.7761.", fonte="Lorenzo + KML"),
dict(zona="6 Ecrins", tipo="logistica", nome="Vallouise e Ceillac (i due consigli)", lat=44.8500, lon=6.4900, quota=0,
     vento="", diff="", aff="L", cat="Base",
     note="LORENZO consiglia vivamente DUE POSTI nel Brianconnese: VALLOUISE e CEILLAC. "
          "Vallouise: decollo ufficiale (Puy Aillaud) e hike & fly molto belli salendo piu su, "
          "con gli Ecrins e i ghiacciai dietro. "
          "Ceillac: paradiso van life, decollo a 200 m dall'atterraggio, dinamica costante, hike & fly "
          "alti con viste spettacolari, ma XC difficile. "
          "L'Izoard/Queyras e bellissimo ma e la rampa dei 300 km: a settembre e molto piu gestibile "
          "che d'estate.", fonte="Lorenzo"),
dict(zona="4 Annecy", tipo="logistica", nome="Dormire ad Annecy", lat=45.8000, lon=6.2100, quota=0,
     vento="", diff="", aff="L", cat="Pernottamento",
     note="LORENZO: MEGLIO NON STARE IN ZONA LAGO, rischio multe. Uscire un pochino: a sud del lago "
          "da qualche parte defilata, o in qualche valle. "
          "Usare l'app PARK4NIGHT, ci sono tante soluzioni.", fonte="Lorenzo"),
dict(zona="4 Annecy", tipo="logistica", nome="Affollamento e XC ad Annecy", lat=45.8300, lon=6.2200, quota=0,
     vento="", diff="", aff="L", cat="Note generali",
     note="LORENZO: posto molto famoso e bello, si fanno CROSS FACILI - piu che altro c'e cosi tanta "
          "gente che basta seguire gli altri come paperelle. Il contro e proprio la quantita di gente, "
          "ma dipende dalla stagione: A SETTEMBRE probabilmente MOLTA MENO GENTE (ma comunque ce n'e). "
          "I decolli ufficiali sono due: Planfait (meta lago, piu basso) e La Forclaz (sud, piu alto). "
          "PER PARTIRE IN XC: LA FORCLAZ.", fonte="Lorenzo"),
dict(zona="4 Annecy", tipo="parcheggio", nome="Parcheggio alto Planfait / Col de Fretes", lat=45.8526, lon=6.2237, quota=1150,
     vento="", diff="", aff="L", cat="",
     note="PUNTO DI PARTENZA dell'hike & fly al Col de Fretes. Ci si arriva in auto, in navetta o "
          "col bus gratuito dall'atterraggio.", fonte="Lorenzo + KML"),
dict(zona="4 Annecy", tipo="parcheggio", nome="Parcheggio La Forclaz", lat=45.8081, lon=6.2459, quota=1050,
     vento="", diff="", aff="L", cat="",
     note="LA STRADA SOPRA E PRIVATA: si parcheggia un bel pezzo prima del decollo. "
          "Alternativa migliore: navette dall'atterraggio a sud del lago, organizzate benissimo.",
     fonte="Lorenzo + KML"),
# ---- cime mancanti ----
dict(zona="6 Ecrins", tipo="cima", nome="Barre des Ecrins", lat=44.9219, lon=6.3606, quota=4102,
     disl=2230, partenza="Pre de Madame Carle 1874 m", diff="Ghiacciaio + cresta, PD+/AD-", aff="V",
     cat="Alpinismo",
     note="90 m piu in alto del Dome de Neige, ma il decollo si fa dal Dome. "
          "A fine settembre il ghiacciaio e scoperto e crepacciato: LA CREPACCIA SOTTO LA BARRE E LA CRUX. "
          "Sentire il gardien del Refuge des Ecrins il giorno prima.", fonte="FFCAM + relazioni"),
dict(zona="3 Oberland", tipo="cima", nome="Morgenberghorn (salita)", lat=46.6560, lon=7.7500, quota=2190,
     disl=1498, partenza="Muelenen", diff="", aff="V", cat="Alpinismo",
     note="Decollo S/SW/W, atterraggio a Interlaken, 1622 m di volo. "
          "Via alternativa da Aeschiried lungo la cresta, con lo Startplatz Spitz a meta per chiudere prima.",
     fonte="hikeandfly.com / baern-gliders.ch"),
dict(zona="4 Annecy", tipo="cima", nome="Pointe de la Sambuy", lat=45.7500, lon=6.2800, quota=2198,
     disl=1420, partenza="Atterraggio Val de Tamie 780 m", diff="", aff="V", cat="Cross",
     note="1420 m per la cima, ma solo 1300 PER IL DECOLLO AL COLLE verso la Petite Sambuy. "
          "Orientamento NE a E.", fonte="lespiedssurterre.blog"),

# ---- decolli hike & fly dell'Oberland (nomi dal listino di una guida locale) ----
dict(zona="3 Oberland", tipo="hike&fly", nome="Baellenhoechst", lat=46.6300, lon=7.8300, quota=1750,
     vento="", diff="", aff="?", cat="Hike & Fly",
     note="Regione Interlaken. Coordinate approssimative: verifica su camptocamp o SHV.", fonte="highabove.me"),
dict(zona="3 Oberland", tipo="hike&fly", nome="Tanzboedeli", lat=46.5600, lon=7.9000, quota=1670,
     vento="", diff="", aff="?", cat="Hike & Fly",
     note="Lauterbrunnental. Coordinate approssimative.", fonte="highabove.me"),
dict(zona="3 Oberland", tipo="hike&fly", nome="Gemmenalphorn", lat=46.7100, lon=7.7600, quota=2061,
     vento="", diff="", aff="?", cat="Hike & Fly",
     note="Zona Niederhorn. Coordinate approssimative.", fonte="highabove.me"),
dict(zona="3 Oberland", tipo="hike&fly", nome="Rotschalp", lat=46.7300, lon=8.0000, quota=1600,
     vento="", diff="", aff="?", cat="Hike & Fly",
     note="Brienzersee. Coordinate approssimative.", fonte="highabove.me"),
dict(zona="3 Oberland", tipo="hike&fly", nome="Startplatz Spitz (Morgenberghorn)", lat=46.6700, lon=7.7400, quota=1600,
     vento="S-SW-W", diff="", aff="V", cat="Hike & Fly",
     note="Alla stazione a monte dello skilift superiore salendo da Aeschiried lungo la cresta. "
          "PRIMA POSSIBILITA DI DECOLLO: se hai gia abbastanza quota o se sopra le condizioni non "
          "vanno, chiudi qui. Coordinate approssimative.", fonte="baern-gliders.ch"),
]

# nome, zona, giorni consigliati, categoria, dislivello, ore, elementi (nome punto), descrizione
GITE = [
 dict(nome="Ebenalp da Wasserauen", zona="1 Alpstein", giorni="sab 12", cat="Cross", disl=770, ore="2h30",
      punti=["Ebenalp a piedi","Ebenalp NW (1.1)","A1 Wasserauen (parapendio)"],
      testo="Sali a piedi da Wasserauen via Seealpsee, decolli dal NW nella finestra 15-18 e "
            "atterri dove hai lasciato l'auto. Con vento da ovest forte lascia perdere: rotore. "
            "Il decollo e tardo, quindi ti si incastra bene dopo l'impegno delle 13 a San Gallo."),
 dict(nome="Kronberg, l'assicurazione", zona="1 Alpstein", giorni="dom 13", cat="Cross", disl=770, ore="2h30",
      punti=["Kronberg a piedi","Kronberg Sud","Kronberg Ovest","Kronberg Nord"],
      testo="Da Jakobsbad. Quattro decolli in cima coprono tutte le direzioni, quindi e il piano "
            "che non salta mai. Atterraggio alla stazione a valle: torni all'auto a piedi. "
            "Il Sud e l'unico decollo dell'Alpstein per vento meridionale."),
 dict(nome="Saentis per il Lisengrat", zona="1 Alpstein", giorni="dom 13", cat="Alpinismo", disl=1634, ore="5h",
      punti=["Saentis via Rotsteinpass e Lisengrat","Saentis"],
      testo="La traversata classica dell'Alpstein: Seealpsee, Meglisalp, Rotsteinpass, poi la cresta "
            "attrezzata del Lisengrat. SOLO CON W-SW DEBOLI, e non si decolla dalla funivia. "
            "Atterri a Unterwasser in Toggenburg: il recupero e dall'altro versante, va organizzato prima. "
            "Se il vento non e quello, ripieghi sul Kronberg."),
 dict(nome="Rigi di pomeriggio", zona="2 Zurigo", giorni="lun 14", cat="Cross", disl=1115, ore="3h",
      punti=["Rigi Staffelhoehe","Rigi Scheidegg"],
      testo="Da Weggis a piedi, oppure con la cremagliera se l'impegno delle 09 a Zurigo si allunga. "
            "Staffelhoehe funziona dalle 14 fino a sera. Se c'e bise forte, il decollo giusto e "
            "Rigi Scheidegg, che e esposto NE."),
 dict(nome="Schynige Platte a piedi", zona="3 Oberland", giorni="mar 15", cat="Cross", disl=1383, ore="4h30",
      punti=["Schynige Platte a piedi","Schynige Platte","Lehn (Interlaken)"],
      testo="Il piu bel hike & fly del viaggio come rapporto fatica/rientro. Parti da Zurigo alle 6:30, "
            "parcheggi a Wilderswil alle 9, sei in cima alle 13:30 dentro la finestra buona, "
            "atterri a Lehn che e a 3 km dall'auto con treno e bus ogni pochi minuti. "
            "NO-GO: vento di valle a Lehn, NW, o bise forte. In quel caso vai a Grindelwald-First."),
 dict(nome="Faulhorn dal First", zona="3 Oberland", giorni="mer 16", cat="Cross", disl=516, ore="2h",
      punti=["Faulhorn","Grindelwald-First"],
      testo="Cabinovia fino a First e due ore di sentiero. Poca fatica, ambiente enorme davanti a "
            "Eiger, Moench e Jungfrau. Se vuoi la giornata piena, la traversata integrale "
            "Wilderswil-Schynige Platte-Faulhorn e 2330 m su 25 km, circa 10 ore."),
 dict(nome="Morgenberghorn", zona="3 Oberland", giorni="mer 16", cat="Alpinismo", disl=1498, ore="5h",
      punti=["Morgenberghorn (salita)","Morgenberghorn","Startplatz Spitz (Morgenberghorn)"],
      testo="Da Muelenen, decollo S/SW/W, 1622 m di volo fino a Interlaken. "
            "Dalla via di Aeschiried c'e lo Startplatz Spitz a meta: se in alto non va, chiudi li."),
 dict(nome="Forclaz, il giorno di cross", zona="4 Annecy", giorni="gio 17", cat="Cross", disl=0, ore="",
      punti=["La Forclaz","Doussard","Parcheggio La Forclaz"],
      testo="LORENZO: per partire in XC si va alla Forclaz, che e piu alta di Planfait. "
            "Ma la strada sopra e privata: lasci l'auto all'atterraggio a sud del lago e prendi "
            "le navette, organizzate benissimo. A settembre c'e molta meno gente che d'estate. "
            "I cross sono facili perche basta seguire gli altri."),
 dict(nome="Col des Fretes", zona="4 Annecy", giorni="gio 17", cat="Hike & Fly", disl=400, ore="1h30",
      punti=["Col des Fretes","Parcheggio alto Planfait / Col de Fretes"],
      testo="LORENZO: il punto di partenza e il parcheggio alto del decollo Planfait, dove arrivi "
            "in navetta o col bus gratuito. Quindi non sono i 1030 m dal fondovalle: solo l'ultimo "
            "pezzo a piedi. Pendio erboso grande e bello, S-SW. "
            "Da li a piedi raggiungi comunque tutti i decolli della zona."),
 dict(nome="Coupe Icare senza coda", zona="5 Saint-Hilaire", giorni="ven 18 - dom 20", cat="Cross", disl=0, ore="",
      punti=["Saint-Hilaire EST (il segreto)","Lumbin","Top landing ufficio turismo"],
      testo="Il decollo Nord il 19-20 e occupato dall'Icarnaval. L'Est e un piccolo decollo nascosto "
            "e pulito per quando il tappeto e troppo affollato: attenzione alle vele che arrivano di lato. "
            "NON SI SALE SOPRA I 3000 m, aeroporto di Lione. "
            "Lascia l'auto all'atterraggio e sali con la funicolare o le navette gratuite."),
 dict(nome="Dent de Crolles dal Col du Coq", zona="5 Saint-Hilaire", giorni="sab 19 - dom 20", cat="Cross",
      disl=650, ore="2h",
      punti=["Dent de Crolles"],
      testo="La via corta: 650 m dal Col du Coq invece dei 1100 da Saint-Hilaire o 1800 da Lumbin. "
            "Decollo nel pendio sommitale, sud o nord. Attenzione a un effetto di compressione sulla cima. "
            "E l'unico modo di volare davvero nel weekend della manifestazione."),
 dict(nome="Dome de Neige e volo", zona="6 Ecrins", giorni="mar 22", cat="Alpinismo", disl=2141, ore="6-7h",
      punti=["Dome de Neige des Ecrins","Refuge des Ecrins","Refuge du Glacier Blanc"],
      testo="Partenza notturna dal Pre de Madame Carle verso l'1:00-2:00 per essere in cima tra le 7 e le 8. "
            "Il decollo si fa SOTTO LA CREPACCIA e il rischio e la neve troppo scaldata in cui sprofondi "
            "correndo: alle 10 hai perso la finestra. Tre opzioni di volo, la piu sicura e lo scavalco "
            "del col de Barre Noire sul Glacier Noir, per non farsi schiacciare dal catabatico. "
            "ACCLIMATAMENTO: vieni da 300 m di Saint-Hilaire. Valuta la notte al locale invernale del "
            "Glacier Blanc (2542 m): dimezza la giornata e ti da una notte in quota."),
 dict(nome="Roche Faurio, la versione ragionevole", zona="6 Ecrins", giorni="mar 22 - mer 23", cat="Alpinismo",
      disl=1850, ore="5-6h",
      punti=["Roche Faurio"],
      testo="300 m in meno del Dome e nessuna difficolta seria, stesso ambiente. "
            "Decollo est/sud-est, due piazzali: uno a ovest poco pendente con spazio per correre, "
            "uno a sud grande e piatto sopra la fine del ghiacciaio. "
            "PORTA I PICCHETTI da piantare nella neve. Volo sopra il Glacier Blanc fino al parcheggio."),
 dict(nome="Pic du Glacier d'Arsine", zona="6 Ecrins", giorni="mer 23", cat="Alpinismo", disl=1500, ore="5h",
      punti=["Pic du Glacier d'Arsine"],
      testo="Decollo OVEST e SUD, quindi e il complemento della Roche Faurio: con qualsiasi vento "
            "uno dei due funziona. 1500 m dal Pre de Madame Carle."),
 dict(nome="Dibona, giornata di roccia", zona="6 Ecrins", giorni="alternativa 21-23", cat="Arrampicata",
      disl=1150, ore="3h avvicinamento",
      punti=["Aiguille Dibona","Refuge du Soreiller"],
      testo="ATTENZIONE: e sul versante OPPOSTO del massiccio (Veneon, lato Isere). "
            "Dal Pre de Madame Carle sono 110 km e due ore. Con tre giorni non ci stanno sia questa "
            "che la Barre: devi sceglierne una. "
            "LA VELA RESTA IN MACCHINA: la cima e una guglia, non si decolla. "
            "Telefona al rifugio (04 76 79 08 32), le date di chiusura sono discordanti."),
 dict(nome="Pointe des Cerces", zona="6 Ecrins", giorni="21 o 23", cat="Cross", disl=1150, ore="4h",
      punti=["Pointe des Cerces"],
      testo="Da Plan Lachat, sulla sinistra salendo al Galibier. Rientra nel budget cross. "
            "Decollo nord/nord-ovest su un ripiano sotto la cima, atterraggio a Plan Lachat, grandi spazi. "
            "Col Mont Thabor (sud-est/sud-ovest) copri i regimi opposti."),
 dict(nome="Ceillac, giornata van life", zona="6 Ecrins", giorni="opzionale", cat="Cross", disl=0, ore="",
      punti=["Ceillac","Ceillac (atterraggio)"],
      testo="LORENZO: paradiso van life. Valle alpina con mega pianoro e paesino caratteristico. "
            "Decollo a 200 m dall'atterraggio, con dinamica costante che ti tiene su. "
            "Ci sono anche hike & fly alti con viste spettacolari. "
            "CONTRO: partire in XC da li non e per niente facile, sei molto in alto e giri in valli alpine. "
            "NOTA LOGISTICA: e 50 km a sud di Vallouise, nel Queyras. Non e sulla strada del Dome."),
]

GIORNI = [
    ("sab 12", "1 Alpstein", "Impegno a San Gallo (13:00 o 10:00). Ebenalp: finestra 15-18."),
    ("dom 13", "1 Alpstein", "Kronberg a piedi (770 m, 4 decolli) oppure Saentis (1634 m, solo W-SW deboli)."),
    ("lun 14", "2 Zurigo", "Impegno a Zurigo (09:00). Pomeriggio: Rigi Staffelhoehe (dalle 14) o una delle cime T2."),
    ("mar 15", "3 Oberland", "Trasferimento Zurigo-Wilderswil (135 km, 2h). Schynige Platte a piedi o Breitlauenen."),
    ("mer 16", "3 Oberland", "GIORNO LIBERATO (era Losanna). Cima dell'Oberland con volo di discesa."),
    ("gio 17", "4 Annecy", "Il vero giorno di cross. Forclaz/Planfait, oppure Tournette in hike & fly."),
    ("ven 18", "5 Saint-Hilaire", "Coupe Icare, Icare Expo 10:00-19:30. Decollo EST per volare senza coda."),
    ("sab 19", "5 Saint-Hilaire", "Icarnaval + Icare Show. Decollo Nord occupato. Alternativa: Dent de Crolles."),
    ("dom 20", "5 Saint-Hilaire", "Idem. Navette gratuite Saint-Hilaire-Lumbin, parcheggi a Lumbin, arrivare presto."),
    ("lun 21", "6 Ecrins", "Trasferimento (190 km, 3h via Lautaret). Ricognizione Pre de Madame Carle. Volo a Prorel/Izoard."),
    ("mar 22", "6 Ecrins", "Il giorno grosso. Dome de Neige (2141 m) o Roche Faurio (1850 m). Partenza notturna."),
    ("mer 23", "6 Ecrins", "Cuscinetto meteo. Se il 22 e saltato, oggi e il giorno buono."),
    ("gio 24", "7 Val Susa/Chisone", "Valle Orco (te la gestisci tu)."),
    ("ven 25", "7 Val Susa/Chisone", ""),
    ("sab 26", "7 Val Susa/Chisone", ""),
    ("dom 27", "7 Val Susa/Chisone", ""),
    ("lun 28", "", "Rientro. Briancon-Milano 300 km, 4h via Monginevro."),
]

TRATTE = [
    ("Milano", "San Gallo", 330, "4h"),
    ("San Gallo", "Zurigo", 85, "1h"),
    ("Zurigo", "Wilderswil", 135, "2h"),
    ("Wilderswil", "Annecy", 250, "3h30"),
    ("Annecy", "Lumbin", 100, "1h20"),
    ("Saint-Hilaire", "Briancon", 190, "3h (Col du Lautaret)"),
    ("Briancon", "Les Etages", 110, "2h"),
    ("Briancon", "Milano", 300, "4h (Monginevro)"),
]

MATERIALE = [
    ("Corda 30 m", "INSUFFICIENTE per le doppie della Dibona. Servono 50 m minimo, 60 per la Voie du Nain."),
    ("Picchetti da neve", "Per i decolli sui ghiacciai degli Ecrins: la vela scivola."),
    ("Vela 16", "Voli di discesa, non termica. Giornate alpinistiche = aria calma di primo mattino."),
    ("Vela cross + pod", "Giornate cross, fascia 12-16. Soglia salita a piedi: 1200 m."),
    ("Ramponi + piccozza", "Ecrins, e Pointe des Fretes in primavera."),
    ("FLARM", "Consigliato nella zona dell'heliport di Trogen."),
]

FONTI = [
    ("SHV/FSVL", "shv-fsvl.ch - siti di volo, anche in italiano", "Svizzera"),
    ("fga.ch", "Fluggemeinschaft Alpstein, con webcam", "Alpstein"),
    ("HFC Alpstein", "Club hike & fly, organizza l'Alpstein Crossing", "Alpstein"),
    ("paragliding.ch/hike-and-fly", "Cime con quota, grado SAC, dislivello, tempo", "Svizzera"),
    ("baern-gliders.ch", "Rotte hike & fly con GPX", "Oberland"),
    ("deltaclub-interlaken.ch", "Info sito Interlaken", "Oberland"),
    ("hikr.org", "Relazioni cime svizzere, gradi SAC", "Svizzera"),
    ("gipfelbuch.ch", "Condizioni aggiornate, da guardare la settimana prima", "Svizzera"),
    ("sac-cas.ch Tourenportal", "Database ufficiale CAS", "Svizzera"),
    ("map.geo.admin.ch", "Swisstopo, overlay pendenza", "Svizzera"),
    ("camptocamp.org", "Waypoint tipo Decollage, TUTTE le Alpi", "Francia + Svizzera"),
    ("lespiedssurterre.blog", "Idees de sommets en rando vol: cime con orientamento decollo", "Francia"),
    ("parapenterando.free.fr", "Database siti rando-vol", "Francia"),
    ("infos-parapente.com", "Topo rando-vol dettagliati", "Francia"),
    ("bivouak.net", "Savoia", "Francia"),
    ("XContest", "Punti di decollo reali dai tracciati", "Ovunque"),
    ("thermal.kk7.ch", "Termiche e traiettorie aggregate", "Ovunque"),
    ("paraglidingearth.com", "Solo GPX, max 99 siti per volta dal riquadro visibile", "Ovunque"),
    ("meteo-parapente.com", "Vento di gradiente per quota, top termico, strato limite", "Meteo"),
    ("camminaevola.it", "SOLO http:// - la versione https e un sito dirottato", "FVG"),
]
