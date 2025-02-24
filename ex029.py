velocidade = int(input('Em quantos KM/h o carro está? '))

if velocidade>80:
    print(f'MULTADO!!\nO carro está em {velocidade}Km/h e ultrapassou o limite de 80Km/h.')
    multa = (velocidade - 80) * 7
    print(f'A multa totalizou em: R${multa}')