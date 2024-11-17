# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('Quanto você ganha por hora?: '))
horas_trabalho = float(input('Quantas horas por dia você trabalha?: '))

salario_mes = (salario_hora * horas_trabalho) * 22

print(f'Seu salário será de R${salario_mes:.2f}')