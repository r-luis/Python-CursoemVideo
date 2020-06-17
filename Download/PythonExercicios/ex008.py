#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
print('Conversor de medidas:\n','*'*20)

m = float(input('Digite uma medida em metros: '))
dm = m*10
cm = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000

print('-'*20)
print('{}m corresponde a:\n{}dm, {}cm e {}mm;'.format(m, dm, cm, mm))
print('Também corresponde a {:.2f}dam, {:.2f}hm e {:.2f}km.'.format(dam, hm, km))