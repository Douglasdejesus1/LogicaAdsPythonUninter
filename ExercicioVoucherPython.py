from random import seed
from random import randint
seed(100)
#funcao de coleta de dados
def insecao_dados(nome,email,telefone,curso):
    dados['Codigo']= randint(100,400)
    dados['Nome'] = nome
    dados['Email']=email
    dados['Telefone'] =telefone
    dados['Curso'] =curso
    cadastro.append(dados.copy())
#funcao de saida de dados
def impressao(cadastro):
    for e in cadastro:
        for i,j in e.items():
            print('{} : {}'.format(i,j))
        print()
    print()
#os dados foram coletados em dicionarios e armazandos na lista cadastro
dados={}
cadastro=[]
#programa principal
while True:
    print('**********MENU**********')
    print('1-Nova inscrição')
    print('2-Visualizar inscrição')
    print('0-Encerrar')
    x=int(input('Opção Escolhida: '))

    if x==1:
        nome=input('Digite seu nome: ')
        email=input('Digite seu email: ')
        telefone=int(input('Digite seu telefone: '))
        curso=input('Digite seu curso: ')
        insecao_dados(nome, email, telefone, curso)
        continue
    elif x==2:
        print('----------------LISTA DE INSCRITOS----------------')
        impressao(cadastro)

        continue
    elif x==0:
        break


