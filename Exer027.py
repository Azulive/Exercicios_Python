# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 >= n2 >= n3:
    ordem = [n1, n2, n3]
elif n1 >= n3 >= n2:
    ordem = [n1, n3, n2]
elif n2 >= n1 >= n3:
    ordem = [n2, n1, n3]
elif n2 >= n3 >= n1:
    ordem = [n2, n3, n1]
elif n3 >= n1 >= n2:
    ordem = [n3, n1, n2]
else:
    ordem = [n3, n2, n1]

print(f'Os números em ordem decrescente são:' ,ordem)