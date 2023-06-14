import { Entity } from "./Entity.js";

export class Sprite extends Entity {
    constructor(src, size, position) {
        super(size, position)
        this.image = new Image()
        this.src = src
        this.setup()
    }
    setup() {
        super.setup()
        this.image.src = this.src
    }
    update(delta) {
        super.update()
        this.image.height = this.size.h
        this.image.width = this.size.w
    }
    render(ctx) {
        ctx.drawImage(this.image, this.position.x, this.position.y, this.size.w, this.size.h)
    }
    
}