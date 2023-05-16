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


def binpraoct(bin):
    pilha = Pilha()

    for digito in bin:
        pilha.empilhar(int(digito))

    oct = ""
    while not pilha.vazia():
        grupo = ""
        for _ in range(3):
            digito = pilha.desempilhar()
            if digito is None:
                break
            grupo += str(digito)

        octa = str(int(grupo, 2))
        oct = octa + oct

    return oct

numbin = input("Digite um número binário: ")
numoct = binpraoct(numbin)
print("Número octal:", numoct)