//Bucles en javascript
//Un bucle repite la acción varias veces mientras se cumpla una condición
/* 
Los bucles ofrecen una forma rápida y sencilla de hacer algo repetidamente
*/

//El bucle for
/* 
Un ciclo for se repite hasta que una condición especificada se evalúe como false.
*/

// for(inicio; condición; incremento){
     //código que se repite
// }

for(let i=0; i<= 5; i++){
    console.log("el valor de i es " + i);
}

/* 
for(let i=5; i >= 0; i--){
    console.log("el valor de i es " + i);
}
*/

//While
/* 
Una declaración while ejecuta sus instrucciones 
siempre que una condición especificada se evalúe como true. 
*/

//Se ejecuta mientras una condición se verdadera
//Se usa cuando no sabemos exactamente cuántas repeticiones habrá

let contador = 0;

while (contador <= 5) {
    console.log("el valor de contador es " + contador);
    contador++;
}

// let condicional = true;
// while (condicional) {
//     condicional = false;
// }


// while (true) {
//     break;
// }


//do while
/* 
La instrucción do...while se repite hasta que una condición especificada se evalúe como falsa.
*/
let cont = 6;

do{
    console.log("el valor de contador es " + cont);
    cont++;
}while(cont <=5);


//Arreglos (Arrays)
//¿Qué es un arreglos?
//Un arreglo es u1na variable que permite guardar varios valores en una sola estructura, ordenados por posición.

//podemos almacenar nombres, notas, lista de abarrotes, edades, correos, etc.

let numeros = [0, 20, 30, 40, 50];
let nombres = ["Ana", "Pedro", "Juan"];
let apellidos = ["Saavedra", "Salazar", "Reyes"];

// console.log(numeros[3] + numeros[4]);
// console.log(nombres[1] + " " + apellidos[1]);

console.log(numeros[0]);
console.log(numeros[1]);
console.log(numeros[2]);
console.log(numeros[3]);
console.log(numeros[4]);

console.log(numeros.length);//length nos permite recuperar la cantidad de elementos del array

console.log("========= Recorriendo Frutas con For =============");
let frutas = ["Manzana", "Frutilla", "Plátano", "Sandía", "Naranja"];

for (let indice = 0; indice < frutas.length; indice++ ){
    console.log("Fruta " + frutas[indice] + " en el indice " + indice);
}

console.log("========= Recorriendo Frutas con While =============");
let contador2 = 0;
while (contador2 < frutas.length) {
    console.log("Fruta " + frutas[contador2] + " en el indice " + contador2);
    contador2++;
}

//otra forma de recorrer los elementos de un array
let colores = ["Azul", "Rojo", "Verde", "Amarillo", "Celeste"];

for(let color of colores){
    console.log(color);
}

//Métodos de javascript para trabajar con arrays

//1.- Métodos para agregar y quitar elementos
//push() -> agregar un elemento al al final del array
let numero2 = [1, 4, 8 , 10 , 26];
console.log(numero2); 

numero2.push(125);
console.log(numero2);

//pop() -> elimina el último elemento del array
numero2.pop();
console.log(numero2);

numero2.pop();
console.log(numero2);

//unshif() -> agrega un elemento al inicio
numero2.unshift(82);
console.log(numero2);

//shif() -> elimina el primero
numero2.shift()
console.log(numero2);

//2.- Métodos para recorrer un array
let frutas2 = ["Manzana", "Frutilla", "Plátano", "Sandía", "Naranja"];

//forEach() -> recorre sin devolver un nuevo array
frutas2.forEach(function(fruta) {
    console.log(fruta);
});

//map() -> transforma elementos y devuelve un nuevo array
let numeros2 = [2,4,6,8,10];

let dobles = numeros2.map(function(numero){
    return numero * 2;
});
console.log(dobles);

//filter() -> filtra elementos
let notas = [5.5, 4.3, 6, 4.9, 6.8, 7, 3.2, 2, 3.9];
console.log(notas);
let aprobados = notas.filter(function(nota){
    return nota >= 4;
});
console.log(aprobados);

//🔹 find() → busca el primer elemento que cumpla condición
let edades = [12, 15, 18, 20];

let mayor = edades.find(function(edad) {
    return edad >= 18;
});

console.log(mayor); // 18

