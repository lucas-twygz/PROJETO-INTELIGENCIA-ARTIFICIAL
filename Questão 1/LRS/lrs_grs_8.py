import numpy as np
import matplotlib.pyplot as plt

def funcao (x1, x2):
    return -(x2 + 47) * np.sin(np.sqrt(np.abs(x1 / 2 + (x2 + 47)))) - x1 * np.sin(np.sqrt(np.abs(x1 - (x2 + 47))))

x1_limit = (-200, 20)
x2_limit = (-200, 20)
max_iteracoes = 10000
s = 0.9
max_viz = 20
min_max = False
x_best = [np.random.uniform(x1_limit[0], x1_limit[1]), np.random.uniform(x2_limit[0], x2_limit[1])]
f_best = funcao(x_best[0], x_best[1])
figura = plt.figure()
ax = figura.add_subplot(projection='3d')

def moda(dados):
    frequencias = {}
    for i in dados:
        if i in frequencias:
            frequencias[i]+=1
        else:
            frequencias[i] = 1
    moda = max(frequencias, key=frequencias.get)
    return moda

def perturb(x1_limit, x2_limit, x_best):
    x1_cand = np.clip(np.random.normal(x_best[0], s), x1_limit[0], x1_limit[1])
    x2_cand = np.clip(np.random.normal(x_best[1], s), x2_limit[0], x2_limit[1])
    return [x1_cand, x2_cand]

def lrs(x_best, f_best, max_iteracoes, max_viz, min_max):
    i = 0
    while i<max_iteracoes:
        for j in range(max_viz):
            x_cand = perturb(x1_limit, x2_limit, x_best)
            f_cand = funcao(x_cand[0],x_cand[1])
            if min_max:
                if f_cand > f_best:
                    x_best = x_cand
                    f_best = f_cand
                    # plt.pause(.1)
                    # ax.scatter(x_best[0], x_best[1],f_best,color='r',marker='x', s=100)
                    break
            else:
                if f_cand < f_best:
                    x_best = x_cand
                    f_best = f_cand
                    # plt.pause(.1)
                    # ax.scatter(x_best[0], x_best[1],f_best,color='r',marker='x', s=100)
                    break
        i+=1
    # ax.scatter(x_best[0], x_best[1], f_best, color="g", marker= "x", s=1000)
    return f_best
    plt.show()

def graf(x1_limit, x2_limit, funcao):
    x1 = np.linspace(x1_limit[0], x1_limit[1], 100)
    x2 = np.linspace(x2_limit[0], x2_limit[1], 100)
    x_1, x_2 = np.meshgrid(x1, x2)
    x_1_2 = funcao(x_1, x_2)
    ax.plot_surface(x_1, x_2, x_1_2,cmap='rainbow',alpha=.6,edgecolor='none')

# graf(x1_limit,x2_limit, funcao)

resultado = []
for i in range(10):
    print(resultado)
    resultado.append(lrs(x_best, f_best, max_iteracoes, max_viz, min_max))

resultado_moda = round(moda(resultado), 2) 
print(resultado_moda)