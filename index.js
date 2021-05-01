const http = require('http');

const server = http.createServer(function(req,res){
    res.statusCode = 200;
    res.end();
});

server.listen(3000,function(){
    consolve.log("Listening on port http://localhost:3000");
});