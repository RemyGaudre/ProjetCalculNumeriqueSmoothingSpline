      SUBROUTINE CHOLESKI (N,A,LDA,B,LDB)
        
        INTEGER N,LDA,LDB
        DOUBLE PRECISION A(LDA,*),B(LDB,*),SOM
        
        INTEGER I,J,K
*f2py intent(inplace) B        
        B(1,1)=SQRT(A(1,1))
        
        DO J = 1,N
           DO I=2,N
              IF (I.EQ.J) THEN
                 SOM = 0
                 DO K=1,I-1
                    SOM = SOM + B(I,K)**2
                 END DO
              B(J,J)=SQRT(A(J,J)-SOM)
              
              ELSE IF(J.GT.I) THEN
                 B(I,J)=0
              ELSE
                 SOM = 0
                 DO K = 1,I-1
                    SOM = SOM + B(I,K)*B(J,K)
                 END DO
                 B(I,J)=(A(I,J)-SOM)/B(J,J)
              END IF
           END DO
        END DO
              SOM = 0
              DO K=1,N-1
                 SOM = SOM + B(N,K)**2
              END DO

        B(N,N)=SQRT(A(N,N)-SOM)
        
      END SUBROUTINE
      
      SUBROUTINE DESCENTE (N,L,LDL,B,W)
        
        INTEGER N,LDL
        DOUBLE PRECISION L(LDL,*),B(LDL),W(LDL),C
        
        INTEGER I,J
!         CALL DPRINT_MPL ('L',N,N,L,10)
!         WRITE (*,*) L(2,2)

*f2py intent(inplace) W 
        W(1)=B(1)/L(1,1)
        
        DO I = 2,N
           C = B(I)
           DO J=1,I-1
              C = C - L(I,J)*W(J)
           END DO
           W(I)=C/L(I,I)
        END DO
        
      END SUBROUTINE
