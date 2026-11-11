#!/usr/bin/env python3
"""Injeta docs/skills.json e docs/agentes.json dentro de docs/index.html.

O skills.json traz tambem as trilhas da curadoria, que vao juntas.

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

NIVEIS_VALIDOS = {"iniciante", "intermediario", "avancado"}

# arquivo -> (chave da lista, campos obrigatorios, origens validas, usos validos)
FONTES = {
    "skills.json": (
        "skills",
        ("nome", "origem", "plugin", "comando", "grupo", "descricao", "quando"),
        {"conta", "nativa", "local", "marketplace", "comunidade"},
        None,
    ),
    "agentes.json": (
        "agentes",
        ("nome", "origem", "plugin", "grupo", "modelo", "uso", "descricao", "quando"),
        {"nativo", "marketplace", "projeto"},
        {"direto", "interno", "sessao"},
    ),
}


def validar_curadoria(rotulo, item, trilhas):
    """Campos da curadoria: opcionais, mas validados quando aparecem."""
    for t in item.get("trilhas", []):
        if t not in trilhas:
            raise ValueError(f"{rotulo} cita a trilha {t!r}, que nao existe")
    if "nivel" in item and item["nivel"] not in NIVEIS_VALIDOS:
        raise ValueError(f"{rotulo} tem nivel invalido {item['nivel']!r}")
    if item.get("trilhas") and not item.get("brilho"):
        raise ValueError(f"{rotulo} esta numa trilha mas nao tem 'brilho'")
    if "instalar" in item and not (
        isinstance(item["instalar"], list) and all(isinstance(c, str) and c for c in item["instalar"])
    ):
        raise ValueError(f"{rotulo}: 'instalar' deve ser lista de comandos")
    if item.get("fonte") and not item["fonte"].startswith("https://"):
        raise ValueError(f"{rotulo}: 'fonte' deve ser https")


def carregar(arquivo):
    """Le e valida um dos JSON, devolvendo a lista de entradas e as trilhas."""
    chave, campos, origens, usos = FONTES[arquivo]
    caminho = DOCS / arquivo
    bruto = json.loads(caminho.read_text(encoding="utf-8"))
    itens = bruto.get(chave)
    trilhas = bruto.get("trilhas") or {}
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
        validar_curadoria(rotulo, item, trilhas)

    for tid, t in trilhas.items():
        nomes = {i["nome"] for i in itens if tid in i.get("trilhas", [])}
        fora = [n for n in t.get("ordem", []) if n not in nomes]
        if fora:
            raise ValueError(f"{arquivo}: a ordem da trilha {tid!r} cita itens fora dela: {fora}")
    return chave, itens, trilhas


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
        chave, itens, trilhas = carregar(arquivo)
        dados[chave] = itens
        if trilhas:
            dados.setdefault("trilhas", {}).update(trilhas)
    resumo = ", ".join(f"{len(v)} {k}" for k, v in dados.items() if k != "trilhas")

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
