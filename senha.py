import random
while True:
    try:
        caracteres = 'abcdefghijklmnopqrstuvwxyz123456789/*-!?'
        tamanho = int(input("Digite o tamanho da senha: "))
        if(tamanho >= 10 ):
            senha = ''
            for i in range(tamanho):
                digito = random.choice(caracteres)
                senha += digito
            print("Senha gerada: " + str(senha))
            print("Pressione CTRL + C + Enter para sair")
        else:
            print("Senha deve conter pelo menos 10 caracteres")
    except KeyboardInterrupt:
        break
    except ValueError:
        print("Tamanho deve ser um número")
    