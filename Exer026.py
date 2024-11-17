# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

preco_1 = float(input('Digite o preço: R$ '))
preco_2 = float(input('Digite o preço: R$ '))
preco_3 = float(input('Digite o preço: R$ '))

if preco_1 > preco_2 and preco_1 > preco_3:
    print(f'O mais caro é: {preco_1}')
elif preco_2 > preco_1 and preco_2 > preco_3:
    print(f'O mais caro é: {preco_2}')
else:
    print(f'O mais caro é: {preco_3}')


if preco_1 < preco_2 and preco_1 < preco_3:
    print(f'O mais barato é: {preco_1}')
elif preco_2 < preco_1 and preco_2 < preco_3:
    print(f'O mais barato é: {preco_2}')
elif preco_3 < preco_1 and preco_3 < preco_2:
    print(f'O mais barato é: {preco_3}')
