

try:
    num = int(input("digite um numero inteiro: "))
    contador = 1

    while (0 > num) or (10 < num):

        if 0 < num < 10:

            while num != 0:
                contador *= num
                num -= 1

                print("O fatorial é {}".format(contador))

        else:
            print("Digite um numero entre 0 e 10")

except:
    print("Digite o que foi solicitado corretamente.")
