let alertas = document.getElementById("alertas");
let form = document.querySelector("#formRegistro");
let nombre = document.querySelector("#nombre");
let correo = document.querySelector("#correo");
let edad = document.querySelector("#edad");

console.log(alertas);
console.log(nombre);

form.addEventListener("submit", function(event){
    //para evitar que se recargue la página
    event.preventDefault();//evita el envìo real del formulario
    //console.log("Evento formulario: " + event);

    // if(nombre.value === "" || correo.value === "" || edad.value === ""){
    //     //lanzar alerta campos vacíos
    //     //console.log("Campos incompletos");
    //     mostrarAlerta("Todos los campos son obligatorios", "danger");
    //     return;
    // }

    //Limpiar div o nodo de las alertas
    alertas.innerHTML = "";

    if(nombre.value === ""){
        //lanzar alerta campos vacíos
        //console.log("Campos incompletos");
        mostrarAlerta("El campo nombre es obligatorio", "danger");
        return;
    }

    if(correo.value === ""){
        //lanzar alerta campos vacíos
        //console.log("Campos incompletos");
        mostrarAlerta("El campo correo es obligatorio", "danger");
        return;
    }

    if(edad.value === ""){
        //lanzar alerta campos vacíos
        //console.log("Campos incompletos");
        mostrarAlerta("El campo edad es obligatorio", "danger");
        return;
    }

    const edadNumero = Number(edad.value);

    if(Number.isNaN(edadNumero)){
        mostrarAlerta("El campo edad debe ser númerico", "danger");
        return; 
    }
    //console.log(edadNumero);

    if(edadNumero < 0){
        mostrarAlerta("El campo edad debe ser mayor a cero", "danger");
        return; 
    }

    //Simulación de envío al backend
    const datosUsuario = {
        nombre: nombre.value,
        correo: correo.value,
        edad: edad.value
    }

    console.log("Enviando datos al backend... " + datosUsuario );

    setTimeout(function() {
        console.log("Datos recibidos en el backend");
        mostrarAlerta("Usuario registrado de manera correcta!!", "success");
        //Reset de los campos del formulario (borra información de los inputs)
        form.reset();
    }, 3000);

});


function mostrarAlerta(mensaje, tipo){
    alertas.innerHTML = `
    <div class="alert alert-${tipo}" role="alert">
        ${mensaje}
    </div>
    `;
}