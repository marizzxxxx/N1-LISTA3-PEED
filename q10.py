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


def expv(exp):
    pilha = Pilha()
    pares = {"(": ")", "{": "}", "[": "]"}
    operadores = ["+", "-", "*", "/"]

    for char in exp:
        if char in "({[":
            pilha.empilhar(char)
        elif char in ")}]":
            if pilha.vazia() or pares[pilha.desempilhar()] != char:
                return False
        elif char in operadores:
            if pilha.vazia() or not pilha.topo() in operadores:
                return False
        elif char.isdigit():
            if not pilha.vazia() and pilha.topo() in operadores:
                pilha.desempilhar()

    return pilha.vazia()


exp = input("Digite uma expressão aritmética: ")
if expv(exp):
    print("A expressão é válida.")
else:
    print("A expressão não é válida.")
