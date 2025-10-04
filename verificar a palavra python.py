palavras = ['python', 'programacao', 'desenvolvimento']
i = 0
while i < len(palavras):
    if palavras[i] == 'python':
        print('python')
        break
    i += 1
else:
    print('Palavra não encontrada')