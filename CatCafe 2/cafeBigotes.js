// Regresa nombre del cafe
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/nombreCafe", function(data) {
        $("#nombre").html(data);
    }).fail(function() {
        $("#nombre").html("<span style='color: red;'>Error al cargar el nombre</span>");
    });
});

// Regresa la animación
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/animacion", function(data) {
        $("#animacion").html(data);
    }).fail(function() {
        $("#animacion").html("<span style='color: red;'>Error al cargar el nombre</span>");
    });
});

// Regresa la descripción
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/descripcion", function(data) {
        $("#descripcion").html(data);
    }).fail(function() {
        $("#descripcion").html("<span style='color: red;'>Error al cargar la descripción</span>");
    });
});

// Regresa el menú desde la base de datos 
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/menu", function(data) {
        $("#menu").html(data);
    }).fail(function() {
        $("#menu").html("<span style='color: red;'>Error al cargar el menú</span>");
    });
});

// Regresa el logo desde la base de datos  
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/logo", function(data) {
        $("#logo").html(data);
    }).fail(function() {
        $("#logo").html("<span style='color: red;'>Error al cargar el menú</span>");
    });
});

// Regresa el titulo de los gatos  
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/tituloGatos", function(data) {
        $("#tituloGatos").html(data);
    }).fail(function() {
        $("#tituloGatos").html("<span style='color: red;'>Error al cargar el menú</span>");
    });
});


// Regresa los 3 gatos desde la base de datos 
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/infoGatos", function(data) {
        $("#contenedorGatos").html(data);
    }).fail(function() {
        $("#contenedorGatos").html("<p style='color: red;'>Error al cargar la información del gato.</p>");
    });

    // Despliega la informacion de los gatos 
    $(document).on("click", "[id^=btnGato]", function() {
        let id = $(this).attr("id").replace("btnGato", "infoGato"); 
        $("#" + id).toggle();
    });
});

// Regresa los horarios  
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/horarios", function(data) {
        $("#horarios").html(data);
    }).fail(function() {
        $("#horarios").html("<span style='color: red;'>Error al cargar el menú</span>");
    });
});

// Regresa la ubicacion  
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/ubicacion", function(data) {
        $("#ubicacion").html(data);
    }).fail(function() {
        $("#ubicacion").html("<span style='color: red;'>Error al cargar el menú</span>");
    });
});

// Regresa el mapa 
$(document).ready(function() {
    $.get("http://127.0.0.1:5000/mapa", function(data) {
        $("#mapa").html(data);
    }).fail(function() {
        $("#mapa").html("<span style='color: red;'>Error al cargar el menú</span>");
    });
});

// Cambia las fotos de los gatos 
$(document).ready(function() {
  $(".cambiarFoto").click(() => { 
      $.get("http://127.0.0.1:5000/foto", (data) => {
          console.log("Imágenes recibidas:", data);
      
          $("#ana1").attr('src', data[0]);
          $("#maria1").attr('src', data[1]);
          $("#sofia1").attr('src', data[2]);
      }).fail(function() {
          console.log("Error al obtener las imágenes del servidor.");
      });
  });
});


$(document).ready(function(){
    $(".gato").click(function(){
      $(this).css("left", "450px");
    });
  });

$(document).ready(function () {
    $("#send").click(function () {
        console.log("send")
        let Usuario;
        let Contraseña;
        Usuario = $("#uusuario").val();
        Contraseña = $("#cusuario").val();

        valores = { "usuario": Usuario, "contraseña": Contraseña};
        $.post("http://127.0.0.1:5000/signup", valores, function (data, status) {
            console.log(status)
            $("#result").text(data);

        });
});


$(document).ready(function () {
  $("#loginBtn").click(function () {
      let usuario = $("#uusuario").val();
      let contraseña = $("#cusuario").val();
      let resultText = $("#result");

      $.ajax({
          url: "http://127.0.0.1:5000/verificar", 
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify({
              usuario: usuario,
              contraseña: contraseña
          }),
          success: function (data) {
              if (data.success) {
                  resultText.html("<span style='color: green;'>✔ " + data.message + "</span>");
              } else {
                  resultText.html("<span style='color: red;'>✘ " + data.message + "</span>");
              }
          },
          error: function () {
              resultText.html("<span style='color: red;'>✘ Error en el servidor</span>");
          }
      });
  });

  $("#signupBtn").click(function () {
      let usuario = $("#uusuario").val();
      let contraseña = $("#cusuario").val();
      let resultText = $("#result");

      $.ajax({
          url: "/signup",
          type: "POST",
          data: { usuario: usuario, contraseña: contraseña },
          success: function (data) {
              if (data.success) {
                  resultText.html("<span style='color: green;'>✔ " + data.message + "</span>");
              } else {
                  resultText.html("<span style='color: red;'>✘ " + data.message + "</span>");
              }
          },
          error: function () {
              resultText.html("<span style='color: red;'>✘ Error en el servidor</span>");
          }
      });
  });
});





});
