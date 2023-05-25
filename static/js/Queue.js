export class Queue {
    constructor() {
        this.queue = new Array()
        this.head = null
        this.tail = null
        this.length = this.queue.length
    }

    add(item, priority='normal') {
        if(priority=='high') {
            const head = this.queue[0]
            if(head) this.queue[0] = item
            this.queue.push(head)
        }
        else this.queue.push(item)
    }

    update_recursivelly(parent, delta) {
        parent.children.forEach(child => {
            if(!child.entity.hide) child.entity.update(delta)
        })
    }
    render_recursivelly(parent, ctx) {
        parent.children.forEach(child => {
            if(!child.entity.hide) child.entity.render(ctx)
        })
    }
    execute(ctx) {
        this.length = this.queue.length
        for(let i = 0; i < this.length; i++){
            this.head = this.queue[i]
            this.tail = this.queue[this.length - 1]
            
            this.queue[i].update()
            this.update_recursivelly(this.queue[i], 'delta')
            if(!this.queue[i].hide) {
                this.queue[i].render(ctx)
                this.render_recursivelly(this.queue[i], ctx)
            }
        }
    }
}