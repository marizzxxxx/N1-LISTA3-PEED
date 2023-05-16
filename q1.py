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


def pb(mat):
    pilha = Pilha()

    for char in mat:
        if char == '(':
            pilha.empilhar(char)
        elif char == ')':
            if pilha.vazia() or pilha.desempilhar() != '(':
                return False

    return pilha.vazia()


mat = input("Digite uma expressão matemática: ")
if pb(mat):
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses não estão balanceados.")
