# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Digite uma letra: ').lower().strip()[0]

if letra == 'f':
    print('Feminino')
elif letra == 'm':
    print('Masculino')
else:
    print('Sexo inválido')