#!/usr/bin/env python3
"""Genera la web estática de Kimu Txalaparta (ES + EU) en public/.

Uso:  python3 tools/build.py
Todo el contenido está en el diccionario T (una entrada por idioma).
Lo marcado con tbd("...") se ve en la web con borde discontinuo: es contenido pendiente.
"""
import json, html, os, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
BASE = "https://kimutxalaparta.netlify.app"
TODAY = datetime.date.today().isoformat()

EMAIL = "ignacio@musubigara.org"
WA_NUM = "34620463558"
IG = "https://www.instagram.com/kimutxalaparta/"
YT = "https://www.youtube.com/@kimutxalaparta"
FB = "https://www.facebook.com/kimutxalaparta/"
SPOTIFY = "https://open.spotify.com/search/Kimu%20Txalaparta"  # PENDIENTE: enlace al perfil de artista
MUSUBI = "https://musubigara.org"

def e(s):
    return html.escape(s, quote=True)

def tbd(s):
    return f'<em class="tbd" title="Pendiente de confirmar">{s}</em>'

ICON = {
 "ig": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>',
 "yt": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9.2v5.6l4.8-2.8z" fill="currentColor"/></svg>',
 "sp": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9.5"/><path d="M7 9.3c3.4-1 7.2-.7 10 .9"/><path d="M7.6 12.4c2.8-.8 5.8-.5 8.2.8"/><path d="M8.2 15.3c2.2-.6 4.4-.4 6.3.6"/></svg>',
 "fb": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 21v-7.5h2.6l.4-3h-3v-1.9c0-.9.3-1.5 1.5-1.5h1.6V4.4a21 21 0 0 0-2.3-.1c-2.3 0-3.8 1.4-3.8 3.9v2.3H9v3h2.5V21"/></svg>',
 "wa": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 11.7a8.5 8.5 0 0 1-12.6 7.5L3.5 20.5l1.4-4.3A8.5 8.5 0 1 1 20.5 11.7z"/><path d="M9.4 8.5c.2 0 .4.1.5.3l.7 1.5c.1.2 0 .4-.1.5l-.5.5c-.1.1-.1.2-.1.3.3.9 1.5 2.1 2.4 2.4.1 0 .2 0 .3-.1l.5-.5c.1-.1.3-.2.5-.1l1.5.7c.2.1.3.3.3.5 0 1-.8 1.7-1.7 1.7-2.9 0-5.9-3-5.9-5.9 0-.9.7-1.7 1.6-1.8z"/></svg>',
 "arrow": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>',
 "dl": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11"/><path d="M7 10l5 5 5-5"/><path d="M5 20h14"/></svg>',
}

VIDEOS = [  # id, título, miniatura grande
 ("d8M4dUgAjjE", "Arditurriko meategian (Oiartzun) · bakarka", True),
 ("A3yv-FnBFF0", "«Zahar Berri» · zuzenean", False),
 ("NPlcK7zX5NM", "«Intro & Agurra» · zuzenean", False),
 ("8ttP5DT_TsE", "«Sambao» · bideoklipa", False),
 ("X9DWKymqqak", "«Agurra» · harrizko txalaparta", False),
 ("54pJoDG15Io", "Otsozelaiako lezetan (Isturitze)", False),
 ("wCQIxSptv14", "«Tetris / Korobeiniki»", False),
 ("bU86T62306g", "«Primavera» (L. Einaudi) · arpa eta txalaparta", False),
]
PHOTOS = ["wCQIxSptv14", "54pJoDG15Io", "X9DWKymqqak", "8ttP5DT_TsE", "A3yv-FnBFF0", "bU86T62306g"]

