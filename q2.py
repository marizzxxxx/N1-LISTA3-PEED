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


def inverter(frase):
    pilha = Pilha()
    palavras = frase.split()

    for palavra in palavras:
        pilha.empilhar(palavra)

    finvertida = ""
    while not pilha.vazia():
        palavra = pilha.desempilhar()
        finvertida += palavra + " "

    return finvertida.strip()


frase = input("Digite uma frase: ")
finvertida = inverter(frase)
print("A fdrase invertida, eh:", finvertida)
