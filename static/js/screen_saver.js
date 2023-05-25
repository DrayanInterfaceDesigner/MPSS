import Canvas from './Canvas.js'
import { Queue } from './Queue.js'
import { Sprite } from './Sprite.js'
import { StaticBody } from './StaticBody.js'

const queue = new Queue()
const canvas = new Canvas()
const logo = new Sprite("{{url_for('static', filename='/assets/images/logo.png')}}", {w: 150, h: 150}, {x:0, y:0})
const WalkingLogo = new StaticBody({w: 100, h:100}, {x:10,y:10})
let bool = true

queue.add(canvas.bounding_box)
queue.add(logo)
queue.add(WalkingLogo)

WalkingLogo.add_child(logo)
logo.copycat(WalkingLogo)
WalkingLogo.collision_shape.hide = true

export const screen_saver = (amount) => {
    // console.log('HIIII')
    let time_start = Date.now()
    let time_elapsed = 0
    setInterval(()=> {
        time_elapsed = (Date.now() - time_start) / 1000
        console.log(time_elapsed)
    }, 1000)
    
    for (var key in window) {
        if (key.search('on') == 0) {
            window.addEventListener(key.slice(2), ()=> {
            time_start = Date.now()
           })
        }
    }
    
    canvas.canvas.style.backgroundColor = `#000000`
    canvas.canvas.style.position = 'absolute'
    canvas.canvas.style.top = '0'
    canvas.canvas.style.left = '0'
    document.body.style.overflow = 'hidden'
    
    let dir1 = 1
    let dir2 = 1
    let deg = 45
    let speed = 1
    let way1 = deg
    let way2 = -deg
    canvas._physics_process = (delta) => {
        canvas.set_size()
        console.log(WalkingLogo.collision_shape.hide)
        WalkingLogo._physics_process = (delta) => {
        
            const boundary = 6
            const collided = WalkingLogo.collision_shape.check_collision(canvas.bounding_box.get_bounding_box())
            canvas.bounding_box.size.w = window.innerWidth
            canvas.bounding_box.size.h = window.innerHeight
            //Lazy code
            if(WalkingLogo.position.x + (WalkingLogo.size.w) > canvas.size.w) {
                WalkingLogo.position.x -= boundary
            }
            if(WalkingLogo.position.x < 0) {
                WalkingLogo.position.x += boundary
            }
            if(WalkingLogo.position.y + (WalkingLogo.size.h) > canvas.size.h) {
                WalkingLogo.position.y -= boundary
            }
            if(WalkingLogo.position.y < 0) {
                WalkingLogo.position.y += boundary
            }
        
            if(collided) {
                let d1, d2
                d1 = dir1
                d2 = dir2
                dir1 *= Math.random() > .5 ? 1 : -1
                dir2 *= Math.random() > .5 ? 1 : -1
                if(dir1 == d1 && dir2 == d2) {
                    dir1 *= -dir1
                    dir2 *= -dir2
                }
            }
            dir1 > 0 ? WalkingLogo.position.x += Math.cos(way1) : WalkingLogo.position.x -= Math.cos(way1) * speed
            dir2 > 0 ? WalkingLogo.position.y += Math.sin(way2) : WalkingLogo.position.y -= Math.sin(way2) * speed
        }
    
        queue.execute(canvas.ctx)
    
    }
    canvas.pause()
    
    setInterval(()=> {
        if(time_elapsed > amount) {
            canvas.canvas.style.display = 'block'
            canvas.resume()
            bool ? canvas.update() : null
            bool = false
        }
        else {
            canvas.canvas.style.display = 'none'
            canvas.pause()
            bool = true
        }
    })
}