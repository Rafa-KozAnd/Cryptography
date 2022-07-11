import binascii, re
from string import ascii_uppercase

def menu():
    print("\n\nCriptografar Mensagens: \n")
    print(" 1 - ROT-13")
    print(" 2 - TROCA DE DOIS VIZINHOS")
    print(" 3 - SEQUÊNCIA DO TECLADO")
    print(" 4 - CIFRA DE CÉSAR")
    print(" 5 - ZENIT POLAR")
    print(" 6 - TENIS POLAR")
    print(" 7 - MILET POLAR")
    print(" 8 - BINÁRIO")
    print(" 9 - HEXADECIMAL")
    print("10 - CÓDIGO MORSE\n")

    choice = input("Escolha uma criptografia: \n")
    decypher = input("[1] - Cifrar ou [2] - Decifrar?\n")

    if (decypher == "1"):
        msg = input("Digite a mensagem a ser criptografada:\n").upper()
        decypher = True
    elif (decypher == "2"):
        msg = input("Digite o criptograma a ser decifrado:\n").upper()
        decypher = False
    else:
        return "Opção Inváida!"

    if choice == "1":
        print(criptoRot13(msg))
        return menu()
    elif choice == "2":
        print(criptoTrocaVizinhos(msg))
        return menu()
    elif choice == "3":
        print(criptoSeqTeclado(msg, decypher))
        return menu()
    elif choice == "4":
        print(criptoCifraCesar(msg, decypher))
        return menu()
    elif choice == "5":
        print(criptoZenitPolar(msg, decypher))
        return menu()
    elif choice == "6":
        print(criptoTenisPolar(msg))
        return menu()
    elif choice == "7":
        print(criptoMiletPolar(msg))
        return menu()
    elif choice == "8":
        print(criptoBinario(msg, decypher))
        return menu()
    elif choice == "9":
        print(criptoHexadecimal(msg, decypher))
        return menu()
    elif choice == "10":
        print(criptoCodMorse(msg, decypher))
        return menu()
    else:
        print("Opção Inválida")
        return menu()


# 1 - ROT-13
def criptoRot13(msg: str) -> str:

    newMsg = ""

    for char in msg:
        if ord(char) < 78:
            newMsg += chr(ord(char) + 13)
        else:
            newMsg += chr(ord(char) - 13)

    return newMsg



# 2 - TROCA DE DOIS VIZINHOS
def criptoTrocaVizinhos(msg: str) -> str:

    newMsg = ""

    for char in msg:
        if ord(char) % 2 == 0:
            newMsg += chr(ord(char) - 1)
        else:
            newMsg += chr(ord(char) + 1)

    return newMsg



# 3 - SEQUÊNCIA DO TECLADO
def criptoSeqTeclado(msg: str, decypher: bool = False) -> str:
    encoder = {
        "A": "Q",
        "B": "W",
        "C": "E",
        "D": "R",
        "E": "T",
        "F": "Y",
        "G": "U",
        "H": "I",
        "I": "O",
        "J": "P",
        "K": "A",
        "L": "S",
        "M": "D",
        "N": "F",
        "O": "G",
        "P": "H",
        "Q": "J",
        "R": "K",
        "S": "L",
        "T": "Z",
        "U": "X",
        "V": "C",
        "W": "V",
        "X": "B",
        "Y": "N",
        "Z": "M",
    }
    decoder = {
        "Q": "A",
        "W": "B",
        "E": "C",
        "R": "D",
        "T": "E",
        "Y": "F",
        "U": "G",
        "I": "H",
        "O": "I",
        "P": "J",
        "A": "K",
        "S": "L",
        "D": "M",
        "F": "N",
        "G": "O",
        "H": "P",
        "J": "Q",
        "K": "R",
        "L": "S",
        "Z": "T",
        "X": "U",
        "C": "V",
        "V": "W",
        "B": "X",
        "N": "Y",
        "M": "Z",
    }

    newMsg = ""

    for char in msg:
        if decypher:
            newMsg += encoder[char]
        else:
            newMsg += decoder[char]

    return newMsg



