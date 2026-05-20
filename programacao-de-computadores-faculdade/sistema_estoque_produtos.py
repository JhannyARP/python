# Lista de dicionários criada por você para armazenar o estoque inicial.
# Cada dicionário é um objeto com atributos de texto (string), inteiros e decimais (float).
estoque_produtos = [
    {"nome": "Perfume", "quantidade": 10, "preco": 59.90},
    {"nome": "Creme", "quantidade": 15, "preco": 29.90},
    {"nome": "Batom", "quantidade": 50, "preco": 19.90}
]

# Primeiro 'while True': Cria o loop do menu principal para que o programa
# continue rodando até que o usuário decida sair digitando 4.
while True:

    # Bloco de prints para desenhar a interface visual do menu no terminal.
    print("\n")
    print("--------------------")
    print("ESTOQUE DE PRODUTOS")
    print("--------------------")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    print("--------------------")

    # Coleta a opção escolhida e a converte para inteiro (int) para permitir as comparações numéricas.
    decisao_usuario = int(input("O que você deseja fazer?:"))

    # Condicional da OPÇÃO 1: Visualização do Estoque.
    if decisao_usuario == 1:
        print("\n")
        print("PRODUTOS:")

        # Laço 'for' que percorre a lista de dicionários, extraindo um produto por vez.
        for produto in estoque_produtos:
            print("--------------------")
            # Exibe os dados formatados. O ':.2f' garante as duas casas decimais no preço.
            print(f"Nome: {produto['nome']} \nQtd: {produto['quantidade']} \nPreço: R${produto['preco']:.2f}")
        print("--------------------")

    # Condicional da OPÇÃO 2: Registrar Entrada (Aqui está a lógica que estamos ajustando).
    elif decisao_usuario == 2:
        print("\n")
        # Solicita o nome do produto que o usuário deseja buscar.
        produto_para_alterar_quantidade = input("Digite o nome do produto: ")

        # Segundo 'while True': Criado para gerenciar a busca e garantir que o fluxo
        # seja interrompido corretamente se o produto for ou não achado.
        while True:
            # Variável de controle (booleana) iniciada como False. Ela serve como um "sinalizador"
            # para o programa saber se a busca no 'for' teve sucesso.
            produto_encontrado = False

            # O 'for' percorre a lista procurando o produto digitado pelo usuário.
            for produto_para_alterar in estoque_produtos:

                # Compara se o nome do produto atual no laço é idêntico ao digitado.
                if produto_para_alterar["nome"] == produto_para_alterar_quantidade:
                    # ⚠️ O PROBLEMA DO SOMADOR ESTÁ AQUI:
                    # Aqui você criou uma nova variável isolada chamada 'acumulador_de_produto_no_estoque'
                    # e copiou o valor da quantidade para dentro dela.
                    acumulador_de_produto_no_estoque = produto_para_alterar["quantidade"]

                    # Solicita a nova quantidade a ser somada.
                    quantidade_nova_produto = int(input("Digite a quantidade a ser acrescentada no estoque: "))

                    # Aqui você somou o valor dentro da variável temporária 'acumulador_de_produto_no_estoque'.
                    # Como essa variável é apenas uma "cópia", a lista original 'estoque_produtos' nunca
                    # recebe o novo valor e o estoque não atualiza.
                    acumulador_de_produto_no_estoque += quantidade_nova_produto

                    # Ativa o sinalizador dizendo que o produto existe.
                    produto_encontrado = True

                    # ⚠️ OUTRO DETALHE DE SINTAXE:
                    # Na f-string abaixo, você usou aspas duplas dentro de aspas duplas ("nome" dentro de f"...").
                    # Para o Python não dar erro, o correto é usar aspas simples por dentro: ['nome']
                    print(f"Nova quantidade de {produto_para_alterar['nome']}: {quantidade_nova_produto}")
                    break  # Quebra o laço 'for' para interromper a busca, pois já achou o produto.

            # Verificações pós-busca fora do 'for':
            if produto_encontrado == True:
                # Se o produto foi achado, este break quebra o segundo 'while True' e volta para o menu principal.
                break
            else:
                # Se o 'for' olhou tudo e a variável continuou False, exibe o aviso e quebra o 'while' para voltar ao menu.
                print("Este produto não existe no estoque.")
                break

    # Condicional da OPÇÃO 4: Finalizar o sistema.
    elif decisao_usuario == 4:
        print("Você finalizou o programa com sucesso!")
        break  # Quebra o primeiro 'while True', encerrando o script.

    # Tratamento de erro caso digitem qualquer outro número (como 5, 6, etc).
    else:
        print("Digite uma opção válida!")