"use strict";

function setup()
{
    var but=document.getElementById("button-autocomplete");
    if(but.accessKeyLabel) { but.value += ' ('+but.accessKeyLabel+')'; }

    document.text_refresher = setTimeout(poll_text, 450);
    document.smoothscrolling_busy = false;
    window.onbeforeunload = function(e) { return "Are you sure you want to abort the session and close the window?"; }
}

function poll_text()
{
    var txtdiv = document.getElementById("textframe");
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function() {
        var DONE = this.DONE || 4;
        clearTimeout(document.text_refresher);
        if (this.readyState === DONE) {
            if(this.responseType=="json")
                var json = this.response;
            else
                var json = JSON.parse(this.responseText);
            if(this.status>=300 || json["error"]) {
                txtdiv.innerHTML += "<p class='server-error'>Server error: "+JSON.stringify(json)+"<br>Perhaps refreshing the page might help. If it doesn't, quit or close your browser and try with a new window.</p>";
                txtdiv.scrollTop = txtdiv.scrollHeight;
                return;
            }
            document.text_refresher = setTimeout(poll_text, 450);   // queue next poll
            var special = json["special"];
            if(special) {
                if(special.indexOf("clear")>=0) {
                    txtdiv.innerHTML = "";
                    txtdiv.scrollTop = 0;
                }
            }
            if(json["text"]) {
                document.getElementById("player-location").innerHTML = json["location"];
                // document.getElementById("player-turns").innerHTML = json["turns"];
                txtdiv.innerHTML += json["text"];
                if(!document.smoothscrolling_busy) smoothscroll(txtdiv, 0);
            }
        }
    }
    ajax.onerror = function(error) {
        txtdiv.innerHTML="<p class='server-error'>Connection error.<br><br>Close the browser or refresh the page.</p>";
        clearTimeout(document.text_refresher);
        var cmd_input = document.getElementById("input-cmd");
        cmd_input.disabled=true;
    }
    ajax.open("GET", "text", true);
    ajax.responseType="json";
    ajax.send(null);
}

function smoothscroll(div, previousTop)
{
    document.smoothscrolling_busy = true;
    if(div.scrollTop < div.scrollHeight) {
        div.scrollTop += 6;
        if(div.scrollTop > previousTop) {
            window.requestAnimationFrame(function(){smoothscroll(div, div.scrollTop);});
            // setTimeout(function(){smoothscroll(div, div.scrollTop);}, 10);
            return;
        }
    }
    document.smoothscrolling_busy = false;
}


function submit_cmd()
{
    var cmd_input = document.getElementById("input-cmd");
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function() {
        var DONE = this.DONE || 4;
        if(this.readyState==DONE) {
            clearTimeout(document.text_refresher);
            document.text_refresher = setTimeout(poll_text, 80);
        }
    }
    ajax.open("POST", "input", true);
    ajax.setRequestHeader("Content-type","application/x-www-form-urlencoded; charset=UTF-8");
    var encoded_cmd = encodeURIComponent(cmd_input.value);
    ajax.send("cmd=" + encoded_cmd);
    cmd_input.value="";
    cmd_input.focus();
    return false;
}

function autocomplete_cmd()
{
    var cmd_input = document.getElementById("input-cmd");
    if(cmd_input.value) {
        var ajax = new XMLHttpRequest();
        ajax.onreadystatechange = function() {
            var DONE = this.DONE || 4;
            if(this.readyState==DONE) {
                clearTimeout(document.text_refresher);
                document.text_refresher = setTimeout(poll_text, 80);
            }
        }
        ajax.open("POST", "input", true);
        ajax.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        ajax.send("cmd=" + encodeURIComponent(cmd_input.value)+"&autocomplete=1");
    }
    cmd_input.focus();
    return false;
}

function quit_clicked()
{
    if(confirm("Quitting like this will abort your game.\nYou will lose your progress. Are you sure?")) {
        window.onbeforeunload = null;
        document.location="quit";
        return true;
    }
    return false;
}
