print("********************************")
print("Bem vindo no jogo de Adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if acertou:
    print("Você acertou!!")
else:
    if chute_maior:
        print("O seu chute foi maior que o número secreto.")
    elif chute_menor:
        print("O seu chute foi menor que o número secreto.")


print("Fim do jogo.")