import math

a = float(input('Digite o valor do ângulo'))

a1 = math.radians(a)
 
c = math.cos(a1)
t = math.tan(a1)
s = math.sin(a1)

print (f' Resultado de Tangente é {t:.2f} \n Resultado do Cosseno é {c:.2f} \n Resultado do Seno é {s:.2f}')