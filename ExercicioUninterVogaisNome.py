#FUNCAO PARA TROCAR AS VOGAIS USANDO REPLACE DE REPLACE
def nome(x):
    nomes=x.upper()
    new_nomes=nomes.replace('A','@').replace('E', '&').replace('I', '!').replace('O', '#').replace('U', '*')
    return new_nomes
#INCERSÃO DO NOME
x= input('Digite um nome: ')

# INPRESSAO DA SAIDA DE DADOS
print(x.upper())
print(nome(x))