//3️⃣ Métodos para REDUCIR datos
let numeros4 = [1, 2, 3, 4];

let suma = numeros4.reduce(function(total, num) {//🧠 Ideal para sumas, promedios, totales
    return total + num;
}, 0);

console.log(suma); // 10

//4️⃣ Métodos para BUSCAR información
//🔹 includes() → verifica si existe un valor
let colores2 = ["Rojo", "Azul", "Verde"];
console.log(colores2.includes("Azul")); // true

//🔹 indexOf() → posición del elemento
console.log(colores.indexOf("Verde")); // 2

//5️⃣ Métodos para ORDENAR y REVERTIR
//🔹 sort() → ordena (¡ojo con números!)
let numeros5 = [3, 1, 10, 2];

numeros5.sort(function(a, b) {
    return a - b;
});

console.log(numeros5); // [1, 2, 3, 10]
/*
❗ ¿Qué pasó?
Por defecto, sort() ordena como texto, no como números.
Es decir:

"10" va antes que "2" porque "1" es menor que "2" al comparar letras.
👉 Por eso necesitamos decirle a JavaScript cómo comparar números.


La función le dice a JavaScript cómo decidir el orden entre dos valores.

🔍 ¿Qué son a y b?
a = un número del arreglo
b = otro número del arreglo

JavaScript va tomando pares de números y los compara.
Ejemplo de pares posibles:

(3, 1)
(1, 10)
(10, 2)

etc.


🧮 ¿Qué significa return a - b?

El resultado de la resta le indica a sort() qué hacer:

Resultado	Significado	Orden
Negativo	a es menor que b	a va antes
Positivo	a es mayor que b	b va antes
0	        Son iguales	        No cambia

*/

//🔹 reverse() → invierte el orden
numeros5.reverse();
console.log(numeros5);

//6️⃣ Métodos para COPIAR o EXTRAER

//🔹 slice() → copia una parte
/* 
🧠 Regla fundamental de slice(inicio, fin)
👉 slice() copia desde la posición inicio
👉 hasta la posición fin, pero SIN incluir fin
📢 El segundo número NO se incluye
*/
let letras = ["a", "b", "c", "d"];

let copia = letras.slice(1, 3);

console.log(copia); // ["b", "c"]

//🔹 splice() → elimina o agrega en cualquier posición
let frutas3 = ["Manzana", "Plátano", "Naranja"];
frutas3.splice(1, 1); // elimina 1 desde la posición 1
console.log(frutas3); // ["Manzana", "Naranja"]

//7️⃣ Métodos para UNIR y CONVERTIR
//🔹 join() → convierte array en texto
let palabras = ["Hola", "mundo"];
let frase = palabras.join(" ");
console.log(frase); // "Hola mundo"

//🔹 concat() → une arrays
let a = [1, 2];
let b = [3, 4];

let unido = a.concat(b);
console.log(unido); // [1, 2, 3, 4]

//Objetos (objetos literales no POO, como variable)
let user = {
    nombres: "Sofía Reyes", 
    edad: 12, 
    direccion: "av siempre viva 1234"
};

console.log("Nombre de usuario: " + user.nombres);
console.log("Edad: " + user.edad);
console.log("Dirección: " + user.direccion);

user.edad = 13;

console.log("La nueva edad de " + user.nombres + " es: " + user.edad);

let usuarios = [
    {
        nombre: "Ana", 
        edad: 34
    },
    {
        nombre: "Pedro",
        edad: 28
    },
    14,
    "Hola munda"    
];

console.log(usuarios[1].nombre);

//Ejmeplo:
//Crear una función que reciba un arreglo de estudiantes (nombre y nota)
//y muestre solo los que tienen nota mayor o igual a 6.0

let alumnos = [
    {nombre: "Ana", nota:6.5},
    {nombre: "Pedro", nota:5.4},
    {nombre: "Juan", nota:5.6},
];

function mostrarAprobados(estudiantes){
    for(let estudiante of estudiantes){
        if(estudiante.nota >= 6){
            console.log(estudiante.nombre + " está aprobado con nota " + estudiante.nota);
        }
    }
}

mostrarAprobados(alumnos);

alumnos.push({
nombre: "Luis", 
nota:3
});

console.log(alumnos);