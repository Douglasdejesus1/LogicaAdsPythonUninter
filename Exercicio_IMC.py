def entrada_dados(nome,peso,altura):
    #INSERINDO NO DICIONÁRIO
    cadastro['nome']=nome.upper()
    cadastro['peso']=peso
    cadastro['altura']=altura
    #INSERINDO NA LISTA
    lista.append(cadastro.copy())
def procesamento_dados(peso,altura):
    IMC=peso/(altura**2)
    return IMC
def impressao(lista):
    for elemento in lista:
        for i,j in elemento.items():
            print("{}:{}".format(i,j))
        print("_____________________")

lista=[]
cadastro={}

while True:
    nome=input('Qual o nome? ')
    peso = float(input('Qual o peso? '))
    altura=float(input('Qual a altura? '))

    #CHAMADA DE FUNCAO
    entrada_dados(nome, peso, altura)
    imc=procesamento_dados(peso,altura)
    print(lista)
    if lista:
        impressao(lista)
        print('{} tem por imc: {:.2f}'.format(nome,imc))
    else:
        print('Lista Vazia')

    opcao=int(input('Deseja encerrar o programa? 0-sim 1-nao '))
    if opcao ==0:
        print('Fim do program!!!')
        break






