import math

ang = int(input('Qual é o ângulo? '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print(f'Com o ângulo {ang}, temos o seno {sen:.2f}, cosseno {cos:.2f} e tangente {tang:.2f}.')