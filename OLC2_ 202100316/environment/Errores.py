from interface.instrucion import Instruction


errores = []

class Errores():
    def __init__(self, line, col, tipo, exp):
        self.line = line
        self.col = col
        self.tipo = tipo
        self.exp = exp

    def ejecutar(self, ast, env):
        pass
           