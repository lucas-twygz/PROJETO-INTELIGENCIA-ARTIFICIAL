import numpy as np

def funcao1 (x1, x2):
    return x1**2 + x2**2

def funcao2 (x1, x2):
    return np.exp(-(x1**2+x2**2)) + 2 * np.exp(-((x1-1.7)**2+(x2-1.7)**2))

def funcao3 (x1,x2):
    return -20 * np.exp(-0.2*np.sqrt(0.5*(x1**2+x2**2))) - np.exp(0.5*(np.cos(2*np.pi*x1)+np.cos(2*np.pi*x2))) + 20 + np.exp(1)

def funcao4 (x1,x2):
    return (x1**2 - 10 * np.cos(2**np.pi*x1) + 10) + (x2**2 - 10 * np.cos(2*np.pi*x2)+10)

def funcao5 (x1,x2):
    return (x1 * np.cos(x1)) / 20 + 2 * np.exp(-(x1**2) - (x2 - 1)**2) + 0.01 * x1 * x2

def funcao6(x1, x2):
    return x1 * np.sin(4 * np.pi * x1) - x2 * np.sin(4 * np.pi * x2 + np.pi) + 1

def funcao7(x1, x2):
    return -np.sin(x1) * (np.sin(x1**2 / np.pi))**(2 * 10) - np.sin(x2) * (np.sin(2 * x2**2 / np.pi))**(2*10)

def funcao8(x1, x2):
    return -(x2 + 47) * np.sin(np.sqrt(np.abs(x1 / 2 + (x2 + 47)))) - x1 * np.sin(np.sqrt(np.abs(x1 - (x2 + 47))))