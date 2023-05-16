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


def hexapradec(hexa):
    
    pilha = Pilha()

    for digito in hexa:
        pilha.empilhar(digito)

    dec = 0
    posicao = 0
    
    while not pilha.vazia():
        digito = pilha.desempilhar()
        if digito.isdigit():
            dec += int(digito) * (16 ** posicao)
        else:
            dec += (ord(digito.upper()) - ord('A') + 10) * (16 ** posicao)
        posicao += 1

    return dec


numhexa = input("Digite um número hexadecimal: ")
numdec = hexapradec(numhexa)
print("Número decimal:", numdec)