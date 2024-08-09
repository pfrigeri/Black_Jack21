#Criar um laço que receba nome e lance do participante e guarde estas variaveis no dicionario
    #Continuar até que não tenha mais nenhum outro participante diferente

#Fazer um dicionario cotendo o nome do participante como chave e sua oferta como valor

#A Ultima maior oferta será o proximo limite minimo para aquisição do bem

#Limpar a tela a cada lance para que haja sigilo

#Colocar este dicionario em laço e verificar quem deu o maior lance

lances_leilao = {}

comprador_final = ""
another_person = True
lance_minimo = float(input("Digite o lance mínimo: "))

while another_person:
    nome = input("Nome do Participante: ")
    #print(f"Lance Minimo: {lance_minimo}")
    oferta = float(input("Lance: R$"))
    if oferta < lance_minimo:
        print("Seu lance foi abaixo do mínimo. Faça outro lance.")
        pass
    else:
        #lance_minimo = oferta
        lances_leilao[nome] = oferta,
    continuar = input("Há algum outro participante?(sim/nao): ").lower()
    print("\n"*10)
        
    if continuar == "nao":
        another_person = False

def Vencedor_Leilao(lances_dicionario):
    maior_oferta = 0
    for participante in lances_dicionario:
        print(participante)
        print(f"Lance Ofertado:R${lances_dicionario[participante]}")     
        if lances_dicionario[participante] > maior_oferta:
            maior_oferta = lances_dicionario[participante]
            comprador_final = participante 
    print(f"Parabéns {comprador_final} !\n Você venceu o leilão e portanto é o comprador do item ! ")   


Vencedor_Leilao(lances_leilao)


print(lances_leilao)



