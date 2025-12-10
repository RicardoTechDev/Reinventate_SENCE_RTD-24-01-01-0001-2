//========== INTRODUCCCIÓN A JAVASCRIPT ============

//Esto es un comentario de una línea

/*  
    Este 
    es 
    un 
    comentario 
    de 
    más 
    de una línea
*/

//====== Variables =========

// Una variable en JavaScript es un espacio de memoria 
// con un nombre para almacenar datos que se pueden utilizar y modificar a lo largo del código.

// PARA DECLARAR VARIABLES 
// No deben contener espacios; se
// recomienda usar _ o camelCase.

//USAMOS EL = PARA ASIGNAR UN VALOR

//Declaración de variables
// var: Era la forma tradicional de declarar variables en JavaScript, pero se ha vuelto
// menos común con la introducción de let y const.
var edad = 25;

/*
let: let permite declarar variables con alcance de bloque, es decir, solo existen dentro
del bloque donde se definen, como en funciones, bucles o condicionales.
pensemos en {   } como bloques
*/
let nombre = "Luis";

/*
const: const se utiliza para declarar constantes, es decir,
variables que no pueden cambiar su valor una vez asignado. Al igual que let, const tiene
un alcance de bloque.
*/
const pi = 3.1416;

edad = 28;//Tipo ded dato entero

edad = "Hola Mundo!"//Tipo de dato String o Texto

console.log(edad);//Función nativa

//=================== Funciones Nativas ===========

/*
Esta función se utiliza para imprimir mensajes en la consola del navegador o en la consola del
entorno de desarrollo. Es útil para realizar pruebas y depurar el código, ya que puedes imprimir
valores y mensajes para verificar el flujo de ejecución.
*/
console.log("Hola Mundo!!");//Imprime Hola mundo

/*
La función alert() muestra una ventana emergente en el navegador con un mensaje para el usuario.
Es útil para mostrar mensajes de advertencia, notificaciones o solicitar confirmación del usuario.
*/
alert("¡Hola, mundo!");

/*
La función confirm() muestra una ventana emergente en el navegador con un mensaje y botones de
confirmación ("Aceptar" y "Cancelar"). Es útil para obtener la confirmación del usuario en situaciones
específicas.
*/
confirm("¿Está seguro de eliminar este elemento?");

/*
El prompt en JavaScript es una función que muestra un cuadro de diálogo al usuario para solicitar una
entrada de datos. Proporciona una forma sencilla de obtener información del usuario a través de una
ventana emergente en el navegador.
*/
prompt("Por favor, ingrese su nombre:")

/*
Estas funciones se utilizan para convertir una cadena de texto en un número entero o de punto
flotante, respectivamente. Son útiles cuando se necesita manipular datos numéricos
ingresados como cadenas de texto.
*/
parseInt("10");
parseFloat("3.14");

//Concatenación 
let primerNombre = "Juan";
let primerApellido = "Perez";

let nombreCompleto = primerNombre + " " + primerApellido + " Salazar";
console.log(nombreCompleto);


let nombreDos = "Juan";
let mensaje = `Hola, ${nombre}!`;
console.log(mensaje);