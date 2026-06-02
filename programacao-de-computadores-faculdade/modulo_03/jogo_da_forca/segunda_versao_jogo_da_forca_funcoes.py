# BIBLIOTECA IMPORTADA:
# Para realizar o sorteio, para otimizar
# o uso de memória e clareza do código, é utilizada a sintaxe 'from random import choice',
# trazendo exclusivamente a função 'choice' da biblioteca random para o ambiente.
from random import choice

def inicializar_jogo(lista_palavras):
    """
    Configura o estado inicial da partida, isolando a preparação dos dados.

    Argumentos:
        lista_palavras (list): Lista contendo as strings das palavras para o sorteio.

    Retorno:
        tuple: Uma string com a palavra secreta e uma lista preenchida com lacunas '_'.
    """
    palavra = choice(lista_palavras)
    lacunas = []
    for tamanho in range(len(palavra)):
        lacunas.append('_')
    return palavra, lacunas

def processar_tentativa(palavra_secreta, lacunas, letra):
    """
    Processa a jogada do utilizador a cada turno, atualizando o tabuleiro.

    Argumentos:
        palavra_secreta (string): A palavra escolhida para a partida.
        lacunas (list): O status atualizado das lacunas descobertas.
        letra (string): O palpite enviado pelo jogador.

    Retorno:
        list: A lista de lacunas modificada caso a letra coincida com alguma posição.
    """
    tamanho_palavra = len(palavra_secreta)
    for posicao in range(tamanho_palavra):
        if palavra_secreta[posicao] == letra:
            lacunas[posicao] = letra
    return lacunas

# LISTA DE PALAVRAS:
# As palavras foram padronizadas em letras minúsculas dentro da List para facilitar a futura
# comparação com os palpites do jogador, evitando conflitos de 'case-sensitivity'.

palavras_sortidas = ["gato", "cachorro", "passarinho"]

# JUSTIFICATIVA DO USO DE CONJUNTOS EM VEZ DE LISTAS:
# Foi escolhido usar um Conjunto para as 'letras_digitadas' por não aceitar
# itens repetidos. Assim, o jogo barra letras duplicadas automaticamente, sem precisar
# criar travas manuais no código. Além disso, o Python consegue checar se uma letra já
# foi digitada de forma direta e muito mais rápida do que se usássemos uma lista comum.

letras_digitadas = set()
chances = 6

# LÓGICA DO SORTEIO:
# A seleção do elemento oculto ocorre fora do fluxo iterativo através da invocação direta
# da função 'inicializar_jogo()'. Esta chamada é realizada no bloco de configurações iniciais,
# onde o programa passa a 'palavras_sortidas' como argumento e recebe simultaneamente a
# palavra secreta definitiva e a estrutura de lacunas pronta, estabelecendo o ponto de partida do
# sistema.

palavra_escolhida, armazenamento_campos_letras = inicializar_jogo(palavras_sortidas)

print("Bem-vindo ao Jogo da Forca!")
print(armazenamento_campos_letras)

# 3. Controle de Fluxo: Estrutura do Laço 'while'
# Esta estrutura atua como o motor central que mantém o jogo ativo através de duas condições simultâneas.
# O laço gerencia a repetição contínua enquanto restarem caracteres ocultos (" '_' ") na lista de lacunas e
# o limite numérico de chances for maior que zero. A cada ciclo, ele exibe o histórico do conjunto,
# solicita a nova letra, penaliza os erros reduzindo o contador e delega a atualização do status das lacunas.

while '_' in armazenamento_campos_letras and chances > 0:
    if len(letras_digitadas) > 0:
        print(f"\nLetras já tentadas: {letras_digitadas}")
    else:
        print()

    tentativa = input("\nDigite uma letra: ").lower()
    letras_digitadas.add(tentativa)

    if tentativa not in palavra_escolhida:
        chances = chances - 1
        print(f"Letra incorreta! Você ainda tem {chances} chances.")

    armazenamento_campos_letras = processar_tentativa(palavra_escolhida, armazenamento_campos_letras, tentativa)
    print(armazenamento_campos_letras)

# 4. Verificação de Encerramento e Feedback
# Este bloco condicional avalia o resultado final assim que o laço principal é interrompido.
# Através de uma verificação de presença lógica, o sistema determina se o utilizador descobriu toda
# a palavra ou esgotou as suas chances, imprimindo uma mensagem de vitória ou a revelação da palavra na derrota.
if '_' not in armazenamento_campos_letras:
    print("\nParabéns! Você descobriu a palavra secreta!")
else:
    print(f"\nGame Over! Suas chances acabaram. A palavra era: {palavra_escolhida}")
