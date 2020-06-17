#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro do número digitado é {}, \nO triplo {}, \nA raiz quadrada é {:.2f}'.format(d, t, r))
