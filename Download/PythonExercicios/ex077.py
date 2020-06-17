'''Desafio 77 Crie um programa que tenha uma tupla com várias palavras (Não usar acentos).
Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.'''
palavras = ('Luffy', 'Zoro', 'Nami', 'Sanji', 'Chopper', 'Robin', 'Franky', 'Brook', 'Jimbe')

vogais = 'aeiou'

for p in palavras:
    print(f'\nA palavra {p.upper()} temos como vogal: ', end='')
    for letra in p:
        if letra in p:
            if letra.lower() in vogais:
                print(letra.upper(), end=' ')
