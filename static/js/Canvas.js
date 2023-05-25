import {CollisionBox} from './CollisionBox.js'

class Canvas {
    constructor(canvas, config) {
        this.canvas = canvas || null
        this.ctx = null
        this.size = config?.size || null 
        this.RAF = null
        this._pause = false
        this.is_fullscreen = false

        this.#setup()

        this.bounding_box = new CollisionBox(this.size, {x:0, y:0})
    }

    pause() {
        this._pause = true
    }

    resume() {
        this._pause = false
    }

    set_size() {
        if(this.is_fullscreen) {
            this.canvas.width = window.innerWidth
            this.canvas.height = window.innerHeight
        }
        else {
            this.canvas.width = this.size.w
            this.canvas.height = this.size.h
        }
    }

    #setup() {
        if(this.canvas == null) {
            this.canvas = document.createElement('canvas')
            this.canvas.style.position = 'relative'
            this.canvas.style.zIndex = '9999'
            document.body.appendChild(this.canvas)
        }
        if(!this.size) {
            this.size = {
                w: window.innerWidth,
                h: window.innerHeight
            }
            this.is_fullscreen = true
        }
        this.ctx = this.canvas.getContext('2d')
        this.set_size()
    }

    _process(delta){}
    _physics_process(delta){}

    update(delta) {
        if(!this._pause) {
            this._process(delta)
            this._physics_process(delta)
            this.RAF = requestAnimationFrame(this.update.bind(this))
        }
    }
    stop() {
        cancelAnimationFrame(this.RAF)
    }
}

export default Canvas