import random

def subset_sum(S, T):
    """
    Função recursiva (Backtracking) para encontrar um subconjunto que some o alvo T.
    """
    def backtrack(index, current_sum, path):
        if current_sum == T and path:
            return path
        
        if index == len(S):
            return None
            
        incluir = backtrack(index + 1, current_sum + S[index], path + [S[index]])
        if incluir:
            return incluir
            
        excluir = backtrack(index + 1, current_sum, path)
        return excluir

    return backtrack(0, 0, [])

print("=== Caso 1: Tamanho Pequeno (n=4) ===")
S_pequeno = [2, 4, 6, 10]
T_pequeno = 16
resultado_pequeno = subset_sum(S_pequeno, T_pequeno)
print(f"S = {S_pequeno} | Alvo T = {T_pequeno}")
print(f"Subconjunto encontrado: {resultado_pequeno}\n")


print("=== Caso 2: Tamanho Médio (n=8) ===")
S_medio = [-5, -2, 1, 3, 7, 12, 15, 21]
T_medio = 0
resultado_medio = subset_sum(S_medio, T_medio)
print(f"S = {S_medio} | Alvo T = {T_medio}")
print(f"Subconjunto encontrado: {resultado_medio}\n")


print("=== Caso 3: Tamanho Grande (n=30) ===")
S_grande = [random.randint(10000, 99999) for _ in range(30)]
T_grande = 500000

elementos_forcados = [100000, 150000, 250000]
S_grande[:3] = elementos_forcados 
random.shuffle(S_grande)

print(f"S = {S_grande[:5]}... (30 elementos) | Alvo T = {T_grande}")
print("Buscando... (Isso pode levar alguns segundos dependendo da combinação)")

resultado_grande = subset_sum(S_grande, T_grande)
if resultado_grande:
    print(f"Subconjunto encontrado: {resultado_grande}")
    print(f"Soma de verificação: {sum(resultado_grande)}")
else:
    print("Nenhum subconjunto exato encontrado para este conjunto aleatório.")
