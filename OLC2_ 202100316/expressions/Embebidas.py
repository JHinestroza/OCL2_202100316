from interface.instrucion import Instruction
from environment.types import ExpressionType
from environment.symbol import Symbol

class Embebida(Instruction):
    def __init__(self, line, col, exp, parseo):
        self.line = line
        self.col = col
        self.exp = exp
        self.parseo = parseo
        

    def ejecutar(self, ast, env):
        result = self.exp.ejecutar(ast, env)
        self.type = result.type
        symbol =None
        # Validar tipo
        if result.type != self.type:
            ast.setErrors("Los tipos de dato son incorrectos")
            return
        # Agregar al entorno
        parseo = self.exp.ejecutar(ast, env).value           
        if self.parseo == "parseInt":
            
            symbol = Symbol(line=self.line, col=self.col, value=int(parseo), type=ExpressionType.INTEGER)
            return symbol


        if self.parseo == "parseFloat":

            symbol = Symbol(line=self.line, col=self.col, value=float(parseo), type=ExpressionType.FLOAT)
            return symbol
        
        if self.parseo == "typeof":
            
            if result.type== ExpressionType.STRING:
                symbol = Symbol(line=self.line, col=self.col, value="string", type=ExpressionType.STRING)
            if result.type== ExpressionType.INTEGER:
                symbol = Symbol(line=self.line, col=self.col, value="number", type=ExpressionType.STRING)
            if result.type== ExpressionType.FLOAT:
                symbol = Symbol(line=self.line, col=self.col, value="float", type=ExpressionType.STRING)
            if result.type== ExpressionType.BOOLEAN:
                symbol = Symbol(line=self.line, col=self.col, value="boolean", type=ExpressionType.STRING)
            if result.type== ExpressionType.ARRAY:
                symbol = Symbol(line=self.line, col=self.col, value="array", type=ExpressionType.STRING)
            return symbol

       
