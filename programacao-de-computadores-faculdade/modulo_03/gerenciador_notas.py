








# Estrutura base baseada em uma lista de dicionários para garantir escalabilidade.
# Cada dicionário encapsula os dados de um estudante sob as chaves 'nome' (string)
# e 'notas' (lista de floats). O uso de uma lista aninhada para as notas oferece
# flexibilidade, permitindo uma quantidade variável de avaliações por aluno.

registro_de_notas = [
    {
        "nome": "Maria",
        "notas": [1.5, 8.0, 9.5]
    },
    {
        "nome": "Joao",
        "notas": [7.5, 8.7, 10.0]
    },
    {
        "nome": "Camila",
        "notas": [9.0, 10.0, 10.0]
    },
    {
        "nome": "Jhanny",
        "notas": [1.4, 2.7, 5.0]
    }
]


def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.

    Args:
    notas (list): Uma lista contendo as notas dos estudantes (floats ou ints).

    Returns:
    float: O valor da média resultante.
    """

    # É mapeado o tamanho da lista e também é usado um laço 'for' para acumular as notas sequencialmente.
    # Essa estratégia manual calcula a média de forma dinâmica sem depender de bibliotecas externas,
    # garantindo que a função funcione para qualquer quantidade de avaliações antes de retornar
    # o resultado final.

    tamanho_lista_de_notas = len(notas)

    if tamanho_lista_de_notas == 0:
        return 0.0

    soma_notas = 0

    for nota in notas:
        soma_notas += nota

    calculo_da_media = soma_notas/tamanho_lista_de_notas

    return calculo_da_media


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se a média obtida atinge o critério mínimo de aprovação institucional.

    Args:
    media (float): A média final obtida pelo estudante.
    media_minima (float, opcional): A nota de corte para aprovação. O padrão é 7.0.

    Returns:
    str: 'Aprovado' se a média for maior ou igual à mínima, caso contrário 'Reprovado'.
    """

    # A estrutura condicional 'if/else' atua como um divisor de caminhos que valida a média
    # contra a nota de corte (media_minima). Dependendo do resultado dessa validação,
    # a função interrompe sua execução retornando apenas uma string limpa ('Aprovado' ou 'Reprovado').
    # Esse retorno isolado garante que o sistema receba um dado padronizado,
    # permitindo que a 'main' decida como exibir ou armazenar o status.

    if media >= media_minima:
        return "Aprovado"
    else:
        return 'Reprovado'


def gerar_relatorio(alunos):
    """
    Gera e exibe no terminal um relatório consolidado com os dados acadêmicos dos estudantes.

    Args:
    alunos (list): A lista completa de dicionários contendo as informações e notas de cada estudante.

    Returns:
    None: Esta função não retorna dados, sua responsabilidade é estritamente a exibição no terminal.
    """

    # A estrutura de repetição 'for' itera sobre a lista completa para processar os dados em lote.
    # Dentro do loop, o sistema integra e reaproveita o motor de lógica chamando sequencialmente
    # 'calcular_media' e 'verificar_aprovacao' para obter resultados isolados, centralizando
    # a responsabilidade de formatação e exibição nítida no terminal para o usuário final.

    for estudante in alunos:
        print("----------------")
        media_final = calcular_media(estudante['notas'])
        situacao_aprovacao = verificar_aprovacao(media_final)

        print("-------------------")
        print(f"Aluno: {estudante['nome']}")
        print(f"Média Final: {media_final:.2f}")
        print(f"Situação: {situacao_aprovacao}")




gerar_relatorio(registro_de_notas)
