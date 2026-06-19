import math
from collections import Counter

def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

clientes_treino = [
    ((40, 20), "Conservador", "Ana"),
    ((50, 35), "Conservador", "Bruno"),
    ((90, 80), "Agressivo", "Carlos"),
    ((80, 65), "Agressivo", "Diana")
]

alvo = (60, 45)
nome_alvo = "Arthur"
k = 3

distancias = []
for dados, perfil, nome in clientes_treino:
    dist = distancia_euclidiana(alvo, dados)
    distancias.append((dist, perfil, nome))

distancias.sort(key=lambda x: x[0])

vizinhos_proximos = distancias[:k]

print(f"--- Distâncias calculadas para {nome_alvo} {alvo} ---")
for dist, perfil, nome in distancias:
    print(f"Cliente: {nome:<7} | Distância: {dist:.2f} | Perfil: {perfil}")

print(f"\n--- Top {k} vizinhos mais próximos ---")
votos = []
for dist, perfil, nome in vizinhos_proximos:
    print(f"Vizinho: {nome:<7} | Voto: {perfil}")
    votos.append(perfil)

contagem_votos = Counter(votos)
perfil_vencedor = contagem_votos.most_common(1)[0][0]

print(f"\nResultado Final: O perfil classificado para {nome_alvo} é **{perfil_vencedor}**.")
