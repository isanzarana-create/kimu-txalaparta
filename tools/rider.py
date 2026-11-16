#!/usr/bin/env python3
"""Genera los riders técnicos en PDF (ES y EU) en public/descargas/."""
import pathlib
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle

OUT = pathlib.Path(__file__).resolve().parent.parent / "public" / "descargas"
pdfmetrics.registerFont(TTFont("Sans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("SansB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))
BG, INK = HexColor("#D8D4CD"), HexColor("#0B0B0B")

TXT = {
 "es": {"t": "Rider técnico", "sub": "Txalaparta de madera y de piedra",
  "blocks": [
   ("01 · Formato acústico (hasta 100 personas)", "Formato previsto para el proyecto de inmersión cultural. La txalaparta de madera y la de piedra suenan con bastantes decibelios, por lo que en salas medianas con un aforo de menos de 100 personas no hace falta sonorizar."),
   ("02 · Formato sonorizado (más de 100 personas)", "En salas grandes o en exteriores (festivales, etc.), con un aforo por encima de 100 personas, conviene sonorizar."),
   ("Material de sonido", "• 6 micrófonos Shure SM57 (o equivalentes)<br/>• 6 pies de micro bajos (uno de ellos para presentar)<br/>• 2 monitores de escenario"),
   ("Escenario", "Superficie plana y estable para montar las dos txalapartas (madera y piedra). Medidas mínimas, tiempo de montaje y necesidades de luz: a confirmar con la organización."),
  ],
  "contact": "Gestión y contratación: Musubigara® · ignacio@musubigara.org · +34 620 463 558"},
 "eu": {"t": "Rider teknikoa", "sub": "Zurezko eta harrizko txalaparta",
  "blocks": [
   ("01 · Formatu akustikoa (100 pertsona arte)", "Murgiltze kulturaleko proiekturako aurreikusitako formatua. Zurezko eta harrizko txalapartek dezibelio dezente ematen dituzte; beraz, 100 pertsonatik beherako edukiera duten areto ertainetan ez da soinu-sistemarik behar."),
   ("02 · Formatu sonorizatua (100 pertsonatik gora)", "Areto handietan edo kanpoaldean (jaialdiak, etab.), 100 pertsonatik gorako edukierarekin, komeni da soinua jartzea."),
   ("Soinu-materiala", "• 6 Shure SM57 mikrofono (edo baliokideak)<br/>• 6 mikrofono-oin baxu (horietako bat aurkezteko)<br/>• 2 agertoki-monitore"),
   ("Agertokia", "Bi txalapartak (zurezkoa eta harrizkoa) muntatzeko gainazal laua eta egonkorra. Gutxieneko neurriak, muntaketa-denbora eta argi-beharrak: antolakuntzarekin baieztatzeko."),
  ],
  "contact": "Kudeaketa eta kontratazioa: Musubigara® · ignacio@musubigara.org · +34 620 463 558"},
}
for lang, d in TXT.items():
    W, H = A4
    c = canvas.Canvas(str(OUT / f"kimu-txalaparta-rider-{lang}.pdf"), pagesize=A4)
    c.setTitle(f"Kimu Txalaparta · {d['t']}"); c.setAuthor("Musubigara®")
    c.setFillColor(BG); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#B9B4AC")); c.setLineWidth(.4)
    for i in range(1, 9): c.line(W*i/9, 0, W*i/9, H)
    c.setFillColor(INK); c.setFont("Sans", 96); c.drawString(28, H-120, "KIMU")
    c.rect(300, H-120, 70, 9, fill=1, stroke=0)
    c.setFont("Mono", 11); c.drawString(380, H-112, "TXALAPARTA")
    c.setFont("SansB", 26); c.drawString(30, H-175, d["t"])
    c.setFont("Mono", 11); c.drawString(30, H-195, d["sub"].upper())
    h = ParagraphStyle("h", fontName="Mono", fontSize=10.5, leading=14, textColor=BG)
    b = ParagraphStyle("b", fontName="Sans", fontSize=11, leading=16, textColor=INK, spaceAfter=18)
    y = H - 230
    for title, body in d["blocks"]:
        c.setFillColor(INK); c.rect(30, y-20, W-60, 22, fill=1, stroke=0)
        c.setFillColor(BG); c.setFont("Mono", 10.5); c.drawString(38, y-13, title.upper())
        p = Paragraph(body, b); w, ph = p.wrap(W-76, 400)
        p.drawOn(c, 38, y-30-ph); y = y - 30 - ph - 26
    c.setFillColor(INK); c.setFont("Mono", 9); c.drawString(30, 40, d["contact"])
    c.showPage(); c.save()
print("ok")
