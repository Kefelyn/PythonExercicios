nome = str(input('Nome completo: '))
divido = nome.split()

print(f"""Letras maiúsculas: {nome.upper()}
Letras minúsuculas: {nome.lower()}
Total de letras: {len(nome)-nome.count(' ')}
Total de letras do primeiro nome: {len(divido[0])}""")
#ou "len(nome.replace(' ', ''))"