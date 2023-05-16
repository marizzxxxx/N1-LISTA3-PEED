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


def verif(string):
    pilha = Pilha()

    string = string.replace(" ", "").lower()

    for char in string:
        pilha.empilhar(char)

    inverso = ""
    while not pilha.vazia():
        inverso += pilha.desempilhar()

    return string == inverso


txt = input("Digite uma string: ")
if verif(txt):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")
