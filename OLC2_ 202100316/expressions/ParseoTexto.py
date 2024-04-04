from interface.instrucion import Instruction
from environment.types import ExpressionType
from environment.symbol import Symbol
from environment.Errores import Errores,errores

class Parseo(Instruction):
    def __init__(self, line, col, Exp, parseo):
        self.line = line
        self.col = col
        self.Exp = Exp
        self.parseo = parseo
        

    def ejecutar(self, ast, env):
        outText = ""
        outText = self.Exp.ejecutar(ast, env).value
        print(outText)
        
            
        if self.parseo == "toLowerCase" and self.Exp.ejecutar(ast, env).type == ExpressionType.STRING:
            outText = outText.lower()
            #print(outText)
            symbol = Symbol(line=self.line, col=self.col, value=outText, type=ExpressionType.STRING)
                # print(symbol.value)
            return symbol

        if self.parseo == "toUpperCase" and self.Exp.ejecutar(ast, env).type == ExpressionType.STRING:
            outText = outText.upper()
            symbol = Symbol(line=self.line, col=self.col, value=outText, type=ExpressionType.STRING)
            return symbol
        
        if self.parseo == "toString":
            outText = str(outText)
            symbol = Symbol(line=self.line, col=self.col, value=outText, type=ExpressionType.STRING)
            return symbol
       
        ast.setErrors('Error: El tipo de dato '+ self.Exp.id +' no es String en la fila: '+ str(self.line))
        err = Errores(self.line, self.col,"Semantico",'Error: El tipo de dato '+ self.Exp.id +' no es String en la fila: '+ str(self.line))
        errores.append(err)
        return  Symbol(line=self.line, col=self.col, value='', type=ExpressionType.NULL)