import os

palavra_secreta = input("Digite a palavra secreta: ")
quantidade_de_tentativas = input("Digite quantidade de tentativas: ")
quantidade_de_tentativas_INT = int(quantidade_de_tentativas)
letras_acertadas = ''
numero_tentativas = 0
os.system('cls')
while True:
    letra_digitada = input ("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("somente 1 letra")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    if numero_tentativas < quantidade_de_tentativas_INT:
        print(f'esta quase acabando as tentativas: {numero_tentativas}')
    elif numero_tentativas == quantidade_de_tentativas_INT:
        print(f'suas tentativas acabaram')
        print(f'foram: {numero_tentativas} tentativas')
        break
        
    
    print("palavra formada:", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCE GANHOU')
        print(f'a palavra era', palavra_secreta)
        print(f'foram: {numero_tentativas} tentativas')
        break   