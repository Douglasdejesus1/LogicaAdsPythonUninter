cadastro={'nome':[],'sexo':[],'ano':[]}
soma= media=count=0
while True:
    terminar=input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para Sim ou N para Não')
        continue
    nome=input('Qual seu nome?')
    while True:
        sexo = input('Qual seu sexo?').upper()[0]
        if sexo in 'MF':
            break
        print('ERRRO! Por favor, digite apenas M ou F.')
    ano = int(input('Qual sua idade?'))
    soma+=ano
    count+=1
    cadastro['nome'].append(nome.upper())
    cadastro['sexo'].append(sexo.upper()[0])
    cadastro['ano'].append(ano)

print(cadastro)

print(f'Ao todo temos {(count)} pessoas cadastradas')
media=soma/count
print(f'a Media das idade é {(media)}')
print('As mulheres cadsatradas foram',end='')
for p in cadastro:
    if p cadastro.sexo=='F':
        print(p['nome'])