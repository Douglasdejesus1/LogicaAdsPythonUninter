qnt=0''
total=0

while True:
    idade=input('Qual a idade?')
    if idade =='sair':
        break
    qnt=qnt+1
    idade= int(idade)
    if (idade<3):
        preco=0
    else:
        if(idade<=12):
            preco=30
        else:
            preco=15
    total=total+preco



midade=total/qnt
print('Total de pessoas que compraram ingressos {}'.format(qnt))
print('Total de dinheiro arrecadado {}'.format(total))
print('A media arrecadade p pessoa é {}'.format(midade))






