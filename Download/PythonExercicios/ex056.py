#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo.
#O nome do homem mais velho
#Quantas mulheres tem menos de 20 anos
idgrupo = 0
media = 0
man = 0
nameman = ''
woman = 0
for grupo in range(1, 5):
    print('{:-^20}'.format(' {}ª Pessoa '.format(grupo)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idgrupo += idade #média
    if grupo == 1 and sexo in 'Mm':
        man = idade
        nameman = nome
    if sexo in 'Mm' and idade > man:
        man = idade
        nameman = nome
    if idade < 20 and sexo in 'Ff':
        woman += 1
media = idgrupo / 4
print('Média de idade do grupo: {} anos.'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nameman, man))
print('O número de mulheres menores de 20 anos é de {}.'.format(woman))


