
compras = [('produto1', 2, 10), ('produto2', 1, 50), ('produto3', 4, 5)]
total = 0
i = 0
while i < len(compras):
    produto, quantidade, preco = compras[i]
    total += quantidade * preco
    i += 1

print(f'Total da compra: R$ {total}')