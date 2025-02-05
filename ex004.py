valor = input('Escreva algo: ')
print('O tipo desse valor é: ', type(valor))
print('É um número? ', valor.isnumeric())
print('É uma string (alfabético)? ', valor.isalpha())
print('É um alfanumérico? ', valor.isalpha())
print('Está em maiúsculo? ', valor.isupper())
print('Só tem espaço? ', valor.isspace())

#ou pode ser:

valor = input('Escreva algo: ')
print(f'O tipo desse valor é: {type(valor)}')
print(f'É um número? {valor.isnumeric()}')
print(f'É uma string (alfabético)? {valor.isalpha()}')
print(f'É um alfanumérico? {valor.isalpha()}')
print(f'Está em maiúsculo? {valor.isupper()}')
print(f'Só tem espaço? {valor.isspace()}')