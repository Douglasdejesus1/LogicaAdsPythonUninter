valor=int(input('Digite um valor: '))
notas100=0
notas50=0
notas20=0
notas10=0
notas5=0
notas2=0
notas1=0

while True:
    if(valor>=100):
        notas100=valor//100
        valor=valor%100
        print('notas100= {}'.format(notas100))
        if not valor:
            break
    if(valor>=50):
        notas50=valor//50
        valor=valor%50
        print('notas50= {}'.format(notas50))
        if not valor:
            break
    if(valor>=20):
        notas20=valor//20
        valor=valor%20
        print('notas20= {}'.format(notas20))
        if not valor:
            break
    if(valor>=10):
        notas10=valor//10
        valor=valor%10
        print('notas10= {}'.format(notas10))
        if not valor:
            break
    if(valor>=5):
        notas5=valor//5
        valor=valor%5
        print('notas5= {}'.format(notas5))
        if not valor:
            break
    if(valor>=2):
        notas2=valor//2
        valor=valor%2
        print('notas2= {}'.format(notas2))
        if not valor:
            break
    if(valor>0):
        notas1=1
        print('notas1= {}'.format(notas1))
        break








