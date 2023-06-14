import { CollisionBox } from "./CollisionBox.js";
import { Entity } from "./Entity.js";
import { Queue } from "./Queue.js";
import { group } from "./utils.js";

export class StaticBody extends Entity {
    constructor(size, position) {
        super(size,position)
        this.sprite = null
        this.animated_sprite = null
        this.collision_shape = new CollisionBox(this.size, this.position)
        this.setup()
    }
    _physics_process(delta) {
        
    }
    setup() {
        super.setup()
        this.add_child(this.collision_shape)
    }

    update(delta) {
        super.update(delta)
        super.group_all()
    }
}