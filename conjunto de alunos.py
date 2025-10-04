# Conjuntos de alunos
alunos_curso = {'Ana', 'Maria', 'João'}
alunos_palestra = {'Maria', 'José', 'Pedro'}

# Operações de conjuntos
uniao = alunos_curso.union(alunos_palestra)
interseccao = alunos_curso.intersection(alunos_palestra)
diferenca = alunos_curso.difference(alunos_palestra)

# União
i = 0
uniao_lista = list(uniao)
while i < len(uniao_lista):
    print(f'União: {uniao_lista[i]}')
    i += 1

# Interseção
i = 0
interseccao_lista = list(interseccao)
while i < len(interseccao_lista):
    print(f'Interseção: {interseccao_lista[i]}')
    i += 1

# Diferença
i = 0
diferenca_lista = list(diferenca)
while i < len(diferenca_lista):
    print(f'Diferença: {diferenca_lista[i]}')
    i += 1