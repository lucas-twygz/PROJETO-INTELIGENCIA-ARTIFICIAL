import numpy as np
import matplotlib.pyplot as plt

# Definindo a função da questão 3
def funcao3(x1, x2):
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))) + 20 + np.exp(1)

# Limites para x1 e x2
x1_limit = (-8, 8)
x2_limit = (-8, 8)
max_iteracoes = 10000
min_max = False  # False = Minimizando

# Definindo o melhor valor inicial
x_best = [np.random.uniform(x1_limit[0], x1_limit[1]), np.random.uniform(x2_limit[0], x2_limit[1])]
f_best = funcao3(x_best[0], x_best[1])

# Função de perturbação que gera um novo candidato aleatório
def perturb():
    x1_cand = np.random.uniform(x1_limit[0], x1_limit[1])
    x2_cand = np.random.uniform(x2_limit[0], x2_limit[1])
    return [x1_cand, x2_cand]

# Algoritmo GRS (Global Random Search)
def grs(x_best, f_best, max_iteracoes, min_max, funcao):
    i = 0
    while i < max_iteracoes:
        x_cand = perturb()
        f_cand = funcao(x_cand[0], x_cand[1])
        if min_max:
            if f_cand > f_best:
                x_best = x_cand
                f_best = f_cand
        else:
            if f_cand < f_best:
                x_best = x_cand
                f_best = f_cand
        i += 1
    return f_best

# Executando o GRS para a função da questão 3
resultado = []
for i in range(100):
    resultado.append(grs(x_best, f_best, max_iteracoes, min_max, funcao3))

# Função para calcular a moda
def moda(dados):
    frequencias = {}
    for i in dados:
        if i in frequencias:
            frequencias[i] += 1
        else:
            frequencias[i] = 1
    moda = max(frequencias, key=frequencias.get)
    return moda

# Mostrando o resultado da moda das soluções
resultado_moda = round(moda(resultado), 2) 
print(resultado_moda)
