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


def binpradec(bin):
    pilha = Pilha()

    for digito in bin:
        pilha.empilhar(int(digito))

    dec = 0
    posicao = 0
    
    while not pilha.vazia():
        digito = pilha.desempilhar()
        dec += digito * (2 ** posicao)
        posicao += 1

    return dec

numbin = input("Digite um número binário: ")
numdec = binpradec(numbin)
print("Número decimal:", numdec)