
# ==============================================================================
# ESTRUTURA DE DADOS ESCOLHIDA: LISTA DE DICIONÁRIOS
# O enunciado sugeriu no exemplo o uso de um dicionário de
# dicionários (estoque['ProdutoX']['quantidade']). No entanto, optei por trabalhar
# com uma LISTA DE DICIONÁRIOS para o 'estoque_produtos'.
#
# MOTIVO DA ESCOLHA E CONTORNO: O PyCharm e o interpretador do Python não permitiriam
# a sintaxe do exemplo direto na minha estrutura. Para contornar isso e garantir a
# flexibilidade de iterar ordenadamente sobre os produtos, implementei um laço 'for'
# que localiza o dicionário correspondente ao produto digitado e manipula a chave
# ['quantidade'] diretamente no nível correto da estrutura.
# ==============================================================================

estoque_produtos = [
    {"nome": "Perfume", "quantidade": 10, "preco": 59.90},
    {"nome": "Creme", "quantidade": 15, "preco": 29.90},
    {"nome": "Batom", "quantidade": 50, "preco": 19.90}
]

# Garante que o sistema permaneça ativo ditando as rotas conforme a decisão do usuário.

while True:

    # TRATAMENTO DE ERROS ANTI-CRASH
    # Atendendo ao requisito de que o sistema não deve falhar caso o usuário digite
    # valores inválidos (como letras no menu ou na quantidade).

    try:
        print("\n")
        print("--------------------")
        print("ESTOQUE DE PRODUTOS")
        print("--------------------")
        print("1 - Visualizar Estoque Atual")
        print("2 - Registrar Entrada de Produto")
        print("3 - Registrar Saída de Produto")
        print("4 - Sair do Sistema")
        print("--------------------")

        # Conversão de tipo str para int diretamente na linha a fim de tornar o código limpo

        decisao_usuario = int(input("O que você deseja fazer?:"))

        # OPÇÃO 1: Lógica que itera e imprime todos os produtos com quantidades
        # e preços formatados.

        if decisao_usuario == 1:
            print("\n")
            print("PRODUTOS:")

            # Iteração sobre a estrutura de dados para exibição limpa ao usuário

            for produto in estoque_produtos:
                print("--------------------")

                # Exibição limpa e formatado para melhor compreensão de usuário

                print(f"Nome: {produto['nome']} \nQuantidade: {produto['quantidade']}")
                print(f"Preço: R${produto['preco']:.2f}")
            print("--------------------")

        # OPÇÃO 2: Solicita o nome e a quantidade. Se o produto existir, soma; se não, avisa.

        elif decisao_usuario == 2:
            print("\n")

            produto_para_mudar_quantidade_estoque = input("Digite o nome do produto:")

            # 'Bandeira' de controle para rastrear a existência do item

            produto_encontrado = False

            # Laço for que varre a lista de dicionários utilizado para procurar
            # o nome exato do produto

            for verificar_estoque in estoque_produtos:
                if verificar_estoque["nome"] == produto_para_mudar_quantidade_estoque:
                    print(f"Estoque atual: {verificar_estoque['quantidade']} unidades.")

                    # Conversão explícita para inteiro da quantidade a ser somada

                    quantidade_atualizada_estoque = int(input("Quantidade a ser acrescentada no estoque: "))

                    # Contorno para atualizar a quantidade na Lista de Dicionários adaptada
                    verificar_estoque['quantidade'] += quantidade_atualizada_estoque

                    print(f"\n >>> Quantidade atualizada: {verificar_estoque['quantidade']} unidades.")

                    produto_encontrado = True
                    break

            # A mensagem de 'produto não encontrado' foi realizada fora por
            # questão lógica de funcionamento

            if not produto_encontrado:
                print("Este produto não existe no estoque.")


        elif decisao_usuario == 3:
            print("\n")
            # Evita disparar falsos avisos de "não encontrado" durante a varredura da lista

            produto_encontrado = False
            compra_produto = input("Digite o nome do produto (Digite 0 para sair):")

            # Laço for de verificação da existência de produto reaproveitado da 'Opção 2'

            for verificar_estoque in estoque_produtos:

                if verificar_estoque["nome"] == compra_produto:

                    print(f"Produto disponível no estoque! Há {verificar_estoque['quantidade']} unidades.")

                    produto_encontrado = True

                    # Solicita a quantidade da retirada e a converte para inteiro (int)
                    # para permitir a realização de operações matemáticas logo em seguida

                    quantidade_compra_produto = int(input("Quantidade do produto a ser comprado: "))

                    # Um "if" dentro do outro, como sugerido pelo enunciado, para separar
                    # a checagem de existência da checagem de saldo disponível.
                    # Se a quantidade pedida for menor ou igual à disponível, a operação é segura

                    if quantidade_compra_produto <= verificar_estoque['quantidade']:

                        # Deduz a quantidade exata vendida diretamente do saldo atual do item

                        verificar_estoque['quantidade'] -= quantidade_compra_produto
                        print("Compra realizada com sucesso!")
                        print(f"Estoque atualizado: {verificar_estoque['quantidade']} unidades.")

                    # Se a demanda for maior que o estoque, bloqueia a operação para evitar saldo negativo

                    elif quantidade_compra_produto > verificar_estoque['quantidade']:

                        print("Estoque insuficiente.")

                    # Como cada produto tem um nome único, assim que ele é processado
                    # (com sucesso ou erro de saldo), o 'break' interrompe o 'for' imediatamente,
                    # poupando processamento inútil no restante da lista

                    break

            if not produto_encontrado:
                print("Produto não encontrado.")

        # Condicional da OPÇÃO 4: Finalizar o sistema (comentado para o escopo atual da tarefa)

        elif decisao_usuario == 4:
            print("Você finalizou o programa com sucesso!")
            break

        # Tratamento de erro para opções numéricas inexistentes (comentado para o escopo)

        else:
            print("Digite uma opção válida!")

    except:
        print(">> Digite um valor válido! <<")