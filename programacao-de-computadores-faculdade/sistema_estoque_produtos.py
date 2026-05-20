#Lista de dicionário
estoque_produtos = [
    {"nome": "Perfume", "quantidade": 10, "preco": 59.90},
    {"nome": "Creme", "quantidade": 15, "preco": 29.90},
    {"nome": "Batom", "quantidade": 50, "preco": 19.90}
]

while True:

    print("\n")
    print("--------------------")
    print("ESTOQUE DE PRODUTOS")
    print("--------------------")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    print("--------------------")
    decisao_usuario = int(input("O que você deseja fazer?:"))

    if decisao_usuario == 1:
        print("\n")
        print("PRODUTOS:")

        for produto in estoque_produtos:
            print("--------------------")
            print(f"Nome: {produto['nome']} \nQtd: {produto['quantidade']} \nPreço: R${produto['preco']:.2f}")

        print("--------------------")

    elif decisao_usuario == 4:
        print("Você finalizou o programa com sucesso!")
        break

    else:
        print("Digite uma opção válida!")