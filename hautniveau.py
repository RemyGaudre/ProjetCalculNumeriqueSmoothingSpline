import scipy.linalg as nla
from scipy.interpolate import CubicSpline #contient des splines
import numpy as np #def matrice
import matplotlib.pyplot as plt #graphique

x = [0., 1.7, 3.3, 5.0, 6.7, 8.4, 10.1]
y = [1.7, 3.4, 0.8, 2.5, 4.3, 4.3, 0.8]
#n+1 points donc n = 6

def spline(x,y):
    cs = CubicSpline(x, y)
    xs = np.arange(min(x),max(x),(max(x)-min(x))/1000)
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(x, y, 'o', label='data')
    ax.plot(xs, cs(xs), label="Spline")
    ax.set_xlim(min(x)-1,max(x)+1)
    ax.legend(loc='lower left', ncol=2)
    plt.show()
    
spline(x,y)
#Le paramètre de lissage est optimal car on ne le précise pas quand on construit la spline.
