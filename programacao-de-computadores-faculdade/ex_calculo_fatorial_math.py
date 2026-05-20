import math

# O laço garante a repetição até o sucesso da operação, enquanto o bloco
# try/except previne o fechamento do programa caso o usuário digite dados
# inválidos (como letras).

while True:
    try:
        # Realiza o casting de string (capturada pelo input) para inteiro através
        # da função int().

        numero_escolhido = int(input("Digite um número inteiro entre 1 e 10: "))

        # Filtra a entrada para o intervalo exigido. Se válido, consome o método
        # otimizado da biblioteca 'math' para calcular o fatorial com o método,
        # exibindo os dados requisitados e encerrando o fluxo com segurança.

        if 1 <= numero_escolhido <= 10:
            resultado_fatorial = math.factorial(numero_escolhido)
            print(f"O fatorial de {numero_escolhido} é {resultado_fatorial}!")
            break
        else:
            print("Número inválido! Deve ser entre 1 e 10.")

    except ValueError:
        print("Digite um valor válido (número inteiro).")

