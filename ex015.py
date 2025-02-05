dias = int(input('Foi alugado por quantos dias? '))
km = float(input('Andou por quantos km? '))

pagar =  dias * 60
rodado = km * 0.15
total = pagar + rodado

print(f'\nTotal de dias: {dias}.\nTotal de km rodados: {km:.2f}.')
print(f'Valor dos dias alugados: R${pagar:.2f}')
print(f'Valor dos km rodados R${rodado:.2f}')
print('-'*40)
print(f'O valor total é de R${total:.2f}.')