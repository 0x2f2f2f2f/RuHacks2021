const upload = document.getElementById("upload");
const image = document.getElementById("image");

$('.first').addClass('animated fadeInUp');

setTimeout(function () {
    $('.second').show().addClass('animated fadeInUp');}, 2000
);
setTimeout(function () {
    $('.third').show().addClass('animated fadeInUp');}, 4000
);
upload.addEventListener('change', (event) =>{
    const files = event.target.files;
    image.src = URL.createObjectURL(files[0]);
});