T = {
"es": {
 "path": "/", "html_lang": "es", "other": "eu",
 "title": "Kimu Txalaparta · Txalaparta de madera y de piedra · Conciertos y contratación",
 "desc": "Kimu Txalaparta: txalaparta de madera y de piedra desde Donostia. Conciertos, inmersión cultural y actuaciones didácticas para instituciones, festivales y asociaciones. Contratación: Musubigara®.",
 "skip": "Saltar al contenido",
 "nav": [("kimu","Kimu"),("biografia","Biografía"),("propuesta","Propuesta"),("multimedia","Multimedia"),("colaboraciones","Colaboraciones"),("contacto","Contacto")],
 "menu_open": "Abrir menú", "menu_close": "Cerrar menú", "lang_label": "Idioma",
 "newtab": "se abre en una pestaña nueva",
 "hero_box": "Txalaparta de madera y de piedra. Ritmo ancestral vasco, creación de hoy. <em>Kimu</em> significa «brote»: la tradición que vuelve a crecer en cada concierto.",
 "hero_side": ["Conciertos, inmersión cultural y actuaciones didácticas para ayuntamientos, instituciones, festivales, asociaciones y agentes culturales.",
               "En euskera y en castellano. Gestión y contratación: Musubigara®."],
 "cta_hire": "Contratar", "cta_watch": "Ver vídeos",
 "hero_cap": "Arditurriko meategia, Oiartzun",
 "ticker": "_Kimu Txalaparta_Zura eta harria_Madera y piedra_Txalaparta_",
 # 01
 "kimu_h": "Kimu",
 "kimu_box": "Somos Kimu Txalaparta: un grupo de Donostia que toca el instrumento más rítmico de la cultura vasca —en madera y en piedra— y lo lleva más allá de la sidrería: a escenarios, festivales, plazas, cuevas, minas e iglesias.",
 "kimu_who": "La txalaparta se toca a dúo: dos personas, cuatro makilas y un diálogo de golpes que se construye en directo. Nosotros partimos de ese diálogo tradicional y lo abrimos a la melodía, a la creación propia y al encuentro con otras músicas.",
 "offers_k": "¿Qué ofrecemos?",
 "offers": [
  ("Concierto", "Repertorio propio y tradicional para escenarios, festivales y fiestas. Para más de 100 personas, con una sonorización sencilla."),
  ("Inmersión cultural", "Formato íntimo y 100 % acústico para menos de 100 personas: escuchar, preguntar y acercarse al instrumento."),
  ("Actuación didáctica", "Para centros educativos, asociaciones y programas culturales: historia, técnica y juego rítmico con el público."),
  ("Eventos y protocolo", "Congresos, recepciones institucionales, homenajes, bodas y celebraciones que piden un momento con identidad."),
 ],
 "why_h": "¿Por qué Kimu?",
 "why": [
  "Dos instrumentos, dos paisajes sonoros: la madera, potente y festiva; la piedra, melódica y sorprendente.",
  "Tradición y creación propia: de los ritmos de siempre a versiones inesperadas, de Einaudi al Tetris.",
  "Más de una década de trayectoria, en Euskal Herria y en escenarios como Manila, Managua o Budapest.",
  "Formato adaptable y logística ligera: acústico en salas pequeñas y un rider sencillo para grandes aforos.",
  "Mediación en euskera y en castellano: contamos al público de dónde viene la txalaparta y cómo se toca.",
  "Un único interlocutor: Musubigara® se ocupa de la contratación, la documentación y la coordinación técnica.",
 ],
 # 02
 "bio_h": "Biografía",
 "bio": [
  "Kimu nace en 2012, después de años tocando juntos, con una pregunta: ¿hasta dónde puede llegar la txalaparta? El grupo se propuso explorar las posibilidades rítmicas, armónicas y melódicas de un instrumento que nació en el caserío, ligado a las labores del campo y a la fiesta de la sidra, y que a mediados del siglo XX estuvo a punto de desaparecer. En septiembre de 2016 presentó <em>Kimu</em>, su primer disco, concebido con la txalaparta como instrumento solista.",
  "Desde entonces el proyecto ha crecido en dos direcciones: hacia la piedra, una txalaparta capaz de construir melodías, y hacia lugares que suenan por sí mismos, como la mina de Arditurri en Oiartzun o las cuevas de Isturitz. Sus videoclips y sus versiones con arpa o de músicas populares han acercado la txalaparta a públicos nuevos, y sus conciertos la han llevado de Donostia y del festival Errobiko a ciudades como Manila, Managua o Budapest.",
 ],
 "bio_alt": "Kimu Txalaparta tocando la txalaparta de madera en un escenario",
 "facts": [("2012","Nace Kimu"),("2016","Primer disco, «Kimu»"),("2","Txalapartas: madera y piedra"),("3","Continentes")],
 # 03
 "prop_h": "Propuesta artística",
 "spec": [("Músicos en escena", tbd("Nº de músicos")),("Instrumentos","Txalaparta de madera y de piedra"),("Duración", tbd("60–75 min")),("Idiomas","Euskera y castellano")],
 "instr": [
  ("v-wCQIxSptv14", "Txalaparta de madera", "Tablones de madera sobre caballetes, golpeados con makilas. Es la txalaparta clásica: potente, rítmica y festiva, la que llamaba a la gente cuando la sidra estaba lista.", "Txalaparta de madera tocada a dúo"),
  ("v-bU86T62306g", "Txalaparta de piedra", "Losas de piedra afinadas que suman notas al ritmo. Permite construir melodías y abre la txalaparta a repertorios nuevos y a diálogos con otros instrumentos.", "Txalaparta de piedra tocada en una iglesia"),
 ],
 "rider_h": "Requerimientos técnicos",
 "rider": [
  "<strong>Salas de hasta 100 personas</strong> (formato de inmersión cultural): no hace falta sonorizar. La txalaparta de madera y la de piedra suenan con bastantes decibelios.",
  "<strong>Salas grandes, exteriores y festivales</strong> (más de 100 personas): conviene sonorizar. Basta con 6 micrófonos SM57 con pies de micro bajos (uno de ellos para presentar) y 2 monitores.",
 ],
 "rider_dl": "Descargar rider (PDF)", "rider_note": "Rider técnico con necesidades de sonido y escenario. Para cualquier duda técnica, escríbenos.",
 # 04
 "mm_h": "Multimedia",
 "videos_h": "Vídeos", "videos_more": "Canal de YouTube",
 "yt_note": "Los vídeos se cargan desde YouTube (modo de privacidad mejorada) solo cuando pulsas «play».",
 "play": "Reproducir vídeo",
 "listen_h": "Escucha", "listen_txt": "Escucha a Kimu Txalaparta en Spotify.", "listen_btn": "Abrir Spotify",
 "photos_h": "Fotos", "photo_alt": "Kimu Txalaparta en directo",
 "ig_h": "Instagram", "ig_txt": "Ensayos, conciertos y lo que pasa entre bambalinas.",
 # 05
 "col_h": "Colaboraciones",
 "col_lead": "Ayuntamientos, instituciones, festivales, asociaciones y medios con los que hemos compartido escenario y proyectos.",
 "col_names": ["Festival Errobiko", "Mikrofilm Festival", "France Bleu Pays Basque", "Mercado de la Bretxa (Donostia)", tbd("+ ayuntamientos e instituciones")],
 "col_end": ", entre otros.",
 # 06
 "con_h": "Contacto",
 "con_box": "¿Programas una temporada, un festival o un evento institucional? Cuéntanos fecha, lugar y aforo y te enviamos propuesta y presupuesto.",
 "con_mgmt": "Gestión y contratación", "con_wa": "Escribir por WhatsApp",
 "f": {"name":"Nombre y apellidos","org":"Entidad (ayuntamiento, festival, asociación…)","email":"Correo electrónico","phone":"Teléfono (opcional)",
       "type":"Tipo de actuación","types":["Concierto","Inmersión cultural (menos de 100 personas)","Actuación didáctica","Evento o protocolo","Otro"],
       "date":"Fecha y lugar previstos","cap":"Aforo aproximado","msg":"Mensaje",
       "consent":'He leído la <a href="/privacidad/">política de privacidad</a> y acepto que se usen mis datos para responder a mi solicitud.',
       "send":"Enviar solicitud"},
 "wa_text": "Hola, quiero información para contratar a Kimu Txalaparta",
 "cta_float": "Hablemos",
 "foot_mgmt": "Gestión y contratación:", "legal": "Aviso legal", "privacy": "Política de privacidad",
 "legal_path": "/aviso-legal/", "privacy_path": "/privacidad/", "thanks_path": "/gracias/",
 "thanks_h": "Gracias", "thanks_p": "Hemos recibido tu solicitud. Te responderemos en breve desde ignacio@musubigara.org.", "back": "Volver a la web",
 "nf_h": "Página no encontrada", "nf_p": "Esta página no existe o ha cambiado de sitio.",
},
"eu": {
 "path": "/eu/", "html_lang": "eu", "other": "es",
 "title": "Kimu Txalaparta · Zurezko eta harrizko txalaparta · Kontzertuak eta kontratazioa",
 "desc": "Kimu Txalaparta: zurezko eta harrizko txalaparta Donostiatik. Kontzertuak, murgiltze kulturala eta emanaldi pedagogikoak udal, erakunde, jaialdi eta elkarteentzat. Kontratazioa: Musubigara®.",
 "skip": "Edukira joan",
 "nav": [("kimu","Kimu"),("biografia","Biografia"),("propuesta","Proposamena"),("multimedia","Multimedia"),("colaboraciones","Lankidetzak"),("contacto","Harremana")],
 "menu_open": "Menua ireki", "menu_close": "Menua itxi", "lang_label": "Hizkuntza",
 "newtab": "fitxa berri batean irekitzen da",
 "hero_box": "Zurezko eta harrizko txalaparta. Antzinako euskal erritmoa, gaur egungo sorkuntza. <em>Kimu</em>: tradiziotik jaiotzen den adar berria, kontzertu bakoitzean hazten dena.",
 "hero_side": ["Kontzertuak, murgiltze kulturala eta emanaldi pedagogikoak udal, erakunde, jaialdi, elkarte eta kultur eragileentzat.",
               "Euskaraz eta gaztelaniaz. Kudeaketa eta kontratazioa: Musubigara®."],
 "cta_hire": "Kontratatu", "cta_watch": "Bideoak ikusi",
 "hero_cap": "Arditurriko meategia, Oiartzun",
 "ticker": "_Kimu Txalaparta_Zura eta harria_Madera y piedra_Txalaparta_",
 "kimu_h": "Kimu",
 "kimu_box": "Kimu Txalaparta gara: euskal kulturako musika-tresnarik erritmikoena —zurezkoa eta harrizkoa— jotzen duen Donostiako taldea. Sagardotegitik haratago eramaten dugu: agertokietara, jaialdietara, plazetara, kobazuloetara, meategietara eta elizetara.",
 "kimu_who": "Txalaparta binaka jotzen da: bi lagun, lau makila eta zuzenean eraikitzen den kolpeen elkarrizketa. Guk elkarrizketa tradizional horretatik abiatuta, melodiara, sorkuntza propiora eta beste musika batzuekiko topaketara zabaltzen dugu.",
 "offers_k": "Zer eskaintzen dugu?",
 "offers": [
  ("Kontzertua", "Errepertorio propioa eta tradizionala agertoki, jaialdi eta jaietarako. 100 pertsonatik gora, soinu-sistema sinple batekin."),
  ("Murgiltze kulturala", "Formatu hurbila eta % 100 akustikoa, 100 pertsonatik beherako taldeentzat: entzun, galdetu eta tresnara hurbildu."),
  ("Emanaldi pedagogikoa", "Ikastetxe, elkarte eta kultur programetarako: historia, teknika eta jolas erritmikoa publikoarekin."),
  ("Ekitaldiak eta protokoloa", "Kongresuak, harrera instituzionalak, omenaldiak, ezkontzak eta nortasuna behar duten ospakizunak."),
 ],
 "why_h": "Zergatik Kimu?",
 "why": [
  "Bi tresna, bi soinu-paisaia: zura, indartsua eta jaiotsua; harria, melodikoa eta harrigarria.",
  "Tradizioa eta sorkuntza propioa: betiko erritmoetatik ustekabeko bertsioetara, Einauditik Tetrisera.",
  "Hamarkada bat baino gehiagoko ibilbidea, Euskal Herrian eta Manila, Managua edo Budapest bezalako agertokietan.",
  "Formatu egokigarria eta logistika arina: akustikoa areto txikietan eta rider sinplea edukiera handietarako.",
  "Bitartekaritza euskaraz eta gaztelaniaz: txalaparta nondik datorren eta nola jotzen den kontatzen diogu publikoari.",
  "Solaskide bakarra: Musubigara®-k kudeatzen ditu kontratazioa, dokumentazioa eta koordinazio teknikoa.",
 ],
 "bio_h": "Biografia",
 "bio": [
  "Kimu 2012an sortu zen, urteetan elkarrekin jo ondoren, galdera batekin: noraino irits daiteke txalaparta? Taldeak tresnaren aukera erritmiko, harmoniko eta melodikoak arakatzeko helburua jarri zuen. Baserrian jaio zen tresna, landa-lanei eta sagardoaren jaiari lotua, eta XX. mendearen erdialdean galtzeko zorian egon zen. 2016ko irailean <em>Kimu</em> aurkeztu zuen, lehen diskoa, txalaparta bakarkako musika-tresna delarik.",
  "Harrezkero proiektua bi norabidetan hazi da: harrirantz, melodiak eraikitzeko gai den txalapartarantz, eta berez soinua duten lekuetarantz, hala nola Oiartzungo Arditurriko meategia edo Isturitzeko kobazuloak. Bideoklipek eta arparekin edo herri-musikekin egindako bertsioek txalaparta publiko berrietara hurbildu dute, eta kontzertuek Donostiatik eta Errobiko jaialditik Manila, Managua edo Budapest bezalako hirietara eraman dute.",
 ],
 "bio_alt": "Kimu Txalaparta zurezko txalaparta jotzen agertoki batean",
 "facts": [("2012","Kimu sortzen da"),("2016","Lehen diskoa, «Kimu»"),("2","Txalaparta: zura eta harria"),("3","Kontinente")],
 "prop_h": "Proposamen artistikoa",
 "spec": [("Musikariak agertokian", tbd("Musikari kopurua")),("Tresnak","Zurezko eta harrizko txalaparta"),("Iraupena", tbd("60–75 min")),("Hizkuntzak","Euskara eta gaztelania")],
 "instr": [
  ("v-wCQIxSptv14", "Zurezko txalaparta", "Astoen gainean jarritako ohol luzeak, makilekin joak. Txalaparta klasikoa da: indartsua, erritmikoa eta jaiotsua, sagardoa prest zegoenean jendea deitzen zuena.", "Zurezko txalaparta binaka jotzen"),
  ("v-bU86T62306g", "Harrizko txalaparta", "Afinatutako harlauzak, erritmoari notak gehitzen dizkiotenak. Melodiak eraikitzeko aukera ematen du eta txalaparta errepertorio berrietara eta beste tresna batzuekiko elkarrizketara zabaltzen du.", "Harrizko txalaparta eliza batean jotzen"),
 ],
 "rider_h": "Behar teknikoak",
 "rider": [
  "<strong>100 pertsona arteko aretoak</strong> (murgiltze kulturaleko formatua): ez da soinu-sistemarik behar. Zurezko eta harrizko txalapartek dezibelio dezente ematen dituzte.",
  "<strong>Areto handiak, kanpoaldeak eta jaialdiak</strong> (100 pertsonatik gora): komeni da soinua jartzea. Nahikoa da 6 SM57 mikrofono oin baxuekin (horietako bat aurkezteko) eta 2 monitore.",
 ],
 "rider_dl": "Riderra deskargatu (PDF)", "rider_note": "Soinu- eta agertoki-beharrak biltzen dituen rider teknikoa. Zalantza teknikoren bat baduzu, idatzi iezaguzu.",
 "mm_h": "Multimedia",
 "videos_h": "Bideoak", "videos_more": "YouTube kanala",
 "yt_note": "Bideoak YouTubetik kargatzen dira (pribatutasun hobetuko moduan), «play» sakatzen duzunean bakarrik.",
 "play": "Bideoa erreproduzitu",
 "listen_h": "Entzun", "listen_txt": "Entzun Kimu Txalaparta Spotifyn.", "listen_btn": "Spotify ireki",
 "photos_h": "Argazkiak", "photo_alt": "Kimu Txalaparta zuzenean",
 "ig_h": "Instagram", "ig_txt": "Entseguak, kontzertuak eta agertoki atzean gertatzen dena.",
 "col_h": "Lankidetzak",
 "col_lead": "Agertokia eta proiektuak partekatu ditugun udal, erakunde, jaialdi, elkarte eta hedabideak.",
 "col_names": ["Errobiko Festibala", "Mikrofilm Festival", "France Bleu Pays Basque", "Bretxako azoka (Donostia)", tbd("+ udalak eta erakundeak")],
 "col_end": ", besteak beste.",
 "con_h": "Harremana",
 "con_box": "Denboraldi bat, jaialdi bat edo ekitaldi instituzional bat antolatzen ari zara? Kontaiguzu data, lekua eta edukiera, eta proposamena eta aurrekontua bidaliko dizkizugu.",
 "con_mgmt": "Kudeaketa eta kontratazioa", "con_wa": "WhatsAppez idatzi",
 "f": {"name":"Izen-abizenak","org":"Erakundea (udala, jaialdia, elkartea…)","email":"Helbide elektronikoa","phone":"Telefonoa (aukerakoa)",
       "type":"Emanaldi mota","types":["Kontzertua","Murgiltze kulturala (100 pertsonatik behera)","Emanaldi pedagogikoa","Ekitaldia edo protokoloa","Beste bat"],
       "date":"Aurreikusitako data eta lekua","cap":"Gutxi gorabeherako edukiera","msg":"Mezua",
       "consent":'<a href="/eu/pribatutasun-politika/">Pribatutasun-politika</a> irakurri dut eta onartzen dut nire datuak eskaerari erantzuteko erabiltzea.',
       "send":"Eskaera bidali"},
 "wa_text": "Kaixo, Kimu Txalaparta kontratatzeko informazioa nahi nuke",
 "cta_float": "Hitz egin dezagun",
 "foot_mgmt": "Kudeaketa eta kontratazioa:", "legal": "Lege-oharra", "privacy": "Pribatutasun-politika",
 "legal_path": "/eu/lege-oharra/", "privacy_path": "/eu/pribatutasun-politika/", "thanks_path": "/eu/eskerrik-asko/",
 "thanks_h": "Eskerrik asko", "thanks_p": "Zure eskaera jaso dugu. Laster erantzungo dizugu ignacio@musubigara.org helbidetik.", "back": "Webgunera itzuli",
 "nf_h": "Ez da orria aurkitu", "nf_p": "Orri hau ez dago edo lekuz aldatu da.",
},
}
T["es"]["ticker"] = "_Kimu Txalaparta_Madera y piedra_Zura eta harria_Txalaparta_"
T["eu"]["ticker"] = "_Kimu Txalaparta_Zura eta harria_Madera y piedra_Txalaparta_"

