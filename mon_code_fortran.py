!    -*- f90 -*-
! Note: the context of this file is case sensitive.

subroutine choleski(n,a,lda,b,ldb) ! in codefortran.f
    integer :: n
    double precision dimension(lda,*) :: a
    integer, optional,check(shape(a,0)==lda),depend(a) :: lda=shape(a,0)
    double precision dimension(ldb,*),intent(inplace) :: b
    integer, optional,check(shape(b,0)==ldb),depend(b) :: ldb=shape(b,0)
end subroutine choleski
subroutine descente(n,l,ldl,b,w) ! in codefortran.f
    integer :: n
    double precision dimension(ldl,*) :: l
    integer, optional,check(shape(l,0)==ldl),depend(l) :: ldl=shape(l,0)
    double precision dimension(ldl),depend(ldl) :: b
    double precision dimension(ldl),intent(inplace),depend(ldl) :: w
end subroutine descente

! This file was auto-generated with f2py (version:2).
! See http://cens.ioc.ee/projects/f2py2e/
