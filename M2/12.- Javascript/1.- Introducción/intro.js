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
let v8 = 10;
/*
Operador AND (&&):
El operador AND devuelve true si ambos
operandos son true, y devuelve false en cualquier
otro caso.
El operador && se utiliza para evaluar dos
expresiones lógicas y devuelve true si ambas
expresiones son verdaderas.

*/
// true (verdadero) && true (Verdadero)  ===> true (verdadero)
// false (falso)    && true (Verdadero)  ===> false
// false (falso)    && false (falso)   ===> false
// true (Verdadero) && false (falso)   ===> false
console.log(v7 > 0 && v8 > 0);

/* 
Operador OR (||):
El operador OR devuelve true si al menos uno
de los operandos es true, y devuelve false solo
si ambos operandos son false.
El operador || se utiliza para evaluar dos
expresiones lógicas y devuelve true si al menos
una de las expresiones es verdadera.
*/

// true (verdadero) || true (Verdadero)  ===> true
// false (falso)    || true (Verdadero)  ===> true
// false (falso)    || false (falso)   ===> false
// true (Verdadero) || false (falso)   ===> true
console.log(v7 > 0 || v8 > 0);

/*
Operador NOT (!):
El operador NOT invierte el valor de una expresión
booleana. Si la expresión es true, el operador NOT
devuelve false, y si la expresión es false, el operador
NOT devuelve true.
El operador ! se utiliza para negar una expresión
lógica. Convierte true en false y viceversa.
*/
console.log(!(v7 > 0));
// Devuelve false
console.log(!(v8 < 0));

/*
Sí — el NOT (!) es súper útil en “cosas reales” cuando 
quieres preguntar lo contrario de una condición, 
o cuando trabajas con banderas tipo isLoggedIn, 
isLoading, isDarkMode, etc.
*/

//Ejemplos
let isDarkMode = false;
// El usuario aprieta un botón "Modo oscuro"
isDarkMode = !isDarkMode;//true
console.log(isDarkMode); // true (se activó)
/*
Aquí ! invierte el valor: false → true, true → false.
Se usa mucho para activar/desactivar cosas.
*/

const isAuthorized = false;
if (!isAuthorized) {
    console.log("Acceso denegado");
}



//============== Sentencias condicionales ========
/* 
Sentencia if-else:
La sentencia if-else es una estructura de control en programación que permite tomar
decisiones basadas en una condición. A diferencia de la sentencia if, que ejecuta un
bloque de código si una condición es verdadera y luego continúa con el resto del
programa, la sentencia if-else permite ejecutar un bloque de código si la condición es
verdadera y otro bloque de código si la condición es falsa.
*/

let hora = 13;
hora--;

if (hora < 12) {
    //Si es verdadera la condición se ejecuta este bloque de código
    console.log("Buenos días");
}else{
    //Si es falsa la condición
    console.log("Buenas tardes");
}

/* 
Operador AND (&&) con IF/ELSE:
El operador && devuelve true si ambas condiciones
son verdaderas. Si alguna de las condiciones es
falsa, devuelve false.
La condición dentro del if utiliza el operador &&
para verificar si la edad es mayor o igual a 18 y si
tiene Licencia es true. Si ambas condiciones son
verdaderas, se muestra el mensaje "puedes
conducir legalmente". Si alguna de las condiciones
es falsa, se muestra el mensaje "No cumples con
los requisitos para conducir".
*/

let edadConductor = 25;
let tieneLicencia = true;

if (edadConductor >= 18 && tieneLicencia){
    console.log("Puedes conducir legalmente.");
}else {
    console.log("No puedes conducir legalmente.");
}

/* 
Operador OR (||) con IF/ELSE:
El operador || devuelve true si al menos una de las
condiciones es verdadera. Solo devuelve false si
ambas condiciones son falsas.
La condición dentro del if utiliza el operador || para
verificar si esEstudiante es true o si esEmpleado es
true. Si al menos una de las condiciones es
verdadera, se muestra el mensaje "Tenes acceso a
descuentos especiales". Si ambas condiciones son
falsas, se muestra el mensaje "No tenes acceso a
descuentos especiales".
*/

let esEstudiante = false;
let esEmpleado = true;

if (esEstudiante || esEmpleado){
    console.log("Tienes acceso a descuentos!!");
}else{
    console.log("No tienes acceso a descuentos!!");
}

/* Switch
La sentencia switch en JavaScript es una estructura de control condicional 
que permite ejecutar diferentes bloques de código basándose en el valor de 
una expresión, sirviendo como una alternativa más organizada y 
legible a múltiples if...else if anidados, evaluando una variable y 
comparándola con varios case (casos), ejecutando el bloque del caso 
coincidente y un default (predeterminado) opcional si no hay coincidencias, 
siendo clave la sentencia break para evitar la "caída" (ejecución de casos posteriores). 

*/

let expr = "Pl";

switch (expr) {
    case "Naranjas":
        console.log("El kilogramo de naranjas cuesta $0.59.");
        break;
    case "Manzanas":
        console.log("El kilogramo de manzanas cuesta $0.32.");
        break;
    case "Platanos":
        console.log("El kilogramo de platanos cuesta $0.48.");
        break;
    case "Cerezas":
        console.log("El kilogramo de cerezas cuesta $3.00.");
        break;
    case "Papayas":
        console.log("El kilogramo de mangos y papayas cuesta $2.79.");
        break;
    default:
        console.log("Lo lamentamos, por el momento no disponemos de " + expr + ".");
}

let foo = 0;

switch (foo) {
    case -1:
        console.log("1 negativo");
        break;
    case 0: // foo es 0, por lo tanto se cumple la condición y se ejecutara el siguiente bloque
        console.log(0);
    // NOTA: el "break" olvidado debería estar aquí
    case 1: // No hay sentencia "break" en el 'case 0:', por lo tanto este caso también será ejecutado
        console.log(1);
        break; // Al encontrar un "break", no será ejecutado el 'case 2:'
    case 2:
        console.log(2);
        break;
    default:
        console.log("default");
}

//========== Operador ternario ========

let num1 = 7;
let num2 = 5;

let rta = num1 < num2 ? "el 1" : "el 2";

/* COMPARACIÓN DE OPERADOR TERNARIO CON IF ELSE
let rta2;

if (num1 < num2) {
    rta2 = "el 1";
}else{
    rta2 = "el 2"
}
console.log(rta2);
*/
console.log(rta);