#Calculadora Simples

def adicao(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

add = adicao
sub = subtracao
mult = multiplicacao
div = divisao

#Dicionario

operacoes = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

#Laço

continuar = True
while True:
    #Permite que o usuario faça outra conta sem nenhuma relação com a anterior ou encerre o programa
    n1 = int(input("\nDigite um número ou [0] para encerrar: "))
    if n1 == 0:
        print("Até logo !")
        break
    while continuar:
    #Separa a atribuição do primeiro número do resto do programa permitindo tanto que uma conta com o resultado anterior seja efetuada
    #quanto que uma conta completamente nova seja executada.
        for simbolo in operacoes:
            print(simbolo)
        op = input("Escolha uma operação: ")
        n2 = int(input("Digite outro número: "))
        resultado = operacoes[op](n1,n2)
        print(f"{n1} {op} {n2} = {resultado}\n")
        continuar_operando = input(f"Deseja fazer outra operação a partir do numero {resultado} ? (s/n): ").lower()
        if continuar_operando == "s":
            n1 = resultado
        elif continuar_operando == "n":
            continuar = False
            