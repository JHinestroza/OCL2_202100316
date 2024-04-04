from interface.instrucion import Instruction
from environment.environment import Environment
from environment.execute import LoopExecuter
from expressions.Access import Access

class For(Instruction):
    def __init__(self, line, col, Ran1,Ran2,block,suma):
        self.line = line
        self.col = col
        self.Ran1 = Ran1
        self.Ran2 = Ran2
        self.block = block
        self.suma = suma    
        
        
    def ejecutar(self, ast, env):
    # Variables de iteración
        safe_cont = 0
        breakFlag = False
        result = None
        self.Ran1.ejecutar(ast, env)
        print("cilco for papa")
        # Ciclo
        while True:
            safe_cont += 1
            # Obtencion de la expresión        
            result = self.Ran2.ejecutar(ast, env)
            print(result)
            # Validación
            if result.value:
                for_env = Environment(env, "FOR")
                breakFlag = LoopExecuter(self.block, ast, for_env)
                self.suma.ejecutar(ast, env)
                if breakFlag:
                    break
            else:
                break
            # Validar limite de seguridad
            if safe_cont >= 1000:
                ast.setErrors('Se ha excedido los ciclos permitidos')
                break
            
            
        # print("PARA EL FOR")

        # print("estrando al for ", self.Ran2)
        # Ran1 = self.Ran1.exp.value
        # self.Ran1.ejecutar(ast,env)
        # print("estrando al fro y soy ran1 ", Ran1)
        # Ran2 = self.Ran2.ejecutar(ast,env)
       
        # print(Ran2)
        # safe_cont = 0
        # print("entre al for pa")
        # if self.signo == "<":
        #      print("entre al for pa 2")
        #      while True:
        #         self.Ran1.exp.value = Ran1
        #         env.setVariable(ast, self.Ran1.id, self.Ran1.exp)
        #         safe_cont += 1
        #         # Obtencion de la expresión
        #         # Validación
        #         if Ran1 < Ran2.value:
        #             self.Ran1.exp.value = Ran1
        #             while_env = Environment(env, "WHILE")
        #             breakFlag = LoopExecuter(self.block, ast, while_env)
        #             if breakFlag:
        #                 break
        #         else:
        #             break
        #         # Validar limite de seguridad
        #         if safe_cont >= 1000:
        #             ast.setErrors('Se ha excedido los ciclos permitidos')
        #             break
        #         Ran1 +=1
                    
        # else:
        #     print("entre al for pa 2")
        #     while True:
        #         self.Ran1.exp.value = Ran1
        #         env.setVariable(ast, self.Ran1.id, self.Ran1.exp)
        #         safe_cont += 1
        #         # Obtencion de la expresión
        #         # Validación
        #         if Ran1 < Ran2.value+1:
        #             while_env = Environment(env, "WHILE")
        #             breakFlag = LoopExecuter(self.block, ast, while_env)
        #             if breakFlag:
        #                 break
        #         else:
        #             break
        #         # Validar limite de seguridad
        #         if safe_cont >= 1000:
        #             ast.setErrors('Se ha excedido los ciclos permitidos')
        #             break
                
        #         Ran1 +=1