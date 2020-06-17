'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado'''
from time import sleep
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('CALCULANDO SUA NOTA...')
sleep(2)
média = (n1 + n2) / 2
print('Média: {}'.format(média))
if média < 5:
    print('Aluno \033[1;31mREPROVADO!\033[m')
elif média >= 7:
    print('Aluno está \033[1;32mAPROVADO!\033[m')
else:
    print('Aluno está de \033[1;33mRECUPERAÇÃO!\033[m')
