algo = input("Digite algo: ")

print(algo.isalpha())

if algo.isnumeric():
    print("A entrada é numérica!")
else:
    print("A entrada NÃO é numérica.")


if algo.isalpha():
    print("A entrada toda é letra!")
else:
    print("A entrada NÃO tem só letra.")


if algo.isalnum():
    print("A entrada é alfabnumerica!")
else:
    print("A entrada NÃO tem números e nem letras.")