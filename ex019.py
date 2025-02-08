import random

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

alunos = [n1, n2, n3, n4]
nome = random.choice(alunos)

print(f'O aluno escolhido é: {nome}')
