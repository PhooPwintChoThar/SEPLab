
import js
from pyscript import document
from abc import ABC, abstractmethod
from datetime import datetime

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id=element_id
        self.__element=None

    
    @property
    def element(self):
        if not self.__element:
            self.__element=document.querySelector(f'#{self.element_id}')
        return self.__element
    
    @abstractmethod
    def drawWidget(self):
        pass

    
def getTime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")


class NotificationWidget(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)

    def on_click(self, event):
        text = self.input_text.value
        js.alert("Hello " + text + " at " + getTime())

    def drawWidget(self):
        self.input_text = document.createElement("input")
        self.input_text.type = "text"
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "Click Me!"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

class CurrencyWidget(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)

    def baht2Dollar(self, event):
        text = self.input_text.value
        js.alert(f"{int(text):.2f} bahts = {int(text)/30:.2f} dollars")

    def dollar2Baht(self, event):
        text = self.input_text.value
        js.alert(f"{int(text):.2f} dollars = {int(text)*30:.2f} bahts")

    def drawWidget(self):
        self.input_text = document.createElement("input")
        self.input_text.type = "text"
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)

        self.button1 = document.createElement("button")
        self.button1.innerText = "B2D"
        self.button1.style.width = "600px"
        self.button1.onclick = self.baht2Dollar
        self.element.appendChild(self.button1)

        self.button2 = document.createElement("button")
        self.button2.innerText = "D2B"
        self.button2.style.width = "600px"
        self.button2.onclick = self.dollar2Baht
        self.element.appendChild(self.button2)

from pyodide.ffi import create_proxy


class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)
        self.counter = 1
        self.isPlaying = True
        self.interval_id = None

    def on_click(self, event):
        if self.isPlaying:
            js.clearInterval(self.interval_id)
            self.button.innerText = "play"
            self.isPlaying = False
        else:
            self.interval_id = js.setInterval(
                create_proxy(self.on_setInterval), 100
            )
            self.button.innerText = "pause"
            self.isPlaying = True

    def on_setInterval(self):
        self.counter += 1

        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1

        self.image.src = "./images/frame-" + str(self.counter) + ".png"

    def drawWidget(self):
        # Image
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        self.element.appendChild(self.image)

        # Sound
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")

        # Start animation
        self.interval_id = js.setInterval(
            create_proxy(self.on_setInterval), 100
        )

        # Button
        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)
import random

class ColorAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        super().__init__(element_id)

    def change_bg_color(self, event):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        self.element.style.backgroundColor = f"rgb({r},{g},{b})"

    def drawWidget(self):
        # Call parent widget UI
        super().drawWidget()

        # Background color button
        self.color_button = document.createElement("button")
        self.color_button.innerText = "Change Background Color"
        self.color_button.style.width = "600px"
        self.color_button.onclick = self.change_bg_color

        self.element.appendChild(self.color_button)


if __name__ == "__main__":
    output = ColorAnimationWidget("container")
    output.drawWidget()
