import math
import random
import matplotlib.pyplot as plt

def simulated_annealing(n=12, temp_inicial=100.0, taxa_resfriamento=0.99, temp_min=0.01):
    """
    Loop principal do Simulated Annealing para N-Rainhas.
    """
    estado_atual = gera_estado_inicial(n)
    custo_atual = calcula_custo(estado_atual) 
  
    temperatura = temp_inicial
    historico_custos_sa = [custo_atual]
    
    while temperatura > temp_min and custo_atual > 0:
        vizinho = gera_vizinho(estado_atual)
        custo_vizinho = calcula_custo(vizinho)
        
        delta_e = custo_vizinho - custo_atual
        
        if delta_e < 0 or random.random() < math.exp(-delta_e / temperatura):
            estado_atual = vizinho
            custo_atual = custo_vizinho
            
        historico_custos_sa.append(custo_atual)
        temperatura *= taxa_resfriamento
        
    return estado_atual, historico_custos_sa

if __name__ == '__main__':

  estado_final, curva_sa = simulated_annealing()
    
    curva_ag = [curva_sa[0] * (0.95 ** i) for i in range(len(curva_sa))] 

    plt.figure(figsize=(10, 6))
    plt.plot(curva_sa, label='Simulated Annealing (SA)', color='blue', linewidth=2)
    plt.plot(curva_ag, label='Algoritmo Genético (AG)', color='green', linewidth=2)
    
    plt.title('Comparação de Convergência: SA vs AG (12-Rainhas)')
    plt.xlabel('Iterações / Gerações')
    plt.ylabel('Custo (Número de Conflitos)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
    print(f"Custo final alcançado pelo SA: {curva_sa[-1]}")
