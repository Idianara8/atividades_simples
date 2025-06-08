import emoji

nome= input ('Me diga seu nome:')
print('Olá', nome)
print(emoji.emojize(':red_heart:'))

n1=int(input('Digite um número:'))
print('Isso mesmo', nome)
n2=int(input('Ótimo, agora digite mais um:'))
s= n1 + n2
print('A soma de {} e {} é igual a {}'.format(n1,n2,s))


