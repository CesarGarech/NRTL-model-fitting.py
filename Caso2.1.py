# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:49:21 2021

@author: César-Garech
"""

#Optimización de parámetros ajustados a datos experimentales
#Importar librerias
import numpy as np
from scipy import optimize
from Error import Error
from ELV import ELV
import matplotlib.pyplot as plt


#Parámetros de Antoine
matriz=np.loadtxt('Antoine.txt')
param=np.array([matriz[0,:],matriz[1,:]])
param=np.transpose(param)

#Datos experimentales
Data=np.loadtxt('Data.txt')
Texp=Data[:,0]
Xexp=Data[:,1]
Yexp=Data[:,2]

#Presión dada
Ptot=1.01325
Tguess= 90+273.15

#Parametros iniciales de NRTL
Paramsup=np.array([-0.5, 0.5, -100, 100])
alfa=np.array([[0, 0.3],[0.3,0]])
#Función error

def error_reg(parametros, Texp, Xexp,Yexp, param, Ptot, alfa):
    aij=np.array([[0,parametros[0]], [parametros[1],0]]) 
    bij=np.array([[0,parametros[2]], [parametros[3],0]])  
    
    n=np.size(Xexp)
    xcalcv=np.zeros((n,2))
    ycalcv=np.zeros((n,2))
    Tcalcv=np.zeros(n)
    
    for i,xi in enumerate(Xexp):
        x2=1-xi
        x=np.array([xi,x2])
        Tcalc=optimize.fsolve(Error,Tguess,args=(x,Ptot,aij, bij,alfa, param))
        Pcalc, ycalc=ELV(Tcalc,x, Ptot, aij, bij,alfa, param)
        Tcalcv[i]=Tcalc
        ycalcv[i,:]=ycalc
        xcalcv[i,:]=x

    errorT=np.sum(((Texp-Tcalcv)/Texp)**2)
    errory=np.sum((Yexp-ycalcv[:,0])**2)
    
    return errorT+errory

prueba=error_reg(Paramsup,Texp, Xexp,Yexp, param, Ptot, alfa )

print(prueba)
paramcalc=optimize.fmin(error_reg,Paramsup,args=(Texp, Xexp,Yexp, param, Ptot, alfa ))

# paramcalc=Paramsup
print(paramcalc)

##Para graficar
xcalc=np.linspace(0,1,100)
Tguess= 90+273.15

xcalcv=np.zeros((100,2))
ycalcv=np.zeros((100,2))
Tcalcv=np.zeros(100)
aij=np.array([[0,paramcalc[0]], [paramcalc[1],0]]) 
bij=np.array([[0,paramcalc[2]], [paramcalc[3],0]]) 
for i,xi in enumerate(xcalc):
    x2=1-xi
    x=np.array([xi,x2])
    Tcalc=optimize.fsolve(Error,Tguess,args=(x,Ptot,aij, bij,alfa, param))
    Pcalc, ycalc=ELV(Tcalc,x, Ptot, aij, bij,alfa, param)
    Tcalcv[i]=Tcalc
    ycalcv[i,:]=ycalc
    xcalcv[i,:]=x


plt.plot(xcalcv[:,0],Tcalcv,'r', linewidth = 2)
plt.plot(ycalcv[:,0],Tcalcv,'b', linewidth = 2)
plt.plot(Data[:,1],Data[:,0],'ro', linewidth = 2,label='Liq')
plt.plot(Data[:,2],Data[:,0],'bo', linewidth = 2,label='Vap')
plt.title('Ethanol(1)-Water(2)')
plt.ylabel('Temperature [K]')
plt.xlabel('X1,Y1')
plt.legend()
plt.show()    









