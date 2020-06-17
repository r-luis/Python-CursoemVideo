'''Escreva um programa que leia um número inteiro qualquer e pela para o usuárui escolher
qual será a base de conversão:
- 1 para binário;
- 2 para octal;
- 3 para hexadecimal'''
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para Binário
[2] para Octal 
[3] para Hexadecimal''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção errada, tente novamente.')