def wa(t):
    from urllib.parse import quote
    return f"https://wa.me/{WA_NUM}?text={quote(t['wa_text'])}"

def social(t):
    items = [(IG,"ig","Instagram"),(YT,"yt","YouTube"),(SPOTIFY,"sp","Spotify"),(FB,"fb","Facebook"),(wa(t),"wa","WhatsApp")]
    return '<ul class="social">' + "".join(
        f'<li><a href="{e(u)}" target="_blank" rel="noopener" aria-label="{n} ({t["newtab"]})">{ICON[i]}</a></li>' for u,i,n in items) + "</ul>"

def lang_nav(t, here_es, here_eu):
    cur = t["html_lang"]
    return (f'<nav class="lang" aria-label="{t["lang_label"]}">'
            f'<a href="{here_eu}" hreflang="eu" lang="eu"{" aria-current=\"true\"" if cur=="eu" else ""}>Eus</a> _ '
            f'<a href="{here_es}" hreflang="es" lang="es"{" aria-current=\"true\"" if cur=="es" else ""}>Cast</a></nav>')

def nav(t, prefix=""):
    return '<ul class="nav">' + "".join(
        f'<li><a href="{prefix}#{i}"><sup>[0{n}]</sup>{e(l)}</a></li>' for n,(i,l) in enumerate(t["nav"], start=1)) + "</ul>"

