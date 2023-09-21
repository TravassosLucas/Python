import random
a1 = input('Digite o primeiro aluno:')
a2 = input('Digite o segundo: ')
a3 = input('Digite o terceiro: ')
a4 = input('Digite o quarto: ')

nomes = (a1, a2, a3, a4)
lista = list(nomes)
random.shuffle(lista)



print(f'{lista}')