from node import Node


class Pilha:
    def __init__(self):
        self.top = None  # ultimo elemento da lista
        self.size = 0  # tamanho da pilha

    def push(self, elem):  # insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self,):  # remove o ultimo elemento da pilha
        if self.size > 0:
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.dado
        else:
            raise IndexError("a pilha está vazia")

    def peek(self):  # observa o ultimo elemento da lista
        if self.size > 0:
            return self.top.dado
        else:
            raise IndexError("a pilha está vazia")

    def __len__(self):
        # retorna o tamanho da lista
        return self.size

    def __repr__(self):
        if self.size > 0:
            r = ""
            ponteiro = self.top
            while ponteiro:
                r = r + str(ponteiro.dado) + "\n"
                ponteiro = ponteiro.next
            return r
        else:
            raise IndexError("a pilha está vazia")


    def __str__(self):
        return self.__repr__()
