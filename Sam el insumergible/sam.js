// Regresa nombre del cafe
$(document).ready(function() {
    $.get("http://127.0.0.1:8080/nombre", function(data) {
        $("#nombre").html(data);
    }).fail(function() {
        $("#nombre").html("<span style='color: red;'>Error al cargar el nombre</span>");
    });
});

// Regresa la animación
$(document).ready(function() {
    $.get("http://127.0.0.1:8080/inicio", function(data) {
        $("#foto").html(data);
    }).fail(function() {
        $("#foto").html("<span style='color: red;'>Error al cargar el nombre</span>");
    });
});

// Regresa la descripción
$(document).ready(function() {
    $.get("http://127.0.0.1:8080/descripcion", function(data) {
        $("#descripcion").html(data);
    }).fail(function() {
        $("#descripcion").html("<span style='color: red;'>Error al cargar la descripción</span>");
    });
});
