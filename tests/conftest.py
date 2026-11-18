# Añade la carpeta raíz del proyecto al path para poder hacer "import calculadora" desde los tests
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
