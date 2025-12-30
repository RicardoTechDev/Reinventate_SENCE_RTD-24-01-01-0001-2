/*========================
1) Evento click
=========================*/
$("#btnClick").on("click", function(){
    console.log("Se presiono el botón con click");
    Swal.fire({
    icon: "success",
    title: "Sweet!",
    text: "Modal with a custom image.",
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 1500,
    timerProgressBar: true,
    })
});

/*========================
2) Evento dblclick
=========================*/
$("#btnDblClick").on("dblclick", function(){
    if($(this).hasClass("btn-secondary")){
        $(this).removeClass("btn-secondary").addClass("btn-danger");
    }else{
        $(this).removeClass("btn-danger").addClass("btn-secondary");
    }
});

/*========================
3) Evento mouseenter
=========================*/
$("#btnMouse").on("mouseenter", function(){
    $(this).addClass("btn-lg");
});

/*========================
4) Evento mouseleave
=========================*/
$("#btnMouse").on("mouseleave", function(){
    $(this).removeClass("btn-lg");
});

/*========================
5) Evento keydown, keyup y keypress
=========================*/
$("#txtTeclado").on("input", function(){
    let texto = $(this).val();
    $("#textoprevio strong").text(texto);
})

$("#txtTeclado").on("keydown", function(){
    $("#eventoteclado strong").text("Evento keydown");
})

$("#txtTeclado").on("keyup", function(){
    $("#eventoteclado strong").text("Evento keyup");
})

$("#txtTeclado").on("keypress", function(){
    $("#eventoteclado strong").text("Evento keypress");
})


