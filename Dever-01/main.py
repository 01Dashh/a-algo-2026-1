import random
import time

# Implementação do Insertion Sort O(n²)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


# Tamanhos das listas
tamanhos = [1000, 5000, 10000, 20000, 50000]

print("Comparação de desempenho: Insertion Sort vs Sorted (Timsort)\n")

for n in tamanhos:

    # Gera lista aleatória
    lista = [random.randint(0, 100000) for _ in range(n)]

    # Cópias da lista
    lista_insertion = lista.copy()
    lista_sorted = lista.copy()

    # Tempo do Insertion Sort
    inicio = time.time()
    insertion_sort(lista_insertion)
    fim = time.time()
    tempo_insertion = fim - inicio

    # Tempo do Sorted (Timsort)
    inicio = time.time()
    sorted(lista_sorted)
    fim = time.time()
    tempo_sorted = fim - inicio

    # Resultado
    print(f"Tamanho da lista: {n}")
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
    print(f"Sorted (Timsort): {tempo_sorted:.6f} segundos")
    print("-" * 40)