#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math


print('='*40)

print('LOJAS DE TINTAS DO ALLU')

print('='*40)

pedido_cliente = float(input('Digite quantos metros quer pintar: '))

print('='*40)

lata_metros = 54
valor_lata = 80.00
metro_pintado = math.ceil(pedido_cliente / lata_metros)
valor_final = metro_pintado * valor_lata


print(f'Para pintar {pedido_cliente} metros, você vai precisar de {metro_pintado:.2f} lata(as) de tinta'
      f'\nTotatlizando: R$ {valor_final:.2f}')

