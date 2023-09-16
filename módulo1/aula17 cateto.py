from math import pow, sqrt
n1 = float(input('Digite o cateto oposto: '))
n2 = float(input('Digite o cateto adjacente: '))

r = pow(n1, 2) + pow(n2, 2)

rr = sqrt(r)


print(f'O comprimento da hipotenusa é: {rr :.2f}')
