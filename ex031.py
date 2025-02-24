dist = int(input('Digite quantos Km/h a viagem tem de distância: '))

if dist <=200:
    passagem = dist*0.50
    print(f'O preço da viagem de {dist}Km/h é de: R${passagem}')
else:
    passagem = dist*0.45
    print(f'O preço da viagem de {dist}Km/h é de: R${passagem}')