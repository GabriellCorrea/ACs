# EXERCÍCIO 1:

# Função para determinar o tipo de triângulo
def determina_tipo_triangulo(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        return "Não é um triângulo"
    if (a == b) and (a == c):
        return "Equilátero"
    elif (a != b) and (b != c) and (c != a):
        return "Escaleno"
    else:
        return "Isosceles"

# Testes
def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4))  # Equilátero
    print(determina_tipo_triangulo(2, 4, 4))  # Isósceles
    print(determina_tipo_triangulo(3, 4, 5))  # Escaleno
    print(determina_tipo_triangulo(1, 1, 4))  # Não é um triângulo
testa_triangulo()

"""====================================================================="""

# EXERCÍCIO 2:

# Funnção para determinar o dia da semana
def dia_semana(dia):
    if dia == 1: return "Domingo"
    elif dia == 2: return "Segunda-Feira"
    elif dia == 3: return "Terça-Feira"
    elif dia == 4: return "Quarta-Feira"
    elif dia == 5: return "Quinta-Feira"
    elif dia == 6: return "Sexta-Feira"
    elif dia == 7: return "Sábado"
    else: return ""

# Testes:
def teste_dia_semana():
    print(dia_semana(2)) # Segunda-Feira
    print(dia_semana(6)) # Sexta-Feira
    print(dia_semana(7)) # Sábado
    print(dia_semana(9)) # String Vazia
teste_dia_semana()

"""======================================================================"""

# EXERCÍCIO 3:

# Funções para determinar o tipo de operação
def soma (n1, n2):
    return n1 + n2
def subtracao (n1, n2):
    return n1 - n2
def multiplicacao (n1, n2):
    return n1 * n2
def divisao (n1, n2):
    return n1 / n2

# CLI
def calculadora():
    return soma, subtracao, multiplicacao, divisao

n1 = float(input("Informe um número:"))
n2 = float(input("Informe outro número:"))
operacao = input("Informe a operação:")

if operacao == "soma":
    resultado = soma(n1, n2)
elif operacao == "subtração":
    resultado = subtracao(n1, n2)
elif operacao == "multiplicação":
    resultado = multiplicacao(n1, n2)
elif operacao == "divisão":
    resultado = divisao(n1, n2)
else:
    resultado = "Operação Inválida"

print("Resultado: {}".format(resultado))

# Executar a calculadora
calculadora()








