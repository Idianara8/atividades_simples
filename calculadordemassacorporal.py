peso= float(input('Qual é o seu peso? (kg):'))
altura= float(input('Qual é a sua altura? (m):'))
imc = peso / (altura ** 2)
print('o IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Voce esta abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está na faixa normal de peso')
elif 25 <= imc <30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print ('Você esta em obesidade')
elif imc >= 40:
    print('Você está na faixa de obesidade mórbida')


