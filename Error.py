# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:41:16 2021

@author: César-Garech
"""
from nrtl import nrtl
from Pvap import Pvap
import numpy as np

def Error (T,x, Ptot, aij, bij,alpha, param):

    tauij=aij+bij/T      
    gamma=nrtl(x,tauij,alpha)
    
    
    
    # Pv1=Pvap(T,param[0,:])
    # Pv2=Pvap(T,param[1,:])
    
    # Pv=np.array([Pv1,Pv2])
    
    Pv=Pvap(T,param)
    
    # Ppal1=x[0]*gamma[0]*Pv[0]
    # Ppal2=x[1]*gamma[1]*Pv[1]
    # Ppal=np.array([Ppal1,Ppal2])
    
    Ppal=x*gamma*Pv
    
    Pcalc=np.sum(Ppal)
    
    Error=Ptot-Pcalc    
   
    return Error
