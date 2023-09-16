import random
a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo: '))
a3 = str(input('Digite o segundo aluno: '))
a4 = str(input('Digite o terceiro aluno: '))

lista = [ a1, a2, a3, a4 ]
escolhido = random.choice(lista)

print (f' O escolhido são {escolhido}')

