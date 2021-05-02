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
    const pythonProcess = spawn('python', ["./VisionAPI_Module.py", `./uploads/${req.file.filename}`]);
    pythonProcess.stdout.on('data', (data) => {
        pythonProcess.kill();
        if (data.toString().slice(0,-2) == ""){
            res.send("No Face Detected");
        } else {
            const secondPython = spawn('python', ["./Sentence_Generator_Module.py", data.toString().slice(0,-2), parseInt(req.body.amount)]);
            secondPython.stdout.on('data', (finalData) => {
                res.send(finalData.toString());
            });
        }
    });
});

app.use(express.static('public'));
app.listen(3000);
console.log("displaying at http://localhost:3000");