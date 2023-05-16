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


def decprahex(dec):
    pilha = Pilha()
    nums = "0123456789ABCDEF"

    while dec > 0:
        resto = dec % 16
        pilha.empilhar(resto)
        dec = dec // 16

    hexa = ""
    while not pilha.vazia():
        digito = pilha.desempilhar()
        hexa += nums[digito]

    return hexa


numdec = int(input("Digite um número decimal: "))
numhex = decprahex(numdec)
print("Número hexadecimal:", numhex)