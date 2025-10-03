
vendas = [
    ('João', 'Produto A', 100),
    ('Maria', 'Produto B', 200),
    ('João', 'Produto C', 150),
    ('Maria', 'Produto D', 50),
    ('Carlos', 'Produto E', 300)
]
total_por_vendedor = {}
i = 0
while i < len(vendas):
    vendedor, produto, valor = vendas[i]  
    if vendedor not in total_por_vendedor:
        total_por_vendedor[vendedor] = 0 
    total_por_vendedor[vendedor] += valor  
    i += 1  


for vendedor, total in total_por_vendedor.items():
    print(f'{vendedor} vendeu {total}')