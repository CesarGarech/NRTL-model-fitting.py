# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:46:58 2021

@author: César-Garech
"""

#Función para calculo de la Pvap con Antoine extendido
import numpy as np


def Pvap(T,Param):
    return np.exp(Param[0]+(Param[1]/T)+Param[2]*np.log(T)+Param[3]*T**Param[4])

