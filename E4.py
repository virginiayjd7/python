# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:46:49 2019

@author: DEPIS22
"""


import matplotlib.pyplot as plt
#PRIMER vector
valor1 = [50,5,15,21,14,4,35,20,20,20,20,20,50,0]

plt.plot(valor1)
plt.xlabel("Eje x: Cantidad")
plt.ylabel("Eje y: venta")
#SEGUNDO VECTOR
valor2 = [10,5,15,21,14,35,20,50,0]
plt.plot(valor2)

valor3 = [40,0,15,21,14,35,20,30,0]
plt.plot(valor3)

title("grafico lineal de ventas por mes")
plt.show()

