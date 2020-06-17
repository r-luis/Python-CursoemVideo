#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
print('Descubra quantos litros de tinta são necessários para pintar a parede da sua casa: ')
h = float(input('Qual a altura da parede? '))
b = float(input('Qual a largura da parede? '))
mq = (b*h)
l = mq/2

print('É necessário {:.1f}L de tinta para pintar uma parede de {:.2f}m².'.format(l, mq))
