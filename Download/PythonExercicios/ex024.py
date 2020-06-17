"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'."""
cid = str(input('Digite o nome da sua cidade: ')).strip()
santo = (cid[:5].upper() == 'SANTO')
sao = (cid[:3].upper() == 'SÃO' or 'SAO')
santa = (cid[:5].upper() == 'SANTA')
ns = (cid[:12].upper() == 'NOSSA SENHORA')
sim = 'Sua cidade tem nome de Santo(a)!'
if santo is True:
    print(sim)
else:
    if sao is True:
        print(sim)
    else:
        if santa is True:
            print(sim)
        else:
            if ns is True:
                print(sim)
            else:
                print('Sua cidade não tem nome de Santo(a)')
