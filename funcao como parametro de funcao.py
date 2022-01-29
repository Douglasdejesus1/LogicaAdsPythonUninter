def imprime_com_condicao(num,fcond):
    if fcond(num):
        print(num)
def par(x):
    return x%2==0
def impar(x):
    return not par(x)
imprime_com_condicao(5,impar)

res=lambda x:x*x
print(res(3))

res=lambda x,y:x+y
print(res(3,5))