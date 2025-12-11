console.log("===== DEMO: Operadores y condicionales =====");

let a = Number(prompt("Ingrese el primer número (a): ")); 
let b = Number(prompt("Ingrese el primer número (b): ")); 

//typeof(a) nos sirve para obtener el tipo de dato de la variable
console.log ("La variable es " + typeof(a));
console.log ("La variable a " + a);
console.log ("La variable b " + b);

if(Number.isNaN(a) || Number.isNaN(b)){
    console.log("Debe ingresar valores validos!!");
}else{
    console.log("a + b :" + (a+b));
    console.log("a - b :" + (a-b));
    console.log("a * b :" + (a*b));
    console.log("a / b :" + (a/b));
    console.log("a % b :" + (a%b));

    console.log("a es mayor que b " + a > b);

    console.log("Menú de operaciones");

    let opcion = prompt(
        "Eliga una opción \n" +
        "1) Sumar\n" +
        "2) Restar\n" +
        "3) Multiplicar\n" +
        "4) Dividir\n" +
        "5) Modulo"
    )    

    switch(opcion){
        case "1":
            console.log("✅ Resultado a + b :" + (a+b));
            break;
        case "2":
            console.log("✅ Resultado a - b :" + (a-b));
            break;
        case "3":
            console.log("✅ Resultado a * b :" + (a*b));
            break;
        case "4":
            console.log("✅ Resultado a / b :" + (a/b));
            break;
        case "5":
            console.log("✅ Resultado a % b :" + (a%b));
            break;

        default:
            console.log("❌ La opción ingresada no es correcta");

    }

}


