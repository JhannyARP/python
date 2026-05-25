# BIBLIOTECA IMPORTADA:
# Para realizar o sorteio, para otimizar
# o uso de memória e clareza do código, é utilizada a sintaxe 'from random import choice',
# trazendo exclusivamente a função 'choice' da biblioteca random para o ambiente.

# CRIAÇÃO DA LISTA DE PALAVRAS:
# As palavras foram padronizadas em letras maiúsculas dentro da List para facilitar a futura
# comparação com os palpites do jogador, evitando conflitos de 'case-sensitivity'.

# LÓGICA DO SORTEIO E COMANDOS EFICIENTES:
# A lógica baseia-se na amostragem aleatória sobre uma sequência indexada. O comando
# do Python que permite essa seleção de forma altamente eficiente é a função 'choice()'
# escolhida na importação. Ela acessa a lista diretamente através de seus índices internos
# em tempo constante, dispensando loops, contagens manuais ou a necessidade de embaralhar
# a estrutura original.

from random import choice

palavras_sortidas = ["gato", "cachorro", "passarinho"]
palavra_escolhida = choice(palavras_sortidas)

armazenamento_campos_letras = []
letras_digitadas = set()

chances = 8

print(palavra_escolhida)
tamanho_palavra = len(palavra_escolhida)

for tamanho in range(tamanho_palavra):
    armazenamento_campos_letras.append('_')

print(armazenamento_campos_letras)


while '_' in armazenamento_campos_letras and chances > 0:
    tentativa = input("Digite uma letra: ")
    letras_digitadas.add(tentativa)

    if tentativa not in palavra_escolhida:
        chances = chances - 1
        print(f"Letra incorreta! Você ainda tem {chances} chances.")

    for posicao in range(tamanho_palavra):

        if palavra_escolhida[posicao] == tentativa:
            armazenamento_campos_letras[posicao] = tentativa


    print(armazenamento_campos_letras)


if '_' not in armazenamento_campos_letras:
    print("\nParabéns! Você descobriu a palavra secreta!")
else:
    print(f"\nGame Over! Suas chances acabaram. A palavra era: {palavra_escolhida}")


































