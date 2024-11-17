# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temp_faren = float(input('Qual a temperatura em Fahrenheit: '))

temp_cel = (temp_faren - 32) * (5 / 9)

print(f'A temperatura em Celsius: {temp_cel}F')