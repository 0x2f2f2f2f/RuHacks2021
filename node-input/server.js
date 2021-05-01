var express = require("express");
var app = express();

app.get("/",function(request,response){
    response.sendFile(__dirname+"/views/index.html");
});

app.listen(3000);
console.log("displaying at http://localhost:3000");