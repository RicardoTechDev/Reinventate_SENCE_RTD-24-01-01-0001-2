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
    // for(let i=0; i < textos.length; i++){
    //     textos[i].classList.add("resaltar");
    // }

    for(let texto of textos){
        texto.style.color = "red";
        texto.style.backgroundColor = "blue";
        texto.style.fontSize = "30px";
    }
});

//🔹 ============== getElementByTagName() ===========
const parrafos = document.getElementsByTagName("p");
const btnCambiarTextos2 = document.getElementById("boton-cambiar-parrafos2");

btnCambiarTextos2.addEventListener("click", function(){
    for(let parrafo of parrafos){
        parrafo.style.color = "red";
        parrafo.style.fontSize = "30px";
    }
});


//4️⃣ Seleccionar con querySelector (recomendado y más usado hoy)
//Busca el primer elemento que coincida con selector css

/*caracteristicas : 
- Usa selectores css
- Devuelve un sólo elemento
- Más flexible
- Más moderno
- Más de recordar

*/
document.querySelector("#titulo"); // seleciono por id
document.querySelector(".texto"); //seleciono por clase
document.querySelector("p"); //seleciono por nombre de la etiqueta

//Si no encuentra el elemento --> devulve un null

//5️⃣ Selecionar con querySelectorAll()
//Busca todos los elementos que coincidad con un selector css

/* 
Carasteristicas: 
- Devuelve un conjunto de nodos o un alista de nodos 
- permite iterar usando bucles, for, while, forEach
- Es más comodo de utilizar que getElementByTagName() y 
getElementsByClassName
*/

const parrafos3 = document.querySelectorAll(".texto")

const btnCambiarTextos3 = document.getElementById("boton-cambiar-parrafos3");

btnCambiarTextos3.addEventListener("click", function(){
    
    parrafos3.forEach(parrafo => {
        parrafo.style.color = "blue";
        parrafo.style.fontSize = "100px";
    });
});

//6️⃣ Obtención y manipulación de textos y valores
const mensaje = document.getElementById("mensaje");
//const mensaje = document.querySelector("#mensaje");
console.log(mensaje.textContent);

mensaje.textContent = "¡Texto cambiado con Javascript!";
console.log(mensaje.textContent);

mensaje.innerHTML = "<strong>Hola mundo!!</strong>"

/*
Diferecia entre usar textContent y innerHTML:
- textContent --> maneja texto plano
- innerHTML --> maneja text + HTML
*/

//7️⃣ Obtener datos de los inputs
const formulario = document.querySelector("#floatingInputGroup1");
console.log(formulario);

let botonMostrar = document.querySelector("#btnMostrar");
console.log(botonMostrar);

botonMostrar.addEventListener("click", function(){
    console.log(formulario.value);
    const parrafo = document.querySelector("#resultado");
    console.log(parrafo);
    //📌 value se usa SOLO para inputs, selects y textareas.
    //“Los inputs no usan textContent, usan value.”
    parrafo.textContent = formulario.value;
});

//Pedir al usuario que ingrese dos números
//Paso 1 selecionar elementos
//TODO: Revisar conversión directa al recuperar con value
//let numeroUno = Number(document.getElementById("num-uno").value); 
// el value quedá undefined, ya que en esta instacia aun el nodo con 
//id num-uno no tiene un value ingresado por el usuario
let numeroUno = document.getElementById("num-uno");
let numeroDos = document.getElementById("num-dos");
let btnSumar = document.getElementById("btnMostrarSuma");
let resultado = document.getElementById("resultadoSuma");

//Con queryselector
// let numeroUno = document.querySelector("#num-uno");
// let numeroDos = document.querySelector("#num-dos");
// let btnSumar = document.querySelector("#btnMostrarSuma");
// let resultadoSuma = document.querySelector(".resultadoSuma");

//Paso 2 Darle funcionalidad al botón
btnSumar.addEventListener("click", function(){
    let suma = Number(numeroUno.value) + Number(numeroDos.value);
    resultado.textContent = suma;
});

//8️⃣ Agregar nodos al DOM (crear elementos o etiquetas html)
//Ejemplo: agregar un nuevo <li> a una lista
let lista = document.querySelector("#lista");
let botonAgregarNodo = document.querySelector("#btnAgregarNodo");

botonAgregarNodo.addEventListener("click", function(){
    let nuevoItem = document.createElement("li");//crear un nuevo nodo o elemento
    nuevoItem.textContent = "Nuevo Nodo!!";//Le da contenido al nuevo nodo
    lista.appendChild(nuevoItem);//agrega nuevo hijo a el nodo lista (ul)
});

//Otro ejemplo, agregar parrafo
let nuevoParrafo = document.createElement("p");// Crear un elemento <p>
// Obtener el nodo padre al que deseas agregar el nuevo 
let contenedorParrafo = document.querySelector("#contenedo-parrafo");
nuevoParrafo.textContent = "Nuevo parrafo!!";// Agregar contenido al elemento
// Agregar el nuevo elemento como hijo del nodo padre
contenedorParrafo.appendChild(nuevoParrafo);

//9️⃣ Quitar nodos del DOM
let btnRemove = document.querySelector("#btnRemove");
let btnRemoveChild = document.getElementById("btnRemoveChild");

btnRemove.addEventListener("click", function(){
    if (lista.lastElementChild){
        lista.lastElementChild.remove();
    }
});

btnRemoveChild.addEventListener("click", function(){
    if (lista.lastElementChild){
        lista.removeChild(lista.lastElementChild);
    }
});

//🔟 Eventos básicos del DOM
//Evento click
let btnClick = document.getElementById("btnClick");

btnClick.addEventListener("click", function(){
    alert("Botón presionado!!");
});


//Evento input
let ingresoTexto = document.querySelector("#ingresoTexto");
let resultadoInput = document.querySelector("#resultadoInput");

ingresoTexto.addEventListener("input", function(){
    console.log(ingresoTexto.value);
    resultadoInput.textContent = ingresoTexto.value;
});

//Evento change
let ingresoTexto2 = document.querySelector("#ingresoTexto2");
let resultadoInput2 = document.querySelector("#resultadoInput2");

ingresoTexto2.addEventListener("change", function(){
    resultadoInput2.textContent = ingresoTexto2.value;
});

//Evento mouseover --> mouse entra 
let caja = document.querySelector("#caja");

caja.addEventListener("mouseover", function(){
    //console.log("Mouse por aquí");
    caja.style.backgroundColor = "red";
    caja.style.color = "#FFFFFF";
    caja.textContent = "Mouse dentro del nodo!!";
});

//Evento mouseout --> mouse sale
caja.addEventListener("mouseout", function(){
    caja.style.backgroundColor = "#05DF72";
    caja.style.color = "blue";
    caja.textContent = "Mouse fuera del nodo!!";
});


//Evento keydown
let ingresoTexto3 = document.getElementById("ingresoTexto3");
let resultadoInput3 = document.getElementById("resultadoInput3");
//TODO: verificar, no marca la tecla espaciadora
ingresoTexto3.addEventListener("keydown", function(event) {
    //console.log("Se presionó una tecla " + event.key);
    resultadoInput3.textContent = event.key;
});
