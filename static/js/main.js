import Camera from './Camera.js'

const canvas = document.querySelector(`#camera`)
const ctx = canvas.getContext(`2d`)
const video_el = document.querySelector('#videoelement')
const btn = document.querySelector(".switch__button")
const box = document.querySelector('.surveillance__camera')
const text = box.querySelector('.text')

const getTimeString = ()=> {
    const time = new Date()
    const time_str = time.toLocaleString('en-us', {hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: true})
    const _time = time.toLocaleTimeString().replace(/([\d]+:[\d]{2})(:[\d]{2})(.*)/, "$1$3")
    const cycle = time_str.slice(-2)
    const date = time.toLocaleString('en-us', {year: 'numeric', day: 'numeric', month: 'long'})
    const str = cycle + " " + _time + "\n"  + date
    return str
}




let emergency = false
btn.addEventListener('click', () => {
    box.classList.toggle('on')
    emergency = !emergency
})

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
    text.innerText = getTimeString()
    requestAnimationFrame(main)
}
main()
