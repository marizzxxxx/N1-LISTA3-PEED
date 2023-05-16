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


def verifp(string):
    pilha = Pilha()

    for char in string:
        pilha.empilhar(char)

    inverso = ""
    while not pilha.vazia():
        digito = pilha.desempilhar()
        inverso += digito

    return string == inverso


num = input("Digite um número: ")
if verifp(num):
    print("A string é um número palíndromo.")
else:
    print("A string não é um número palíndromo.")