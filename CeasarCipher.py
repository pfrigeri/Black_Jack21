alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def encrypt(original_text, shift):
    encoded = ""
    for letter in original_text: #Pega cada letra na mensagem
        if letter in alphabet: #Verifica se a letra está no alfabeto
            index = alphabet.index(letter) #Busca o index da letra caso estiver
            new_index = (index + shift) % len(alphabet) #Soma o Index ao número de posições a serem deslocdas e se o novo index for maior
            encoded += alphabet[new_index] # que o tamanho da lista o módulo é calculado garantindo uma rotação circular entre a lista.
        else:
            encoded += letter #caso o caractere não esteja no alfabeto ele será diretamente adicionado. Isso garante a inclusão de espaços 
    print(f"This is the encoded message: {encoded}")
            
def dencrypt(text, shift):
    decoded =""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift) % len(alphabet)
            decoded += alphabet[new_index]
        else:
            decoded += letter
    print(f"This is the encoded message: {decoded}")

def caesar(message, shift, direction):
    if direction == "encode":
        encrypt(message, shift)
    elif direction == "decode":
        dencrypt(message, shift)

caesar(text, shift, direction)



