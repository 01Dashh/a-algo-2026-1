import sys
import time

# Aumenta o limite de recursão
sys.setrecursionlimit(2000)

def fatorial_recursivo(n):
    # Base: o fatorial de 0 ou 1 é 1
    if n <= 1:
        return 1
    # Recursivo: n * fatorial de (n-1)
    else:
        return n * fatorial_recursivo(n - 1)

# Valores para o teste
valores_teste = [10, 100, 500, 1000]

print(f"{'n':<10} | {'Tempo de Execução (segundos)':<30}")
print("-" * 45)

for n in valores_teste:
    inicio = time.perf_counter()
    resultado = fatorial_recursivo(n)
    fim = time.perf_counter()
    
    tempo_total = fim - inicio
    print(f"{n:<10} | {tempo_total:.10f}")