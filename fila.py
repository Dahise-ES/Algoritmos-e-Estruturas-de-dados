from node import Node


class Fila:
    def __init__(self):
        self.primeiro = None  # primeiro elemento da fila
        self.ultimo = None  # ultimo elemento da lista
        self.size = 0  # tamanho da fila

    def push(self, elem):  # insere um elemento na fila
        node = Node(elem)
        if self.ultimo is None:
            self.ultimo = node
            self.primeiro = node
        else:
            self.ultimo.next = node
            self.ultimo = node

        self.size += 1

    def pop(self):  # remove o ultimo elemento da fila
        if self.size > 0:
            elem = self.primeiro
            self.primeiro = self.primeiro.next
            self.size -= 1
            return elem
        else:
            raise IndexError("a fila está vazia")

    def peek(self):  # observa o ultimo elemento da lista
        if self.size > 0:
            return self.primeiro.dado
        else:
            raise IndexError("a fila está vazia")

    def __len__(self):
        # retorna o tamanho da lista
        return self.size

    def __repr__(self):
        if self.size > 0:
            r = ""
            ponteiro = self.primeiro
            while ponteiro:
                r = r + str(ponteiro.dado) + "\n"
                ponteiro = ponteiro.next
            return r
        else:
            raise IndexError("a fila está vazia")


    def __str__(self):
        return self.__repr__()
