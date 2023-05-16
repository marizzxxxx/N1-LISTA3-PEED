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


def decpraoct(dec):
    pilha = Pilha()

    while dec > 0:
        resto = dec % 8
        pilha.empilhar(resto)
        dec = dec // 8

    oct = ""
    while not pilha.vazia():
        digito = pilha.desempilhar()
        oct += str(digito)

    return oct


numdec = int(input("Digite um número decimal: "))
numoct = decpraoct(numdec)
print("Número octal:", numoct)