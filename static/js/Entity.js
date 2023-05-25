export class Entity {
    constructor(size, position){
        this.size = size || null
        this.position = position || null
        this.children = new Array()
        this.is_copycat = false
        this.copycat_entity = null
        this.hide = false
        // this.setup()
    }

    copycat(entity) {
        this.size = entity.size
        this.position = entity.position
        this.is_copycat = true
        this.copycat_entity = entity
    }

    watch() {
        this.copycat(this.copycat_entity)
    }

    inherit(entity) {

    }
    add_child(child) {
        this.children.push({entity: child})
    }
    group_all() {
        this.children.forEach(child => {
            this.group(child.entity, child?.offset)
        })
    }
    group(child, offset = 0) {
        child.position.x = this.position.x + offset
        child.position.y = this.position.y + offset
    }
    setup() {
        if(!this.size) this.size = {w:0, h:0}
        if(!this.position) this.position = {x:0, y:0}
    }
    _process(delta){}
    _physics_process(delta){}

    update(delta) {
        this._physics_process(delta)
        this._process(delta)
        Object.keys(this).forEach(key => {
            this[key] = this[key]
        })
        this.is_copycat && this.watch()
    }
    render(ctx) {
        if(this.hide) return
        this.group_all()
    }
}