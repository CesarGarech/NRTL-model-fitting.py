# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:47:31 2021

@author: César-Garech
"""

import numpy as np
import matplotlib.pyplot as plt

ax=plt.axes(projection='3d')

zline=np.linspace(0,15,100)
xline=np.sin(zline)
yline=np.cos(zline)

ax.plot(xline,yline,zline)
# ax.set_zlim(0, 10)
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('Z')