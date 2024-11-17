# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

# calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_hora = float(input('Quanto você ganha por hora?: '))
horas_trabalho_mes = float(input('Quantas horas por mês você trabalha?: '))

salario_mes = (salario_hora * horas_trabalho_mes)

print(f'Seu salario bruto será de R${salario_mes:.2f}')

salario_bruto = salario_mes

ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sind = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - ir - inss - sind

print(f'Salário Bruto : R$ {salario_bruto:.2f}'
      f'\nIR (11%) : R$ {ir:.2f}'
      f'\nINSS (8%) : R$ {inss:.2f}'
      f'\nSindicato (5%) : R$ {sind:.2f}'
      f'\nSalário Líquido : R$ {salario_liquido:.2f}')




# salario / dias = / horas trabalhadas