from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("week3_cython.pyx"),
)