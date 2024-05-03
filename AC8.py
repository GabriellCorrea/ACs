# FIGURINHAS

testes = int(input())

for i in range(testes):
    figurinhas = input()
    F1, F2 = figurinhas.split()
    F1 = int(F1)
    F2 = int(F2)

    while True:
        if F1 > F2:
            resto1 = F1 % F2
            if resto1 == 0:
                MDC = F2
                print(MDC)
                break
            else:
                resto2 = F2 % resto1
                if resto2 == 0:
                    MDC = resto1
                    print(MDC)
                    break
                else:
                    F2 = resto1
                    F1 = resto2

        if F2 > F1:
            resto1 = F2 % F1
            if resto1 == 0:
                MDC = F1
                print(MDC)
                break
            else:
                resto2 = F1 % resto1
                if resto2 == 0:
                    MDC = resto1
                    print(MDC)
                    break
                else:
                    F2 = resto1
                    F1 = resto2

"============================================================="
# DAMA

while True:
    coordenadas = input()
    x1, y1, x2, y2 = map(int, coordenadas.split())

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    else:
        if x2 == x1 and y2 == y1:
            print(0)
        else:
            if (x2 - x1) == (y1 - y2):
              print(1)
            else:
                if (x2 - x1) == (y2 - y1):
                    print(1)
                else:
                    if (x1 - x2) == (y1 - y2):
                        print(1)
                    else:
                        if (x1 - x2) == (y2 - y1):
                            print(1)
                        else:
                            if x2 == x1 or y2 == y1:
                                print(1)
                            else:
                                print(2)

"============================================================="
# SOMA DE FATORIAIS

while True:
    try:
        M_fatorial = 1
        N_fatorial = 1
        fatoriais = input()
        M, N = map(int, fatoriais.split())

        for i in range(M, 0, -1):
           M_fatorial *= i

        for i in range(N, 0, -1):
            N_fatorial *= i

        if M == 0:
            M_fatorial = 1
        if N == 0:
            N_fatorial = 1

        print(N_fatorial + M_fatorial)

    except EOFError:
        break

"============================================================="
# BLOBS

testes = int(input())
dia = 0

for i in range(testes):
    comida = float(input())
    while comida > 1:
        comida /= 2
        dia += 1
    print("{} dias".format(dia))
    dia = 0

"============================================================="
# FREQÊNCIA DE NÚMEROS

valores = int(input())
lista = []

for i in range(valores):
    valor = int(input())
    lista.append(valor)

ordem_crescente = sorted(lista)

quantidade = {}

for valor in ordem_crescente:
    if valor in quantidade:
        quantidade[valor] += 1
    else:
        quantidade[valor] = 1

for valor in quantidade:
    print("{} aparece {} vez(es)".format(valor, quantidade[valor]))

"============================================================="
# PRIMO RÁPIDO

import math

testes = int(input())

for _ in range(testes):
    valor = int(input())
    divisores = 0
    for i in range(1, int(math.sqrt(valor)) + 1):
        if valor % i == 0:
            divisores += 1
    if divisores == 1:
        print("Prime")
    else:
        print("Not Prime")

"============================================================="
# CARA OU COROA

while True:
    maria = 0
    joao = 0

    n = int(input())

    if n == 0:
        break

    valores = map(int, input().split())

    for num in valores:
        if num == 0:
            maria += 1
        if num == 1:
            joao += 1

    print("Mary won {} times and John won {} times".format(maria, joao))

"============================================================="
# FUNÇÕES

testes = int(input())

for i in range(testes):
    valores = input()
    x, y = map(int, valores.split())

    rafael = ((3 * x) ** 2) + y ** 2
    beto = 2 * (x ** 2) + (5 * y) ** 2
    carlos = -100 * x + y ** 3

    if carlos > beto and carlos > rafael:
        print("Carlos ganhou")
    if beto > carlos and beto > rafael:
        print("Beto ganhou")
    if rafael > carlos and rafael > beto:
        print("Rafael ganhou")

