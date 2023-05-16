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


def bin(num):
    
    pilha = Pilha()
    
    while num > 0:
        digito = num % 2
        pilha.empilhar(digito)
        num = num // 2

    bina = ""
    while not pilha.vazia():
        bina += str(pilha.desempilhar())

    return bina


nums = input("Digite uma string contendo números: ")
numdec = int(nums)
numbin = bin(numdec)
print("Número binário:", numbin)