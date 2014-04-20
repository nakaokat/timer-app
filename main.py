"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

from httphandler import get_htmltemplate

timerHtml = """<div id="sec" style="font-size:128px">0.00</div>
<div id="buttons">
<input type="button" value="Start" id="run">
<input type="button" value="Stop" id="stop">
<input type="button" value="Reset" id="reset"> 
</div>
"""
script = """
(function(){
window.onload = function(){

var startTime;
var stopTime;
var timerId;
var running = false;

document.getElementById('run').onclick = function(){
    run();
    return true;
}
document.getElementById('stop').onclick = function(){
    stop();
    return true;
}
document.getElementById('reset').onclick = function(){
    reset();
    return true;
}



var run = function(){
    if(running) return;
    running = true;
    
    if(stopTime){
        startTime = startTime + (new Date()).getTime() - stopTime;
    }
    
    if(!startTime){
        startTime = (new Date()).getTime();
    }
    
    timer();
}

// app print: startTime - current time

function timer(){
    document.getElementById('sec').innerHTML = (((new Date()).getTime() - startTime)/1000).toFixed(2);
    timerId = setTimeout(function(){
        timer();
    }, 100);
}

function stop(){
    if(!running) return false;
    running = false;
    clearTimeout(timerId);
    stopTime = (new Date()).getTime();
}

function reset(){
    if(running) return;
    startTime = undefined;
    document.getElementById('sec').innerHTML = "0:00";
}

}

})();

"""

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    body = get_htmltemplate()
    return body.format(title="Simple Stopwatch", script=script, body=timerHtml)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
