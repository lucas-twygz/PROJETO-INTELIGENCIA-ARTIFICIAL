import numpy as np
import matplotlib.pyplot as plt

def funcao (x1, x2):
    return np.exp(-(x1**2+x2**2)) + 2 * np.exp(-((x1-1.7)**2+(x2-1.7)**2))

x1_limit = (-2, 4)
x2_limit = (-2, 5)
max_iteracoes = 10000
e = .9
max_viz = 20
min_max = True
x_best = [x1_limit[0], x2_limit[0]]
f_best = funcao(x_best[0], x_best[1])
# figura = plt.figure()
# ax = figura.add_subplot(projection='3d')

# false = minimo, true = maximo

def moda(dados):
    frequencias = {}
    for i in dados:
        if i in frequencias:
            frequencias[i]+=1
        else:
            frequencias[i] = 1
    moda = max(frequencias, key=frequencias.get)
    return moda

def perturb(x_best):
    cand_1 = np.clip(np.random.uniform(low=x_best[0] - e, high=x_best[1] + e), a_min=x1_limit[0], a_max= x1_limit[1])
    cand_2 = np.clip(np.random.uniform(low=x_best[0] - e, high=x_best[1] + e), a_min=x2_limit[0], a_max= x2_limit[1])
    return [cand_1, cand_2]

def hill_climbing(x_best, f_best, max_iteracoes, max_viz, min_max):
    melhoria = True
    i = 0
    while i<max_iteracoes and melhoria:
        melhoria = False
        for j in range(max_viz):
            x_cand = perturb(x_best)
            f_cand = funcao(x_cand[0],x_cand[1])
            if min_max:
                if f_cand > f_best:
                    x_best = x_cand
                    f_best = f_cand
                    melhoria = True
                    # plt.pause(.1)
                    # ax.scatter(x_best[0], x_best[1],f_best,color='r',marker='x', s=100)
                    break
            else:
                if f_cand < f_best:
                    x_best = x_cand
                    f_best = f_cand
                    melhoria = True
                    # plt.pause(.1)
                    # ax.scatter(x_best[0], x_best[1],f_best,color='r',marker='x', s=100)
                    break
        i+=1
    # ax.scatter(x_best[0], x_best[1], f_best, color="g", marker= "x")
    return f_best
    plt.show()

def graf(x1_limit, x2_limit, funcao):
    x1 = np.linspace(x1_limit[0], x1_limit[1], 100)
    x2 = np.linspace(x2_limit[0], x2_limit[1], 100)
    x_1, x_2 = np.meshgrid(x1, x2)
    x_1_2 = funcao(x_1, x_2)
    ax.plot_surface(x_1, x_2, x_1_2,cmap='rainbow',alpha=.9,edgecolor='none')

resultado = []
for i in range(100):
    resultado.append(hill_climbing(x_best, f_best, max_iteracoes, max_viz, min_max))

resultado_moda = round(moda(resultado), 2) 
print(resultado_moda)