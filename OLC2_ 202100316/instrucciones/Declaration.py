from interface.instrucion import Instruction
from environment.types import ExpressionType

class Declaration(Instruction):
    def __init__(self, line, col, id, type, exp):
        self.line = line
        self.col = col
        self.id = id
        self.type = type
        self.exp = exp

    def ejecutar(self, ast, env):
        # Obtener simbolo
        result = self.exp.ejecutar(ast, env)
        if self.type == ExpressionType.NULL:
            self.type = result.type
        # Validar tipo
        if result.type != self.type:
            if (result.type == ExpressionType.FLOAT and self.type == ExpressionType.INTEGER)  or (result.type == ExpressionType.INTEGER and self.type == ExpressionType.FLOAT):
                self.type = result.type
            else:
                ast.setErrors("Los tipos de dato son incorrectos")
                return
        # Agregar al entorno
        env.saveVariable(ast, self.id, result)