def head(t, title, desc, canon, alt_es, alt_eu, extra="", noindex=False):
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    og_img = f"{BASE}/img/og.jpg"
    return f'''<!doctype html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{BASE}{canon}">
<link rel="alternate" hreflang="es" href="{BASE}{alt_es}">
<link rel="alternate" hreflang="eu" href="{BASE}{alt_eu}">
<link rel="alternate" hreflang="x-default" href="{BASE}{alt_es}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kimu Txalaparta">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{BASE}{canon}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="{"es_ES" if t["html_lang"]=="es" else "eu_ES"}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#D8D4CD">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/ibm-plex-mono-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/kimu.css">
{extra}
</head>'''

def topbar(t, prefix, here_es, here_eu, home):
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="top">
<a class="wordmark" href="{home}" aria-label="Kimu Txalaparta">KIMU<span class="u" aria-hidden="true"></span><small aria-hidden="true">TXALAPARTA</small></a>
<div class="bar">
<a class="brand-mini" href="{home}">KIMU_TXALAPARTA</a>
{nav(t, prefix)}
{lang_nav(t, here_es, here_eu)}
{social(t)}
<button class="plus" id="plus" type="button" aria-expanded="false" aria-controls="panel" aria-label="{t["menu_open"]}" data-open="{t["menu_open"]}" data-close="{t["menu_close"]}"></button>
</div>
<div class="panel" id="panel">{nav(t, prefix)}{lang_nav(t, here_es, here_eu)}{social(t)}</div>
</header>'''

def footer(t):
    home = t["path"]
    return f'''<footer class="foot">
<div class="c1"><p><strong>Kimu Txalaparta</strong></p><p>Donostia · Euskal Herria</p>{social(t)}</div>
<div class="c2"><p>{t["foot_mgmt"]}</p><p><a href="{MUSUBI}" target="_blank" rel="noopener">Musubigara®</a></p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="c3"><ul><li><a href="{t["legal_path"]}">{t["legal"]}</a></li><li><a href="{t["privacy_path"]}">{t["privacy"]}</a></li></ul><p style="margin-top:12px">© 2026 Kimu Txalaparta</p></div>
<div class="big" aria-hidden="true">KIMU_</div>
</footer>
<a class="cta-float" href="{e(wa(t))}" target="_blank" rel="noopener" aria-label="{t["cta_float"]} — WhatsApp ({t["newtab"]})">{t["cta_float"]} {ICON["arrow"]}</a>
<script src="/assets/kimu.js" defer></script>
</body>
</html>'''

def jsonld(t):
    data = {
      "@context": "https://schema.org",
      "@type": "MusicGroup",
      "name": "Kimu Txalaparta",
      "alternateName": "KIMU Txalaparta",
      "url": BASE + t["path"],
      "image": BASE + "/img/og.jpg",
      "description": t["desc"],
      "genre": ["Txalaparta", "Música tradicional vasca", "Percusión"],
      "foundingDate": "2012",
      "foundingLocation": {"@type": "Place", "name": "Donostia / San Sebastián"},
      "inLanguage": t["html_lang"],
      "sameAs": [YT, IG, FB],
      "album": {"@type": "MusicAlbum", "name": "Kimu", "datePublished": "2016-09"},
      "contactPoint": {"@type": "ContactPoint", "contactType": "booking", "email": EMAIL, "telephone": "+" + WA_NUM, "availableLanguage": ["eu", "es"]},
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"

def home(lang):
    t = T[lang]
    other = T[t["other"]]
    es_p, eu_p = T["es"]["path"], T["eu"]["path"]
    f = t["f"]
    out = [head(t, t["title"], t["desc"], t["path"], es_p, eu_p, jsonld(t)), "<body>", topbar(t, "", es_p, eu_p, t["path"]), '<main id="main">']
    # Portada
    out.append(f'''<section class="hero" aria-label="Kimu Txalaparta">
<h1 class="vh">Kimu Txalaparta</h1>
<div class="grid hero-grid">
<p class="box hero-box">{t["hero_box"]}</p>
<div class="hero-side">{"".join(f"<p>{e(p).replace('Musubigara®','<a href=\"'+MUSUBI+'\" target=\"_blank\" rel=\"noopener\">Musubigara®</a>')}</p>" for p in t["hero_side"])}</div>
<div class="hero-ctas"><a class="btn" href="#contacto">{t["cta_hire"]} {ICON["arrow"]}</a><a class="btn ghost" href="#multimedia">{t["cta_watch"]}</a></div>
<figure class="hero-img"><img src="/img/v-d8M4dUgAjjE-l.webp" width="1280" height="720" alt="Kimu Txalaparta, Arditurri" fetchpriority="high"><figcaption>{t["hero_cap"]}</figcaption></figure>
</div></section>
<div class="ticker" aria-hidden="true"><span>{(e(t["ticker"])*6)}</span></div>''')
    # 01
    offers = "".join(
        f'<article class="card"><span class="n">[0{i}]</span><h3>{e(h)}</h3><p>{e(p)}</p>' +
        (f'<p style="margin-top:10px"><a href="{INMERSION_PATH[lang]}">{e(INMERSION[(lang,"more")])} →</a></p>' if i == 2 else '') +
        '</article>'
        for i,(h,p) in enumerate(t["offers"],1))
    why = "".join(f"<li>{e(w)}</li>" for w in t["why"])
    out.append(f'''<section class="sec" id="kimu" aria-labelledby="kimu-t">
<h2 class="sec-h" id="kimu-t"><span class="idx">[01]</span>{t["kimu_h"]}</h2>
<div class="intro"><p class="box">{e(t["kimu_box"])}</p><p class="who">{e(t["kimu_who"])}</p></div>
<p class="kicker" style="margin-top:56px">{t["offers_k"]}</p>
<div class="offers" style="margin-top:0">{offers}</div>
<div class="why"><h3>{t["why_h"]}</h3><ul>{why}</ul></div>
</section>''')
    # 02
    facts = "".join(f"<div><strong>{a}</strong><span>{e(b)}</span></div>" for a,b in t["facts"])
    out.append(f'''<section class="sec" id="biografia" aria-labelledby="bio-t">
