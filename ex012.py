valor = float(input('Qual é o preço do produto? '))
desconto = (5/100)*valor
preco = valor-desconto

print(f'O produto do valor de {valor:.2f} reais, tem um desconto de 5%, ou seja: {desconto:.2f} reais, assim totalizando o preço de {preco:.2f} reais.')
