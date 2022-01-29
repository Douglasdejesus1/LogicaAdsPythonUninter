while True:
    #DESCRICAO DA POSICAO DOS QUARTOS
    print("       HOTEL DOS ANIMAIS")
    print('Especificando posição:')
    print('[1,2,3,4]')
    print('[5,6,7,8]')
    print()

    print('Bem vindos a fase 1!')
    print('Na Fase 1 o jogador deve alocar o RATO e o GATO na seguinte matriz que representra os quartos:')
    hotel=[['*','*','_','G'],['R','_','*','*']]

    #IMPRESSÃO DA LISTA DE LISTAS COM O FOR
    for linha in hotel:
        print(linha)
    #INSERÇÃO DE DA JOGADA DO PLAYER
    posi_rato=int(input('Em qual posição quer alocar o RATO? '))
    posi_gato=int(input('Em qual posição quer alocar o GATO? '))
    #COMPARAÇÃO LOGICA PARA AVANÇAR O PERDER O JOGO
    if posi_rato==6 and posi_gato==3:
        print('Parabens, passe a proxima fase!')
    else:
        print('Game over!!')
        break
    print()
    print('Na Fase 2 o jogador deve alocar os CAES e o OSSO na seguinte matriz que representra os quartos:')
    hotel=[['_','*','*','*'],['*','C','_','_']]
    for linha in hotel:
        print(linha)
    posi_osso=int(input('Em qual posição quer alocar o OSSO? '))
    posi_cao1=int(input('Em qual posição quer alocar o primeiro CAO? '))
    posi_cao2=int(input('Em qual posição quer alocar o segundo CAO? '))

    if posi_osso==1 and (posi_cao1==7 or posi_cao1==8) and (posi_cao2==7 or posi_cao2==8):
        print('Parabens, passe a proxima fase!')
    else:
        print('Game over!!')
        break
    print()
    print('Na Fase 3 o jogador deve alocar o GATO, o RATO e o OSSO na seguinte matriz que representra os quartos:')
    hotel=[['_','*','*','*'],['_','G','_','*']]
    for linha in hotel:
        print(linha)
    posi_gato=int(input('Em qual posição quer alocar o GATO? '))
    posi_rato=int(input('Em qual posição quer alocar o RATO? '))
    posi_osso=int(input('Em qual posição quer alocar o OSSO? '))

    if posi_gato==7 and posi_rato==1 and posi_osso==5:
        print('Parabens, passe a proxima fase!')
    else:
        print('Game over!!')
        break
    print()
    print('Na Fase 4 o jogador deve alocar os QUEIJOS e o OSSO na seguinte matriz que representra os quartos:')
    hotel=[['_','_','_','*'],['*','R','*','*']]
    for linha in hotel:
        print(linha)
    posi_queijo1=int(input('Em qual posição quer alocar o primeiro QUEIJO? '))
    posi_queijo2=int(input('Em qual posição quer alocar o segundo QUEIJO? '))
    posi_osso=int(input('Em qual posição quer alocar o OSSO? '))

    if posi_osso==2 and (posi_queijo1==1 or posi_queijo1==3) and (posi_queijo2==1 or posi_queijo2==3):
        print('Você ganhou!')
        break
    else:
        print('Game over!!')
        break
