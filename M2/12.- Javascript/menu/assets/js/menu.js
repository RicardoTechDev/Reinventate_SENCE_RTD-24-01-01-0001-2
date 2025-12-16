let opcion;

// for(inicio; condición; incremento){
//     //ejecución del código
// }

do{
    //1° Capturar lo ingrese el usuario
    opcion = prompt(
        "MEMÚ PRINCIPAL\n" +
        "1. Saludar\n" +
        "2. Mostrar fecha\n" +
        "3. Salir\n\n" +
        "Elige una opción:"
    )

    switch(opcion){
        case "1":
            alert("Hola! Bienvenido al programa");
            break;
        case "2":
            let fecha = new Date();
            alert("Fecha actual: " + fecha.toLocaleDateString());
            break;
        case "3":
            alert("Saliendo del programa...");
            break;
        default:
            alert("Opción no válida, intentelo nuevamente");
    }
    //ejecución del código
}while(opcion !== "3");