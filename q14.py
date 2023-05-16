# Código essencial da pilha
class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def topo(self):
        if not self.vazia():
            return self.itens[-1]

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()

def polon(exp):
    
    nums = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    pilha = Pilha()
    saida = []

    for caracter in exp:
        if caracter.isdigit():
            saida.append(caracter)
        elif caracter in nums:
            while (not pilha.vazia()) and (pilha.topo() in nums) and (nums[caracter] <= nums[pilha.topo()]):
                saida.append(pilha.desempilhar())
            pilha.empilhar(caracter)
        elif caracter == "(":
            pilha.empilhar(caracter)
        elif caracter == ")":
            while (not pilha.vazia()) and (pilha.topo() != "("):
                saida.append(pilha.desempilhar())
            if not pilha.vazia() and pilha.topo() == "(":
                pilha.desempilhar()

    while not pilha.vazia():
        saida.append(pilha.desempilhar())

    return "".join(saida)

exp = "(2+3)*4^2"
print(polon(exp)) 