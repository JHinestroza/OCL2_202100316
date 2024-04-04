from interface.expresion import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType

class ArrayInstruccion(Expression):
    def __init__(self, line, col, id,instruccion, expresion):
        self.line = line
        self.col = col
        self.id = id
        self.instruccion = instruccion
        self.exp = expresion 

    def ejecutar(self, ast, env):
        if self.instruccion == 'length':
             sym = env.getVariable(ast, self.id)
             symbol = Symbol(self.line,self.col, len(sym.value) , ExpressionType.INTEGER)   
             return symbol
        if self.instruccion == 'push':
            sym = env.getVariable(ast, self.id)
            result = self.exp.ejecutar(ast,env)
            bandera = False
            arr2 = []
            for arr in sym.value:
                arr2.append(arr)
                
            symbol = Symbol(self.line,self.col, result.value , result.type)
            arr2.append(symbol)      
            symbol2 = Symbol(self.line,self.col, arr2 , sym.type)
            for arr in arr2:
                print(arr.value)
            env.setVariable(ast, self.id, symbol2)
            
        if self.instruccion == 'indexOf':
            sym = env.getVariable(ast, self.id)
            result = self.exp.ejecutar(ast,env)
            contador = 0
            bandera = False
            print("entre a indexof")
            for arr in sym.value:
                if arr.value == self.exp.value:   
                    bandera = True          
                    symbol = Symbol(self.line,self.col, contador , ExpressionType.INTEGER)
                    return symbol
                
                contador +=1
           
            if not bandera:
               symbol = Symbol(self.line,self.col, -1 , ExpressionType.INTEGER)
               return symbol
            
        
        if self.instruccion == 'join':
            sym = env.getVariable(ast, self.id)
            cadena = ""
            for arr in sym.value:
                cadena += str(arr.value )+ ","
            print(cadena)
            symbol = Symbol(self.line,self.col, cadena , ExpressionType.STRING)
            return symbol
        
        if self.instruccion == 'pop':
            sym = env.getVariable(ast, self.id)
            symbol2 = Symbol(self.line,self.col, sym.value[-1].value , ExpressionType.STRING)
            sym.value.pop()
            symbol = Symbol(self.line,self.col, sym.value , sym.type)
            env.setVariable(ast, self.id, symbol)
            return symbol2