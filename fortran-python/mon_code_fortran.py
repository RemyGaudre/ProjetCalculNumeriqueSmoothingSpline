!    -*- f90 -*-
! Note: the context of this file is case sensitive.

subroutine descente(m,a,lda,b) ! in descente.f
    integer, optional,check(len(b)>=m),depend(b) :: m=len(b)
    double precision dimension(lda,*) :: a
    integer, optional,check(shape(a,0)==lda),depend(a) :: lda=shape(a,0)
    double precision dimension(m),intent(inplace) :: b
end subroutine descente
subroutine newton_dd(n,x,y,m,abscisses,ordonnees) ! in Newton_dd.f
    integer, optional,check((len(x)-1)>=n),depend(x) :: n=(len(x)-1)
    double precision dimension(n + 1) :: x
    double precision dimension(n + 1),depend(n) :: y
    integer, optional,check(len(abscisses)>=m),depend(abscisses) :: m=len(abscisses)
    double precision dimension(m) :: abscisses
    double precision dimension(m),intent(inplace),depend(m) :: ordonnees
end subroutine newton_dd

! This file was auto-generated with f2py (version:2).
! See http://cens.ioc.ee/projects/f2py2e/
