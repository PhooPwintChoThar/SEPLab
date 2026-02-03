import js
from pyscript import document
from pyodide.ffi import create_proxy
from PyScriptWidget import AbstractWidget


class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)
        self.counter = 1

    def on_click(self, event):
        """Pause / Resume animation"""
        pass

    def on_setInterval(self):
        self.counter += 1

        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1

        self.image.src = "./images/frame-" + str(self.counter) + ".png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"

        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)

        self.element.appendChild(self.image)

        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")

        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click

        self.element.appendChild(self.button)


if __name__ == "__main__":
    output = AnimationWidget("container")
    output.drawWidget()