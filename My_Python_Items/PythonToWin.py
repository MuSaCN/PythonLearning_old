# Author:Zhang Yuan

file = "C:\\Users\\i2011\\PycharmProjects\\PythonLearning\\My_Python_Items\\AutoMyPackageZip.py"

from distutils.core import setup
import py2exe

options = {"py2exe": {"optimize": 2}}
setup(
    options=options,
    zipfile=None,
    console=[file],
     )






