//Bucles en javascript
//Un bucle repite la acción varias veces mientras se cumpla una condición

//El bucle for
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

let cont = 6;

do{
    console.log("el valor de contador es " + cont);
    cont++;
}while(cont <=5);