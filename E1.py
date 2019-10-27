# -*- coding: utf-8 -*-
"""
Editor de Spyder
"""

from pylab import*
ax = axes([10,10,0.9,0.9])#4
labels='Leche','Aceite','Arroz','Galleta','Aceituna','Pollo'
valores = [3,7,3,2,12,23]
explode = (0,0.1,0,0,0,0)


pie(valores, explode=explode, labels=labels, autopct='%10.0f%%',shadow=True)     #distancia


legend(loc='center left', bbox_to_anchor=(1.1,0.5)) #distancia
title('grafico de aji gallina')
savefig("c://Ficheros\graficosaji.png",bbox_inches='tight')
show()

