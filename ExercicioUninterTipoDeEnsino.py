
tipodeensino=0

while True:
    #ENTRADA DE DADOS: NOME E IDADE
    crianca=input("Nome da criança: ")
    idade=int(input("Idade: "))
    #TESTE LOGICO PARA VER EM QUAL TIPODE ENSINO A IDADE SE ENQUANDRA
    if((idade>0) and (idade<=5)):
        tipodeensino='Educacao Infantil'
    elif((idade>=6) and (idade<=10)):
        tipodeensino='Enino Fundamental I'
    elif((idade>=11) and (idade<=14)):
        tipodeensino='Enino Fundamental II'
    elif(idade>=15):
        tipodeensino='Ensino Médio'
    #IMPRESSAO
    print('A aluna {} tem {} e está no {}'.format(crianca,idade,tipodeensino))
    saida = int(input("Deseja continuar 0-Não 1-Sim "))
    #VERIFICACAO LOGICA SE DESEJA REPETIR O PROGRAMA OU SAIR
    if (saida==1):
        continue
    if (saida==0):
        break