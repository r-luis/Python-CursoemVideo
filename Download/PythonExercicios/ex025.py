"""Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome."""
nome = str(input('Digite o seu nome: ')).strip()
enc = 'SILVA' in nome.upper()
if enc is True:
    print('Seu nome tem Silva.')
else:
    print('Você não tem Silva no nome.')