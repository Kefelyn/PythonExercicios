from random import randint
from time import sleep

print('====== VOU PENSAR EM UM NÚMERO.. TENTE DESCOBRIR.. ======')

escolhido = randint(0,5) #O computador escolhe um número aleatório de 0 a 5
resposta = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)

if resposta == escolhido:
    print(f'Parabéns! Você venceu. O número era: {escolhido}.')
else:
    print(f'HAHAHA! Você perdeu. O número era: {escolhido}')