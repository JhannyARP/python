# -------> DICIONÁRIO DE DICIONÁRIOS (Chave sendo o nome do produto)

#Nesta estrutura, o produto é a própria "etiqueta" (a chave primária) que te dá acesso direto aos detalhes dele.
# O nome do produto é a chave principal

produtos_dict = {
    "Notebook": {"preco": 4500, "estoque": 10},
    "Mouse Wireless": {"preco": 150, "estoque": 45},
    "Monitor 24": {"preco": 1200, "estoque": 15},
}
# O Superpoder: Busca Instantânea
# Se você precisa saber o preço do Mouse Wireless, você vai direto ao ponto, sem precisar ler mais nada no código:

preco_mouse = produtos_dict["Mouse Wireless"]["preco"]




# -------> LISTA DE DICIONÁRIOS

#Aqui, os produtos são apenas elementos soltos dentro de um vetor (uma lista organizada por posição numérica 0, 1, 2...).
# O nome do produto passa a ser um dado comum dentro do registro.
# Cada elemento da lista é um registro independente

produtos_lista = [
    {"nome": "Notebook", "preco": 4500, "estoque": 10},
    {"nome": "Mouse Wireless", "preco": 150, "estoque": 45},
    {"nome": "Monitor 24", "preco": 1200, "estoque": 15},
]
#O Superpoder: Flexibilidade e Ordenação
#Se você quiser listar os produtos do mais barato para o mais caro, ou filtrar apenas os itens com estoque baixo,
# a lista é perfeita para isso. Ela aceita produtos com o mesmo nome sem problemas.
#No entanto, para descobrir o preço do Mouse Wireless aqui, você é obrigado a olhar item por item (fazer um loop)
# até encontrar o nome correspondente:
# É preciso percorrer a lista inteira até achar

for produto in produtos_lista:
    if produto["nome"] == "Mouse Wireless":
        print(produto["preco"])
        break