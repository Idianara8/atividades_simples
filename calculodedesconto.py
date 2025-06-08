valor=float(input('Qual é o valor da sua compra?( use ponto para destacar os centavos) R$:'))
desconto= valor - (valor * 5 / 100)
print('Com o desconto de 5%, o valor do produto ficará R${:.2f}' .format(desconto))

