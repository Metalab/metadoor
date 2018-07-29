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

// Config Time Since
const refresh = true;
const refreshSeconds = 1;
const origin = new Date("2018-07-24");

// Program
main();
function main(){
  function display(origin){
    let display = document.querySelector("#timesince-display");
    output = timeSince(new Date(origin).getTime());
    display.innerHTML = output;
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

  let msg = `<b class="timer">${timeSince.d}</b> Days, `
           +`<b class="timer">${timeSince.h}</b> Hours, `
           +`<b class="timer">${timeSince.m}</b> Minutes, and `
           +`<b class="timer">${timeSince.s}</b> seconds.`;
  return msg;
}
