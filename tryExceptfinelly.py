def div():
    try:
        num1=int(input("Digite um numero: "))
        num2=int(input("Digite outro numero: "))
        res=num1/num2
    except ZeroDivisionError:
        print("Opps! nao divida por zero")
    except:
        print("algo mais de errado")
    else:
        return res
    finally:
         print("Executará sempre")


print(div())