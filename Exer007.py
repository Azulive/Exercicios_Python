#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o lado do quadrado: '))

area = lado ** 2
dobro_area = area * 2
print(f'A area do quadrado é {area:.2f}'
      f'\nE o dobro é {dobro_area:.2f}')