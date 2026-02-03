from datetime import datetime
import js
from pyscript import document
from PyScriptWidget import AbstractWidget


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


if __name__ == "__main__":
    output = NotificationWidget("container")
    output.drawWidget()