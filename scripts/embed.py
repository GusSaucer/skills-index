#!/usr/bin/env python3
"""Injeta docs/skills.json e docs/agentes.json dentro de docs/index.html.

A pagina nao faz fetch dos JSON de proposito: um fetch falharia ao abrir o
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
DOCS = RAIZ / "docs"
HTML_PATH = DOCS / "index.html"

INICIO = "<!-- DADOS:INICIO -->"
FIM = "<!-- DADOS:FIM -->"

# arquivo -> (chave da lista, campos obrigatorios, origens validas, usos validos)
FONTES = {
    "skills.json": (
        "skills",
        ("nome", "origem", "plugin", "comando", "grupo", "descricao", "quando"),
        {"conta", "nativa", "local", "marketplace"},
        None,
    ),
    "agentes.json": (
        "agentes",
        ("nome", "origem", "plugin", "grupo", "modelo", "uso", "descricao", "quando"),
        {"nativo", "marketplace", "projeto"},
        {"direto", "interno", "sessao"},
    ),
}


def carregar(arquivo):
    """Le e valida um dos JSON, devolvendo a lista de entradas."""
    chave, campos, origens, usos = FONTES[arquivo]
    caminho = DOCS / arquivo
    itens = json.loads(caminho.read_text(encoding="utf-8")).get(chave)
    if not isinstance(itens, list) or not itens:
        raise ValueError(f"{arquivo}: a chave '{chave}' deve ser uma lista nao vazia")

    for i, item in enumerate(itens):
        rotulo = f"{arquivo}: entrada {i} ({item.get('nome', '?')})"
        faltando = [c for c in campos if c not in item]
        if faltando:
            raise ValueError(f"{rotulo} sem os campos {faltando}")
        if item["origem"] not in origens:
            raise ValueError(f"{rotulo} tem origem invalida {item['origem']!r}")
        if usos is not None and item["uso"] not in usos:
            raise ValueError(f"{rotulo} tem uso invalido {item['uso']!r}")
    return chave, itens


def montar_bloco(dados):
    """Monta o trecho de HTML que vai entre os marcadores."""
    payload = json.dumps(dados, ensure_ascii=False, separators=(",", ":"))
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

    dados = {}
    for arquivo in FONTES:
        chave, itens = carregar(arquivo)
        dados[chave] = itens
    resumo = ", ".join(f"{len(v)} {k}" for k, v in dados.items())

    html = HTML_PATH.read_text(encoding="utf-8")
    de = html.find(INICIO)
    ate = html.find(FIM)
    if de == -1 or ate == -1 or ate < de:
        print(f"erro: marcadores {INICIO} / {FIM} nao encontrados em {HTML_PATH.name}")
        return 1

    novo = html[:de] + montar_bloco(dados) + html[ate + len(FIM):]

    if novo == html:
        print(f"ok: {HTML_PATH.name} sincronizado ({resumo})")
        return 0

    if args.check:
        print(f"fora de sincronia: os JSON mudaram sem rodar o build ({resumo}). Rode: python scripts/embed.py")
        return 1

    HTML_PATH.write_text(novo, encoding="utf-8")
    print(f"gravado: {HTML_PATH.name} com {resumo}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as e:
        print(f"erro: {e}")
        sys.exit(1)
