$(document).ready(function () {

    $("#send").click(function () {
        console.log("send")
        let idC;
        let Nombre;
        let Edad;
        let Info;
        idC = $("#idnumber").val();
        Nombre = $("#ncreator").val();
        Edad = $("#ecreator").val();
        Info = $("#icreator").val();

        valores = { "identifier": idC, "name": Nombre, "age": Edad, "info": Info };
        $.post("http://127.0.0.1:5000/increador", valores, function (data, status) {
            console.log(status)
            $("#result").text(data);

        });
    });




});