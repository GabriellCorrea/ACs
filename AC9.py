# DISTÂNCIA

distancia = int(input())

tempo = distancia * 2

print("{} minutos".format(tempo))

'========================================================================================'
# FATORIAL SIMPLES

valor = int(input())
fatorial = 1

for i in range(1, valor+1):
    fatorial *= i

print(fatorial)

'========================================================================================'
# IDA À FEIRA

produtos_disponiveis = {}
testes = int(input())

for _ in range(testes):
    produtos_a_venda = int(input())

    for _ in range(produtos_a_venda):
        vendas = input()
        produto1, preco = vendas.split()
        produto1 = str(produto1)
        preco = float(preco)
        produtos_disponiveis[produto1] = preco

    compras = int(input())

    preco_final = 0

    for _ in range(compras):
        compras = input()
        produto2, quantidade = compras.split()
        produto = str(produto2)
        quantidade = float(quantidade)

        if produto2 in produtos_disponiveis:
            preco = produtos_disponiveis[produto2]
            preco_final += preco * quantidade

    print("R$ {:.2f}".format(preco_final))

'========================================================================================'
# IDENTIFICANDO O CHÁ

resposta_certa = 0

cha_correto = int(input())

respostas = input()
A, B, C, D, E = map(int, respostas.split())

if A == cha_correto:
    resposta_certa += 1
if B == cha_correto:
    resposta_certa += 1
if C == cha_correto:
    resposta_certa += 1
if D == cha_correto:
    resposta_certa += 1
if E == cha_correto:
    resposta_certa += 1

print(resposta_certa)

'========================================================================================'
# AVIÕES DE PAPEL

while True:
    try:
        valores = input()
        C, P, F = map(int, valores.split())

        folhas_necessarias = C * F

        if folhas_necessarias <= P:
            print("S")
        else:
            print("N")

    except EOFError:
        break

'========================================================================================'
# TACÓGRAFO

testes = int(input())
distancia_total = 0

for i in range(testes):
    tempo = input()
    horas, velocidade = map(int, tempo.split())

    distancia = horas * velocidade
    distancia_total += distancia

print(distancia_total)

'========================================================================================'
# BUSCA NA INTERNET

while True:
    try:
       terceiro_link = int(input())

       primeiro_link = terceiro_link * 4

       print(primeiro_link)

    except EOFError:
        break

'========================================================================================'
# SEQUÊNCIA SECRETA

sequencia = int(input())
lista = []

for i in range(sequencia):
    valor = int(input())
    lista.append(valor)

max_num_lista = len(lista)
nova_lista = [lista[0]]

for i in range(1, max_num_lista):
    if lista[i] != lista[i - 1]:
        nova_lista.append(lista[i])

max_circulos = len(nova_lista)
print(max_circulos)