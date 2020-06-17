'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto;
- à vista cartão: 5% de desconto;
- até 2x no cartão: preço normal;
- 3x + no cartão: 20% de juros'''
print('{:=^35}'.format(' LOJAS SIQUEIRA '))
#variáveis
preço = float(input('Qual o preço do produto? R$'))
dinheiro = preço - (preço * 10) / 100
cartaov = preço - (preço * 5) / 100
cartaop = preço + (preço * 20) / 100
#escolha do método de pagamento
print('Digite [ 1 ] para pagamento à vista em dinheiro ou cheque\n'
      'Digite [ 2 ] para pagamento à vista no cartão \n'
      'Digite [ 3 ] para pagamento no cartão parcelado')
pag = str(input('Qual o método de pagamento: '))
#Condições
if pag == '1':
    print('O preço final do produto será de R${:.2f}'.format(dinheiro))
elif pag == '2':
    print('O preço final do produto será de R${:.2f}'.format(cartaov))
elif pag == '3':
    par = int(input('Quantas parcelas: '))
    if par == 1:
        print('O mínimo de parcelas é de 2x.')
    elif par == 2:
        print('Ficará parcelado em {}x de R${:.2f}. Sem acréscimo.'.format(par, (preço/par)))
    else:
        print('Ficará parcelado em {}x de R${:.2f}, com acréscimo de 20%, que dá um total de: {:.2f}'.format(par, (cartaop / par), cartaop))
else:
    print('Erro na escolha de pagamento, tente novamente.')
print('OBRIGADO POR COMPRAR. VOLTE SEMPRE!')
