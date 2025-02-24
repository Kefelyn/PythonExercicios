r1 = float(input('Digite o comprimento da primeira régua: '))
r2 = float(input('Digite o comprimento da segunda régua: '))
r3 = float(input('Digite o comprimento da terceira régua: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2}, {r3} conseguem formar um triângulo.')
else:
    print(f'As retas {r1}, {r2}, {r3} não conseguem formar um triângulo.')