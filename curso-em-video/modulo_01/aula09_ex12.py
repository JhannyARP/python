nome_pessoa = input("Qual seu nome?")

nome_maiusc = nome_pessoa.upper()
nome_minusc = nome_pessoa.lower()
tamanho_nome = len(nome_pessoa)
primeiro_nome = ""



for caractere in nome_pessoa:

    if caractere == " ":
        tamanho_nome = len(nome_pessoa) - 1

for caractere in nome_pessoa:

    if caractere == " ":
        break
    primeiro_nome = primeiro_nome + caractere


tamanho_primeiro_nome = len(primeiro_nome)
print(f'\nSeu nome em maiusculo: {nome_maiusc}')
print(f'Seu nome em minusculo: {nome_minusc}')
print(f"Seu nome tem {tamanho_nome} letras!")
print(f"O seu primeiro nome tem {tamanho_primeiro_nome} letras!")