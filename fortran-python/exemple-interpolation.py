import numpy as np
import mon_code_fortran as mcf
import matplotlib.pyplot as plt
# les coordonnées des points à interpoler
x = np.array([0., 1.7, 3.3, 5.0, 6.7, 8.4, 10.1])
y = np.array([1.7, 3.4, 0.8, 2.5, 4.3, 4.3, 0.8])
# 100 points pris entre -.5 et 10.6 (pour la visualisation graphique)
abscisses = np.linspace(x[0]-.5,x[-1]+.5,100)
# un tableau de dimension 100 pour recevoir les ordonnées
ordonnees = np.zeros(abscisses.shape)
# Calcul des ordonnées et visualisation
mcf.newton_dd(x,y,abscisses,ordonnees)
plt.scatter(x,y)
plt.plot(abscisses,ordonnees)
plt.show ()

