nome = str(input('Digite o seu nome: ')).strip().split()

print(f"""Primeiro nome: {nome[0]}
último nome: {nome[len(nome)-1]}
""")