<h2 class="sec-h" id="bio-t"><span class="idx">[02]</span>{t["bio_h"]}</h2>
<div class="bio"><figure><img src="/img/v-54pJoDG15Io-l.webp" width="1280" height="720" alt="{e(t["bio_alt"])}" loading="lazy"></figure>
<div class="txt">{"".join(f"<p>{p}</p>" for p in t["bio"])}</div>
<div class="facts">{facts}</div></div>
</section>''')
    # 03
    spec = "".join(f"<div><dt>{e(a)}</dt><dd>{b}</dd></div>" for a,b in t["spec"])
    instr = "".join(f'<article><img src="/img/{img}.webp" width="960" height="540" alt="{e(alt)}" loading="lazy"><div class="in"><h3>{e(h)}</h3><p>{e(p)}</p></div></article>' for img,h,p,alt in t["instr"])
    rider_pdf = f"/descargas/kimu-txalaparta-rider-{lang}.pdf"
    out.append(f'''<section class="sec" id="propuesta" aria-labelledby="prop-t">
<h2 class="sec-h" id="prop-t"><span class="idx">[03]</span>{t["prop_h"]}</h2>
<dl class="spec">{spec}</dl>
<div class="instr">{instr}</div>
<div class="rider"><div class="box"><h3>{t["rider_h"]}</h3>{"".join(f"<p>{r}</p>" for r in t["rider"])}</div>
<div class="dl"><a class="btn" href="{rider_pdf}" download>{ICON["dl"]} {t["rider_dl"]}</a><p>{e(t["rider_note"])}</p></div></div>
</section>''')
    # 04
    vids = "".join(
        f'<figure class="video{" big" if big else ""}"><button class="play" type="button" data-yt="{vid}" data-title="{e(title)}" aria-label="{t["play"]}: {e(title)}">'
        f'<img src="/img/v-{vid}{"-l" if big else ""}.webp" alt="" loading="lazy" width="960" height="540"></button><figcaption>{e(title)}</figcaption></figure>'
        for vid,title,big in VIDEOS) + f'<a class="video more" href="{YT}" target="_blank" rel="noopener"><span>{t["videos_more"]} ↗</span></a>'
    photos = "".join(f'<a href="/img/v-{p}-l.webp" target="_blank" rel="noopener"><img src="/img/v-{p}.webp" alt="{e(t["photo_alt"])}" loading="lazy" width="960" height="540"></a>' for p in PHOTOS)
    out.append(f'''<section class="sec" id="multimedia" aria-labelledby="mm-t">
<h2 class="sec-h" id="mm-t"><span class="idx">[04]</span>{t["mm_h"]}</h2>
<div class="sub" style="margin-top:0"><h3>_{t["videos_h"]}</h3><a href="{YT}" target="_blank" rel="noopener">{t["videos_more"]} ↗</a></div>
<div class="videos">{vids}</div>
<p class="yt-note">{e(t["yt_note"])}</p>
<div class="sub"><h3>_{t["listen_h"]}</h3></div>
<div class="listen"><div class="box"><p>{e(t["listen_txt"])}</p><a class="btn" href="{SPOTIFY}" target="_blank" rel="noopener">{ICON["sp"]} {t["listen_btn"]}</a></div></div>
<div class="sub"><h3>_{t["photos_h"]}</h3></div>
<div class="photos">{photos}</div>
<div class="sub"><h3>_{t["ig_h"]}</h3><a href="{IG}" target="_blank" rel="noopener">@kimutxalaparta ↗</a></div>
<div class="ig"><a class="handle" href="{IG}" target="_blank" rel="noopener">@kimutxalaparta</a><span>{e(t["ig_txt"])}</span></div>
</section>''')
    # 05
    names = ", ".join(n if n.startswith("<em") else f"<span>{e(n)}</span>" for n in t["col_names"])
    out.append(f'''<section class="sec" id="colaboraciones" aria-labelledby="col-t">
<h2 class="sec-h" id="col-t"><span class="idx">[05]</span>{t["col_h"]}</h2>
<div class="collab"><p class="lead">{e(t["col_lead"])}</p><p class="names">{names}{t["col_end"]}</p></div>
</section>''')
    # 06
    opts = "".join(f"<option>{e(o)}</option>" for o in f["types"])
    out.append(f'''<section class="sec" id="contacto" aria-labelledby="con-t">
<h2 class="sec-h" id="con-t"><span class="idx">[06]</span>{t["con_h"]}</h2>
<div class="contact">
<div class="direct"><p class="box">{e(t["con_box"])}</p>
<p class="kicker">{t["con_mgmt"]} · <a href="{MUSUBI}" target="_blank" rel="noopener">Musubigara®</a></p>
<a class="big" href="mailto:{EMAIL}?subject=Kimu%20Txalaparta">{EMAIL}</a>
<a class="btn ghost" href="{e(wa(t))}" target="_blank" rel="noopener">{ICON["wa"]} {t["con_wa"]}</a></div>
<form class="f" name="contratacion" method="POST" action="{t["thanks_path"]}" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="contratacion"><input type="hidden" name="idioma" value="{lang}">
<p class="hp"><label>No rellenar <input name="bot-field"></label></p>
<div><label for="f-name-{lang}">{f["name"]}</label><input id="f-name-{lang}" name="nombre" autocomplete="name" required></div>
<div><label for="f-org-{lang}">{f["org"]}</label><input id="f-org-{lang}" name="entidad" autocomplete="organization"></div>
<div><label for="f-email-{lang}">{f["email"]}</label><input id="f-email-{lang}" name="email" type="email" autocomplete="email" required></div>
<div><label for="f-tel-{lang}">{f["phone"]}</label><input id="f-tel-{lang}" name="telefono" type="tel" autocomplete="tel"></div>
<div><label for="f-type-{lang}">{f["type"]}</label><select id="f-type-{lang}" name="tipo">{opts}</select></div>
<div><label for="f-cap-{lang}">{f["cap"]}</label><input id="f-cap-{lang}" name="aforo" inputmode="numeric"></div>
<div class="full"><label for="f-date-{lang}">{f["date"]}</label><input id="f-date-{lang}" name="fecha_lugar"></div>
<div class="full"><label for="f-msg-{lang}">{f["msg"]}</label><textarea id="f-msg-{lang}" name="mensaje"></textarea></div>
<div class="full"><label class="chk"><input type="checkbox" name="consentimiento" value="si" required><span>{f["consent"]}</span></label></div>
<div class="full"><button class="btn" type="submit">{f["send"]} {ICON["arrow"]}</button></div>
</form></div>
</section>''')
    out.append("</main>")
    out.append(footer(t))
    return "\n".join(out)

# ── Páginas legales ──────────────────────────────────────────────
TITULAR_ES = ("<p><strong>Titular:</strong> Ignacio Sanz Arana (Musubigara®), responsable de la gestión y contratación de Kimu Txalaparta.<br>"
              "<strong>NIF:</strong> 72752567W<br><strong>Domicilio:</strong> Pintor Pablo Uranga 12, 01008 Vitoria-Gasteiz (Álava), España.<br>"
              f"<strong>Correo electrónico:</strong> <a href=\"mailto:{EMAIL}\">{EMAIL}</a></p>")
TITULAR_EU = ("<p><strong>Titularra:</strong> Ignacio Sanz Arana (Musubigara®), Kimu Txalapartaren kudeaketaren eta kontratazioaren arduraduna.<br>"
              "<strong>IFZ:</strong> 72752567W<br><strong>Helbidea:</strong> Pintor Pablo Uranga 12, 01008 Vitoria-Gasteiz (Araba), Espainia.<br>"
              f"<strong>Helbide elektronikoa:</strong> <a href=\"mailto:{EMAIL}\">{EMAIL}</a></p>")

LEGAL = {
 ("es","legal"): ("Aviso legal", f'''<p>Última actualización: 16 de noviembre de 2026</p>
