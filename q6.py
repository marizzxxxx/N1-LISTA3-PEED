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


def charbalan(string):
    pilha = Pilha()
    pares = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in "({[":
            pilha.empilhar(char)
        elif char in ")}]":
            if pilha.vazia() or pilha.desempilhar() != pares[char]:
                return False

    return pilha.vazia()


mat = input("Digite uma expressão com caracteres: ")
if charbalan(mat):
    print("Os caracteres estão balanceados.")
else:
    print("Os caracteres não estão balanceados.")