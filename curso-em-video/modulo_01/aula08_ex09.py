import random

al01 = input("Digite o primeiro do aluno: ")
al02 = input("Digite o segundo do aluno: ")
al03 = input("Digite o terceiro do aluno: ")
al04 = input("Digite o quarto do aluno: ")


nomes = [al01, al02, al03, al04]

sorteio = random.choice(nomes)

print("O sorteado para vir apagar o quadro é: {}".format(sorteio))