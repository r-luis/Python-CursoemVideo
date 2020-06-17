'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar;
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

y = date.today().year
print('\033[7;32mExército Brasileiro - Alistamento Obrigatório\033[m')
print('-'*45)
nasc = int(input('Digite seu ano de nascimento: '))
idade = y - nasc #(ano atual - ano de nascimento)
if idade == 18:
    print('\033[1;32mEstá na hora de se alistar, procure o centro de alistamento mais próximo!\033[m')
elif idade > 18:
    diff = idade - 18
    ano = y - diff
    print('''\033[1;31mVocê deveria ter se alistado em {}.
Se você não se alistou ainda, você está {} ano(s) atrasado, procure o centro de alistamento mais próximo.\033[m
Caso contrário, obrigado por servir o Brasil!'''.format(ano, diff))
else:
    diff = 18 - idade
    ano = y + diff
    print('''\033[1;33mVocê ainda não está na idade para se alistar.
Para você ainda falta {} ano(s), que será em {}. Não se esqueça do seu dever com a pátria.\033[m'''.format(diff, ano))

print('-'*45)
print('\033[7;32mO Exército Brasileiro Agradece!\033[m')
