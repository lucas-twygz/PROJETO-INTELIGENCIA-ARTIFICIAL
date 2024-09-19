import numpy as np
import time

# Questão 1: Função que recebe um vetor com 8 componentes e retorna o número de conflitos
def f(sol):
    ataques = 0
    n = len(sol)
    for i in range(n):
        for j in range(i+1, n):
            if sol[i] == sol[j]: 
                ataques += 1
            if abs(sol[i] - sol[j]) == abs(i - j):
                ataques += 1
    return ataques

# Questão 2: Definição da temperatura inicial
T_initial = 100

# Questão 3: Testar três maneiras diferentes de escalonar a temperatura
def escalonamento_linear(T, alfa):
    return T * alfa

def escalonamento_log(T, k):
    return T / (1 + k * np.log(1 + k))

def escalonamento_exponencial(T, beta):
    return T * np.exp(-beta)

# Questão 4: Perturbação controlada para limitar o espaço de busca
def perturbar_limitado(sol):
    n = len(sol)
    sol_cand = sol.copy()
    col = np.random.randint(0, n)
    linha_nova = np.random.randint(0, n)
    
    while linha_nova == sol_cand[col]:
        linha_nova = np.random.randint(0, n)
    
    sol_cand[col] = linha_nova
    return sol_cand

# Questão 5: O algoritmo para quando o número máximo de iterações é atingido ou o valor ótimo é encontrado
def tempera_simulada(n_rainhas, max_iter=1000, T_min=1e-3, T_escalonamento='linear', alfa=0.99, beta=0.01):
    
    sol_atual = np.random.permutation(n_rainhas)
    custo_atual = f(sol_atual)

    melhor_sol = sol_atual.copy()
    melhor_custo = custo_atual

    T = T_initial
    historico_custo = [custo_atual]
    iteracao = 0
    
    while T > T_min and iteracao < max_iter:
        # gera solucao com pertubacao
        sol_cand = perturbar_limitado(sol_atual)
        custo_cand = f(sol_cand)
        
        # condicao para aceitacao de solucao
        if custo_cand < custo_atual:
            sol_atual = sol_cand
            custo_atual = custo_cand
            if custo_cand < melhor_custo:
                melhor_sol = sol_cand
                melhor_custo = custo_cand
        else:
            delta = custo_cand - custo_atual
            prob_aceitacao = np.exp(-delta / T)
            if np.random.rand() < prob_aceitacao:
                sol_atual = sol_cand
                custo_atual = custo_cand
        
        # escolher o melhor metodo de escalonamento
        if T_escalonamento == 'linear':
            T = escalonamento_linear(T, alfa)
        elif T_escalonamento == 'log':
            T = escalonamento_log(T, iteracao + 1)
        elif T_escalonamento == 'exponencial':
            T = escalonamento_exponencial(T, beta)
        
        iteracao += 1
        historico_custo.append(custo_atual)
        
        if melhor_custo == 0:
            break

    return melhor_sol, melhor_custo, historico_custo


# Questão 6: Avaliar o custo computacional e rodar até encontrar todas as soluções
def solucoes_otimas():
    solucoes = set()
    start_time = time.time()
    tentativas = 0
    max_tentativas = 1000

    while len(solucoes) < 92 and tentativas < max_tentativas:
        tentativas += 1
        solucao, custo, _ = tempera_simulada(n_rainhas=8, max_iter=1000, T_escalonamento='linear')
        
        
        if custo == 0:
            solucoes.add(tuple(solucao))
        
        
        if tentativas % 300 == 0 or len(solucoes) == 92:
            tempo_atual = time.time() - start_time
            print(f"Tentativa: {tentativas}, Solucoes unicas encontradas: {len(solucoes)}, Tempo decorrido: {tempo_atual:.2f} segundos")
    
    end_time = time.time()
    tempo_total = end_time - start_time
    return solucoes, tentativas, tempo_total

solucoes_unicas, total_tentativas, tempo_gasto = solucoes_otimas()


print(f"\nAs {len(solucoes_unicas)} solucoes otimas encontradas sao:")
for sol in solucoes_unicas:
    print(list(map(int, sol)))  # mostra como vetor todas as soluções ótimas

print(f"\nTotal de tentativas para encontrar {len(solucoes_unicas)} solucoes unicas: {total_tentativas}")
print(f"Tempo total gasto: {tempo_gasto:.2f} segundos")
print(f"Numero de soluces unicas encontradas: {len(solucoes_unicas)}")
