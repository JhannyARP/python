import math

cat_op = float(input("Digite o cateto oposto: "))
cat_adj = float(input("Digite o cateto adjacente: "))

hipotenusa = math.sqrt(math.pow(cat_op, 2) + math.pow(cat_adj, 2))

print(hipotenusa)