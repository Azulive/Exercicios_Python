# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


altura = float(input('Qual a sua altura?: '))
sexo = input('Qual o seu sexo?:[M/F]').strip().lower()[0]

if sexo == 'm':
    peso_ideal_m = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso_ideal_m:.2f}')
elif sexo == 'f':
    peso_ideal_f = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal_f:.2f}')