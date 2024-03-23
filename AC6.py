# EXERCÍCIO 1:
print("Hello World!")

# EXERCÍCIO 2:
a = int(input())
b = int(input())

x = a + b
print("X =", x)

# EXERCÍCIO 3:
dados1 = input()
dados2 = input()
dados1 = dados1.split(" ")
dados2 = dados2.split(" ")

valor1 = int(dados1[1]) * float(dados1[2])
valor2 = int(dados2[1]) * float(dados2[2])
total = valor1 + valor2

print(f"VALOR A PAGAR: R$ {total:.2f}")

# EXERCÍCIO 4:
dados = input()
dados = dados.split(" ")

maior_ab = (int(dados[0]) + int(dados[1]) + abs(int(dados[0]) - int(dados[1]))) / 2
maior = (maior_ab + int(dados[2]) + abs(maior_ab - int(dados[2]))) / 2

print("{} eh o maior".format(int(maior)))

# EXERCÍCIO 5:
p1 = input()
p2 = input()
p1 = p1.split(" ")
p2 = p2.split(" ")

distancia = ((float(p2[0]) - float(p1[0]))**2 + ((float(p2[1]) - float(p1[1])))**2) ** 0.5

print("{:.4f}".format(distancia))