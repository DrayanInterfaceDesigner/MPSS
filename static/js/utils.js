const lerp = (a,b,t)=> {
    return (1 - t) * a + t * b
}

const group = (parent, child, offset = 0) => {
    child.position.x = parent.position.x + offset
    child.position.y = parent.position.y + offset
}

// const request_static_image = async (static_path)=> {
//     const address = `/static/${static_path}`
//     try {
//         const response = await fetch(address)
//         if (response.ok) {
//           emergency__button__img.setAttribute("src", address)
//         } else {
//           console.log("Error loading image:", response.status)
//         }
//       } catch (error) {
//         console.log("Error:", error)
//     }
// }

export {lerp, group}