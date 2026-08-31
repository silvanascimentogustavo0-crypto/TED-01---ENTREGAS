import csv
import os

# Localiza o CSV pela estrutura do projeto.
PASTA_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO = os.path.join(PASTA_PROJETO, "dados", "entregas.csv")

# Integrantes: Kauê Lima Oliveira e Gustavo Silva do Nascimento
# Cenário: 11 - Entregas

def ler_dados():
    entregas = []

    with open(ARQUIVO, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha["distancia_km"] = int(linha["distancia_km"])
            entregas.append(linha)

    return entregas


def remover_duplicados(entregas):
    vistos = set()
    resultado = []

    for entrega in entregas:
        # A tupla representa uma entrega para facilitar a comparação.
        registro = (
            entrega["id_entrega"],
            entrega["cidade"],
            entrega["entregador"],
            entrega["regiao"],
            entrega["distancia_km"],
            entrega["status"]
        )

        if registro not in vistos:
            vistos.add(registro)
            resultado.append(entrega)

    return resultado


def contar(entregas, campo):
    resultado = {}

    for entrega in entregas:
        valor = entrega[campo]

        if valor not in resultado:
            resultado[valor] = 0

        resultado[valor] += 1

    return resultado


def mostrar_maiores(contagem):
    maior = max(contagem.values())
    return [(nome, qtd) for nome, qtd in contagem.items() if qtd == maior]


def comparar_regioes(entregas):
    # List Comprehensions para separar os status.
    concluidas = [e for e in entregas if e["status"] == "Entregue"]
    atrasadas = [e for e in entregas if e["status"] == "Atrasado"]

    regioes_concluidas = {e["regiao"] for e in concluidas}
    regioes_atrasadas = {e["regiao"] for e in atrasadas}

    em_comum = regioes_concluidas & regioes_atrasadas
    somente_concluidas = regioes_concluidas - regioes_atrasadas
    somente_atrasadas = regioes_atrasadas - regioes_concluidas

    return em_comum, somente_concluidas, somente_atrasadas


def organizar_por_regiao(entregas):
    # Dicionário dentro de dicionário: regiao -> cidade -> quantidade.
    dados = {}

    for entrega in entregas:
        regiao = entrega["regiao"]
        cidade = entrega["cidade"]

        if regiao not in dados:
            dados[regiao] = {}

        if cidade not in dados[regiao]:
            dados[regiao][cidade] = 0

        dados[regiao][cidade] += 1

    return dados


def imprimir_tabela(titulo, dados):
    print("\n" + titulo)
    print("-" * len(titulo))

    for nome, qtd in sorted(dados.items(), key=lambda item: (-item[1], item[0])):
        print(f"{nome:<35} {qtd}")


def main():
    dados_originais = ler_dados()
    entregas = remover_duplicados(dados_originais)

    print("=" * 55)
    print("TED 01 - CENARIO 11: ENTREGAS")
    print("=" * 55)
    print("Registros lidos:", len(dados_originais))
    print("Registros sem repeticao:", len(entregas))
    print("Duplicados retirados:", len(dados_originais) - len(entregas))

    # 1. Regioes e cidades
    por_regiao = contar(entregas, "regiao")
    por_cidade = contar(entregas, "cidade")

    imprimir_tabela("1 - ENTREGAS POR REGIAO", por_regiao)
    print("Maior volume:", mostrar_maiores(por_regiao))

    imprimir_tabela("2 - ENTREGAS POR CIDADE", por_cidade)
    print("Maior volume:", mostrar_maiores(por_cidade))

    # 2. Entregadores e atrasos
    por_entregador = contar(entregas, "entregador")
    atrasadas = [e for e in entregas if e["status"] == "Atrasado"]
    por_atraso = contar(atrasadas, "entregador")

    imprimir_tabela("3 - ENTREGAS POR ENTREGADOR", por_entregador)
    print("Maior numero de entregas:", mostrar_maiores(por_entregador))

    imprimir_tabela("4 - ATRASOS POR ENTREGADOR", por_atraso)
    print("Mais atrasos:", mostrar_maiores(por_atraso))

    # 3. Comparacao com sets
    em_comum, somente_concluidas, somente_atrasadas = comparar_regioes(entregas)

    print("\n5 - COMPARACAO DAS REGIOES")
    print("-" * 30)
    print("Em comum:", sorted(em_comum))
    print("Somente concluidas:", sorted(somente_concluidas))
    print("Somente atrasadas:", sorted(somente_atrasadas))

    # 4. Distancias
    nao_canceladas = [e for e in entregas if e["status"] != "Cancelado"]
    total_km = sum(e["distancia_km"] for e in nao_canceladas)
    media_km = total_km / len(nao_canceladas)

    print("\n6 - DISTANCIAS")
    print("-" * 30)
    print("Distancia total:", total_km, "km")
    print("Distancia media:", round(media_km, 2), "km")

    # Dict Comprehension para criar um resumo dos status.
    contagem_status = contar(entregas, "status")
    resumo_status = {
        status: quantidade
        for status, quantidade in contagem_status.items()
        if quantidade > 0
    }

    print("\n7 - RESUMO DOS STATUS")
    print("-" * 30)
    for status, quantidade in resumo_status.items():
        print(status, ":", quantidade)

    # Estrutura aninhada
    organizacao = organizar_por_regiao(entregas)

    print("\n8 - CIDADES DENTRO DE CADA REGIAO")
    print("-" * 40)

    for regiao in sorted(organizacao):
        print(regiao, ":", organizacao[regiao])


if __name__ == "__main__":
    main()
