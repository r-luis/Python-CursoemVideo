'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''
print('CÁLCULO DE IMC')
peso = float(input('Qual o seu peso (em KG)? '))
altura = float(input('Qual a sua altura (em M): '))
imc = peso / (altura ** 2)
print('IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[31mABAIXO DO PESO.\nProcure um médico urgentemente.\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[34mPESO IDEAL.\nParabéns! Continue assim!\033[m')
elif imc >= 25 and imc < 30:
    print('\033[33mSOBREPESO.\nTome cuidado, controle sua alimentação.\033[m')
elif imc >= 30 and imc < 40:
    print('\033[31mOBESIDADE.\nProcure um médico.\033[m')
else:
    print('\033[1;30;41mOBESIDADE MÓRBIDA.\033[31m\nProcure um médico URGENTEMENTE!\033[m')
