import math

def f_recursivo(n):
    # Caso Base: F(1) = 2
    if n == 1:
        return 2
    # Passo Recursivo: F(n) = 2 * F(n-1) + n^2
    else:
        return 2 * f_recursivo(n - 1) + n**2

# Solicitação do valor ao usuário
try:
    n_usuario = int(input("Digite o valor de n"))
    
    if n_usuario < 1:
        print("insira um número inteiro maior ou igual a 1.")
    else:
        resultado = f_recursivo(n_usuario)
        print(f"O resultado de F({n_usuario}) via recursão é: {resultado}")
        
except ValueError:
    print("Por favor, digite um número inteiro.")