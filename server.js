var express = require("express");
var app = express();

app.get("/",function(request,response){
    response.sendFile(__dirname+"/public/index.html");
});

express.static(root,[options])
app.use(express.static('public'));
app.listen(3000);
console.log("displaying at http://localhost:3000");