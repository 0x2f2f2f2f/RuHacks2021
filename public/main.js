const upload = document.getElementById("upload");
const image = document.getElementById("image");

upload.addEventListener('change', (event) =>{
    const files = event.target.files;
    image.src = URL.createObjectURL(files[0]);

});
