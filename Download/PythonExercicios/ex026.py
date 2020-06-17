"""Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez. """

frase = str(input('Digite uma frase: ')).strip().upper()
#up = frase.upper()
print('Quantas vezes aparece a letra A? {}'.format(frase.count('A')))
print('Primeira letra A: Posição {}'.format(frase.find('A')+1))
print('Última letra A: Posição {}'.format(frase.rfind('A')+1))
