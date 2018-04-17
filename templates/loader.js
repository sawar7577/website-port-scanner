function makeRequest() 
{
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/ajax/nmout/{{ nmap_key }}", true);
    xhttp.send();
    xhttp.onreadystatechange = function() {
        console.log(xhttp.responseText)
        data = JSON.parse(xhttp.responseText)
        if(data.valid === false) 
        {
            clearTimeout(timer_id)
            return;
        }
        
        if(data.progress == 100) 
        {
            clearTimeout(timer_id)
            document.getElementById("result").innerHTML += 'Summary: ' + data.summary + "%\n";
            window.location.href="/res/{{ nmap_key}} ";
        }
        document.getElementById("result").innerHTML = 'Progress: ' + data.progress + "%\n";
        var elem = document.getElementById("myBar");
        elem.style.width = data.progress+"%";
        document.getElementById("myBar").innerHTML = data.progress+"%";
        
    };		
};
var timer_id = setInterval(makeRequest, 1000);