# EXERCÍCIO 1:

"""Calculo das raízes:"""

# Função:
def eq_seg_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = ((-b + delta ** 0.5) / 2 * a)
    x2 = ((-b - delta ** 0.5) / 2 * a)
    return x1, x2

# Armazenamento de Dados:
a = float(input('Digite o valor de a:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))
x1, x2 = eq_seg_grau(a, b, c)

# Saída de Dados:
print("As raízes da equação são {} e {}".format(x1, x2))


"""Ano bissexto:"""

# Função:
def bissexto(ano):
    return (ano % 4 == 0 and not ano % 100 == 0) or (ano % 400 == 0)

# Exemplos:
print(bool(bissexto(1900)))
print(bool(bissexto(2000)))
print(bool(bissexto(2024)))
print(bool(bissexto(2050)))

"""====================================================================="""

# EXERCÍCIO 2:

# Função:
def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario_bruto = valor_hora * num_horas
    porcentagem = salario_bruto * irpf
    salario_liquido = salario_bruto - porcentagem
    return salario_liquido

# Exemplos:
print('O salário líquido do funcionário é R${:.2f}'.format(calcula_salario(75, 160)))
print('O salário líquido do funcionário é R${:.2f}'.format(calcula_salario(140, 30)))








