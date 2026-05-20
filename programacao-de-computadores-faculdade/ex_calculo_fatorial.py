# Loop para repetir o prompt até receber o dado correto.
# O try/except evita travamentos caso digitem texto.

while True:
    try:

        # Realiza o casting de string (capturada pelo input) para inteiro através
        # da função int().

        numero_escolhido = int(input("Digite um número inteiro entre 1 e 10: "))
        acumulador_fatorial = 1

        # Valida o escopo e calcula o fatorial de forma regressiva.

        if 1 <= numero_escolhido<= 10:
            while (numero_escolhido >= 1) and (numero_escolhido <= 10):
                acumulador_fatorial *= numero_escolhido
                numero_escolhido-= 1

            print("O fatorial é {}".format(acumulador_fatorial))
            break
        else:
            print("Número inválido! Deve ser entre 1 e 10.")

    except:
        print("Digite um valor valido (numero inteiro).")

