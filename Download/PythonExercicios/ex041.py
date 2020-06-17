'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mosrte sua categoria, de acordo com a idade:
- Até 9: MIRIM
- Até 14: INFANTIL
- Até 19: JÚNIOR
- Até 25: SÊNIOR
- Acima: MASTER'''
from datetime import date
y = date.today() .year
print('\033[1;30;44mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('-'*32)
ano = int(input('Digite o ano de nascimento para saber sua categoria: '))
idade = y - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: \033[36mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[36mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[36mJÚNIOR\033[m')
elif idade <= 25:
    print('Categoria: \033[36mSÊNIOR\033[m')
else:
    print('Categoria: \033[36mMASTER\033[m')
print('-'*32)
print('\033[1;34mA Confederação agradece\033[m!')
