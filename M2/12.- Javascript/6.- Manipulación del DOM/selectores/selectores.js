/* 
1️⃣ ¿Qué es el DOM? (explicación simple)

El DOM (Document Object Model) es la forma en que JavaScript “ve” la página web.
📌 El HTML se transforma en un árbol de objetos, donde:

<html> es el nodo principal
<body>, <h1>, <p>, <button> son nodos hijos

👉 JavaScript puede:

Leer elementos
Cambiarlos
Eliminarlos
Crear nuevos

2️⃣ ¿Cómo accedemos al DOM?
JavaScript interactúa con el DOM (Document Object Model) a través del objeto document.

🧠 ¿Qué es el objeto document?

    * El objeto document es el puente entre el código HTML (lo que ves en la página web) y JavaScript.
    * Representa todo el contenido de la página: el HTML, los elementos, los atributos y el texto.

En resumen, document es como el “manejador” de todo lo que está en la página web.

🔍 ¿Cómo usamos document?

Con document, podemos seleccionar, leer y modificar los elementos del HTML de la página. 
Existen varias formas de acceder a los elementos del DOM, y aquí te voy a explicar las más comunes.
*/

//============= SELECTORES ====================
//Selecionamos por id
const titulo = document.getElementById("titulo");
const btnCambiarTitulo = document.getElementById("boton-cambiar-titulo");
console.log(titulo.textContent);//textContent método que me permite recuperar el texto

btnCambiarTitulo.addEventListener("click", function(){
    titulo.textContent = "Nuevo título!!";
});

//Selecionar por clase
const textos = document.getElementsByClassName("texto");
const btnCambiarTextos = document.getElementById("boton-cambiar-parrafos");

btnCambiarTextos.addEventListener("click", function(){
    for(let i=0; i < textos.length; i++){
        textos[i].classList.add("resaltar");
    }
});
