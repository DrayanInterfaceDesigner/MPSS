import { Entity } from "./Entity.js"
import { lerp } from "./utils.js"

export class CollisionBox extends Entity{
    constructor(size, position) {
        super(size, position)
        this.size = size || null
        this.bounding_box = this.get_bounding_box()
        this.color = '#ffffff'
        this.hide = true
        this.last_collision_offset = 0
    }
    
    get_bounding_box() {
        if(!this.size) return null
        const points = [
            [this.position.x + 0, this.position.y + 0],
            [this.position.x + this.size.w, this.position.y + 0],
            [this.position.x + this.size.w, this.position.y + this.size.h],
            [this.position.x + 0, this.position.y + this.size.h]
        ]

        return points
    }

    get_line_intersection(a, b, c, d) {
        this.bounding_box = this.get_bounding_box()
        const tTop = (d[0] - c[0]) * (a[1] - c[1]) - (d[1] - c[1]) * (a[0] - c[0])
        const uTop = (c[1] - a[1]) * (a[0] - b[0]) - (c[0] - a[0]) * (a[1] - b[1])
        const bottom = (d[1] - c[1]) * (b[0] - a[0]) - (d[0] - c[0]) * (b[1] - a[1])
    
        if (bottom != 0) {
            const t = tTop / bottom
            const u = uTop / bottom
    
            if (t >= 0 && t <= 1 && u >= 0 && u <= 1) {
                this.last_collision_offset = t
                return {
                    x: lerp(a[0], b[0], t),
                    y: lerp(a[1], b[1], t),
                    offset: t
                }
            }
        }
    
        return null
    }

    check_collision(poly_b) {
        const poly_a = this.get_bounding_box()
        for (let i = 0; i < poly_a.length; i++) {
            for (let k = 0; k < poly_b.length; k++) {
                const touch = this.get_line_intersection(
                    poly_a[i],
                    poly_a[(i + 1) % poly_a.length],
                    poly_b[k],
                    poly_b[(k + 1) % poly_b.length]
                )
                if (touch) {
                    this.color = '#ff0000'
                    return true
                }
            }
        }
        this.color = '#ffffff'
        return false
    }

    render(ctx) {
        this.bounding_box = this.get_bounding_box()
        
        //dirty solution but... it works.
        for(let p = 1; p < this.bounding_box.length + 1; p++) {
            const i = p > this.bounding_box.length -1 ? 0 : p
            ctx.beginPath()
            ctx.strokeStyle = this.color
            ctx.moveTo(this.bounding_box[p-1][0], this.bounding_box[p-1][1])
            ctx.lineTo(this.bounding_box[i][0], this.bounding_box[i][1])
            ctx.stroke()
        }
    }
}