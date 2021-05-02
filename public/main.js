const upload = document.getElementById("upload");
const image = document.getElementById("image");

upload.addEventListener('change', (event) =>{
    const files = event.target.files;
    image.src = URL.createObjectURL(files[0]);
});

document.getElementById('imageForm').onsubmit = function(event){
    event.preventDefault() // prevent form from posting without JS
    var xhttp = new XMLHttpRequest(); // create new AJAX request

    xhttp.onreadystatechange = function() {
        console.log(xhttp.status);
        console.log(this.response);
    }

    xhttp.open("POST", "/upload")
    var fileData = new FormData();
    fileData.append("file", upload.files[0]);

    xhttp.send(fileData)
}