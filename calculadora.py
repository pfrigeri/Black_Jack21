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
while continuar:
    n1 = int(input("\nDigite um número: "))
    for simbolo in operacoes:
        print(simbolo)
    op = input("Escolha uma operação: ")
    n2 = int(input("Digite outro número: "))
    resultado = operacoes[op](n1,n2)
    print(f"Resultado: {resultado}\n")
    continuar_operando = input("Deseja fazer outra operação a partir deste resultado?(s/n) ou [x] para encerrar: ").lower()
    if continuar_operando == "s":
        n1 = resultado
        op = input("Escolha uma operação(+ , - , * , /): ")
        n2 = int(input("Digite outro número: "))
        resultado = operacoes[op](n1,n2)
        print(f"Resultado: {resultado}\n")
        continuar_operando = input("Deseja fazer outra operação a partir deste resultado?(s/n) ou [x] para encerrar: ").lower()
        if continuar_operando == "x":
            print("Até logo !")
            break
    elif continuar_operando == "x":
        print("Até logo !")
        break