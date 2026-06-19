# Complexidade de Tempo: O(n)

O raciocínio é simples: para calcular o fatorial de n, a função chama a si mesma n vezes.

Se n = 10, ocorrem 10 chamadas.
Se n = 1000, ocorrem 1000 chamadas.

Como o trabalho realizado dentro de cada chamada (uma subtração e uma multiplicação) é constante, o tempo de execução cresce de forma linear em relação a n.

# Complexidade de Espaço: O(n)

A recursão consome memória na pilha de chamadas. Cada vez que a função chama a si mesma, o estado atual é "guardado" na memória até que o caso base seja atingido. Portanto, para uma entrada n, ocupamos n espaços na pilha.

# Resultados:

n          | Tempo de Execução (segundos)  
---------------------------------------------
10         | 0.0000147000  
100        | 0.0000493000  
500        | 0.0002611000  
1000       | 0.0005420000
