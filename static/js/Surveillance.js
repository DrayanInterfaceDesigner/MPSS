let emergency__button = document.querySelector(".emergency__button__container")
let emergency__button__img = emergency__button.querySelector(".emergency__button")

let emergency__lcd = document.querySelector(".emergency__text")
let emergency__lcd__text = emergency__lcd.querySelector("p")

let monitoring__led = document.querySelector(".monitoring__led")
let monitoring__led2 = document.querySelector(".monitoring__led2")

let monitoring__lever = document.querySelector(".monitoring__lever")
let monitoring__lever__image = monitoring__lever.querySelector("img")

let emergency__button__status = false
let last_emergency_hour = "n o n e"


const setLightsOff = () => {
    monitoring__led.classList.add("off")
    monitoring__led2.classList.add("off")
}
const setLightsOn = () => {
    monitoring__led.classList.remove("off")
    monitoring__led2.classList.remove("off")
}
const toggleLights = () => {
    monitoring__led.classList.toggle("off")
    monitoring__led2.classList.toggle("off")
}

const setLCDText = (string) => {
    emergency__lcd__text.innerText = string
}

emergency__button.addEventListener("click", async () => {
    if(!emergency__button__status) {
        try {
            const response = await fetch("/static/assets/images/button.png");
            if (response.ok) {
              emergency__button__img.setAttribute("src", "/static/assets/images/button.png")
              emergency__button__status = true
            } else {
              console.log("Error loading image:", response.status)
            }
          } catch (error) {
            console.log("Error:", error)
          }
    } else {
        emergency__button__img.setAttribute("src", "/static/assets/images/button_up.png")
        emergency__button__status = false
    }
})

emergency__button.addEventListener("mouseup", ()=> {
    
})

monitoring__lever.addEventListener("click", ()=> {
    monitoring__lever__image.classList.toggle("flip")
    last_emergency_hour = getTimeString()
    setLCDText("NO EMERGENCIES SINCE : " + last_emergency_hour)
    toggleLights()
})

const getTimeString = ()=> {
    const time = new Date()
    const _time = time.toLocaleTimeString().replace(/([\d]+:[\d]{2})(:[\d]{2})(.*)/, "$1$3")
    const str = _time + "\n" 
    return str
}

setLCDText("NO EMERGENCIES SINCE : " + last_emergency_hour)