import math

def f_recursivo(n):
    # Caso base
    if n == 1:
        return 2
    # Chamada recursiva: F(n) = 2 * F(n-1) + n^2
    return 2 * f_recursivo(n - 1) + n**2

def f_fechada(n):
   
    return 3 * math.pow(2, n) - math.pow(n, 2) - (2 * n) - 3

# Entrada do usuário
try:
    n = int(input("Digite o valor de n: "))

    if n < 1:
        print("O valor deve ser maior ou igual a 1.")
    else:
        
        res_rec = f_recursivo(n)
        
        res_fechado = f_fechada(n)

        print(f"\n--- Resultados para F({n}) ---")
        print(f"Recursivo: {res_rec}")
        print(f"Fórmula Fechada: {int(res_fechado)}")

except ValueError:
    print("Entrada inválida, Digite um número inteiro.")