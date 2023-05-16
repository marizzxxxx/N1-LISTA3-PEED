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


def calcular(nums):
    pilha = Pilha()

    for token in nums.split():
        if token.isdigit():
            pilha.empilhar(int(token))
        else:
            num2 = pilha.desempilhar()
            num1 = pilha.desempilhar()

            if token == "+":
                resultado = num1 + num2
            elif token == "-":
                resultado = num1 - num2
            elif token == "*":
                resultado = num1 * num2
            elif token == "/":
                resultado = num1 / num2

            pilha.empilhar(resultado)

    return pilha.desempilhar()


nums = input("Digite a expressão matemática na notação polonesa reversa: ")
resultado = calcular(nums)
print("Resultado:", resultado)