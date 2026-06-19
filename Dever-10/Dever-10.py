def dijkstra(vertices, grafo, origem, destino):
    dist = {v: float('inf') for v in vertices}
    pred = {v: None for v in vertices}
    dist[origem] = 0
    visitados = set()

    print(f"{'Nó Visitado':<12} | " + " | ".join([f"Nó {v:<5}" for v in vertices]))
    print("-" * 65)

    while len(visitados) < len(vertices):
        u = min((v for v in vertices if v not in visitados), key=lambda v: dist[v], default=None)
        
        if u is None or dist[u] == float('inf'):
            break
            
        visitados.add(u)

        for v, peso in grafo.get(u, {}).items():
            if v not in visitados and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                pred[v] = u

        linha = []
        for v in vertices:
            d = dist[v] if dist[v] != float('inf') else '∞'
            p = pred[v] if pred[v] is not None else '-'
            linha.append(f"{str(d) + ' (' + str(p) + ')':<7}")
            
        print(f"{u:<12} | " + " | ".join(linha))

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = pred[atual]
    caminho.reverse()

    print("\n" + "=" * 30)
    print("RESULTADOS FINAIS")
    print("=" * 30)
    print(f"Caminho percorrido : {' -> '.join(map(str, caminho))}")
    print(f"Custo mínimo total : {dist[destino]}")

vertices = [0, 1, 2, 3, 4]
grafo = {
    0: {1: 4, 2: 1},
    2: {1: 2, 4: 5},
    1: {3: 1},
    3: {4: 1},
    4: {}
}

dijkstra(vertices, grafo, 0, 4)
