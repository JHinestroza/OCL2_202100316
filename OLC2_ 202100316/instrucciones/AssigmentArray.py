from interface.instrucion import Instruction
from environment.types import ExpressionType

class AssigmentArray(Instruction):
    def __init__(self, line, col, id, exp):
        self.line = line
        self.col = col
        self.id = id
        self.exp = exp

    def ejecutar(self, ast, env):
        # Obtener simbolo
        result = self.exp.ejecutar(ast, env)
        print("asignando",result.value)
        # Agregar al entorno
