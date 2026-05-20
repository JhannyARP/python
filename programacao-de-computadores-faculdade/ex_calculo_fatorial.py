
# É com 'While: True' e 'Break' que se faz laço de repetição para pedir as condições corretas!

while True:
    try:
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
        acumulador_fatorial = 1

        if 1 <= numero <= 10:
            while (numero >= 1) and (numero <= 10):
                acumulador_fatorial *= numero
                numero -= 1

            print(f"O fatorial é {acumulador_fatorial}")
            break
        else:
            print("Número inválido! Deve ser entre 1 e 10.")

    except:
        print("Digite um valor valido (numero inteiro).")

