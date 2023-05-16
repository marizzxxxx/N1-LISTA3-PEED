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


def pradec(string):
    pilha = Pilha()
    numeros = "0123456789"

    for char in string:
        if char in numeros:
            pilha.empilhar(char)

    dec = 0
    posicao = 0
    
    while not pilha.vazia():
        digito = int(pilha.desempilhar())
        dec += digito * (10 ** posicao)
        posicao += 1

    return dec


nums = input("Digite uma string contendo números: ")
numdec = pradec(nums)
print("Número decimal:", numdec)
