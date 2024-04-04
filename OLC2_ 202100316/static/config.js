var myTextarea = document.getElementById("Entrada");

// Número deseado de líneas
var numLines = 40; // Por ejemplo, establece el número deseado de líneas aquí

// Calcular la altura del editor
var lineHeight = 20; // Altura de una línea (puedes ajustar esto según tu configuración)
var editorHeight = numLines * lineHeight + "px";



// Inicializar CodeMirror
var myCodeMirrorEntrada = CodeMirror.fromTextArea(myTextarea, {
    lineNumbers: true,  // Activar números de línea
    mode: "javascript",  // Modo de lenguaje (por ejemplo, JavaScript)
    theme: "material",
    viewportMargin: 20
});

myCodeMirrorEntrada.setSize(800, editorHeight);

var myTextareaSalida = document.getElementById("Salida");

// Inicializar CodeMirror
var TextoSalida = CodeMirror.fromTextArea(myTextareaSalida, {
    lineNumbers: true,  // Activar números de línea
    mode: "javascript",
    theme: "material" ,
    viewportMargin: 20// Modo de lenguaje (por ejemplo, JavaScript)
});


TextoSalida.setSize(800, editorHeight);

document.getElementById("ejecutar").addEventListener('click', function () {
    fetch('/obtener-texto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            EntradaTexto: myCodeMirrorEntrada.getValue()
            
    
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.mensaje)
            var objetoJSON = JSON.parse(JSON.stringify(data.mensaje))
            var consola = objetoJSON.console
            var errores = objetoJSON.errors
            console.log(consola)
            var texto = consola + errores
            console.log("hola que hace consola pedorra " , typeof consola)
            TextoSalida.setValue(texto)
            


        })
        .catch(error => {
            //console.error('Error por aca:', error);
        });
   
});

