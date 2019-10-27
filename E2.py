# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:31:54 2019

@author: CEPIS15
"""

import numpy as np
import matplotlib.pyplot as plt

valores = [[10,3,1,15,8],[4,8,0,6,2,],[0,0,20,5,3],[50,6,7,10,3]]
x = np.arange(5)

plt.bar(x + 0.00, valores[0], color = "purple", width=0.20)
plt.bar(x + 0.20, valores[1], color = "green", width=0.20)
plt.bar(x + 0.40, valores[2], color = "orange", width=0.20)
plt.bar(x + 0.60, valores[3], color = "pink", width=0.20)

title("Grafico de Barras de venta de Productos")

plt.xticks(x + 0.20, ["Leche", "Aceite", "Arroz", "Galleta"])