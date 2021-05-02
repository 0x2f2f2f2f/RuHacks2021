const upload = document.getElementById("upload");
const image = document.getElementById("image");
const sentenceDiv = document.getElementById("sentences");

$('.first').addClass('animated fadeInUp');

setTimeout(function () {
    $('.second').show().addClass('animated fadeInUp');}, 1000
);
setTimeout(function () {
    $('.third').show().addClass('animated fadeInUp');}, 2000
);
upload.addEventListener('change', (event) =>{
    const files = event.target.files;
    image.src = URL.createObjectURL(files[0]);
});

document.getElementById('imageForm').onsubmit = function(event){
    event.preventDefault() // prevent form from posting without JS
    var xhttp = new XMLHttpRequest(); // create new AJAX request

    xhttp.onreadystatechange = function() {
        while(sentenceDiv.firstChild){
            sentenceDiv.removeChild(sentenceDiv.firstChild);
        }

        var sentence = document.createElement("h1");
        var text = document.createTextNode(this.response);
        sentence.appendChild(text);
        sentenceDiv.appendChild(sentence);
        console.log(xhttp.status);
        console.log(this.response);
    }

    xhttp.open("POST", "/upload")
    var fileData = new FormData();
    fileData.append("file", upload.files[0]);

    xhttp.send(fileData)
}