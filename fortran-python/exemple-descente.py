import numpy as np
import mon_code_fortran as mcf
A = np.array ([[2,0,0],[3,-1,0],[0,1,5]])
b = np.array ([4,5,16])
print(A)
print(b)
# Résolution du système d'équations linéaires de dimension 3
# b est modifié
mcf.descente(A,b)
print(b)
# Résolution du sous-système formé des deux premières équations
b = np.array ([4,5,16])
mcf.descente(A,b,m=2)
print(b)
