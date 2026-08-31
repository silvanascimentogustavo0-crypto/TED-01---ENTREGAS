# TED 01 - Cenario 11: Entregas

## Integrantes

- Kaue Lima Oliveira
- Gustavo Silva do Nascimento

## Cenario

**11 - Entregas**

## Sobre o trabalho

Neste trabalho foi feito um programa em Python para analisar os dados de entregas do arquivo CSV.

Primeiro os dados sao lidos e os registros repetidos sao retirados. Depois sao feitas algumas consultas sobre regioes, cidades, entregadores, atrasos e distancia das entregas.

A ideia foi usar as colecoes que foram estudadas na disciplina, sem usar bibliotecas externas.

## Estruturas usadas

- **Lista:** guarda todas as entregas que foram lidas do arquivo.
- **Tupla:** usada para representar os dados de uma entrega na hora de procurar registros repetidos.
- **Dicionario:** usado para contar entregas por regiao, cidade, entregador e status.
- **Dicionario aninhado:** organiza as cidades dentro de cada regiao.
- **Set:** usado para verificar os registros repetidos e tambem para comparar as regioes.

## Comprehensions

Foram usadas List Comprehensions para filtrar as entregas atrasadas, concluidas e as que nao foram canceladas.

Tambem foi usada uma Dict Comprehension para montar o resumo dos status:

```python
resumo_status = {
    status: quantidade
    for status, quantidade in contagem_status.items()
    if quantidade > 0
}
```

## Sets

Os sets foram usados para evitar que uma entrega repetida fosse adicionada novamente.

Tambem foram usados para comparar as regioes:

- `&` para encontrar as regioes em comum;
- `-` para encontrar as regioes exclusivas.

## Funcoes

As principais funcoes criadas foram:

1. `ler_dados()` - le o arquivo CSV.
2. `remover_duplicados()` - tira os registros repetidos.
3. `contar()` - faz as contagens.
4. `mostrar_maiores()` - mostra os maiores valores.
5. `comparar_regioes()` - compara as regioes usando sets.
6. `organizar_por_regiao()` - cria o dicionario aninhado.
7. `imprimir_tabela()` - organiza a apresentacao no terminal.
8. `main()` - junta as partes do programa.

## Analises realizadas

O programa faz as seguintes analises:

1. Quantidade de entregas por regiao.
2. Quantidade de entregas por cidade.
3. Entregadores com maior numero de entregas.
4. Entregadores com maior numero de atrasos.
5. Comparacao entre regioes com entregas concluidas e atrasadas.
6. Distancia total e distancia media das entregas que nao foram canceladas.
7. Quantidade de entregas por status.
8. Organizacao das cidades por regiao.

## Como executar

Dentro da pasta do projeto, execute:

```bash
python src/main.py
```

O programa usa somente a biblioteca `csv`, que ja faz parte do Python.

## Dados

O arquivo `dados/entregas.csv` foi mantido como foi recebido. O programa apenas le os dados e faz o processamento em memoria.

## Observacao

Os resultados podem ser conferidos executando o programa novamente. O arquivo CSV original nao e alterado.
