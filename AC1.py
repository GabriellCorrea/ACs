# Exercício 1:

# Pergunta:
a = int(input('Informe o parâmetro A da equação:'))
b = int(input('Informe o parâmetro B da equação:'))
c = int(input('Informe o parâmetro C da equação:'))

# Fórmula de Bhaskara:
delta = b ** 2 - 4 * a * c
raiz1 = (-b + delta ** 0.5) / 2 * a
raiz2 = (-b - delta ** 0.5) / 2 * a

# Resposta:
print('A primeira raiz da equação é {}'.format(raiz1))
print('A segunda raiz da equação é {}'.format(raiz2))

""""============================================================="""

# Exercício 2:

# Pergunta:
ano = int(input('Informe o ano:'))

# Cálculo do ano bissexto:
anobissexto = (ano % 4 == 0 and not (ano % 100 == 0) or (ano % 400 == 0))

# Resposta:
print(anobissexto)
