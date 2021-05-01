var express = require("express");
var app = express();

app.get("/",function(request,response){
    express.static(root,[options])
    app.use(express.static('public'));
    response.sendFile(__dirname+"/index.html");
});

app.listen(3000);
console.log("displaying at http://localhost:3000");