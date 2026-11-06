#!/usr/bin/env python3
"""Injeta docs/skills.json dentro de docs/index.html.

A pagina nao faz fetch do JSON de proposito: um fetch falharia ao abrir o
index.html como arquivo local, porque o navegador bloqueia requisicao em
file://. Os dados ficam embutidos entre dois marcadores no HTML, e este
script e o unico lugar que reescreve esse trecho.

Uso:
    python scripts/embed.py            # injeta
    python scripts/embed.py --check    # so verifica se esta sincronizado
"""

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_PATH = RAIZ / "docs" / "skills.json"
HTML_PATH = RAIZ / "docs" / "index.html"

INICIO = "<!-- DADOS:INICIO -->"
FIM = "<!-- DADOS:FIM -->"

CAMPOS = ("nome", "origem", "plugin", "comando", "grupo", "descricao", "quando")
ORIGENS_VALIDAS = {"conta", "nativa", "local", "marketplace"}


def carregar_skills():
    """Le e valida o JSON, devolvendo a lista de skills."""
    dados = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    skills = dados.get("skills")
    if not isinstance(skills, list) or not skills:
        raise ValueError("skills.json: a chave 'skills' deve ser uma lista nao vazia")

    for i, s in enumerate(skills):
        faltando = [c for c in CAMPOS if c not in s]
        if faltando:
            raise ValueError(
                f"skills.json: entrada {i} ({s.get('nome', '?')}) sem os campos {faltando}"
            )
        if s["origem"] not in ORIGENS_VALIDAS:
            raise ValueError(
                f"skills.json: entrada {i} ({s['nome']}) tem origem invalida {s['origem']!r}"
            )
    return skills


def montar_bloco(skills):
    """Monta o trecho de HTML que vai entre os marcadores."""
    payload = json.dumps({"skills": skills}, ensure_ascii=False, separators=(",", ":"))
    # Um "</" literal encerraria o <script> antes da hora.
    payload = payload.replace("</", "<\\/")
    return (
        f'{INICIO}\n<script type="application/json" id="dados">\n'
        f"{payload}\n</script>\n{FIM}"
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="nao escreve nada; sai com 1 se o HTML estiver fora de sincronia",
    )
    args = ap.parse_args()

    skills = carregar_skills()
    html = HTML_PATH.read_text(encoding="utf-8")

    de = html.find(INICIO)
    ate = html.find(FIM)
    if de == -1 or ate == -1 or ate < de:
        print(f"erro: marcadores {INICIO} / {FIM} nao encontrados em {HTML_PATH.name}")
        return 1

    novo = html[:de] + montar_bloco(skills) + html[ate + len(FIM):]

    if novo == html:
        print(f"ok: {HTML_PATH.name} sincronizado ({len(skills)} skills)")
        return 0

    if args.check:
        print(
            f"fora de sincronia: {JSON_PATH.name} mudou sem rodar o build "
            f"({len(skills)} skills no JSON). Rode: python scripts/embed.py"
        )
        return 1

    HTML_PATH.write_text(novo, encoding="utf-8")
    print(f"gravado: {HTML_PATH.name} com {len(skills)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
