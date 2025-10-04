notas = [10, 7, 3, 5, 8]
total = 0
i = 0
while i < len(notas):
 total += notas[i]
 i += 1
media = total / len(notas)
if media >= 7:
 print('Aprovado')
else:
 print('Reprovado')