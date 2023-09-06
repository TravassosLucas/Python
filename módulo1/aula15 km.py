
print('--' *20)
k = float(input('Quantos Km foram rodados?'))
d = int (input('Quantos dias foi alugado?'))
print('--' *20)

print('--' *20)
print(f'O preço total por Kilometragem que foi de {k}km e de {d} dias foi {(60*d)+(0.15*k):.2f} R$')
print('--' *20)