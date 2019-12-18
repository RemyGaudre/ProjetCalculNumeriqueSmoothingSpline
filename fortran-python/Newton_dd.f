* Implantation des différences divisées de Newton
* En entrée : n+1 points (x(0),y(0)), ..., (x(n),y(n))
*                 définissant un polynôme d'interpolation P(x)
*             un tableau d'abscisses de dimension m
* En sortie : le tableau des m ordonnées de P, évalué en chacune des abscisses

      SUBROUTINE NEWTON_DD (N, X, Y, M, ABSCISSES, ORDONNEES)
      IMPLICIT NONE
* Depuis Python, il n'est pas nécessaire de passer les dimensions n et m.
* Si on ne les précise pas, elles sont calculées automatiquement à partir
* des autres paramètres. La correspondance est déduite de ces déclarations :
      INTEGER N, M
      DOUBLE PRECISION X(0:N), Y(0:N), ABSCISSES(M), ORDONNEES(M)
* Le commentaire suivant est un DIRECTIVE DE COMPILATION pour f2py
* Son but : que les modifications sur ORDONNEES se répercutent au niveau Python
*f2py intent(inplace) ordonnees
      DOUBLE PRECISION C(0:N,0:N), Z, P
      INTEGER I, J
      DO I = 0,N
         C(I,0) = Y(I)
      END DO
      DO J = 1,N
         DO I = 0,N-J
            C(I,J) = (C(I+1,J-1) - C(I,J-1))/(X(I+J) - X(I))
         END DO
      END DO
* Schéma de Horner
      DO J = 1,M
         Z = ABSCISSES(J)
         P = C(0,N)
         DO I = N-1,0,-1
            P = P*(Z-X(N-I))+C(N-I,I)
         END DO
         ORDONNEES(J) = P
      END DO
      END SUBROUTINE

