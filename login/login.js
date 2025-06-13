$(document).ready(function(){
    $("#verificar").click(function(){
        usuario =$("#usuario").val();
        contraseña =$("#contraseña").val();
        valores = valores = { usuario: usuario, contraseña: contraseña };
        $.post("http://127.0.0.1:5000/verificar", valores,function(data,status){
            console.log(status)
            $("#result").text(data)
        });
    });
});