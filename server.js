var express = require("express");
const multer = require('multer');
const spawn = require("child_process").spawn;
const fs = require('fs');
var app = express();

app.get("/",function(request,response){
    response.sendFile(__dirname+"/public/index.html");
});

const upload = multer({
    storage: multer.diskStorage({
        destination: 'uploads',
        filename: function(req, file, cb) {
            cb(null, file.originalname)
        }
    })
})
app.post('/upload', upload.single('file'), (req, res, next) => {
    console.log(req.body.amount);
    const pythonProcess = spawn('python', ["./test.py", req.file.filename]);
    pythonProcess.stdout.on('data', (data) => {
        res.send(data.toString());
    });
});

app.use(express.static('public'));
app.listen(3000);
console.log("displaying at http://localhost:3000");