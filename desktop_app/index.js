let request = require('request');
const { shell } = require('electron')
window.$ = window.jQuery = require('jquery');

//shell.openExternal('http://google.cl');

$(document).ready(function () {
    $("#myInput").on("keyup", function () {
        var value = $(this).val();
        $(".cuadroTarea").each(function () {

            if ($(this).text().match(value)) {
                $(this).show();
            }
            else {
                $(this).hide();
            }

        });
    });
});

function OpenExternal(url)
{
    shell.openExternal(url);
}

function makeRequest()
{
    request("http://127.0.0.1:2222/api/jobs/tasks", function(err, response, body){
    body = JSON.parse(body);
    let randomQuote = "";

    body.forEach(function(task) {

        classStatus = "tareaPendiente";
        if (task["estado"] == "Terminado")
        {
            classStatus = "tareaTerminada";
        }

        randomQuote += "<div id ='" + task["ID"] + "' class='cuadroTarea'>";
        randomQuote += "<div class='topLeft'>" + task["name"] +  "&nbsp;&nbsp;<a href='http://127.0.0.1:1111/taskStatusDesktop/" + task["ID"] + "' target='_blank' class='button'>Ver detalle</a></div>";
        randomQuote += "<div class='topRight'><span class='" + classStatus + "'>"+ task["estado"] + "</span></div>";
        randomQuote += "<div class='bottomLeft'>ID "  + task["ID"] + "</div>";
        randomQuote += "<div class='bottomRight'>Creación: "  + task["creation"] + "</div>";
        //randomQuote += "<div class='center'><a href='http://127.0.0.1:1111/taskStatusDesktop/" + task["ID"] + "' target='_blank' class='button'>Ver detalle</a></div>";
        randomQuote += "</div>";
    });

    document.getElementById("quote").innerHTML = randomQuote;
    });
}

makeRequest();

setInterval(function(){
    makeRequest();
}, 5000);