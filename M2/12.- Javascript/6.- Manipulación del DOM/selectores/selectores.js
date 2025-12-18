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
/*
3️⃣ Seleccionar elementos del DOM

🔹 ========== Por ID (el más usado) =================
<h1 id="titulo">Hola Mundo</h1>
*/
// Seleccionamos el elemento por ID
const titulo = document.getElementById("titulo");
// Seleccionamos el botón
const btnCambiarTitulo = document.getElementById("boton-cambiar-titulo");
console.log(titulo.textContent);//textContent método que me permite recuperar el texto

// Agregamos el evento click
btnCambiarTitulo.addEventListener("click", function(){
    //Manipulación de valores

    /*👉 textContent Lee o modifica TODO el texto real del elemento,
    tal como está en el HTML, sin importar estilos. 

    ✅ Características
    Devuelve todo el texto
    Incluye texto oculto (display: none)
    No interpreta HTML
    Es más rápido
    Es el más recomendado para cambiar texto
    */
    titulo.textContent = "¡Título cambiado con JavaScript! 🚀";

    /*La propiedad innerText de un nodo nos permite modificar su nodo de texto. 
    Es decir, acceder y/o modificar el contenido textual de algún elemento del DOM.
    
    👉 Lee o modifica SOLO el texto visible en pantalla.
    ✅ Características
    Respeta CSS (display:none)
    No muestra texto oculto
    Depende del renderizado
    Es más lento
    Se usa cuando importa lo que el usuario ve
    */
    titulo.innerText = "Nuevo texto con innerText!!";
});

//🔹 ===========  Por clase =======================
//📌 Devuelve una colección, no un solo elemento.
const textos = document.getElementsByClassName("texto");
const btnCambiarTextos = document.getElementById("boton-cambiar-parrafos");

btnCambiarTextos.addEventListener("click", function(){
    for(let i=0; i < textos.length; i++){
        textos[i].classList.add("resaltar");
    }
});
