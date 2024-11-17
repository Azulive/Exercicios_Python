# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.

temp_cel = float(input('Digite a temperatura em Celsius: '))

temp_faren = (temp_cel) * (9 / 5) + 32

print(f'A temperatura em fahrenheits será de {temp_faren:.1f}')