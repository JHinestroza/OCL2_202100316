from flask import Flask,render_template, request, jsonify
from parser.Gramatica import Parser
from environment.ast import Ast
from environment.environment import Environment
from environment.execute import RootExecuter
import os
from parser.Gramatica import ast
from parser.Gramatica import simbolos
import graphviz
from environment.Errores import errores


app = Flask(__name__,template_folder="./Templates")
env = Environment(None, 'GLOBAL')

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/obtener-texto", methods=['POST'])
def obtener_texto():
    global simbolos
    data = request.get_json()
    texto = data['EntradaTexto']
    parser = Parser()
    instructionsArr = parser.analizar(texto)
    RootExecuter(instructionsArr, ast, env)
    errores = ast.getErrors()
    res = {"result": True,"console":ast.getConsole(),"errors": ' '.join(map(str,errores)) }
    try:
        tabla = generar_grafo_tabla()
        print(tabla)
    except:
        pass
    generar_grafo_tablaErrores()
    errores.clear()
    simbolos.clear()
    ast.Limpiar()
    env.limpieza()
    print(len(errores))
    return jsonify({'mensaje': res})#esto es lo que retorno y el nombre de la variable







def generar_tabla_html_graphviz():
    global simbolos
    # Encabezado de la tabla
    tabla_html = "<table border='1' cellspacing='0'>\n"
    tabla_html += "<tr><td>ID</td><td>Tipo de símbolo</td><td>Tipo de dato</td><td>Línea</td><td>Columna</td></tr>\n"
    contador = 0
    valor = None
    # Iterar sobre las filas y columnas para generar las celdas de la tabla
    for dato in simbolos:
        tabla_html += "<tr>\n"
        try:
            valor = env.getVariable(ast, dato)
            cadena = str(valor.type)
            cadena = cadena.replace("ExpressionType.", "")
            tabla_html += f"<td> {dato} </td> <td> Variable  </td>  <td> {cadena} </td>  <td> {valor.line}</td> <td> {valor.col}</td>\n"  
        except:
            pass
               

        try:
            valor = env.getVariable(ast, dato)
            valor = env.getFunction(ast, dato)
            cadena = str(valor['type'])
            cadena = cadena.replace("ExpressionType.", "")
            tabla_html += f"<td> {dato} </td> <td> Funcion  </td>  <td> {cadena} </td>  <td> {contador}</td> <td> {contador}</td>\n"
        except:
                pass
        contador +=1
        tabla_html += "</tr>\n"

    # Cierre de la tabla
    tabla_html += "</table>"
    
    return tabla_html

def generar_grafo_tabla():
    tabla_html = generar_tabla_html_graphviz()
    grafo = "digraph G {\n"
    grafo += "node [shape=plaintext]\n"
    grafo += "nodo [label=<{}>]\n".format(tabla_html)
    grafo += "}"
    with open("grafo.dot", "w") as dot_file:
        dot_file.write(grafo)

    # Generar la imagen a partir del archivo DOT
    graph = graphviz.Source(grafo)
    graph.render("tabla de simbolos", format="png",  directory= "./static/Reportes",cleanup=True)
    print("Imagen generada con éxito.")




def generar_tabla_html_Errores():
    global simbolos
    # Encabezado de la tabla
    tabla_html = "<table border='1' cellspacing='0'>\n"
    tabla_html += "<tr>   <td>Tipo</td>  <td>Descripcion</td> <td>Ammbito</td>  <td>Línea</td>  <td>Columna</td>  </tr>\n"
    contador = 0
    valor = None
    # Iterar sobre las filas y columnas para generar las celdas de la tabla
    for error in errores:
        tabla_html += "<tr>\n"
        tabla_html += f"<td> {error.tipo} </td>   <td> {error.exp} </td>  <td> GLOBAL</td>   <td> {error.line}</td> <td> {error.col}</td>\n"
        tabla_html += "</tr>\n"

    # Cierre de la tabla
    tabla_html += "</table>"
    
    return tabla_html

def generar_grafo_tablaErrores():
    tabla_html = generar_tabla_html_Errores()
    grafo = "digraph G {\n"
    grafo += "node [shape=plaintext]\n"
    grafo += "nodo [label=<{}>]\n".format(tabla_html)
    grafo += "}"
    with open("grafo.dot", "w") as dot_file:
        dot_file.write(grafo)

    # Generar la imagen a partir del archivo DOT
    graph = graphviz.Source(grafo)
    graph.render("tablaErrores", format="png",  directory= "./static/Reportes",cleanup=True)
    errores.clear()
    print("Imagen generada con éxito.")





if __name__ == '__main__':
    archivo_a_borrar = "./parser/parsetab.py"

# Intenta borrar el archivo
    try:
        os.remove(archivo_a_borrar)
        print(f"El archivo '{archivo_a_borrar}' ha sido borrado exitosamente.")
    except OSError as e:
        print(f"No se pudo borrar el archivo '{archivo_a_borrar}': {e}")
    app.run(debug=True)