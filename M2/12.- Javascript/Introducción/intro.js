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

//============ Expresiones aritméticas =============
let x = 5;
let y = 3;

let suma = x + y;
console.log("La suma de x más y es igual a: " + suma);

let resta = x - y
console.log("La resta de x menos y es igual a: " + resta);

let multiplicacion = x * y;
console.log("La multiplicación de x por y es igual a: " + multiplicacion);

let division = x/y;
console.log("La división de x por y es igual a: " + division);

let resto = x % y;
console.log("Resto es igual a: " + resto);

let exponente = x ** y;
console.log("Exponente es igual a: " + exponente);

//============ Operadores de incremento y decremento
/* 
En JavaScript, existen operadores especiales que
permiten aumentar (++) o disminuir (--) el valor de una
variable de forma abreviada, en lugar de escribir una
suma o resta manualmente.
Estos operadores son muy útiles en bucles y en
situaciones donde es necesario modificar el valor de
una variable de manera sencilla.
*/
let variable1 = 10;
console.log(variable1);
variable1 = variable1 + 1;
console.log(variable1);

variable1++;//Incremento en 1
console.log(variable1);//Tiene un valor de 12

variable1 = variable1 - 1;
console.log(variable1);//Tiene un valor de 11

variable1--;
console.log(variable1);

//================ Operadores de asignación ========
let z = 10;

z += 5;
console.log(z);

z -= 3;
console.log(z);

z *= 2;
console.log(z);

z /= 4;
console.log(z);

z %= 2;
console.log(z);


//============== Operadores lógicos =========
let v1 = 5;
let v2 = "5";

/* 
Igualdad (==):
Compara si dos valores son iguales, sin tener en
cuenta el tipo de dato.
*/
console.log(v1 == v2);

/* 
Igualdad estricta (===):
Compara si dos valores son iguales, teniendo en
cuenta tanto el valor como el tipo de dato.
Devuelve true si son iguales en valor y tipo, y false
si no lo son.
*/
console.log( v1 === v2);


/* 
Desigualdad (!= o !==):
Compara si dos valores no son iguales. Devuelve
true si son diferentes y false si son iguales.
El operador !== también verifica el tipo de dato.
Tanto la comparación x != y como x !== y devuelven
true porque los valores son diferentes.
*/
let v3 = 10;//int
let v4 = "10";//string

console.log(v3 != v4);//true
console.log(v3 !== v4);//false

let v5 = 5;
let v6 = 10;

console.log(v5 > v6);
console.log(v5 < v6);
console.log(v5 >= v6);
console.log(v5 <= v6);


//================= Operadores lógicos ==========

let v7 = 5;
let v8 = -10;

// true (verdadero) && true (Verdadero)  ===> true (verdadero)
// false (falso)    && true (Verdadero)  ===> false
// false (falso)    && false (falso)   ===> false
// true (Verdadero) && false (falso)   ===> false
console.log(v7 > 0 && v8 > 0);

// true (verdadero) || true (Verdadero)  ===> true
// false (falso)    || true (Verdadero)  ===> true
// false (falso)    || false (falso)   ===> false
// true (Verdadero) || false (falso)   ===> true
console.log(v7 > 0 || v8 > 0);
