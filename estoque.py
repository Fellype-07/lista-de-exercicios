
estoque = [('produto1', 10), ('produto2', 5), ('produto3', 7)]
estoque.append(('produto4', 12))
i = 0
while i < len(estoque):
    produto, quantidade = estoque[i]
    print(f'{produto}: {quantidade}')
    i += 1