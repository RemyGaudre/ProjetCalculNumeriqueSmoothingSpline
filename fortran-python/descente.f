* Résolution d'un système linéaire A . x = b par substitution avant
* La matrice A est triangulaire inférieure
* LDA = Leading Dimension of A (hauteur d'une colonne dans le tableau A)
* M   = dimension mathématique
      SUBROUTINE DESCENTE (M, A, LDA, B)
      IMPLICIT NONE
      INTEGER M, LDA
* Au niveau Python, on peut ne passer que A et B en paramètre
* LDA et M sont alors déterminés automatiquement
* Les relations entre tous ces paramètres sont déduites de ces déclarations : 
      DOUBLE PRECISION A(LDA,*)
      DOUBLE PRECISION B(M)
* Le commentaire suivant est une DIRECTIVE DE COMPILATION pour f2py.
* Son but : que les modifications sur B se répercutent au niveau Python
*f2py intent(inplace) b
      DOUBLE PRECISION DDOT
      INTEGER I
      DO I = 1,M
* Utilise la BLAS ddot (produit scalaire de deux vecteurs)
         B(I) = B(I) - DDOT(I-1, A(I,1), LDA, B, 1)
         B(I) = B(I) / A(I,I)
      END DO
      END SUBROUTINE

