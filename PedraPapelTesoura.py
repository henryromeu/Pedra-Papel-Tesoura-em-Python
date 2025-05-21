# Biblioteca que faz a maquina fazer uma escolha aleatoria
import random

# jogador escolhe a opcao que ele quer jogar
jogador = input("\nEscolha pedra, papel ou tesoura: ").lower()
# Maquina escolhe uma opcao aleatoria
computador = random.choice(["pedra", "papel", "tesoura"])

# Se o jogador não escolher uma opcao valida, ele retorna "Escolha invalida"
if jogador not in ["pedra", "papel", "tesoura"]:
    print("Escolha inválida!")
# Se o jogador jogar pedra e a maquina jogar tesoura, o jogador ganha
elif jogador == "pedra" and computador == "tesoura":
    print("\nVocê ganhou!")
# Se o jogador jogar papel e a maquina jogar pedra, o jogador ganha
elif jogador == "papel" and computador == "pedra":
    print("\nVocê ganhou!")
# Se o jogador jogar tesoura e a maquina jogar papel, o jogador ganha
elif jogador == "tesoura" and computador == "papel":
    print("\nVocê ganhou!")
# Se o jogador jogar pedra e a maquina jogar papel, a maquina ganha
elif jogador == "pedra" and computador == "papel":
    print("\nComputador ganhou!")
# Se o jogador jogar papel e a maquina jogar tesoura, a maquina ganha
elif jogador == "papel" and computador == "tesoura":
    print("\nComputador ganhou!")
# Se o jogador jogar tesoura e a maquina jogar pedra, a maquina ganha
elif jogador == "tesoura" and computador == "pedra":
    print("\nComputador ganhou!")
# Se o jogador e a maquina jogarem a mesma opcao, da empate
else:
    print("\nEmpate!")

# Exibe o resultado da jogada
print("🤖 Computador jogou:", computador)
print("🧍 Você jogou:", jogador)
