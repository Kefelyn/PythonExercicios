#O QUADRADO DA HIPOTENUSA É IGUAL A SOMA DOS QUADRADOS DOS CATETOS

import math

op = float(input('Qual é o comprimento do cateto oposto? '))
adj = float(input('Qual é o comprimento do cateto adjacente? '))
hip = math.sqrt(op * op + adj * adj)

print(f'O comprimento do cateto oposto é: {op}m²')
print(f'O comprimento do cateto adjacente é: {adj}n²')
print(f'O comprimento da hipotenusa é de: {hip:.2f}m²')