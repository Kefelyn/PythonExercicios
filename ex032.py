from datetime import date

ano = int(input('Digite o ano: '))

if ano == 0:
    ano = date.today().year #reconhece o 0 como o ano atual

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} NÃO é bissexto.')