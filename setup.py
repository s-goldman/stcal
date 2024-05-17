import numpy as np
from Cython.Build import cythonize
from Cython.Compiler import Options
from setuptools import Extension, setup

Options.docstrings = True
Options.annotate = False

# importing these extension modules is tested in `.github/workflows/build.yml`; 
# when adding new modules here, make sure to add them to the `test_command` entry there
extensions = [
    Extension(
        "stcal.ramp_fitting.ols_cas22._ramp",
        ["src/stcal/ramp_fitting/ols_cas22/_ramp.pyx"],
        include_dirs=[np.get_include()],
        language="c++",
    ),
    Extension(
        "stcal.ramp_fitting.ols_cas22._jump",
        ["src/stcal/ramp_fitting/ols_cas22/_jump.pyx"],
        include_dirs=[np.get_include()],
        language="c++",
    ),
    Extension(
        "stcal.ramp_fitting.ols_cas22._fit",
        ["src/stcal/ramp_fitting/ols_cas22/_fit.pyx"],
        include_dirs=[np.get_include()],
        language="c++",
    ),
]

setup(ext_modules=cythonize(extensions))
