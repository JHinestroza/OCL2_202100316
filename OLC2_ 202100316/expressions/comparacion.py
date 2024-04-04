from interface.expresion import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol
from environment.Errores import Errores,errores

dominant_table = [
    [ExpressionType.INTEGER, ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.FLOAT,   ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.STRING,  ExpressionType.STRING, ExpressionType.STRING, ExpressionType.STRING,  ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.STRING, ExpressionType.BOOLEAN, ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.NULL,   ExpressionType.NULL,    ExpressionType.NULL],
]

class Comparation(Expression):
    def __init__(self, line, col, operador, opL, opR):
        self.line = line
        self.col = col
        self.operador = operador
        self.opL = opL
        self.opR = opR

    def ejecutar(self, ast, env):
        # print("entre a ejecutarme")
        op1 = self.opL.ejecutar(ast, env)
        op2 = None
        dominant_type = ExpressionType.NULL
        if self.opR != None:
            op2 = self.opR.ejecutar(ast, env)
            dominant_type = dominant_table[op1.type.value][op2.type.value]
        elif self.operador == '!':
            dominant_type = ExpressionType.BOOLEAN

         # IGUAL
        if self.operador == "==":
            return Symbol(line=self.line, col=self.col, value=op1.value == op2.value, type=ExpressionType.BOOLEAN)
        # DIFERENTE
        if self.operador == "!=":
            return Symbol(line=self.line, col=self.col, value=op1.value != op2.value, type=ExpressionType.BOOLEAN)