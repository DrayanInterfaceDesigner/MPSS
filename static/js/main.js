import Camera from './Camera.js'

const canvas = document.querySelector(`#camera`)
const ctx = canvas.getContext(`2d`)
const video_el = document.querySelector('#videoelement')

const config = {
    width: 1920 /   4,
    height: 1080 /  4,
    video_width: 1920,
    video_height: 1080
}

const update = () => {
    canvas.width = config.width
    canvas.height = config.height
}
update()

const camera = new Camera(canvas, videoelement, {
    video: { width: config.video_width, height: config.video_height}
})

const main = () => {
    // update()
    camera.render()

    requestAnimationFrame(main)
}
main()
