#import scipy.linalg as nla
#from scipy.interpolate import CubicSpline #contient des splines
import numpy as np #def matrice
import matplotlib.pyplot as plt #graphique
#import mon_code_fortran as mcf
#import Gnuplot

x = [0., 1.7, 3.3, 5.0, 6.7, 8.4, 10.1]
y = [1.7, 3.4, 0.8, 2.5, 4.3, 4.3, 0.8]
n = len(x) - 1

h = np.array([x[1]-x[0]])
for i in range(1,n):
    h = np.append(h, x[i+1]-x[i])
print(h)

T1 = np.diag(2*(h[:n-1]+h[1:n]))
T2 = np.diag(h[1:n-1], -1)
T3 = np.diag(h[1:n-1], 1)

T = (T1+T2+T3)/3


g = 1/h

Qpremiereligne = np.append([g[0]], np.zeros(n-2))
Q = np.array([Qpremiereligne])                         

Q1 = np.diag(g[1:n-1],1)
Q2 = np.diag(-g[:n-1]-g[1:n])
Q3 = np.diag(g[1:n-1],-1)
Q = np.append(Q, Q1 + Q2 + Q3, axis=0)

Qderniereligne = np.append(np.zeros(n-2), [g[n-1]])
Q = np.append(Q, [Qderniereligne], axis=0)

p = pow(10,5)
QT = np.transpose(Q)

A = np.matmul(QT,Q) + p*T
b = p*np.matmul(QT, np.transpose(y))

L = np.linalg.cholesky(A)
w = np.linalg.solve(L,b)
c = np.linalg.solve(np.transpose(L),w)
a = y - (1/p)*np.matmul(Q,c)
print(c.shape)
c0 = np.append([[0]], c)
c0 = np.append(c0,[[0]])



d = np.array([(c0[1]-c0[0])/(3*h[0])])
for i in range(1,n):
    d = np.append(d, (c0[i+1]-c0[i])/(3*h[i]))

    
b = np.array([((a[1]-a[0])/(h[0]))-c0[0]*h[0]-d[0]*h[i]**2])
for i in range(1,n):
    b = np.append(b,((a[i+1]-a[i])/(h[i]))-c0[i]*h[i]-d[i]*h[i]**2)

x1=np.linspace(x[0],x[n],1000*n)
#y1 = np.array([a[0]+b[0]*((x1[0]-x[0]))+c[0]*pow((x1[0]-x[0]),2)+d[0]*pow(((x1[0]-x[0])),3)])
y1 = np.array([])
for i in range(0,n):
    for j in range(0,1000):
        y1 = np.append(y1,a[i]+b[i]*((x1[i*1000+j]-x[i]))+c0[i]*pow((x1[i*1000+j]-x[i]),2)+d[i]*pow(((x1[i*1000+j]-x[i])),3))
        

print(a)
print(b)
print(c)
print(c0)
print(d)
#print(y1)
#print(x1)
    
    
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(x1,y1, label="Spline")
ax.set_xlim(min(x)-1,max(x)+1)
ax.legend(loc='lower left', ncol=2)
plt.show()    
#line = plt.plot(x1,y1,',')
#plt.setp(line, linewidth=1)
#plt.plot(x,y)
#plt.show()



#lines = np.array([])
#for i in range(0,n):
    #y1 = np.array([])
    #for j in range(0,1000):
        #y1 = np.append(y1,a[i]+b[i]*((x1[i*1000+j]-x[i]))+c[i]*pow((x1[i*1000+j]-x[i]),2)+d[i]*pow(((x1[i*1000+j]-x[i])),3))
    #lines = np.append(lines,plt.plot(x1[i*1000:(i+1)*1000], y1))
    #plt.setp(lines[i], linewidth=1)

#plt.legend(('Splines'),
           #loc='upper right')
#plt.title('Splines')
#plt.show()

    
    