# 4 - CIFRA DE CÉSAR
def criptoCifraCesar(msg: str, decypher: bool = False) -> str:
    encoder = list(ascii_uppercase)
    newMsg = ''

    vlr = int(input('Entre com o valor de deslocamento: '))

    for letter in msg:
        if decypher:
            idx = ord(letter)-65
            newMsg += encoder[(idx + vlr) % len(encoder)] if letter in encoder else letter
        else:
            idx = ord(letter)+65
            newMsg += encoder[(idx - vlr) % len(encoder)] if letter in encoder else letter

    return newMsg



# 5 - ZENIT POLAR
def criptoZenitPolar(msg: str, decypher: bool = False) -> str:
    encoder = {
        'z':'p',
        'e':'o',
        'n':'l',
        'i':'a',
        't':'r',
        'Z':'P',
        'E':'O',
        'N':'L',
        'I':'A',
        'T':'R',
        'p':'z',
        'o':'e',
        'l':'n',
        'a':'i',
        'r':'t',
        'P':'Z',
        'O':'E',
        'L':'N',
        'A':'I',
        'R':'T'
        }

    newMsg = ""

    newMsg = re.sub("|".join(encoder.keys()), lambda match: encoder[match.string[match.start():match.end()]], msg)
    
    return newMsg



# 6 - TENIS POLAR
def criptoTenisPolar(msg: str) -> str:
    encoder = {
        't':'p',
        'e':'o',
        'n':'l', 
        'i':'a', 
        's':'r',
        'T':'P',
        'E':'O',
        'N':'L',
        'I':'A',
        'S':'R',
        'p':'t',
        'o':'e',
        'l':'n',
        'a':'i',
        'r':'s',
        'P':'T',
        'O':'E',
        'L':'N',
        'A':'I',
        'R':'S'
        }

    newMsg = ""

    newMsg = re.sub("|".join(encoder.keys()), lambda match: encoder[match.string[match.start():match.end()]], msg)
    
    return newMsg



# 7 - MILET POLAR
def criptoMiletPolar(msg):
    encoder = {
        'm':'p',
        'i':'o',
        'l':'l',
        'e':'a',
        't':'r',
        'M':'P',
        'I':'O',
        'L':'L',
        'E':'A',
        'T':'R',
        'p':'m',
        'o':'i',
        'l':'l',
        'a':'e',
        'r':'t',
        'P':'M',
        'O':'I',
        'L':'L',
        'A':'E',
        'R':'T'
        }
    
    newMsg = ""

    newMsg = re.sub("|".join(encoder.keys()), lambda match: encoder[match.string[match.start():match.end()]], msg)

    return newMsg



# 8 - BINÁRIO
def criptoBinario(msg: str, decypher: bool = False) -> str:

    newMsg = ""

    for char in msg:
        if decypher:
            newMsg = ' '.join(format(ord(c), 'b') for c in msg)
        else:
            newMsg = "".join([chr(int(binary, 2)) for binary in msg.split(" ")])

    return newMsg


# 9 - HEXADECIMAL
def criptoHexadecimal(msg: str, decypher: bool = False) -> str:

    newMsg = ""

    for char in msg:
        if decypher:
            newMsg = binascii.hexlify(bytes(msg, "utf-8"))
            newMsg = str(newMsg).strip("b")
            newMsg = newMsg.strip("'")
        else:
            newMsg = binascii.unhexlify(bytes(msg, "utf-8"))
            newMsg = str(newMsg).strip("b")
            newMsg = newMsg.strip("'")

    return newMsg



# 10 - CÓDIGO MORSE
def criptoCodMorse(msg: str, decypher: bool) -> str:
    morse = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----'.split()
    alf = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

    newMsg = ""

    if decypher:
        for i in msg:
            if i == ' ':
                newMsg += ' '
            else:
                newMsg += morse[alf.index(i)]
                newMsg += ' '
        return newMsg[:-1]
    else:
        msg = msg.split(' ')
        for i in msg:
            i = i.split()
            for x in i:
                newMsg += alf[morse.index(x)]
            newMsg += ' '
        return newMsg


print(menu())