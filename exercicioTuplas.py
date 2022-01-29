palavras=('douglas','hanna','flavia','mouse','janela','cadeira','tech','java','tv','note')
print(palavras)

for palavra in palavras:
    print('\nPalavras: {}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(),end='')


