# Construit un module python3 appelé 'mon_code_fortran.py' 
# à partir de fichiers FORTRAN. 
#
# Sont fabriqués : un fichier source '.py' et un fichier compilé '.so'

# Le nom du module
MODULE=mon_code_fortran

# Les fichiers FORTRAN
FORTRAN_FILES=descente.f Newton_dd.f

# L'utilitaire de compilation
F2PY3=f2py3
# CPPFLAGS et CFLAGS évitent des warnings dus à des codes C mal écrits.
F2PY3_CPPFLAGS=-DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION
F2PY3_CFLAGS=-Wno-unused-function -Wno-misleading-indentation
# LDFLAGS et LIBS permettent d'appeler BLAS et LAPACK depuis FORTRAN
F2PY3_LDFLAGS=-L/usr/lib/x86_64-linux-gnu/lapack -L/usr/lib/x86_64-linux-gnu/blas
F2PY3_LIBS=-llapack -lblas
# Autorise le remplacement de l'ancien '.py'
F2PY3_H_FLAGS=--overwrite-signature

.PHONY: all clean

# f2py3 -c construit le '.so'
# f2py3 -h construit le '.py'
all:
	CPPFLAGS="$(F2PY3_CPPFLAGS)" CFLAGS="$(F2PY3_CFLAGS)" $(F2PY3) -c -m $(MODULE) $(F2PY3_LDFLAGS) $(FORTRAN_FILES) $(F2PY3_LIBS)
	$(F2PY3) -h $(MODULE).py $(F2PY3_H_FLAGS) $(FORTRAN_FILES)

clean:
	-rm $(MODULE)*.so
	-rm $(MODULE).py
