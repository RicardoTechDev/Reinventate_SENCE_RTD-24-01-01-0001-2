//Uso de try catch
//estructura básica

try {
    //Código que pudiera generar un error
}catch(error){
    //Código que se ejecuta si ocurre un error
}

/*
try :
- Contiene el código que podría fallar
Javascript lo intenta ejecutar

catch:
Se ejecuta sólo si ocurrio un error
recibe un objeto error con la información 
del error o del proble que esta ocurriendo
*/

//Ejemplo
function calcularTotal(precio, cantidad){
    return precio * cantidadd;//No existe la variable cantidadd con 2 d
}

try{
    const total = calcularTotal(1000, 2);
    console.log("Total: " + total);
}catch(error){
    console.error("Error en el calculo del total: " + error.message);
}