"""
@author: lorenzo
Chiede l'inserimento manuale di n coppie nella forma [x,y] e
calcola i coefficienti della retta di regressione riporatandoli
nell'output
"""
import numpy as np

n = int(input("Inserire il numero di coppie di dati: "))

narray = []
for i in range(n):
    coppia_dati = np.array(eval(input(" " + str(i+1) + "^ :> ")))
    narray.append(coppia_dati)

nparray = np.array(narray)

nparrayX_Y = nparray.transpose()

dati_x = nparrayX_Y[0]
dati_y = nparrayX_Y[1]

XY = []
for i in range(n):
    XY.append(dati_x[i] * dati_y[i])

quadrato_x = dati_x**2

a = (n*sum(XY) - sum(dati_x)*sum(dati_y)) / (n*sum(quadrato_x) - sum(dati_x)**2)
b = (sum(dati_y) - a*sum(dati_x))/n

print()
print("a = " + str(a))
print("b = " + str(b))