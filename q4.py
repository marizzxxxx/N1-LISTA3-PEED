class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.items.pop()
        else:
            return None

    def topo(self):
        if not self.vazia():
            return self.items[-1]
        else:
            return None

    def tamanho(self):
        return len(self.items)


def decprabin(dec):
    pilha = Pilha()

    while dec > 0:
        resto = dec % 2
        pilha.empilhar(resto)
        dec = dec // 2

    bin = ""
    while not pilha.vazia():
        bit = pilha.desempilhar()
        bin += str(bit)

    return bin


numdec = int(input("Digite um número decimal: "))
numbin = decprabin(numdec)
print("Número binário:", numbin)
