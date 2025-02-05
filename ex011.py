largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))

area = altura*largura
tinta = area/2

print(f'Com a largura {largura:.1f}m e a altura {altura:.1f}m, '
      f'temos uma área de {area:.1f}m² que será necessário {tinta:.1f} tintas para pintá-la.')
