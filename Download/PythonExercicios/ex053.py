#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
invertido = junto[::-1]
#letras = len(junto)
'''for letra in range(len(junto) -1, -1, -1):
    invertido += junto[letra]'''
if junto == invertido:
    print('{} invertido é {}. Ou seja, É UM PALÍNDROMO!'.format(junto, invertido))
else:
    print('{} invertido é {}. Ou seja, NÃO É UM PALÍNDROMO'.format(junto, invertido))
