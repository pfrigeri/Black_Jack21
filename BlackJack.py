
#Definir Funções para otimizar o código. Tais como: Função para calcular os pontos, atualizar a mão do jogador, etc.

import random as rd
def inicio():
    inicio_partida = input("Digite 's' para jogar uma partida de 21 e 'n' para encerrar o programa: ").lower()
    if inicio_partida == 's':
        return True
    elif inicio_partida == 'n':
        return False
    else:
        print("Entrada Inválida ! Responda com: 's' ou 'n'.")
        inicio()

def pegar_carta(mao_do_baralho):
     #Puxa as primeiras cartas para a mão do jogador
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    if mao_do_baralho == []:
        mao_do_baralho += (rd.choices(cartas, k = 2))
    else:
        mao_do_baralho.append(rd.choice(cartas))
    return mao_do_baralho

def pontuador(mao_do_baralho):
    #Soma as cartas da mão do jogador compondo sua pontuação
    pontuacao = 0
    for carta in mao_do_baralho:
        pontuacao += carta
    #Se a carta for um 'A' ela pode transmutar seu valor para 1 precavendo a derrota por excedência
    if pontuacao > 21 and 11 in mao_do_baralho:
        pontuacao -= 10
    return pontuacao

def mostrar_mao(mao1,mao2,fim_de_jogo):
    #Mostra a mão e a pontuação do jogador e revela a segunda carta do distribuidor
    if fim_de_jogo == False:
        print(f"Estas são suas cartas: {mao1}.\nPontuação: {pontuador(mao1)}")
        print(f"Carta do Distribuidor:[Carta Oculta, {mao2[1]}].")
    else:
        print(f"Estas são suas cartas: {mao1}.\nPontuação: {pontuador(mao1)}")
        print(f"Cartas do Distribuidor: {mao2}.\nPontuação: {pontuador(mao2)}")

def Jogo():
    mao_jogador = []
    mao_distribuidor = []
    pontuacao_jogador = 0
    pontuacao_distribuidor = 0
    fim_de_jogo = False
    # for _ in range(2):  # Inicia o jogo com duas cartas para cada jogador
    #     pegar_carta(mao_jogador)
    #     pegar_carta(mao_distribuidor)

    #Pega as cartas do distribuidor
    while pontuacao_distribuidor < 17:
        mao_distribuidor = pegar_carta(mao_distribuidor)
        pontuacao_distribuidor = pontuador(mao_distribuidor)

    #Pega as cartas do Jogador
    while True:

        mao_jogador = pegar_carta(mao_jogador)
        pontuacao_jogador = pontuador(mao_jogador)

        if pontuacao_jogador >= 21:
                break
        
        mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)

        comprar_carta = input("Deseja comprar mais uma carta ? 's' ou 'n': ").lower()

        if comprar_carta == 's':
            continue
        elif comprar_carta == 'n':
            break

    #Verifica o Estado do jogo e o tipo de Vitório, Derrota ou Empate
    if pontuacao_jogador == 21 and pontuacao_distribuidor != 21:
            print(f"Você Fez {pontuacao_jogador} ! \nVocê Venceu !🎈🤞🤑🍀✨🎉\n")
            fim_de_jogo = True
            mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)
    elif pontuacao_jogador > 21:
            print("Sua pontuação estourou o limite.\n Você perdeu !😪😬👺💢💥\n")
            fim_de_jogo = True
            mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)
    elif pontuacao_jogador < 21 and pontuacao_distribuidor > 21:
        print("Você Venceu ! Seu oponente estourou o limite 😅💥\n")
        fim_de_jogo = True
        mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)
    elif pontuacao_jogador > pontuacao_distribuidor:
        print(f"Sua pontuação ({pontuacao_jogador}) foi maior que a do oponente ({pontuacao_distribuidor}).\nVocê Venceu !🎈✨🎉\n")
        fim_de_jogo = True
        mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)
    elif pontuacao_jogador == pontuacao_distribuidor:
        print(f"Vocês empataram... 😑✋😒✋\n")
        fim_de_jogo = True
        mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)
    elif pontuacao_distribuidor == 21 and pontuacao_jogador != 21:
        print(f"Você foi BRUTALMENTE ESMIGALHADO ! 😨😭😱💀\n Seu oponente Fez {pontuacao_distribuidor}🐐🍀\n")
        fim_de_jogo = True
        mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)
    elif pontuacao_jogador < pontuacao_distribuidor and pontuacao_distribuidor != 21:
        print(f"Seu Oponente obteve uma pontuação maior que a sua ({pontuacao_distribuidor})...Você perdeu !😪👺💢")
        fim_de_jogo = True
        mostrar_mao(mao_jogador, mao_distribuidor, fim_de_jogo)
     

while inicio():
    Jogo()
    print(10*"\n")
    