<h2>1. Datos identificativos</h2><p>En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), se informa de que este sitio web es titularidad de:</p>{TITULAR_ES}
<h2>2. Objeto y condiciones de uso</h2><p>Esta web presenta el proyecto musical Kimu Txalaparta y permite solicitar información para su contratación. El acceso y uso de la web atribuyen la condición de usuario e implican la aceptación de este aviso legal. El usuario se compromete a hacer un uso adecuado de los contenidos, conforme a la ley, la buena fe y el orden público.</p>
<h2>3. Propiedad intelectual e industrial</h2><p>Los textos, fotografías, vídeos, diseño y demás contenidos de esta web pertenecen a Kimu Txalaparta, a Musubigara® o a sus respectivos autores, y se utilizan con la debida autorización. Queda prohibida su reproducción, distribución, comunicación pública o transformación sin autorización expresa y por escrito.</p>
<h2>4. Responsabilidad</h2><p>Se hace lo posible por que la información sea exacta y esté actualizada, pero no se garantiza la ausencia de errores ni la disponibilidad continua del sitio. La web contiene enlaces a sitios de terceros (YouTube, Instagram, Spotify, Facebook, WhatsApp) sobre cuyo contenido no se tiene control ni se asume responsabilidad.</p>
<h2>5. Protección de datos y cookies</h2><p>El tratamiento de datos personales se rige por la <a href="/privacidad/">política de privacidad</a>. Esta web no instala cookies propias ni de análisis.</p>
<h2>6. Legislación aplicable y jurisdicción</h2><p>Este aviso legal se rige por la legislación española. Para cualquier controversia, las partes se someten a los juzgados y tribunales de Vitoria-Gasteiz, salvo que la normativa de consumidores y usuarios establezca otro fuero imperativo.</p>'''),
 ("es","privacy"): ("Política de privacidad", f'''<p>Última actualización: 16 de noviembre de 2026</p>
<h2>1. Responsable del tratamiento</h2>{TITULAR_ES}
<h2>2. Qué datos tratamos y para qué</h2><p><strong>Formulario de contratación.</strong> Nombre y apellidos, entidad, correo electrónico, teléfono (opcional), tipo de actuación, fecha y lugar previstos, aforo, mensaje e idioma de la página. La finalidad es atender tu solicitud y enviarte una propuesta.</p><p><strong>Correo electrónico o WhatsApp.</strong> Nombre, dirección o teléfono y el contenido de tu mensaje, para responder a tu consulta.</p><p>No elaboramos perfiles ni tomamos decisiones automatizadas, y no te suscribimos a ningún boletín.</p>
<h2>3. Base jurídica</h2><p>Tu consentimiento (art. 6.1.a RGPD), que prestas al marcar la casilla del formulario o al escribirnos, y la aplicación de medidas precontractuales a petición tuya (art. 6.1.b RGPD). Puedes retirar el consentimiento en cualquier momento.</p>
<h2>4. Destinatarios y transferencias internacionales</h2><p>No cedemos tus datos a terceros salvo obligación legal. Nos apoyamos en proveedores que actúan como encargados del tratamiento: <strong>Netlify, Inc.</strong> (Estados Unidos), alojamiento de la web y recepción de los formularios; <strong>Google Ireland Limited</strong>, servicio de correo. Si decides escribirnos por WhatsApp o visitar Instagram o Facebook, se aplica la política de <strong>Meta Platforms Ireland Ltd.</strong>; si reproduces un vídeo, la de <strong>Google (YouTube)</strong>. Las transferencias a Estados Unidos se amparan en las cláusulas contractuales tipo de la Comisión Europea o en el Marco de Privacidad de Datos UE-EE. UU.</p>
<h2>5. Vídeos de YouTube y cookies</h2><p>Esta web no usa cookies propias ni herramientas de análisis. Los vídeos se muestran como imagen y el reproductor de YouTube (dominio youtube-nocookie.com) solo se carga cuando pulsas «play»; a partir de ese momento, YouTube puede tratar datos según su propia política.</p>
<h2>6. Plazo de conservación</h2><p>Mientras se gestiona tu solicitud y, después, bloqueados durante los plazos de prescripción legal.</p>
<h2>7. Tus derechos</h2><p>Puedes ejercer los derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. Si consideras que no se han respetado, puedes reclamar ante la Agencia Española de Protección de Datos (www.aepd.es).</p>'''),
 ("eu","legal"): ("Lege-oharra", f'''<p>Azken eguneratzea: 2026ko azaroaren 16a</p>
<h2>1. Datu identifikatzaileak</h2><p>Informazioaren Gizartearen Zerbitzuen eta Merkataritza Elektronikoaren 34/2002 Legearen (LSSI-CE) 10. artikulua betez, jakinarazten da webgune honen titularra hau dela:</p>{TITULAR_EU}
<h2>2. Xedea eta erabilera-baldintzak</h2><p>Webgune honek Kimu Txalaparta musika-proiektua aurkezten du eta hura kontratatzeko informazioa eskatzeko aukera ematen du. Webgunera sartzeak eta hura erabiltzeak erabiltzaile izaera ematen du eta lege-ohar hau onartzea dakar.</p>
<h2>3. Jabetza intelektuala eta industriala</h2><p>Webgune honetako testuak, argazkiak, bideoak, diseinua eta gainerako edukiak Kimu Txalapartarenak, Musubigara®-renak edo dagozkien egileenak dira, eta behar bezalako baimenarekin erabiltzen dira. Debekatuta dago horiek erreproduzitzea, banatzea, jendaurrean komunikatzea edo eraldatzea, berariazko baimen idatzirik gabe.</p>
<h2>4. Erantzukizuna</h2><p>Ahalegina egiten da informazioa zehatza eta eguneratua izan dadin, baina ez da bermatzen akatsik ez dagoenik edo webgunea etengabe erabilgarri dagoenik. Webguneak hirugarrenen guneetarako estekak ditu (YouTube, Instagram, Spotify, Facebook, WhatsApp), eta horien edukiaren gaineko erantzukizunik ez da hartzen.</p>
<h2>5. Datuen babesa eta cookieak</h2><p>Datu pertsonalen tratamendua <a href="/eu/pribatutasun-politika/">pribatutasun-politikak</a> arautzen du. Webgune honek ez du cookie propiorik ez analitikorik instalatzen.</p>
<h2>6. Legeria aplikagarria eta jurisdikzioa</h2><p>Lege-ohar hau Espainiako legeriak arautzen du. Edozein gatazkatarako, aldeak Vitoria-Gasteizko epaitegi eta auzitegien mende jartzen dira, kontsumitzaileen araudiak beste foru derrigorrezko bat ezartzen ez badu.</p>'''),
 ("eu","privacy"): ("Pribatutasun-politika", f'''<p>Azken eguneratzea: 2026ko azaroaren 16a</p>
