def bellman_ford(vertices, arestas, origem):
    dist = {v: float('inf') for v in vertices}
    pred = {v: None for v in vertices}
    dist[origem] = 0

    for i in range(1, len(vertices)):
        for u, v, w in arestas:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
        
        linha = f"Iteração {i} |"
        for v in vertices:
            d = dist[v] if dist[v] != float('inf') else '∞'
            p = pred[v] if pred[v] is not None else '-'
            linha += f" V{v}: {d} ({p}) |"
        print(linha)

    tem_ciclo = False
    for u, v, w in arestas:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            tem_ciclo = True
            break
            
    print(f"\nExiste ciclo negativo? {'Sim' if tem_ciclo else 'Não'}")

vertices = [0, 1, 2, 3, 4]
arestas = [
    (0, 1, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 1),
    (4, 3, -1)
]

bellman_ford(vertices, arestas, 0)
