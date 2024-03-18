"""
Programação Estruturada
2024.1
18/03/2024

Estruturas de Repetição
AC5
"""
from random import randint

def main():
    # Atributos do aventureiro
    vida_aventureiro = 100
    att_aventureiro = randint(10, 20)
    def_aventureiro = randint(1, 5)

    # Atributos do monstro
    vida_monstro = randint(60, 80)
    att_monstro = randint(20, 30)

    # Exibição dos atributos
    print(f"Aventureiro: Vida {vida_aventureiro} - Ataque {att_aventureiro} - Defesa {def_aventureiro}")
    print(f"Monstro: Vida {vida_monstro} - Ataque {att_monstro}")

    # rodadas
    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print(f"\nRodada {rodada}:")
        rodada = rodada + 1

    # Aventureiro ataca o monstro
        dano_aventureiro = randint(1, att_aventureiro)
        vida_monstro = vida_monstro - dano_aventureiro


    # Monstro ataca o aventureiro
        dano_monstro = randint(1, att_monstro) - def_aventureiro
        vida_aventureiro = vida_aventureiro - dano_monstro

        if vida_monstro <= 0:
            print("O monstro morreu!")
            break

        if vida_aventureiro <= 0:
            print("O aventureiro morreu!")
            break

        print(f"Monstro: vida {vida_monstro} - att {att_monstro}")
        print(f"Aventureiro: vida {vida_aventureiro} - att {att_aventureiro} - def {def_aventureiro}")

main()
