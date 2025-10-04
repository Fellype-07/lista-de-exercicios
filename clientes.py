
clientes = []
clientes.append({'nome': 'João', 'email': 'joao@email.com', 'telefone': '123456789'})
clientes.append({'nome': 'Maria', 'email': 'maria@email.com', 'telefone': '987654321'})
clientes.append({'nome': 'Carlos', 'email': 'carlos@email.com', 'telefone': '111222333'})
clientes.append({'nome': 'Ana', 'email': 'ana@email.com', 'telefone': '444555666'})
i = 0
while i < len(clientes):
    print("Cliente", i + 1)
    print("Nome:", clientes[i]['nome'])
    print("Email:", clientes[i]['email'])
    print("Telefone:", clientes[i]['telefone'])
    print("--------------------------")
    i += 1