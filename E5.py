# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:00:00 2019

@author:ara
"""

import numpy as np
import matplotlib.pyplot as palt

cantidad = 50
tamanio = 20

x = np.random.rand(cantidad)
y = np.random.rand(cantidad)

color =np.random.rand(cantidad)
area = np.pi *(tamanio * np.random.rand(cantidad))**2

plt.scatter(x,y, s=area, c=color , alpha=0.5)
plt.show()