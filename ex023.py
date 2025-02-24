n = int(input('Digite um número: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10

print(f"""unidade: {uni}
dezenas: {dez}
centenas: {cen}
milhar: {mil}
""")