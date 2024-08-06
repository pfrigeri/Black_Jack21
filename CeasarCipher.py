alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift, encode_or_decode):
    if encode_or_decode == "decode":
        shift *= -1
    output = ""
    for letter in message: #Pega cada letra na mensagem
        if letter in alphabet: #Verifica se a letra está no alfabeto
            index = alphabet.index(letter) #Busca o index da letra caso estiver
            new_index = (index + shift) % len(alphabet) #Soma o Index ao número de posições a serem deslocdas e se o novo index for maior
            output += alphabet[new_index] # que o tamanho da lista o módulo é calculado garantindo uma rotação circular entre a lista.
        else:
            output += letter #caso o caractere não esteja no alfabeto ele será diretamente adicionado. Isso garante a inclusão de espaços 
    print(f"This is the {encode_or_decode}d message: {output}")

while True: #Uma Flag poderia ter sido usada também.
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    caesar(text, shift, direction)
    answer = input("Would you like to continue?: (yes/no)").lower()
    if answer == "no":
        print("See you later than !")
        break



