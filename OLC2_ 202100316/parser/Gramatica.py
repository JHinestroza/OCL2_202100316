from environment.types import ExpressionType
from environment.ast import Ast
from environment.Errores import Errores, errores
from ply.lex import LexToken


from expressions.operaciones import Operation
from expressions.primitive import Primitive
from expressions.comparacion import Comparation
from expressions.Relational import Relational
from expressions.Logicos import Logic
from expressions.Array_acces import ArrayAccess
from expressions.Access import Access
from expressions.break_statetement import Break
from expressions.ParseoTexto import Parseo
from expressions.Operadores import Operadores
from expressions.continue_statement import Continue
from expressions.Array import Array
from expressions.interfaceAccess import InterfaceAccess
from expressions.return_statement import Return
from expressions.Call import Call
from expressions.Array_instruction import ArrayInstruccion
from expressions.Embebidas import Embebida
from expressions.ternario import Ternario

from instrucciones.console import Print
from instrucciones.While import While
from instrucciones.Assigment import Assignment
from instrucciones.ArrayDeclaration import ArrayDeclaration
from instrucciones.Declaration import Declaration
from instrucciones.condicion import Condicion
from instrucciones.For import For
from instrucciones.Function import Function
from instrucciones.SwitchStatement import Switch
from instrucciones.case_statement import Cases
from instrucciones.Interface import Interface
from instrucciones.Interface_Declaration import InterfaceDeclaration
from instrucciones.AssigmentArray import AssigmentArray


ast = Ast()
simbolos = []


class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column

reservadas = {
    'console' : 'CONSOLE',
    'number': 'NUMBER',
    'var': 'VAR',
    'char': 'CHAR',
    'string': 'STRING',
    'float': 'FLOAT',
    'while': 'WHILE',
    'boolean': 'BOOLEAN',
    'if': 'IF',
    'else': 'ELSE',
    'log': 'LOG',
    'for': 'FOR',
    'const': 'CONST',
    'tolowercase': 'LCASE',
    'touppercase': 'UPCASE',
    'break' : 'BREAK',
    'continue': 'CONTINUE',
    'function' : 'FUNC',
    'interface' : 'INTERFACE',
    'return' : 'RETURN',
    'length' : 'LENGHT',
    'push' : 'PUSH',
    'indexof':'INDEXOF',
    'join' : 'JOIN',
    'pop' : 'POP',
    'parseint': 'PARSEINT',
    'parsefloat': 'PARSEFLOAT',
    'tostring': 'TOSTRING',
    'typeof': 'TYPEOF',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    
    
}


tokens = [
    
    'PARIZQ',
    'PARDER',
    'CHR_IZQ',
    'CHR_DER',
    'IGUAL',
    'CORIZQ',
    'CORDER',

    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MOD',


    'IGUALDAD',
    'DIFERENTE',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'AND',
    'OR',
    'NOT',

    'PUNTO',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'COMA',


    'CADENA',
    'ENTERO',
    'DECIMAL',
    'BOOLEANO',
    'true',
    'false',
    'ID',
    'TERN',

] + list(reservadas.values())


t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CHR_IZQ    = r'\{'
t_CHR_DER    = r'\}'
t_CORIZQ        = r'\['
t_CORDER        = r'\]'
t_IGUAL    = r'='

t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_MOD      =  r'\%'

t_IGUALDAD = r'=='
t_DIFERENTE = r'!='

t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_PUNTO    = r'\.'
t_PUNTOCOMA    = r';'
t_DOSPUNTOS = r':'
t_COMA = r'\,'
t_false = r'false'
t_true = r'true'
t_TERN          = r'\?'


