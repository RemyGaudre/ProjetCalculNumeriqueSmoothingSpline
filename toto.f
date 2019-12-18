      SUBROUTINE CHOLESKI (N, A, LDA, B)
      INTEGER N, LDA
      DOUBLE PRECISION A(LDA,N), B(N)
*f2py intent(inplace) b
      INTEGER I, J
      DO I = 1,N
        DO J = 1,N
            WRITE (*,*) I, J, A(I,J)
        END DO
        B(I) = 109
      END DO
      END SUBROUTINE
