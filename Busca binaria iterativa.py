def buscaBinaria(lista, elem):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if elem == lista[meio]:
            return meio
        elif elem < lista[meio]:
            fim = meio -1
        elif elem > lista[meio]:
            inicio = meio +1
    return -1


if __name__ == '__main__':
    lista = [1, 4, 7, 10, 35, 40, 69, 70, 76, 85, 86, 97, 110]
    x = buscaBinaria(lista, 35)
    if x == -1:
        print("elemento não encontrado")
    else:
        print(x)