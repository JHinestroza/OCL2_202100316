from interface.expresion import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType
from environment.Errores import Errores,errores

class Break(Expression):
    def __init__(self, line, col):
        self.line = line
        self.col = col

    def ejecutar(self, ast, env):
        if env.LoopValidation():
            return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.BREAK)
        ast.setErrors('La sentencia de transferencia no se encuentra dentro de un ciclo')
        err = Errores(self.line, self.col,"Semantico", 'La sentencia de transferencia no se encuentra dentro de un ciclo')
        errores.append(err)
        return Symbol(line=self.line, col=self.col, value=None, type=ExpressionType.NULL)