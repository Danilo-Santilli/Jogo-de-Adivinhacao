import random

print("******************")
print("Bem vindo ao Jogo!")
print("******************")

secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil")
print("(2) Médio")
print("(3) Difícil")

nivel = int(input("Defina um nível: "))

while(nivel < 1 or nivel > 3):
    nivel = int(input("Digite um nível válido entre 1 e 3:"))
    if(nivel == 1 or nivel == 2 or nivel == 3):
        break

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número de 1 a 100: ")
    chute = int(chute_str)

    print("Você digitou {}".format(chute))

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = secreto == chute
    maior   = chute > secreto
    menor   = chute < secreto

    pontos_perdidos = abs(secreto - chute)
    pontos = pontos - pontos_perdidos

    if(acertou):
        print("Você acertou e fez {} pontos!!!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto")
            if(rodada == total_de_tentativas):
                print("O número secreto era {} e sua pontuação foi {}".format(secreto, pontos))
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto")
            if(rodada == total_de_tentativas):
                print("O número secreto era {} e sua pontuação foi {} pontos".format(secreto, pontos))

print("***********")
print("Fim do Jogo")
print("***********")