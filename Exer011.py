# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
nr = float(input('Digite um número real: '))

dobro_primeiro = n1 * 2 + ( n2 / 2 )
soma_triplo = (n1 * 3) + nr
terceiro_elevado = nr ** 3

print(f'O produto do dobro do primeiro com a metade do segundo é: {dobro_primeiro}'
      f'\nA soma do triplo do primeiro numero com o terceiro é: {soma_triplo}'
      f'\nO terceiro elevado ao cubo é: {terceiro_elevado}')