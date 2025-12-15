function saludar(nombre, edad){
    console.log("¡Hola " + nombre + " tienes " + edad + " años!")
}

saludar("Luis Ríos", 32);
saludar("Ariel Lazcano", 31);


function sumaTresNumeros(nun1, nun2, nun3){
    
    let suma = nun1 + nun2 + nun3;
    return suma;
}
console.log(nun1);

let edad = 45;
let z = 15;
let y = 23;

let resultado = sumaTresNumeros(y, z, edad);
console.log("resultado " + resultado);

//============= Funciones anónimas ============
/* 
Las funciones anónimas son útiles cuando se necesitan funciones temporales o cuando se
desea utilizar una función como argumento en otra función, como en el caso de funciones de
devolución de llamada (callback functions) o funciones de orden superior (higher-order
functions).
Es importante tener en cuenta que, aunque las funciones anónimas no tienen un nombre
específico, se asignan a variables u otros elementos para poder ser utilizadas posteriormente.
*/

let suma = function (a, b) {return a+b};
let resta = function (a, b) {return a-b};

console.log(suma(15,20));
console.log(resta(15,5));


//Funciones Flechas =>
/* 
Se declara una variable miFuncion y se le asigna una función flecha como valor. El cuerpo de la
función se encuentra dentro de los corchetes {}, donde se pueden escribir las operaciones que
realizará la función.
Si la función flecha tiene un solo parámetro, se pueden omitir los paréntesis alrededor del parámetro.
*/

let suma2 = (a, b) => {return a + b};
let resta2 = (a, b) => {return a - b}; 

console.log(suma2(15,20));
console.log(resta2(15,5));

//Callback
/* 
Los callbacks son funciones que se pasan como
argumentos a otras funciones. Son una forma común
de lograr la ejecución asíncrona y la programación
basada en eventos en JavaScript.
La idea principal detrás de los callbacks es permitir
que una función sea llamada dentro de otra función
después de que se haya completado una tarea o
evento específico. Esto permite una programación
más flexible y dinámica, ya que puedes definir el
comportamiento que se debe ejecutar después de
ciertas operaciones.
*/

function operacionAsincrona(callback){
    console.log("Hola mundo!");
    callback();
}


function miOtraFuncion() {
    console.log("La operación asincrónica se ha completado.");
}

operacionAsincrona(miOtraFuncion);


//Ejemplo tarea que tarda en ejecutarse con callback

function cargarDatos(callback){
    console.log("Cargando datos...");
    //setTimeout es una función de Javascript que sirve para
    //ejecutar algo después de un tiempo (un retraso)
    setTimeout(function () {
        console.log("Datos cargados");
        callback();//Se jecuta luego del tiempo de retraso
    },10000);
}

function mostrarMensaje() {
    console.log("Ya puedes usar los datos");
}

cargarDatos(mostrarMensaje);

/*
1) Saber si un número es par

Enunciado:
Crea una función esPar(numero) que retorne true si el número es par y false si es impar.


2) Convertir grados Celsius a Fahrenheit

Enunciado:
Crea una función celsiusAFahrenheit(c) que reciba grados Celsius y retorne su equivalente en Fahrenheit.
Fórmula: F = (C * 9/5) + 32


3) Devolver el mayor de dos números

Enunciado:
Crea una función mayor(a, b) que retorne el número más grande. Si son iguales, retorna cualquiera (por ejemplo a).

4) Calcular el área de un rectángulo

Enunciado:
Crea una función areaRectangulo(base, altura) que reciba la base y la altura, y retorne el área.
Fórmula: área = base * altura


5) Convertir años a días

Enunciado:
Crea una función aniosADias(anios) que reciba una cantidad de años y retorne cuántos días son (considera que 1 año tiene 365 días).

*/