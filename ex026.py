frase = str(input('Digite uma frase: ')).upper().strip()

print(f""""A" letra A aparece: {frase.count('A')} vez
A primeira posição: {frase.find('A')+1}
A última posição: {frase.rfind('A')+1}
""")