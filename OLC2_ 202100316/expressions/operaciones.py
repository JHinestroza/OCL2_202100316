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

class Operation(Expression):
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
        # Suma
        if self.operador == "+":
            if type(op1.value) == str or type(op2.value) == str :
                symbol = Symbol(line=self.line, col=self.col, value=str(op1.value)+str(op2.value), type=dominant_type)
                return symbol
            else:
                symbol = Symbol(line=self.line, col=self.col, value=op1.value+op2.value, type=dominant_type)
                # print(symbol.value)
                return symbol
        # Resta
        if self.operador == "-":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value-op2.value, type=dominant_type)
            ast.setErrors('Error: tipos incorrectos para restar')
            err = Errores(self.line, self.col,"Semantico",'Error: tipos incorrectos para restar')
            errores.append(err)
            
            
        # Multiplicación
        if self.operador == "*":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value*op2.value, type=dominant_type)
            ast.setErrors('Error: tipos incorrectos para multiplicar')
            err = Errores(self.line, self.col,"Semantico",'Error: tipos incorrectos para restar')
            errores.append(err)
        # División
        if self.operador == "/":
            if op2.value == 0:
                ast.setErrors("Error: no se puede dividir por 0")
                return 
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value/op2.value, type=dominant_type)
            ast.setErrors('Error: tipos incorrectos para dividir')
            err = Errores(self.line, self.col,"Semantico",'Error: tipos incorrectos para dividir')
            errores.append(err)
        # Modular
        if self.operador == "%":
            if dominant_type == ExpressionType.INTEGER or dominant_type == ExpressionType.FLOAT:
                return Symbol(line=self.line, col=self.col, value=op1.value % op2.value, type=dominant_type)
            ast.setErrors('Error: tipos incorrectos para multiplicar')
            err = Errores(self.line, self.col,"Semantico",'Error: tipos incorrectos para multiplicar')
            errores.append(err)