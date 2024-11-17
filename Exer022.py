# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ').lower().strip()[0]

if letra in ('aeiou'):
    print('É vogal')
else:
    print('É consoante')