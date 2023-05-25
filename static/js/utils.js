const lerp = (a,b,t)=> {
    return (1 - t) * a + t * b
}

const group = (parent, child, offset = 0) => {
    child.position.x = parent.position.x + offset
    child.position.y = parent.position.y + offset
}

export {lerp, group}