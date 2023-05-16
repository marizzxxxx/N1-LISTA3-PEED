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


def ordenar(lista):
    pilha = Pilha()

    for item in lista:
        while not pilha.vazia() and pilha.topo() > item:
            lista.append(pilha.desempilhar())
        pilha.empilhar(item)

    while not pilha.vazia():
        lista.append(pilha.desempilhar())

    return lista


lista = input("Digite uma lista de inteiros separados por espaço: ").split()
lista = [int(item) for item in lista]
ordenada = ordenar(lista)
print("Lista ordenada:", ordenada)