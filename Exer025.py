# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior é: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior é: {n2}')
else:
    print(f'O maior é: {n3}')


if n1 < n2 and n1 < n3:
    print(f'O menor é: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor é: {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor é: {n3}')