from interface.instrucion import Instruction
from environment.execute import BlockExecuter
from environment.execute import StatementExecuter
from environment.environment import Environment

class Condicion(Instruction):
    def __init__(self, line, col, exp, block_if, block_else=None):
        self.line = line
        self.col = col
        self.exp = exp
        self.block_if = block_if
        self.block_else = block_else


    def ejecutar(self, ast, env):
        # Obtener simbolo
        validate = self.exp.ejecutar(ast, env)
        # Evaluar
        if validate.value:
            # Crear entorno del If
            if_env = Environment(env, "IF")
            returnValue = StatementExecuter(self.block_if, ast, if_env)
            if returnValue is not None:
                return returnValue
        elif self.block_else is not None:
            # Crear entorno del Else
            else_env = Environment(env, "ELSE")
            returnValue = StatementExecuter(self.block_else, ast, else_env)
            if returnValue is not None:
                return returnValue
        return None