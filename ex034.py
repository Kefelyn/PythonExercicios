salario = float(input('Qual é o seu salário: R$'))

if salario >1250.00:
    aumento = (10/100*salario)+salario
    print(f'O seu salário de R${salario} teve um aumento de 10%, totalizando em: R${aumento:.2f}.')
else:
    aumento = (15/100*salario)+salario
    print(f'O seu salário de R${salario} teve um aumento de 15%, totalizando em R${aumento:.2f}.')

