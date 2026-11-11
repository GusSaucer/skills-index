#!/usr/bin/env python3
"""Gera docs/og.png (1200x630), a imagem de previa para LinkedIn/WhatsApp.

Os numeros saem de docs/skills.json; rode de novo quando o catalogo mudar.
Requer Pillow e as fontes DejaVu (padrao no Linux).

Uso:
    python scripts/og.py
"""

import json
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
JSON_PATH = RAIZ / "docs" / "skills.json"
SAIDA = RAIZ / "docs" / "og.png"
FONTES = Path("/usr/share/fonts/truetype/dejavu")

BG = "#fbfaf9"
TEXTO = "#1d1b19"
DIM = "#5f5a54"
ACCENT = "#b1511c"
BORDA = "#e2ded8"
CORES = {"conta": "#2d6a4f", "nativa": "#1f5a8f", "local": "#7b3f9d", "marketplace": "#8a6513"}


def fonte(nome, tamanho):
    return ImageFont.truetype(str(FONTES / nome), tamanho)


def main():
    skills = json.loads(JSON_PATH.read_text(encoding="utf-8"))["skills"]
    por_origem = Counter(s["origem"] for s in skills)
    ativas = len(skills) - por_origem["marketplace"]

    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1200, 10], fill=ACCENT)

    d.text((80, 90), "CLAUDE CODE", font=fonte("DejaVuSansMono-Bold.ttf", 28), fill=ACCENT)
    d.text((80, 140), "Índice de Skills", font=fonte("DejaVuSerif-Bold.ttf", 92), fill=TEXTO)
    corpo = fonte("DejaVuSans.ttf", 34)
    d.text((80, 270), "O que cada skill faz e quando ela entra em ação,", font=corpo, fill=DIM)
    d.text((80, 318), "num catálogo com busca.", font=corpo, fill=DIM)

    # Barra proporcional por origem.
    x, y, largura = 80, 420, 1040
    for origem in ("conta", "nativa", "local", "marketplace"):
        n = por_origem.get(origem, 0)
        if not n:
            continue
        w = round(largura * n / len(skills))
        d.rectangle([x, y, x + w - 4, y + 22], fill=CORES[origem])
        x += w

    mono = fonte("DejaVuSansMono.ttf", 28)
    d.text((80, 470), f"{ativas} ativas  ·  {por_origem['marketplace']} no marketplace", font=mono, fill=TEXTO)
    d.line([80, 540, 1120, 540], fill=BORDA, width=2)
    d.text((80, 558), "skills.gustavopires.dev", font=mono, fill=ACCENT)

    img.save(SAIDA, optimize=True)
    print(f"gerado {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