<h2>1. Tratamenduaren arduraduna</h2>{TITULAR_EU}
<h2>2. Zer datu tratatzen ditugu eta zertarako</h2><p><strong>Kontratazio-formularioa.</strong> Izen-abizenak, erakundea, helbide elektronikoa, telefonoa (aukerakoa), emanaldi mota, aurreikusitako data eta lekua, edukiera, mezua eta orriaren hizkuntza. Helburua zure eskaerari erantzutea eta proposamen bat bidaltzea da.</p><p><strong>Posta elektronikoa edo WhatsApp.</strong> Izena, helbidea edo telefonoa eta zure mezuaren edukia, zure kontsultari erantzuteko.</p><p>Ez dugu profilik egiten ez erabaki automatizaturik hartzen, eta ez zaitugu inolako buletinetara harpidetzen.</p>
<h2>3. Oinarri juridikoa</h2><p>Zure baimena (DBEO 6.1.a art.), formularioko laukia markatzean edo guri idaztean ematen duzuna, eta zuk eskatuta kontratu aurreko neurriak aplikatzea (DBEO 6.1.b art.). Baimena edozein unetan erretira dezakezu.</p>
<h2>4. Hartzaileak eta nazioarteko transferentziak</h2><p>Ez diegu zure datuak hirugarrenei lagatzen, legezko betebeharrik ez badago. Tratamendu-eragile gisa jarduten duten hornitzaileez baliatzen gara: <strong>Netlify, Inc.</strong> (Ameriketako Estatu Batuak), webgunearen ostatua eta formularioen jasoera; <strong>Google Ireland Limited</strong>, posta-zerbitzua. WhatsAppez idaztea edo Instagram edo Facebook bisitatzea erabakitzen baduzu, <strong>Meta Platforms Ireland Ltd.</strong>-en politika aplikatzen da; bideo bat erreproduzitzen baduzu, <strong>Googlerena (YouTube)</strong>. AEBetarako transferentziak Europako Batzordearen kontratu-klausula tipoetan edo EB-AEB Datuen Pribatutasun Esparruan oinarritzen dira.</p>
<h2>5. YouTube bideoak eta cookieak</h2><p>Webgune honek ez du cookie propiorik ez analisi-tresnarik erabiltzen. Bideoak irudi gisa erakusten dira, eta YouTuberen erreproduzigailua (youtube-nocookie.com domeinua) «play» sakatzen duzunean bakarrik kargatzen da; une horretatik aurrera, YouTubek bere politikaren arabera trata ditzake datuak.</p>
<h2>6. Kontserbazio-epea</h2><p>Zure eskaera kudeatzen den bitartean eta, ondoren, blokeatuta, legezko preskripzio-epeetan.</p>
<h2>7. Zure eskubideak</h2><p>Sarbide, zuzenketa, ezabaketa, aurkaratze, mugatze eta eramangarritasun eskubideak erabil ditzakezu <a href="mailto:{EMAIL}">{EMAIL}</a> helbidera idatziz. Errespetatu ez direla uste baduzu, Datuak Babesteko Espainiako Bulegoan (www.aepd.es) erreklama dezakezu.</p>'''),
}

# ── Inmersión Kultural (pestaña propia) ──────────────────────────
INMERSION_PATH = {"es": "/inmersion-kultural-txalaparta-euskadi/", "eu": "/eu/murgiltze-kulturala-txalaparta-euskadin/"}

INMERSION = {
 ("es","title"): "Inmersión Kultural: txalaparta y cata en Euskadi | Kimu Txalaparta",
 ("es","desc"): "Concierto inmersivo de txalaparta con cata de sidra, txakoli o vino de Rioja Alavesa en sagardotegis, txokos y enclaves emblemáticos de Euskadi.",
 ("es","h1"): "Inmersión Kultural con Kimu Txalaparta: música ancestral y gastronomía vasca en una experiencia única",
 ("es","more"): "Descubre la experiencia",
 ("es","body"): f'''<p>Kimu Txalaparta propone una experiencia de inmersión cultural en Euskadi que une dos de los grandes patrimonios del País Vasco: la txalaparta, uno de sus instrumentos de percusión más antiguos y singulares, y una gastronomía reconocida internacionalmente. En un único formato, el visitante asiste a un concierto inmersivo en directo y participa en una cata de producto local, en enclaves emblemáticos de la geografía vasca.</p>
<h2>Una experiencia, dos patrimonios</h2>
<p>La Inmersión Kultural es una propuesta de turismo experiencial de entre 45 y 60 minutos de duración, concebida para que el público no solo escuche la txalaparta, sino que la viva de cerca: su ritmo, el diálogo entre sus intérpretes y su vínculo histórico con la cultura del caserío y de la sidra/vino. La actuación se acompaña de una cata de bebida autóctona, creando una sinergia singular entre la tradición musical y la tradición —e innovación— culinaria vasca.</p>
<h2>Escenarios emblemáticos de Euskadi</h2>
<p>La experiencia se celebra en lugares con identidad propia, seleccionados para reforzar la autenticidad del encuentro:</p>
<ul><li>Sagardotegis (sidrerías tradicionales).</li><li>Restaurantes de cocina tradicional vasca.</li><li>Txokos (sociedades gastronómicas).</li><li>Museos y espacios culturales.</li><li>Otros enclaves de interés turístico y patrimonial.</li></ul>
<h2>Maridaje con producto de la tierra</h2>
<p>Durante el concierto, el público disfruta de una cata adaptada al territorio en el que se desarrolla la experiencia:</p>
<ul><li><strong>Sagardoa (sidra natural vasca):</strong> emblema de la cultura de la sagardotegi y compañera histórica de la txalaparta.</li><li><strong>Txakoli:</strong> en Bizkaia y Gipuzkoa, el vino blanco joven, fresco y atlántico de la costa vasca.</li><li><strong>Vino de Rioja Alavesa:</strong> en las experiencias celebradas en Araba, tierra de bodegas y viñedo con tradición centenaria.</li></ul>
<p>Así, cada sesión se convierte en un viaje sensorial por el territorio: el sonido de la madera y el sabor del producto local se funden en un mismo relato.</p>
<h2>¿A quién va dirigida?</h2>
<p>La Inmersión Kultural está diseñada para un público que busca experiencias auténticas y de calidad:</p>
<ul><li>Turismo nacional e internacional que desea descubrir la cultura vasca más allá de lo convencional.</li><li>Visitantes que no conocen la txalaparta y quieren vivir un primer contacto memorable con ella.</li><li>Amantes de la gastronomía y del enoturismo interesados en el producto local de calidad.</li><li>Agencias de viaje, turoperadores, organizadores de eventos y empresas que buscan actividades diferenciales para grupos e incentivos.</li></ul>
<h2>Formato de la experiencia</h2>
<ul><li><strong>Duración:</strong> 45-60 minutos.</li><li><strong>Contenido:</strong> concierto inmersivo de txalaparta en directo y cata de bebida autóctona.</li><li><strong>Ubicación:</strong> espacios emblemáticos de Euskadi (sagardotegis, restaurantes tradicionales, txokos, museos y otros enclaves turísticos).</li><li><strong>Producto de la cata:</strong> sidra, txakoli o vino de Rioja Alavesa, según el territorio.</li></ul>
<h2>Por qué vivir la Inmersión Kultural</h2>
<p>Porque condensa en una sola experiencia dos de los grandes referentes que Euskadi ofrece al mundo: su patrimonio musical inmaterial y su cultura gastronómica. Una propuesta auténtica, cercana y diferente, que sitúa al visitante en el corazón de la identidad vasca, refuerza el atractivo turístico del territorio y convierte cada viaje en un recuerdo difícil de olvidar.</p>
<p>¿Quieres incorporar la Inmersión Kultural a tu programa, evento o establecimiento? Ponte en contacto con Kimu Txalaparta y diseñaremos contigo la experiencia.</p>
<p style="margin-top:28px"><a class="btn" href="/#contacto">Contratar {ICON["arrow"]}</a></p>''',
 ("eu","title"): "Murgiltze Kulturala: txalaparta eta dastaketa Euskadin | Kimu Txalaparta",
 ("eu","desc"): "Zuzeneko txalaparta-kontzertu murgiltzailea, sagardo, txakolin edo Arabako Errioxako ardo dastaketarekin, Euskadiko sagardotegi, txoko eta gune enblematikoetan.",
 ("eu","h1"): "Murgiltze Kulturala Kimu Txalapartarekin: antzinako musika eta euskal gastronomia esperientzia bakar batean",
 ("eu","more"): "Ezagutu esperientzia",
 ("eu","body"): f'''<p>Kimu Txalapartak Euskadin murgiltze kulturaleko esperientzia bat proposatzen du, Euskal Herriko bi ondare handi batzen dituena: txalaparta, perkusio-tresnarik zaharren eta berezienetako bat, eta nazioartean aitortutako gastronomia bat. Formatu bakar batean, bisitariak zuzeneko kontzertu murgiltzaile bat ikusten du eta bertako produktu baten dastaketan parte hartzen du, euskal geografiako gune enblematikoetan.</p>
