
#def comida():
    #//print(ovos)
#ovos = 12
#comida()

def comida():
    ovos = 'variavel local de comida'
    print(ovos)

def bacon():
    ovos='variavel local de bacon'
    print(ovos)
    comida()
    print(ovos)

ovos='variavel global'
bacon()
print(ovos)

print('segundo exemplo: ')

def comida2():
    global ovos
    ovos='comida'

ovos='global'
comida2()
print(ovos)