def t_CADENA(t):
    r'"[^"]*"'
    try:
        strValue = str(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, strValue.replace('"', ''), ExpressionType.STRING)
    except ValueError:
        print("Error al convertir string %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        
        intValue = float(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, intValue, ExpressionType.FLOAT)
    except ValueError:
        print("Error al convertir a decimal %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t

def t_BOOLEANO(t):
    r'true | false'
    print(t.value)
    try:
        boolValue = True 
        if t.value == 'true':
            boolValue = True 
        else:
            boolValue = False
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        # print("esto es un booleano",t.value, " en linea ",t)
        t.value = Primitive(line, column, boolValue, ExpressionType.BOOLEAN)
    except ValueError:
        print("Error al convertir a boleano %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        intValue = int(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, intValue, ExpressionType.INTEGER)
    except ValueError:
        print("Error al convertir a entero %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t


def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t
 



t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(p):
    params = get_params(p) 
    error = Errores(params.line, params.column,"Lexico",p.value[0])
    print(f"Error de Lexico en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'\n   ")
    ast.setErrors(f"Error de Lexico en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'\n   ")
    errores.append(error)
    print(f"Error léxico: Carácter ilegal '{p.value[0]}'")
    p.lexer.skip(1) 

    
#SINTACTICO
precedence = (
    ('left','MAS','MENOS','MOD'), 
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    ('left', 'MENORQUE', 'MAYORQUE'),
    ('left', 'MENORIGUAL', 'MAYORIGUAL'),
)

#START
def p_start(t):
    '''s : block'''
    t[0] = t[1]

def p_instruction_block(t):
    '''block : block instruccion
            | instruccion '''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_instruction_list(t):
    '''instruccion : print PUNTOCOMA
                    | ifinstruction 
                    | declaration
                    | assignment 
                    | whileinstruction
                    | instancia PUNTOCOMA
                    | operadores PUNTOCOMA
                    | forinstruction
                    | breakstmt PUNTOCOMA
                    | continuestmt
                    | arraydeclaration
                    | functionstmt
                    | call
                    | returnstmt
                    | pusheo
                    | switch_statement
                    | constante
                    | interfacecreation
                    | interdeclaration
                    | assigmentarray
                
                     '''
 
    t[0] = t[1]

#Listado de instrucciones
def p_instruccion_console(t):
    '''print : CONSOLE PUNTO LOG PARIZQ expressionList PARDER '''
    params = get_params(t)
    t[0] = Print(params.line, params.column, t[5])

def p_instruction_declaration(t):
    'declaration : VAR ID DOSPUNTOS type IGUAL expresion PUNTOCOMA'
    simbolos.append(t[2])
    params = get_params(t)
    t[0] = Declaration(params.line, params.column, t[2], t[4], t[6])
    
def p_instruction_declaration_const(t):
    'constante : CONST ID DOSPUNTOS type IGUAL expresion PUNTOCOMA'
    simbolos.append(t[2])
    params = get_params(t)
    t[0] = Declaration(params.line, params.column, t[2], t[4], t[6])
    
def p_instruction_assignment(t):
    'assignment : VAR ID IGUAL expresion PUNTOCOMA'
    simbolos.append(t[2])
    params = get_params(t)
    print(t[4])
    t[0] = Declaration(params.line, params.column, t[2], ExpressionType.NULL , t[4])
    
def p_instruction_assignment_const(t):
    'constante : CONST ID IGUAL expresion PUNTOCOMA'
    simbolos.append(t[2])
    params = get_params(t)
    t[0] = Declaration(params.line, params.column, t[2], ExpressionType.NULL  , t[4])


def p_instruction_array_declaration(t):
    '''arraydeclaration : VAR ID DOSPUNTOS type CORIZQ CORDER IGUAL expresion PUNTOCOMA'''
    
    simbolos.append(t[2])
    params = get_params(t)
    t[0] = ArrayDeclaration(params.line, params.column, t[2], t[4], t[8])
    
def p_expression_array_primitiva(t):
    '''expresion : CORIZQ expressionList CORDER'''
    params = get_params(t)
    t[0] = Array(params.line, params.column, t[2])

def p_expression_array_lenght(t):
    '''expresion : ID PUNTO LENGHT
                | ID PUNTO INDEXOF PARIZQ expresion PARDER
                | ID PUNTO POP PARIZQ PARDER'''
    params = get_params(t)
    print(t[3])
    if t[3] == 'length':
        t[0] = ArrayInstruccion(params.line, params.column, t[1], t[3], None)
    if t[3] == 'indexOf':
        t[0] = ArrayInstruccion(params.line, params.column, t[1], t[3], t[5])
    if t[3] == 'pop':
        t[0] = ArrayInstruccion(params.line, params.column, t[1], t[3], None)

    
def p_expression_array_push(t):
    '''pusheo : ID PUNTO PUSH PARIZQ expresion PARDER PUNTOCOMA'''
    params = get_params(t)
    t[0] = ArrayInstruccion(params.line, params.column, t[1], t[3], t[5])
    

def p_expression_array_join(t):
    '''expresion :  ID PUNTO JOIN PARIZQ PARDER  '''
    params = get_params(t)
    t[0] = ArrayInstruccion(params.line, params.column, t[1], t[3], None)


    
def p_instruction_instancia(t):
    'instancia : ID IGUAL expresion '
    params = get_params(t)
    t[0] = Assignment(params.line, params.column, t[1], t[3])

def p_instruction_operadores(t):
    '''operadores : expresion MAS MAS  '''
    params = get_params(t)
    t[0] = Operadores(params.line, params.column,'+=',t[1], Primitive(params.line, params.column, 1, ExpressionType.INTEGER))

def p_type_prod(t):
    '''type : NUMBER
            | FLOAT
            | STRING
            | BOOLEAN
            | ID'''
    if t[1] == 'number':
        t[0] = ExpressionType.INTEGER
    elif t[1] == 'float': 
        t[0] = ExpressionType.FLOAT
    elif t[1] == 'string':
        t[0] = ExpressionType.STRING
    elif t[1] == 'boolean':
        t[0] = ExpressionType.BOOLEAN
    else:
        print("soy un structura")
        t[0] = ExpressionType.STRUCT


def p_expression_array_primitiva_variable(t):
    '''type : type CORIZQ CORDER'''
    t[0] = ExpressionType.ARRAY
    
    

def p_instruction_while(t):
    'whileinstruction : WHILE PARIZQ expresion PARDER CHR_IZQ block CHR_DER'
    params = get_params(t)
    t[0] = While(params.line, params.column, t[3], t[6])

def p_instruction_FOR(t):
    '''forinstruction : FOR PARIZQ declaration  expresion PUNTOCOMA operadores PARDER CHR_IZQ block CHR_DER  '''
    params = get_params(t)
    print("ENTRE AL FOR")
    t[0] = For(params.line, params.column, t[3], t[4], t[9],t[6])

def p_instruction_embebidas(t):
    '''expresion :    PARSEINT PARIZQ expresion PARDER 
                    | PARSEFLOAT PARIZQ expresion PARDER '''
                    
    params = get_params(t)
    t[0] = Embebida(params.line, params.column, t[3], t[1])



def p_instruction_embebidas_string(t):
    '''expresion :    expresion PUNTO TOSTRING PARIZQ PARDER '''          
    params = get_params(t)
    t[0] = Parseo(params.line, params.column,t[1], t[3])

def p_instruction_embebidas_string2(t):
    '''expresion :    ID PUNTO TOSTRING PARIZQ PARDER '''          
    params = get_params(t)
    acceso = Access(params.line, params.column, t[1])
    t[0] = Parseo(params.line, params.column,acceso, t[3])

def p_instruction_embebidas_typeof(t):
    '''expresion :    TYPEOF expresion '''          
    params = get_params(t)
    print(t[1])
    t[0] = Embebida(params.line, params.column, t[2] , t[1])


def p_instruction_if_else(t):
    '''ifinstruction : IF PARIZQ expresion PARDER CHR_IZQ block CHR_DER ELSE CHR_IZQ block CHR_DER
                     | IF PARIZQ expresion PARDER CHR_IZQ block CHR_DER ELSE ifinstruction
                     | IF PARIZQ expresion PARDER CHR_IZQ block CHR_DER'''
    params = get_params(t)
    if len(t) == 8:
        t[0] = Condicion(params.line, params.column, t[3], t[6], None)
    elif len(t) == 12:
        t[0] = Condicion(params.line, params.column, t[3], t[6], t[10])
    else:
        t[0] = Condicion(params.line, params.column, t[3], t[6], [t[9]])


def p_switch_statement(t):
    '''switch_statement : SWITCH PARIZQ expresion PARDER CHR_IZQ cases_statement default_case CHR_DER   
                        | SWITCH PARIZQ expresion PARDER CHR_IZQ cases_statement CHR_DER'''
    print(len(t[6]))
    params = get_params(t)
    if len(t) == 9:
        t[0] = Switch(params.line, params.column,t[3],t[6],t[7])
    else:
        t[0] = Switch(params.line, params.column,t[3],t[6],None)

    
    
    
def p_cases_statement(t):
    '''cases_statement : cases_statement case_statement
                       | case_statement'''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

    
def p_case_statement(t):
    'case_statement : CASE expresion DOSPUNTOS block '
    params = get_params(t)
    t[0] = Cases(params.line, params.column,t[2],t[4])

def p_default_statement(t):
    'default_case : DEFAULT DOSPUNTOS block'
    
    params = get_params(t)
    primitivo =  Primitive(params.line, params.column,"default", ExpressionType.STRING)
    t[0] = Cases(params.line, params.column,primitivo,t[3])

# ESTO ES 
# UNA FUNCION

def p_instruction_call_function(t):
    '''call : ID PARIZQ expressionList PARDER PUNTOCOMA
            | ID PARIZQ PARDER PUNTOCOMA'''
    params = get_params(t)
    if len(t) > 5:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])


def p_instruction_function(t):
    'functionstmt : FUNC ID funcparams functype CHR_IZQ block CHR_DER'
    params = get_params(t)
    simbolos.append(t[2])
    t[0] = Function(params.line, params.column, t[2], t[3], t[4], t[6])
    
    
def p_instruction_interface_creation(t):
    'interfacecreation : INTERFACE ID CHR_IZQ attributeList CHR_DER '
    params = get_params(t)
    t[0] = Interface(params.line, params.column, t[2], t[4])


def p_instruction_interface_declaration(t):
    'interdeclaration : VAR ID DOSPUNTOS ID IGUAL CHR_IZQ interfaceContent CHR_DER PUNTOCOMA'
    params = get_params(t)
    t[0] = InterfaceDeclaration(params.line, params.column, t[2], t[4],t[7])

def p_instruction_interface_declarationvar(t):
    'interdeclaration : CONST ID DOSPUNTOS ID IGUAL CHR_IZQ interfaceContent CHR_DER PUNTOCOMA'
    params = get_params(t)
    t[0] = InterfaceDeclaration(params.line, params.column, t[2], t[4],t[7])

def p_instruction_interface_content(t):
    '''interfaceContent : interfaceContent COMA ID DOSPUNTOS expresion
                | ID DOSPUNTOS expresion'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

    
def p_instruction_interface_attribute(t):
    '''attributeList : attributeList ID DOSPUNTOS type PUNTOCOMA
                | ID DOSPUNTOS type PUNTOCOMA'''
    arr = []
    if len(t) > 5:
        param = {t[2] : t[4]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr


def p_instruction_function_params_list(t):
    '''funcparams : PARIZQ paramsList PARDER
                |  PARIZQ PARDER'''
    if len(t) > 3:
        t[0] = t[2]
    else:
        t[0] = []
        
        
def p_expression_param_list(t):
    '''paramsList : paramsList COMA ID DOSPUNTOS type
                | ID DOSPUNTOS type'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr
        

def p_instruction_function_type(t):
    '''functype : DOSPUNTOS type
                | '''
    if len(t) > 2:
        t[0] = t[2]
    else:
        t[0] = ExpressionType.NULL

def p_instruction_return(t):
    '''returnstmt : RETURN expresion PUNTOCOMA
                | RETURN PUNTOCOMA'''
    params = get_params(t)
    if len(t) > 3:
        t[0] = Return(params.line, params.column, t[2])
    else:
        t[0] = Return(params.line, params.column, None)

#Expresion

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion MOD expresion     '''
    params = get_params(t)
    if t[2] == '+'  : t[0] = Operation(params.line, params.column, "+", t[1], t[3])
    elif t[2] == '-': t[0] = Operation(params.line, params.column, "-", t[1], t[3])
    elif t[2] == '*': t[0] = Operation(params.line, params.column, "*", t[1], t[3])
    elif t[2] == '/': t[0] = Operation(params.line, params.column, "/", t[1], t[3])
    elif t[2] == '%': t[0] = Operation(params.line, params.column, "%", t[1], t[3])

 
def p_expression_call_function(t):
    '''expresion : ID PARIZQ expressionList PARDER
            | ID PARIZQ PARDER'''
    params = get_params(t)
    if len(t) > 4:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])
    
def p_expresion_Relacionales(t):
    '''expresion : expresion MENORQUE expresion
                  | expresion MAYORQUE expresion
                  | expresion MENORIGUAL expresion
                  | expresion MAYORIGUAL expresion'''
    params = get_params(t)
    if t[2] == '<'  :  t[0] = Relational(params.line, params.column, "<", t[1], t[3])
    elif t[2] == '>':  t[0] = Relational(params.line, params.column, ">", t[1], t[3])
    elif t[2] == '<=': t[0] = Relational(params.line, params.column, "<=", t[1], t[3])
    elif t[2] == '>=': t[0] = Relational(params.line, params.column, ">=", t[1], t[3])
    
    
def p_expression_ternario(t):
    'expresion : expresion TERN expresion DOSPUNTOS expresion'
    params = get_params(t)
    t[0] = Ternario(params.line, params.column, t[1], t[3], t[5])
    
    

def p_expresion_logicos(t):
    '''expresion : expresion AND expresion
                  | expresion OR expresion
                  | NOT expresion'''
    
    params = get_params(t)              
    if t[2] == '&&'  : t[0] = Logic(params.line, params.column, "&&", t[1], t[3])
    elif t[2] == '||': t[0] = Logic(params.line, params.column, "||", t[1], t[3])
    elif t[1] == '!':  
        print(t[2])
        t[0] = Logic(params.line, params.column, "!", t[2],  None)

def p_expresion_comparacion(t):
    '''expresion : expresion IGUALDAD expresion
                  | expresion DIFERENTE expresion'''
    
    params = get_params(t)              
    if t[2] == '=='  :  t[0] =  Comparation(params.line, params.column, "==", t[1], t[3])
    elif t[2] == '!=':  t[0] =  Comparation(params.line, params.column, "!=", t[1], t[3])
    
def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "-", Primitive(params.line, params.column, 0, t[2].type), t[2])

def p_expression_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_parseo(t):
    '''expresion    : ID PUNTO  LCASE PARIZQ PARDER  
                | ID PUNTO UPCASE PARIZQ PARDER   '''
    params = get_params(t)
    t[0] = Parseo(params.line, params.column, Access(params.line, params.column, t[1]) , t[3])

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | BOOLEANO   
                    | CADENA
                    | listArray  
                    | DECIMAL        
                    '''
   
    t[0] = t[1]
    
def p_instruction_continue(t):
    'continuestmt : CONTINUE PUNTOCOMA'
    params = get_params(t)
    t[0] = Continue(params.line, params.column)

def p_instruction_break(t):
    'breakstmt : BREAK'
    params = get_params(t)
    t[0] = Break(params.line, params.column)

def p_expression_list(t):
    '''expressionList : expressionList COMA expresion
                    | expresion '''
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

idarreglo = str


def p_assignacion_array(t):
    'assigmentarray :  listArray2 IGUAL expresion PUNTOCOMA'
    global idarreglo
    params = get_params(t)
    t[0] = AssigmentArray(params.line, params.column ,t[1],t[3])


def p_expression_list_array2(t):
    '''listArray2 : listArray2 CORIZQ expresion CORDER
                | listArray2 PUNTO ID
                | ID'''
    global idarreglo
    params = get_params(t)
    if len(t) > 4:
        t[0] = ArrayAccess(params.line, params.column, t[1], t[3])
    elif len(t) == 4:
        t[0] = InterfaceAccess(params.line, params.column, t[1], t[3])
    else:
        idarreglo = t[1]
        t[0] = Access(params.line, params.column, t[1])


def p_expression_list_array(t):
    '''listArray : listArray CORIZQ expresion CORDER
                | listArray PUNTO ID
                | ID'''
    params = get_params(t)
    if len(t) > 4:
        t[0] = ArrayAccess(params.line, params.column, t[1], t[3])
    elif len(t) == 4:
        t[0] = InterfaceAccess(params.line, params.column, t[1], t[3])
    else:
        t[0] = Access(params.line, params.column, t[1])


def p_error(p):
    params = get_params(p)
    if p:
        error = Errores(params.line, params.column,"Sintactico",p.value)
        ast.setErrors(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'\n   ")
        errores.append(error)
        print(f"Error de sintaxis en el token '{p.value}'")
    else:
        print("Error de sintaxis en EOF")
    
    
    # global errores
    # if p:
    #     print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    #     errores.append(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")   
    #     ast.setErrors(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'\n   ")
    #     #Errores(p.lineno, p.lexpos, "sintaxis", p.value)
    # else:
    #     print("Error de sintaxis")
    
    
    


def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)

import parser.ply.lex as Lex
import parser.ply.yacc as yacc

class Parser:
    def __init__(self):
        pass

    def analizar(self,input):
        # print("************ENTRADA***************")
        # print(texto)
        lexer = Lex.lex()
        parser = yacc.yacc()
        result = parser.parse(input)
        return result