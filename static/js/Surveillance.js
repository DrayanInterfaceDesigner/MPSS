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
let last_message = null
let messages = new Array()
let lever_stts = false


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
    try {
        const response = await fetch("/surveillance/emergency");
        if (response.ok) {
          console.log(response)
        } else {
          console.log("Error loading image:", response.status)
        }
      } catch (error) {
        console.log("Error:", error)
    }
})

emergency__button.addEventListener("mouseup", ()=> {
    
})

monitoring__lever.addEventListener("click", ()=> {
    monitoring__lever__image.classList.toggle("flip")
    setLCDText(last_message + " : " + last_emergency_hour)
    setLightsOff()
    lever_stts = !lever_stts
})

const getTimeString = ()=> {
    const time = new Date()
    const _time = time.toLocaleTimeString().replace(/([\d]+:[\d]{2})(:[\d]{2})(.*)/, "$1$3")
    const str = _time + "\n" 
    return str
}

// setInterval(()=>{
//     const eventSource = new EventSource('/stream');

//         eventSource.onmessage = function (event) {
//             const message = event.data;
//             console.log('Received message:', message);
//             // Process the received message as needed
//         };
// }, 5500)

const eventSource = new EventSource('/surveillance/stream')


eventSource.onmessage = async function (event) {
    const message = await event.data;
    console.log('Received message:', message)
    messages.push(message)
    last_message = message
    last_emergency_hour = getTimeString()
    if(!lever_stts) {
        setLightsOn()
        setLCDText(`Intruder Detected! [ ${messages.length} ]`)
    }
    else {
        setLCDText(last_message + "\n" + last_emergency_hour)
    }
    // Process the received message as needed
}

setLCDText("NO EMERGENCIES SINCE : " + last_emergency_hour)