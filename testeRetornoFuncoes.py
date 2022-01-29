
while True:
    def valida_string(pergunta,min,max):
        s1=input(pergunta)
        tam=len(s1)
        while((tam<min) or(tam>max)):
            print('tente novamente')
            s1=input(pergunta)
            tam=len(s1)
        return s1
    x= valida_string('Digite uma senha de 4 a 8 caracteres: ',4,8)
    print('Você digitou a senha: {}. \n Dado válido.'.format(x))
    confirma=input('Posso confirmar? s/n')
    if confirma=='s':
        break