<h2>Esperientzia bat, bi ondare</h2>
<p>Murgiltze Kulturala 45 eta 60 minutu arteko iraupena duen turismo esperientzialeko proposamen bat da, publikoak txalaparta entzun ez ezik, hurbiletik bizi dezan pentsatua: erritmoa, jotzaileen arteko elkarrizketa eta baserriko zein sagardoaren/ardoaren kulturarekin duen lotura historikoa. Emanaldia bertako edari baten dastaketarekin osatzen da, tradizio musikalaren eta euskal sukaldaritza-tradizioaren —eta berrikuntzaren— artean sinergia berezia sortuz.</p>
<h2>Euskadiko gune enblematikoak</h2>
<p>Esperientzia nortasun propioa duten lekuetan egiten da, topaketaren autentikotasuna indartzeko aukeratuak:</p>
<ul><li>Sagardotegiak (sagardotegi tradizionalak).</li><li>Euskal sukaldaritza tradizionaleko jatetxeak.</li><li>Txokoak.</li><li>Museoak eta kultur guneak.</li><li>Turismo- eta ondare-interesa duten beste gune batzuk.</li></ul>
<h2>Bertako produktuarekin maridaia</h2>
<p>Kontzertuan zehar, publikoak esperientzia garatzen den lurraldera egokitutako dastaketa bat gozatzen du:</p>
<ul><li><strong>Sagardoa (euskal sagardo naturala):</strong> sagardotegiaren kulturaren ikurra eta txalapartaren bidelagun historikoa.</li><li><strong>Txakolina:</strong> Bizkaian eta Gipuzkoan, euskal kostaldeko ardo zuri gaztea, freskoa eta atlantikoa.</li><li><strong>Arabako Errioxako ardoa:</strong> Araban egindako esperientzietan, upategi eta mahastien mendeetako tradizioa duen lurraldean.</li></ul>
<p>Horrela, saio bakoitza lurraldean zeharreko bidaia sentsorial bihurtzen da: zurezko soinua eta bertako produktuaren zaporea narrazio bakar batean batzen dira.</p>
<h2>Nori zuzenduta dago?</h2>
<p>Murgiltze Kulturala esperientzia autentiko eta kalitatezkoen bila dabilen publikoarentzat diseinatuta dago:</p>
<ul><li>Euskal kultura ohikoa baino harago ezagutu nahi duen barne- eta nazioarteko turismoa.</li><li>Txalaparta ezagutzen ez duten eta harekin lehen kontaktu gogoangarri bat bizi nahi duten bisitariak.</li><li>Bertako produktu kalitatezkoaren eta enoturismoaren zaleak.</li><li>Talde eta pizgarrietarako jarduera bereizgarriak bilatzen dituzten bidaia-agentziak, turoperadoreak, ekitaldi-antolatzaileak eta enpresak.</li></ul>
<h2>Esperientziaren formatua</h2>
<ul><li><strong>Iraupena:</strong> 45-60 minutu.</li><li><strong>Edukia:</strong> zuzeneko txalaparta-kontzertu murgiltzailea eta bertako edariaren dastaketa.</li><li><strong>Kokapena:</strong> Euskadiko gune enblematikoak (sagardotegiak, jatetxe tradizionalak, txokoak, museoak eta beste turismo-gune batzuk).</li><li><strong>Dastatutako produktua:</strong> sagardoa, txakolina edo Arabako Errioxako ardoa, lurraldearen arabera.</li></ul>
<h2>Zergatik bizi Murgiltze Kulturala</h2>
<p>Euskadik munduari eskaintzen dizkion bi erreferente handi esperientzia bakar batean biltzen dituelako: bere ondare musikal immateriala eta bere kultura gastronomikoa. Proposamen autentiko, hurbil eta ezberdina, bisitaria euskal identitatearen bihotzean jartzen duena, lurraldearen erakargarritasun turistikoa indartzen duena eta bidaia bakoitza ahazteko zaila den oroitzapen bihurtzen duena.</p>
<p>Murgiltze Kulturala zure programan, ekitaldian edo establezimenduan txertatu nahi duzu? Jarri harremanetan Kimu Txalapartarekin eta elkarrekin diseinatuko dugu esperientzia.</p>
<p style="margin-top:28px"><a class="btn" href="/eu/#contacto">Kontratatu {ICON["arrow"]}</a></p>''',
}

def inmersion_page(lang):
    t = T[lang]
    es_p, eu_p = INMERSION_PATH["es"], INMERSION_PATH["eu"]
    path = INMERSION_PATH[lang]
    title = INMERSION[(lang,"title")]
    desc = INMERSION[(lang,"desc")]
    h1 = INMERSION[(lang,"h1")]
    body = INMERSION[(lang,"body")]
    home_p = t["path"]
    out = [head(t, title, desc, path, es_p, eu_p), "<body>",
           topbar(t, home_p, es_p, eu_p, home_p),
           f'<main id="main" class="legal"><h1>{e(h1)}</h1>{body}<p style="margin-top:40px"><a class="btn ghost" href="{home_p}">{t["back"]}</a></p></main>',
           footer(t)]
    return "\n".join(out)

def simple_page(lang, title, body, path, alt_es, alt_eu, noindex=False):
    t = T[lang]
    home_p = t["path"]
    out = [head(t, f"{title} · Kimu Txalaparta", t["desc"], path, alt_es, alt_eu, noindex=noindex), "<body>",
           topbar(t, home_p, alt_es, alt_eu, home_p),
           f'<main id="main" class="legal"><h1>{e(title)}</h1>{body}<p style="margin-top:40px"><a class="btn" href="{home_p}">{t["back"]}</a></p></main>',
           footer(t)]
    return "\n".join(out)

def write(rel, content):
    p = PUB / rel.lstrip("/")
    if rel.endswith("/"):
        p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def main():
    write("/", home("es"))
    write("/eu/", home("eu"))
    write(INMERSION_PATH["es"], inmersion_page("es"))
    write(INMERSION_PATH["eu"], inmersion_page("eu"))
    pairs = {"legal": ("/aviso-legal/", "/eu/lege-oharra/"), "privacy": ("/privacidad/", "/eu/pribatutasun-politika/")}
    for kind,(pes,peu) in pairs.items():
        for lang, path in (("es",pes),("eu",peu)):
            title, body = LEGAL[(lang,kind)]
            write(path, simple_page(lang, title, body, path, pes, peu))
    for lang, path in (("es","/gracias/"),("eu","/eu/eskerrik-asko/")):
        t = T[lang]
        write(path, simple_page(lang, t["thanks_h"], f"<p>{e(t['thanks_p'])}</p>", path, "/gracias/", "/eu/eskerrik-asko/", noindex=True))
    t = T["es"]
    write("/404.html", simple_page("es", t["nf_h"], f"<p>{e(t['nf_p'])}</p><p lang=\"eu\">{e(T['eu']['nf_p'])}</p>", "/404.html", "/", "/eu/", noindex=True))
    # sitemap + robots
    urls = [("/","/eu/"),(INMERSION_PATH["es"],INMERSION_PATH["eu"]),("/aviso-legal/","/eu/lege-oharra/"),("/privacidad/","/eu/pribatutasun-politika/")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for es_u, eu_u in urls:
        for u in (es_u, eu_u):
            sm.append(f'<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod>'
                      f'<xhtml:link rel="alternate" hreflang="es" href="{BASE}{es_u}"/><xhtml:link rel="alternate" hreflang="eu" href="{BASE}{eu_u}"/>'
                      f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{es_u}"/></url>')
    sm.append("</urlset>")
    write("/sitemap.xml", "\n".join(sm))
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print("OK")

if __name__ == "__main__":
    main()
