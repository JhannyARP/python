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

# ESTRUTURA PARA A PALAVRA MASCARADA (LISTA):
# Optou-se por uma LISTA vazia porque precisamos manter a ordem exata
# das letras e permitir elementos duplicados (vários tracinhos '_').

armazenamento_campos_letras = []

# ESTRUTURA PARA AS TENTATIVAS (CONJUNTO / SET):
# Set utilizado para impedir o acúmulo de duplicatas caso o jogador digite
# a mesma letra repetidamente, evitando uma contagem indevida para o nosso jogo.

letras_digitadas = set()

# Define o limite numérico de erros permitidos antes do encerramento do jogo.

chances = 8

# Mede-se o comprimento da palavra sorteada para preencher a lista de
# lacunas com a quantidade exata de 'caracteres ocultos'.

tamanho_palavra = len(palavra_escolhida)

# O loop 'for' associado ao 'range' garante que adicionaremos
# exatamente um tracinho '_' para cada letra existente na palavra oculta,
# organizando e separando cada elemento exato do índice.

for tamanho in range(tamanho_palavra):
    armazenamento_campos_letras.append('_')

# Exibição das lacunas para exibição do tamanho da palavra (ex: ['_', '_', '_', '_'])
print(armazenamento_campos_letras)

# LOOP PRINCIPAL DO JOGO:
# Utiliza-se o loop 'while' combinado com o operador lógico 'and',
#
# jogo continua rodando dinamicamente ENQUANTO o jogador não adivinhar
# todas as letras E possuir vidas maiores que zero.

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


































