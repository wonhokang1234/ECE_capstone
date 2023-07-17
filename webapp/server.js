import Peer from 'peerjs';
var http = require('http');
var fs = require('fs');

//loads welcome page
function welcome(request, response) {
    response.writeHead(200, {"Content-Type": 'text/html'});
    fs.readFile('./index.html', null, function(error, data) {
        if (error) {
            response.writeHead(404);
            response.write('File not found');
        } else {
            response.write(data);
        }
        response.end();
    });
}

//loads loading page
function loading(request, response) {
    response.writeHead(200, {"Content-Type": 'text/html'});
    fs.readFile('./load.html', null, function(error, data) {
        if (error) {
            response.writeHead(404);
            response.write('File not found');
        } else {
            response.write(data);
        }
        response.end();
    });
}

//loads result page
function result(request, response) {
    response.writeHead(200, {"Content-Type": 'text/html'});
    fs.readFile('./result.html', null, function(error, data) {
        if (error) {
            response.writeHead(404);
            response.write('File not found');
        } else {
            response.write(data);
        }
        response.end();
    });
}

//build a peerjs connection//

//declare a new peer(id = web)
var peer = new Peer(id='web');

//create a connection with the mobile app(id = mobile)
//var conn = peer.connect('mobile');

peer.on("open", function(id="web") {
    console.log('My peer id is' + id);
});

var window = new Window();
window.location.origin = 'localhost:8000';

peer.on("connection", function(conn=peer.connect('mobile')) {
    conn.on('data', function(data) {
        console.log("Data recieved");
        void request, response;
        switch (data) {
            case 'Load':
                loading(request, response);
                http.createServer(loading).listen(8000);
                window.location.reload();
                console.log("loading page");
                break;
            case 'Result':
                result(request, response);
                http.createServer(result).listen(8000);
                window.location.reload();
                console.log("result page");
                break;
            case 'Reset':
                welcome(request, response);
                http.createServer(welcome).listen(8000);
                window.location.reload();
                console.log("reset to welcome");
                break;
            default:
                welcome(request, response);
                http.createServer(welcome).listen(8000);
                window.location.reload();
                console.log("default welcome page");
                break;
        };
    });
});

