#!/usr/bin/env python3
"""Gera docs/og.png (1200x630), a imagem de previa para LinkedIn/WhatsApp.

Os numeros saem de docs/skills.json; rode de novo quando o catalogo mudar.
Requer Pillow e as fontes DejaVu (padrao no Linux).

Uso:
    python scripts/og.py
"""

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
JSON_PATH = RAIZ / "docs" / "skills.json"
SAIDA = RAIZ / "docs" / "og.png"
FONTES = Path("/usr/share/fonts/truetype/dejavu")

BG = "#050505"
PONTO = "#1a1a1a"
TEXTO = "#ededec"
DIM = "#a3a3a0"
BORDA = "#2a2a2a"
SUPERFICIE = "#0d0d0d"
# Uma cor por trilha, na mesma ordem da pagina.
TRILHAS = (("alunos", "#22c55e"), ("arquiteto", "#00d9ff"), ("presenca", "#f472b6"))


def fonte(nome, tamanho):
    return ImageFont.truetype(str(FONTES / nome), tamanho)


def main():
    dados = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    skills = dados["skills"]
    curadas = sum(1 for s in skills if s.get("trilhas"))

    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)

    # Grade de pontos, como no topo da pagina.
    for y in range(11, 630, 22):
        for x in range(11, 1200, 22):
            d.point((x, y), fill=PONTO)

    d.text((80, 70), "CLAUDE CODE · CURADORIA", font=fonte("DejaVuSansMono.ttf", 24), fill="#f472b6")
    titulo = fonte("DejaVuSans-Bold.ttf", 76)
    d.text((80, 112), "Superpoderes para", font=titulo, fill=TEXTO)
    d.text((80, 200), "o seu Claude Code.", font=titulo, fill=TEXTO)
    corpo = fonte("DejaVuSans.ttf", 30)
    d.text((80, 310), f"{curadas} skills e agentes escolhidos a dedo, com o", font=corpo, fill=DIM)
    d.text((80, 352), "comando para instalar e a hora certa de usar.", font=corpo, fill=DIM)

    # As tres trilhas como cartoes.
    mono = fonte("DejaVuSansMono-Bold.ttf", 22)
    x = 80
    for tid, cor in TRILHAS:
        t = dados["trilhas"][tid]
        n = sum(1 for s in skills if tid in s.get("trilhas", []))
        d.rounded_rectangle([x, 430, x + 330, 530], radius=14, fill=SUPERFICIE, outline=cor, width=2)
        d.text((x + 20, 446), f"{n} ITENS", font=mono, fill=cor)
        d.text((x + 20, 480), t["titulo"], font=fonte("DejaVuSans-Bold.ttf", 23), fill=TEXTO)
        x += 355

    d.line([80, 565, 1120, 565], fill=BORDA, width=2)
    d.text((80, 578), "skills.gustavopires.dev", font=fonte("DejaVuSansMono.ttf", 24), fill="#22c55e")

    img.save(SAIDA, optimize=True)
    print(f"gerado {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
