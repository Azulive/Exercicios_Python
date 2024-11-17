# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.


import math


print('='*40)

print('LOJA DE TINTAS DO ALLU')

print('='*40)

pedido_cliente = float(input('Digite quantos metros quer pintar: '))

print('='*40)

lata_metros = 108
valor_lata = 80.00
galao_metros = 21.6
valor_galao = 25.00
litros_lata = 18
litros_galao = 3.6

quantas_latas = math.ceil(pedido_cliente / lata_metros)
quantos_galao = math.ceil(pedido_cliente / galao_metros)
quantas_latas_galao = math.ceil((pedido_cliente / 6) * 1.1)

lata = quantas_latas_galao // 18
galao = math.ceil((quantas_latas_galao - lata * 18) / 3.6)
preco = lata * valor_lata + galao * valor_galao

valor_final_lata = quantas_latas * valor_lata
valor_final_galao = quantos_galao * valor_galao

latas_necessarias = math.floor(valor_lata / quantas_latas)

print(f'Para pintar {pedido_cliente} metros, você vai precisar de:'
      f'\n1. {quantas_latas:.2f} Lata(as) de tinta de 18 litros custando R$ {valor_final_lata:.2f}'
      f'\n2. {quantos_galao:.2f} Galão(ões) de tinta de 3,6 litros custando R$ {valor_final_galao:.2f}'
      f'\n3. {lata} lata(as) e  {galao} galão(ões) ao custo de R$ {preco:.2f}')