class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'

    for caracter in expressao:
        if caracter.isdigit():
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.push(caracter)
        elif caracter == ')':
            while not operadores.is_empty() and operadores.top() != '(':
                posfixa.append(operadores.pop())
            if not operadores.is_empty() and operadores.top() == '(':
                operadores.pop()
        elif caracter in precedencia:
            while not operadores.is_empty() and precedencia.get(caracter, 0) <= precedencia.get(operadores.top(), 0):
                posfixa.append(operadores.pop())
            operadores.push(caracter)

    while not operadores.is_empty():
        posfixa.append(operadores.pop())

    return ''.join(posfixa)


expressao_infixa = input("Digite a expressão matemática na notação infixa: ")
expressao_posfixa = infixa_para_posfixa(expressao_infixa)
print("Expressão posfixa:", expressao_posfixa)