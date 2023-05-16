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


def binprahexa(bin):
    pilha = Pilha()

    for digito in bin:
        pilha.empilhar(int(digito))

    hexa = ""
    while not pilha.vazia():
        grupo = ""
        for _ in range(4):
            digito = pilha.desempilhar()
            if digito is None:
                break
            grupo += str(digito)

        hexad = hex(int(grupo, 2))[2:].upper()
        hexa = hexad + hexa

    return hexa

numbin = input("Digite um número binário: ")
numhexa = binprahexa(numbin)
print("Número hexadecimal:", numhexa)