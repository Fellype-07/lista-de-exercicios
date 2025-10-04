
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto_unido = conjunto1.union(conjunto2)
soma = 0
i = 0
conjunto_lista = list(conjunto_unido)
while i < len(conjunto_lista):
 soma += conjunto_lista[i]
 i += 1
print(soma)