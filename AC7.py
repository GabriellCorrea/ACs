# AUMENTO DE SALÁRIO

salario = float(input())

if salario >= 0 and salario <= 400:
    novo_salario = salario * 15 / 100 + salario
    reajuste_ganho = salario * 15 / 100
    print("Novo salario: {:.2f}".format(novo_salario))
    print("Reajuste ganho: {:.2f}".format(reajuste_ganho))
    print("Em percentual: 15 %")

if salario > 400 and salario <= 800:
    novo_salario = salario * 12 / 100 + salario
    reajuste_ganho = salario * 12 / 100
    print("Novo salario: {:.2f}".format(novo_salario))
    print("Reajuste ganho: {:.2f}".format(reajuste_ganho))
    print("Em percentual: 12 %")

if salario > 800 and salario <= 1200:
    novo_salario = salario * 10 / 100 + salario
    reajuste_ganho = salario * 10 / 100
    print("Novo salario: {:.2f}".format(novo_salario))
    print("Reajuste ganho: {:.2f}".format(reajuste_ganho))
    print("Em percentual: 10 %")

if salario > 1200 and salario <= 2000:
    novo_salario = salario * 7 / 100 + salario
    reajuste_ganho = salario * 7 / 100
    print("Novo salario: {:.2f}".format(novo_salario))
    print("Reajuste ganho: {:.2f}".format(reajuste_ganho))
    print("Em percentual: 7 %")

if salario > 2000:
    novo_salario = salario * 4 / 100 + salario
    reajuste_ganho = salario * 4 / 100
    print("Novo salario: {:.2f}".format(novo_salario))
    print("Reajuste ganho: {:.2f}".format(reajuste_ganho))
    print("Em percentual: 4 %")

'========================================================================================'

# PARES ENTRE CINCO NÚMEROS

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

pares = 0

if n1 % 2 == 0:
    pares += 1

if n2 % 2 == 0:
    pares += 1

if n3 % 2 == 0:
    pares += 1

if n4 % 2 == 0:
    pares += 1

if n5 % 2 == 0:
    pares += 1

print("{} valores pares".format(pares))

'========================================================================================'

# MÚLTIPLOS DE 13

x = int(input())
y = int(input())

soma = 0

for i in range(x, y + 1):
    if i % 13 != 0:
        soma += i

for i in range(y, x + 1):
    if i % 13 != 0:
        soma += i

print(soma)

'========================================================================================'

# PREENCHIMENTO DE VETOR I

valor = int(input())

print("N[0] = {}".format(valor))

for n in range(1, 10):
        valor *= 2
        print("N[{}] = {}".format(n, valor))

'========================================================================================'

# MENOR E POSIÇÃO

n = int(input())
valores = input()

valores = valores.split()

menor = int(valores[0])
posicao = 0

for i in range(0, n):
    valores[i] = int(valores[i])
    if valores[i] < menor:
        menor = valores[i]
        posicao = i

print("Menor valor: {}".format(menor))
print("Posicao: {}".format(posicao))

'========================================================================================'

# COLUNA NA MATRIZ

C = int(input())
T = input()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

coluna = 0
for i in range(12):
    coluna += matriz[i][C]

if T == "M":
   print("{:.1f}".format(coluna / 12))
if T == "S":
    print(coluna)

'========================================================================================'

# ORDENAÇÃO POR TAMANHO

testes = int(input())

for i in range(testes):
    frase = input()
    lista = frase.split()
    ordem_decrescente = sorted(lista, key=len, reverse=True)
    print(" ".join(ordem_decrescente))