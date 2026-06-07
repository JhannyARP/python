while True:
    # 1. Lemos como TEXTO (str) para o 'for' conseguir percorrer depois
    numero_texto = input('Digite um numero: ')

    # 2. Convertemos para número apenas para fazer o teste matemático
    numero_inteiro = int(numero_texto)

    volta = 0

    if (numero_inteiro > 0) and (numero_inteiro <= 9999):

        # Agora o 'for' funciona porque 'numero_texto' é uma string!
        for numeros in numero_texto:
            if volta == 0:
                print(f"Milhar: {numeros}")
            elif volta == 1:
                print(f"Centena: {numeros}")
            elif volta == 2:
                print(f"Dezena: {numeros}")
            else:
                print(f"Unidade: {numeros}")

            # Corrigida a indentação (alinhado com o 'if' interno)
            volta += 1

        break  # Sai do while True se tudo deu certo
    else:
        print("Numero invalido! Digite novamente.")