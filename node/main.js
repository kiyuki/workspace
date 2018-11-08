
var fs=require("fs");

fs.readFile('input.txt', function(err, data){
  if(err) return console.error(err);
  console.log(data.toString());
});
console.log("Program Ended");
/*
var fs = require("fs");

var data = fs.readFileSync('input.txt');

console.log(data.toString());
console.log("Program Ended");

/*console.log("hello, world!")
var http = require("http");
http.createServer(test).listen(8081);
function test(request, response) {
   // Send the HTTP header
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});

   // Send the response body as "Hello World"
   response.end('Hello World\n');
   response.end('kokoko KIta\n');
}
// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');
*/
