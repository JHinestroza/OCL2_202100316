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

class Relational(Expression):
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

        # MAYOR QUE
        if self.operador == ">":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value > op2.value, type=ExpressionType.BOOLEAN)
            ast.setErrors('Error: tipos incorrectos para mayor qué')
            err = Errores(self.line, self.col,"Semantico",'Error: tipos incorrectos para mayor qué')
            errores.append(err)
        # MENOR QUE
        if self.operador == "<":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value < op2.value, type=ExpressionType.BOOLEAN)
            ast.setErrors('Error: tipos incorrectos para menor qué')
            err = Errores(self.line, self.col,"Semantico",  'Error: tipos incorrectos para menor qué')
            errores.append(err)
        # MAYOR IGUAL QUE
        if self.operador == ">=":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value >= op2.value, type=ExpressionType.BOOLEAN)
            ast.setErrors('Error: tipos incorrectos para mayor igual qué')
            err = Errores(self.line, self.col,"Semantico",'Error: tipos incorrectos para mayor igual ')
            errores.append(err)
        # MENOR IGUAL QUE
        if self.operador == "<=":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value <= op2.value, type=ExpressionType.BOOLEAN)
            
            err = Errores(self.line, self.col,"Semantico",'Error: tipos incorrectos para menor igual qué')
            errores.append(err)
            ast.setErrors('Error: tipos incorrectos para menor igual qué')