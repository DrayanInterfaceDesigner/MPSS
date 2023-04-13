import Camera from './Camera.js'

const canvas = document.querySelector(`#camera`)
const videoelement = document.querySelector('#videoelement')

const ctx = canvas.getContext(`2d`)
canvas.width = window.innerWidth / 2
canvas.height = window.innerHeight / 2

const camera = new Camera(canvas, videoelement, {
    audio: true,
    video: { width: window.innerWidth / 2, height: window.innerHeight / 2 }
} )




if (videoelement) {
    navigator.mediaDevices
    .getUserMedia({
        audio: true,
        video: { width: window.innerWidth / 2, height: window.innerHeight / 2 }
    })
    .then()
    .catch(function (e) {
        if (confirm("An error with camera occured:(" + e.name + ") Do you want to reload?")) {
            location.reload();
        }
    });
}
//if stream found 
function init(stream) {
    videoelement.srcObject = stream 
    videoelement.play()
}


camera.setup()
function main () {
    camera.render()
    ctx.drawImage(videoelement, 0, 0, canvas.width, canvas.height);

    requestAnimationFrame(main)
}

main()





// var videoelement = document.getElementById("videoelement");
// var streamContraints = {
//     audio: true,
//     video: { width: 1920, height: 1080 },
// };
// var canvaselement = document.querySelector('#camera');
// var ctx = canvaselement.getContext('2d', { alpha: false });
// var canvasInterval = null;
// var fps=60



// function drawImage(video) {
//     ctx.drawImage(video, 0, 0, canvaselement.width, canvaselement.height);
// }
// canvasInterval = window.setInterval(() => {
//     drawImage(videoelement);
//     console.log(`hi`)
// }, 1000 / fps);