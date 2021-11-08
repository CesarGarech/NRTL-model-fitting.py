# Función que calcula el coeficiente de actividad usando la ecuación NRTL
# cada llamado evalua una composición
# x = vector de n fracciones molares de una mezcla de n componentes, tamaño n-1
# tau = valores de tau en forma de matriz cuadrada (n-1)x(n-1)
# alpha = valores de alfa en forma de matriz cuadrada (n-1)x(n-1), esta matriz es simétrica

import numpy as np

def nrtl(x, tau, alpha):
    nComp = np.size(x) # calcula el número de componentes
    x += 1e-50 # se asegura que x no sea igual a cero
    # Algunos mensajes para entender errores
    if np.shape(tau)[1] != np.shape(tau)[0]:
        print('La matriz de energía tau debe ser cuadrada')
    if np.shape(alpha)[1] != np.shape(alpha)[0]:
        print('La matriz alpha debe ser cuadrada')
    if nComp != np.shape(tau)[1]:
        print('La matriz tau no corresponde al número de componentes según el vector x')
    if nComp != np.shape(alpha)[1]:
        print('La matriz alpha no corresponde al número de componentes según el vector x')
    
    ## Usando las ecuaciones para el calculo de gamma
    
    # es necesario transponer las matrices dadas porque python entiende a la
    # la composición como un vector columna
    alpha = np.transpose(alpha)
    tau = np.transpose(tau)  
    # Calculando la matriz Gij
    Gij = np.exp(-alpha*tau)
    # Numerador y denominador 1
    num1 = np.dot(tau*Gij, x)
    den1 = np.dot(Gij, x)
    # Creando las matrices xm y matr
    xm = np.zeros((nComp, nComp))
    matr = np.zeros((nComp, nComp))
    # Llenando la matriz xm
    for i in range(nComp):
        xm[i,:] = x[:]
    # Numerador 2
    num2 = xm*np.transpose(Gij)
    num2 = np.transpose(num2)
    # Llenando la matriz matr
    for i in range(nComp):
        matr[:,i] = num2[:,i]/den1*(tau[:,i]-num1/den1)
    # Creando un vector de term 2
    term2 = np.array([1.,1.])
    term2 [0] = np.sum(matr[:,0])
    term2 [1] = np.sum(matr[:,1])
    # Calculando gamma
    gamma = np.exp(num1/den1+term2)
    
    return gamma

