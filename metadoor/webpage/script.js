var xmlhttp;
var xmlhttpdoor;
var onsiteStatusDiv = document.getElementById("onsite-status");
onsiteStatusDiv.style.display = "inline";
var doorStatusDiv = document.getElementById("door-status");
doorStatusDiv.style.display = "inline";
let iconLink = null;


if (window.XMLHttpRequest) {
  xmlhttpdoor = new XMLHttpRequest();
} else {status
  // code for IE6, IE5
  xmlhttpdoor = new ActiveXObject("Microsoft.XMLHTTP");
}

if (window.XMLHttpRequest) {
  xmlhttp = new XMLHttpRequest();
} else {status
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

      onsiteStatusDiv.className = status;
      onsiteStatusDiv.innerHTML = status;
      document.title = "Metalab Door is " + status;

      if (status !== "down") {
        // Add icon to <head> if it doesn't already exist
        if (!iconLink) {
          iconLink = document.createElement("link");
          iconLink.setAttribute("rel", "icon");
          document.head.append(iconLink);
        }

        iconLink.setAttribute("href", "icons/" + status + ".png");
      }
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

xmlhttpdoor.onreadystatechange = function() {
  if (xmlhttpdoor.readyState == XMLHttpRequest.DONE ) {
    if(xmlhttpdoor.status == 200){
      var status = JSON.parse(xmlhttpdoor.responseText).status;
      status = status === "open" ||
               status === "closed" ?
               status :
               "down";

      doorStatusDiv.className = status;
      doorStatusDiv.innerHTML = status;

    } else {
      console.log('Error: ' + xmlhttpdoor.status)
    }
  }
}

xmlhttpdoor.open("GET", "doorstatus.json", true);
xmlhttpdoor.send();

setInterval(function(){
  xmlhttpdoor.open("GET", "doorstatus.json", true);
  xmlhttpdoor.send();
}, 30000);


// Config Time Since
const refresh = true;
const refreshSeconds = 1;
const origin = new Date("2024-11-19");

// Program
main();
function main(){
  function display(origin){
    let display = document.querySelector("#timesince-display");
    display.innerHTML = "This Door Status is working without <b>apocalyptic incidents</b> for: "
      + timeSince(new Date(origin).getTime())
      + "\n\n  The Metalab door didn't crash the network for: "
      + timeSince(new Date(origin).getTime())
      + "\n\n  The information on this page refreshes automatically.";
  }

  if(refresh){
      setInterval(function() {
          display(origin);
      }, refreshSeconds*1000);
  }
  else
    display(origin);
}

function timeSince(origin){
  function conversion(ms) {
      var d, h, m, s;
      s = Math.floor(ms / 1000);
      m = Math.floor(s / 60);
      s = s % 60;
      h = Math.floor(m / 60);
      m = m % 60;
      d = Math.floor(h / 24);
      h = h % 24;
      return { d: d, h: h, m: m, s: s };
  };

  let now = Date.now();
  let timeSince = conversion(now - origin);

  let msg = `${timeSince.d} Days, ${timeSince.h} Hours, ${timeSince.m} Minutes, and ${timeSince.s} seconds.`;
  return msg;
}
