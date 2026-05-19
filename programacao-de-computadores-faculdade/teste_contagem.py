

num = int(input("digite um numero inteiro: "))
contador = 1

while num != 0:
    contador *= num
    num -= 1

print("O fatorial é {}".format(contador))
