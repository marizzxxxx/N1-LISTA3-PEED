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


def octpradec(oct):
    
    pilha = Pilha()

    for digito in oct:
        pilha.empilhar(int(digito))

    dec = 0
    posicao = 0
    
    while not pilha.vazia():
        digito = pilha.desempilhar()
        dec += digito * (8 ** posicao)
        posicao += 1

    return dec

numoct = input("Digite um número octal: ")
numdec = octpradec(numoct)
print("Número decimal:", numdec)