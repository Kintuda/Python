import random
while(True):
    try:
        player = str(input("Escolha entre pedra, papel, tesoura: ")).upper()
        escolha = ['PAPEL','TESOURA','PEDRA']
        vencedor = ''
        bot = random.choice(escolha)
        if(bot == player):
            vencedor = 'bot/player'
        if(player == 'PEDRA' and bot == 'PAPEL'):
            vencedor = 'bot'
        else:
            vencedor = 'player'
        if(player == 'TESOURA' and bot == 'PEDRA'):
            vencedor = 'bot'
        else:
            vencedor = 'player'
        if(player == 'PAPEL' and bot == 'TESOURA'):
            vencedor = 'bot'
        else:
            vencedor = 'player'
        print('Escolha do player: ' + player + ' ' + 'Escolha do bot:' +bot)
        print(vencedor)
    except KeyboardInterrupt:
        break
       

    

    

