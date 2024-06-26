from interface.expresion import Expression

class InterfaceAccess(Expression):
    def __init__(self, line, col, exp, id):
        self.line = line
        self.col = col
        self.exp = exp
        self.id = id

    def ejecutar(self, ast, env):
        envInterface = self.exp.ejecutar(ast, env)
        # Retornar busqueda de atributo
        sym = envInterface.getVariable(ast, self.id)
        return sym