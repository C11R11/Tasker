let request = require('request');

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


        randomQuote += "<div id ='" + task["ID"] + "' class='" + classStatus + "'" +task["ID"] + ">";
        randomQuote += " " + task["estado"];
        randomQuote += " " + task["name"];
        randomQuote += "</div><br>";
    });

    document.getElementById("quote").innerHTML = randomQuote;
    });
}

makeRequest();

setInterval(function(){
    makeRequest();
}, 5000);