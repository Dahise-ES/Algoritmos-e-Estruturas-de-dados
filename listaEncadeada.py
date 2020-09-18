from node import Node


class ListaLigada:
    def __init__(self):
        self.head = None  # posição inicial da lista
        self.size = 0  # tamanho da lista

    def append(self, elem):  # adiciona um item ao final da lista
        if self.head:
            # quando a lista ja possui elementos
            ponteiro = self.head  # o ponteiro começa do começo da lista

            while ponteiro.next:  # laço para percorrer os elementos da lista
                ponteiro = ponteiro.next
            ponteiro.next = Node(elem)  # adiciona o novo elemento no proximo espaço e liga com o anterior

        else:
            # quando a lista não tem elementos
            self.head = Node(elem)  # o novo elemento será a cabeça da lista
        self.size = self.size + 1  # após adicionado um elemento na lista ela aumenta seu tamanho em +1

    def __len__(self):
        # retorna o tamanho da lista
        return self.size

    def getnode(self, index):  # retorna o ponteiro do index
        ponteiro = self.head

        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("List index out of range")
        return ponteiro

    def __getitem__(self, index):  # visualizar o dado do elemento
        # a = lista[index]
        ponteiro = self.getnode(index)
        if ponteiro:
            return ponteiro.dado
        else:
            raise IndexError("List index out of range")

    def __setitem__(self, index, elem):  # modificar o dado
        # lista[index] = 9
        ponteiro = self.getnode(index)
        if ponteiro:
            ponteiro.dado = elem
        else:
            raise IndexError("List index out of range")

    def index(self, elem):  # retorna o index do elemento
        ponteiro = self.head
        i = 0
        while ponteiro:
            if ponteiro.dado == elem:
                return i
            else:
                ponteiro = ponteiro.next
                i += 1
        raise ValueError("{} is not in List".format(elem))

    def inserir(self, index, elem):  # adiciona um elemento em qualquer lugar da lista
        node = Node(elem)  # cria um nó para o novo elemento
        if index == 0:
            node.next = self.head  # adiciona na cabeça
            self.head = node
        else:
            ponteiro = self.getnode(index - 1)  # encontra o index do elemento anterior do index que queremos adicionar
            node.next = ponteiro.next  # liga o ponteiro next do novo elemento ao proximo elemento da lista
            ponteiro.next = node  # adiciona o novo elemento
        self.size += 1

    def remover(self, elem):  # remove um elemento da lista

        if self.head is None:  # se a lista estiver vazia
            raise ValueError("{} is not in List".format(elem))

        elif self.head.dado == elem:  # remover a cabeça
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            anterior = self.head  # remover qualquer elemento
            ponteiro = self.head.next
            while ponteiro:
                if ponteiro.dado == elem:  # verifica se o dado do ponteiro é igual ao elemento que queremos eliminar
                    anterior.next = ponteiro.next  # exclui a ponte entre o anterior e o elemento removido e liga com o proximo elemento
                    ponteiro.next = None
                    self.size -= 1
                    return True
                anterior = ponteiro
                ponteiro = ponteiro.next
        raise ValueError("{} is not in List".format(elem))

    # imprimir a lista completa

    def __repr__(self):
        r = ""
        ponteiro = self.head
        while ponteiro:
            r = r + str(ponteiro.dado) + "->"
            ponteiro = ponteiro.next
        return "[" + r + "]"

    def __str__(self):
        return self.__repr__()
