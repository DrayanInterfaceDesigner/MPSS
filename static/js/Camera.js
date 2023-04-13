class Camera {
    constructor(canvas, video, constraints) {
        this.canvas = canvas
        this.ctx = canvas.getContext('2d')
        this.video = video
        this.constraints = constraints
        this.setup()
    }

    green_channel_only(x, y) {
        const img_data = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height, {
            willReadFrequently: true
        })
        const data = img_data.data
        for(let i = 0; i < data.length; i+=4) {
            data[i] = 0;
            data[i + 2] = 0;
        }
        this.ctx.putImageData(img_data, 0, 0)
    }
    setup(){
        if (this.video) {
            navigator.mediaDevices
            .getUserMedia(this.constraints)
            .then(this.init.bind(this))
            .catch( (e) => {
                if (confirm(`Error: ${e}, please try reloading the page.`)) {
                    location.reload();
                }
            });
        }
    }
    init(stream) {
        this.video.srcObject = stream
        this.video.play()
    }
    render(){

        const x = (this.canvas.width ) / 2;
        const y = (this.canvas.height ) / 2;
        
        this.ctx.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height)
        this.green_channel_only(x, y)
    }
}

export default Camera 