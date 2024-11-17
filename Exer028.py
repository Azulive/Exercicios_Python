# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno_trabalho = input('Em que turno você trabalha?'
                       '\nM - Matutino'
                       '\nV - Vespertino'
                       '\nN - Noturno'
                       '\n--------------------> ').lower().strip()[0]

if turno_trabalho == 'm':
    print('Bom Dia!')
elif turno_trabalho == 'v':
    print('Boa Tarde!')
elif turno_trabalho == 'n':
    print('Boa Noite')
else:
    print('Valor Inválido')