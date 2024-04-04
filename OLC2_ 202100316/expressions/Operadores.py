from interface.expresion import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol

dominant_table = [
    [ExpressionType.INTEGER, ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.FLOAT,   ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.STRING,  ExpressionType.STRING, ExpressionType.STRING, ExpressionType.STRING,  ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.STRING, ExpressionType.BOOLEAN, ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.NULL,   ExpressionType.NULL,    ExpressionType.NULL],
]

class Operadores(Expression):
    def __init__(self, line, col, operador, id, exp):
        self.line = line
        self.col = col
        self.operador = operador
        self.id = id
        self.exp = exp

    def ejecutar(self, ast, env):
        variable = self.id.ejecutar(ast, env)
        print("esto es la valor de la variable" ,variable.type)
        suma = self.exp.value
        if self.operador == "+=": 
            result = variable.value + suma
            symbol=  Symbol(line=self.line, col=self.col, value=result, type=variable.type)
            env.setVariable(ast, self.id.id, symbol)
            
        if self.operador == "-=":
            result = variable.value - suma.value
            symbol=  Symbol(line=self.line, col=self.col, value=result, type=variable.type)
            env.setVariable(ast, self.id.id, symbol)