const upload = document.getElementById("upload");

upload.addEventListener('change', (event) =>{
    const files = event.target.files;
    console.log(files);
});