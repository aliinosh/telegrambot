let tg = window.Telegram.WebApp

tg.expand()

function generate(){

let topic = document.getElementById("topic").value

let slides = document.getElementById("slides").value

let images = document.getElementById("images").checked


let data = {

topic: topic,
slides: slides,
images: images

}

tg.sendData(JSON.stringify(data))

}
