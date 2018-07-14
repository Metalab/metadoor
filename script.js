var xmlhttp;
var statusDiv = document.getElementById("status");
statusDiv.style.display = "inline";

if (window.XMLHttpRequest) {
  xmlhttp = new XMLHttpRequest();
} else {
  // code for IE6, IE5
  xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}

xmlhttp.onreadystatechange = function() {
  if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
    if(xmlhttp.status == 200){
      var status = JSON.parse(xmlhttp.responseText).status;
      status = status === "open" ||
               status === "closed" ?
               status :
               "down";

      statusDiv.className = status;
      statusDiv.innerHTML = status;
    } else {
      console.log('Error: ' + xmlhttp.status)
    }
  }
}

xmlhttp.open("GET", "status.json", true);
xmlhttp.send();

setInterval(function(){
  xmlhttp.open("GET", "status.json", true);
  xmlhttp.send();
}, 30000);
