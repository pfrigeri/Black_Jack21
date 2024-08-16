#Criar uma lista contendo todas as possíveis cartas a serem sorteadas para os jogadores
     #Mostrar as cartas sorteadas
     #Perguntar se o jogador deseja sortear mais cartas
#Somar as cartas compondo a pontuação dos jogadores
    #Se a pontuação passar de 21 o jogador perde
#A carta 'A' Pode mudar seu valor 

#Perguntar se o jogador deseja jogar novamente (deixando o jogo em laço)
import random as rd

cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]

mao_jogador = []
mao_distribuidor = []
pontuacao_jogador = 0
pontuacao_distribuidor = 0

inicio_partida = input("Digite 's' para jogar uma partida de 21 e 'n' para encerrar o programa: ").lower()
if inicio_partida == 's':
    partida = True
elif inicio_partida == 'n':
    partida = False
else:
    print("Entrada Inválida ! Responda com: 's' ou 'n'.")

while partida:
    #Puxa as duas primeiras cartas para a mão do jogador
    mao_jogador += rd.choices(cartas, k = 2)
    #Soma as cartas da mão do jogador compondo sua pontuação
    for carta in mao_jogador:
        pontuacao_jogador += carta

    mao_distribuidor.append(rd.choice(cartas))
    for carta in mao_distribuidor:
        pontuacao_distribuidor += carta
    print(f"Estas são suas cartas: {mao_jogador}.\nPontuação: {pontuacao_jogador}")
    print(f"Carta do Distribuidor: {mao_distribuidor}.")
    comprar_carta = input("Deseja comprar mais uma carta ? 's' ou 'n': ").lower()
    if comprar_carta == 's':
        mao_jogador.append(rd.choice(cartas))
        if pontuacao_jogador > 21:
            print("Sua pontuação estourou o limite.\n Você perdeu !😪😬👺💢💥")
    elif comprar_carta == 'n':
        if pontuacao_jogador > pontuacao_distribuidor:
            print(f"Sua pontuação ({pontuacao_jogador}) foi maior que a do oponente ({pontuacao_distribuidor}).\nVocê Venceu !🎈🤞🤑🍀✨🎉")
        elif pontuacao_jogador == pontuacao_distribuidor:
            print(f"Vocês empataram... 😑✋😒✋")
        elif pontuacao_jogador < pontuacao_distribuidor:
            print("Você perdeu !😪😬👺💢💥")
    break
    
print(mao_jogador, pontuacao_jogador, mao_distribuidor)
