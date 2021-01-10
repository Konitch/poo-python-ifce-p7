import random

lista = []
for i in range(6):
    n = random.randint(1,60)
    lista.append(n)
lista.sort()
print(lista)