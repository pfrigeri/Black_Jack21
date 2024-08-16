
#A carta 'A' Pode mudar seu valor 

#Definir Funções para otimizar o código. Tais como: Função para calcular os pontos, atualizar a mão do jogador, etc.

import random as rd
def inicio():
    inicio_partida = input("Digite 's' para jogar uma partida de 21 e 'n' para encerrar o programa: ").lower()
    if inicio_partida == 's':
        partida = True
    elif inicio_partida == 'n':
        partida = False
    else:
        print("Entrada Inválida ! Responda com: 's' ou 'n'.")
        inicio()
    return partida

def pegar_carta(mao_do_baralho):
     #Puxa as primeiras cartas para a mão do jogador
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    mao_do_baralho += rd.choices(cartas, k = 2)
    #mao_do_baralho.append(rd.choices(cartas, k = 2))
    return mao_do_baralho

def pontuador(mao_do_baralho):
    #Soma as cartas da mão do jogador compondo sua pontuação
    pontuacao = 0
    for carta in mao_do_baralho:
        pontuacao += carta
    return pontuacao

def mostrar_mao(mao1,mao2,pontuacao1):
    print(f"Estas são suas cartas: {mao_jogador}.\nPontuação: {pontuacao_jogador}")
    print(f"Carta do Distribuidor: {mao_distribuidor}.")


mao_jogador = []
mao_distribuidor = []
pontuacao_jogador = 0
pontuacao_distribuidor = 0

partida = inicio()


while partida:

    mao_jogador = pegar_carta(mao_jogador)
    mao_distribuidor = pegar_carta(mao_distribuidor)

    pontuacao_jogador = pontuador(mao_jogador)
    pontuacao_distribuidor = pontuador(mao_distribuidor)

    mostrar_mao(mao_jogador, mao_distribuidor, pontuacao_jogador)

    comprar_carta = input("Deseja comprar mais uma carta ? 's' ou 'n': ").lower()
    if comprar_carta == 's':
        mao_jogador = pegar_carta(mao_jogador)
        mao_distribuidor = pegar_carta(mao_distribuidor)
        pontuacao_jogador = pontuador(mao_jogador)
        pontuacao_distribuidor = pontuador(mao_distribuidor)
        mostrar_mao(mao_jogador, mao_distribuidor, pontuacao_jogador)
        if pontuacao_jogador > 21:
            print("Sua pontuação estourou o limite.\n Você perdeu !😪😬👺💢💥")
    elif comprar_carta == 'n':
        if pontuacao_jogador > pontuacao_distribuidor:
            print(f"Sua pontuação ({pontuacao_jogador}) foi maior que a do oponente ({pontuacao_distribuidor}).\nVocê Venceu !🎈🤞🤑🍀✨🎉")
        elif pontuacao_jogador == pontuacao_distribuidor:
            print(f"Vocês empataram... 😑✋😒✋")
        elif pontuacao_jogador < pontuacao_distribuidor:
            print("Você perdeu !😪😬👺💢💥")

    partida = inicio()
    
