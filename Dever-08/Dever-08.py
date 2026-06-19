import heapq

def algoritmo_prim(grafo, vertice_inicial):
    mst = []
    visitados = set([vertice_inicial])
    
    arestas = [
        (peso, vertice_inicial, destino)
        for destino, peso in grafo[vertice_inicial].items()
    ]
    heapq.heapify(arestas)
    
    custo_total = 0

    while arestas and len(visitados) < len(grafo):
        peso, origem, destino = heapq.heappop(arestas)
        
        if destino not in visitados:
            visitados.add(destino)
            mst.append((origem, destino, peso))
            custo_total += peso
            
            for proximo_destino, proximo_peso in grafo[destino].items():
                if proximo_destino not in visitados:
                    heapq.heappush(arestas, (proximo_peso, destino, proximo_destino))
                    
    return mst, custo_total

grafo = {
    'A': {'B': 2, 'C': 6, 'D': 3},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 6, 'D': 4},
    'D': {'A': 3, 'B': 5, 'C': 4}
}

arestas_mst, custo = algoritmo_prim(grafo, 'A')

print("### Árvore Geradora Mínima (MST) ###\n")
for origem, destino, peso in arestas_mst:
    print(f"Vértice de Origem: {origem} | Vértice de Destino: {destino} | Peso: {peso}")

print(f"\nCusto Total (Soma dos pesos): {custo}")
