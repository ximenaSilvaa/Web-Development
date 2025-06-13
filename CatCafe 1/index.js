function gato(nombre){
    document.getElementById("contenido").innerHTML = '';
    document.getElementById("contenido1").innerHTML = '';
    document.getElementById("contenido2").innerHTML = '';
    document.getElementById("contenido3").innerHTML = '';
    document.getElementById("contenido4").innerHTML = '';

    if (nombre == 'ana') {
        document.getElementById("contenido").innerHTML = '<figcaption>Es una gatita con disfraz de oso. Cuidado es salvaje.</figcaption>';
    } else if (nombre == 'maría') {
        document.getElementById("contenido1").innerHTML = '<figcaption>No se dejen engañar por los ojos de esta gatita, puede rasguñar.</figcaption>';
    } else if (nombre == 'sofía') {
        document.getElementById("contenido2").innerHTML = '<figcaption>Esta gatita es muy chismosa, le gusta investigar..</figcaption>';
    } else if (nombre == 'camila') {
        document.getElementById("contenido3").innerHTML = '<figcaption>Esta gatita es muy juguetona.</figcaption>';
    } else if (nombre == 'karen') {
        document.getElementById("contenido4").innerHTML = '<figcaption>Esta gatita roba comida, pongan mucha atención.</figcaption>';
    }
   
}

function menu() {
    const daysOfWeek = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];
    const today = new Date().getDay(); 
    const day = daysOfWeek[today]; 

    document.getElementById("menu").innerHTML = '';
    document.getElementById("menu1").innerHTML = '';
    document.getElementById("menu2").innerHTML = '';
    document.getElementById("menu3").innerHTML = '';
    document.getElementById("menu4").innerHTML = '';
    document.getElementById("menu5").innerHTML = '';

    if (day == 'lunes') {
        document.getElementById("menu").innerHTML = `
        <ul>
            <li>Café Americano............ $40 </li>
             <li>Café Latte............ $50 </li>
            <li>Sándwich de pollo con aguacate........... $85 </li>
            <li>Pastel de zanahoria.......................... $55 </li>
            <li>Focaccia de romero y aceitunas........... $50 </li>
        </ul>
    `;
    } else if (day == 'martes') {
        document.getElementById("menu1").innerHTML = `
        <ul>
            <li>Café Latte............ $50 </li>
            <li>Cappuccino............ $55 </li>
            <li>Baguette de jamón y queso................... $75 </li>
            <li>Macaron de fresa.......................... $30 </li>
            <li>Granola con yogur natural........... $60 </li>
        </ul>
    `;
    } else if (day == 'miércoles') {
        document.getElementById("menu2").innerHTML = `
        <ul>
            <li>Cappuccino............ $55 </li>
            <li>Pan de chocolate................... $45 </li>
            <li>Tostadas con aguacate y huevo pochado.......................... $80 </li>
            <li>Muffin de arándano............................. $40 </li>
            <li>Croissant de almendra........................... $50 </li>
        </ul>
    `;
    } else if (day == 'jueves') {
        document.getElementById("menu3").innerHTML = `
        <ul>
            <li>Frappuccino de vainilla............ $70 </li>
            <li>Ensalada César con pollo................... $95 </li>
            <li>Bagel de salmón ahumado.......................... $85 </li>
            <li>Brownie de chocolate............. $55 </li>
            <li>Chai Latte........................... $60 </li>
        </ul>
    `;
    } else if (day == 'viernes') {
        document.getElementById("menu4").innerHTML = `
        <ul>
            <li>Espresso Doble............ $40 </li>
            <li>Panini de pollo y pesto................... $90 </li>
            <li>Cheesecake de frutos rojos.......................... $70 </li>
            <li>Ensalada de quinoa con vegetales............. $80 </li>
            <li>Café Mocha........................... $65 </li>
        </ul>
    `;
    } else {
        document.getElementById("menu5").innerHTML = `
        <p>
            Hoy no hay menú es fin de semana y descansamos. ¡Los esperamos el lunes!
        </p>
    `;
    }
}



function darkMode() {
    document.body.style.backgroundColor = "#121212";
    document.body.style.color = "#FFFFFF";

    let arreglo = [".introduccion", ".menu", ".gatos", ".horarios", ".ubicacion", ".mapa", ".botones"];
    
    arreglo.forEach(clase => {
        let sections = document.querySelectorAll(clase);
        sections.forEach(section => {
            section.style.backgroundColor = "#333333";
            section.style.color = "#FFFFFF";
        });
    });

    let buttons = document.querySelectorAll('button');  
    buttons.forEach(button => {
        button.style.backgroundColor = "#555555";
        button.style.color = "#FFFFFF";
    });
}

