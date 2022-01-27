var http = require('http');
var fs = require('fs');

const PORT = 8080;
const HOST = '0.0.0.0';

var server = http.createServer(function (req, resp) {
    console.log("Request for demo file received.");
    fs.readFile("./front/index.html", function (error, data) {
        if (error) {
            resp.writeHead(404);
            resp.write('Contents you are looking for-not found');
            resp.end();
        } else {
            resp.writeHead(200, {
                'Content-Type': 'text/html',
            });
            resp.write(data.toString());
            resp.end();
        }
    });
}).listen(PORT, HOST);

console.log("Listening on port " + PORT);