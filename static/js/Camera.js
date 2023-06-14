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

    fisheye_derived_strange_displacement(x, y) {
        const img_data = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height)
        const data = img_data.data
      
        const centerX = x
        const centerY = y
        const strength = 0.01
      
        for (let row = 0; row < this.canvas.height; row++) {
          for (let col = 0; col < this.canvas.width; col++) {
            const dx = col - centerX
            const dy = row - centerY
            const distance = Math.sqrt(dx * dx + dy * dy)
            const factor = 1 - (distance * strength)
              const srcX = Math.floor(centerX + dx * factor)
              const srcY = Math.floor(centerY + dy * factor)
      
              const srcIndex = (srcY * this.canvas.width + srcX) * 5
              const destIndex = (row * this.canvas.width + col) * 5
              data[destIndex] = data[srcIndex]
              data[destIndex + 1] = data[srcIndex + 1]
              data[destIndex + 2] = data[srcIndex + 2]
              data[destIndex + 3] = data[srcIndex + 3]
          }
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
        // this.fisheye_derived_strange_displacement(x,y)
    }
}

export default Camera 