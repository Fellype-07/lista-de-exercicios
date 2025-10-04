agenda = [('Fellype', '123456789', 'fellype@email.com')]
agenda.append(('Louhany', '987654321', 'Louhany@email.com'))
i = 0
while i < len(agenda):
 nome, telefone, email = agenda[i]
 print(f'{nome} - {telefone} - {email}')
 i +=1