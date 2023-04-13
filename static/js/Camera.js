class Camera {
    constructor(canvas, video, constraints) {
        this.canvas = canvas
        this.ctx = canvas.getContext('2d')
        this.video = video
        this.constraints = constraints
        
        console.log('im camera')
        this.init.bind(this)
        this.setup.bind(this)
        // this.setup()
    }

    run(){}
    call(){}
    setup(){
        if (this.video) {
            navigator.mediaDevices
            .getUserMedia({
                video:  { width: 1920, height: 1080 }
            })
            .then(this.init)
            .catch( (e) => {
                if (confirm("An error with camera occured:(" + e.name + ") Do you want to reload?")) {
                    location.reload();
                }
            });
        }
    }
    init(stream) {
        const videoelement = document.querySelector('#videoelement')
        console.log(videoelement)
        this.video.srcObject = stream
        this.video.play()
    }
    render(){
        this.ctx.drawImage(this.video, 0, 0, this.canvas.height, this.canvas.width)
    }
}

export default Camera 