import js
from pyscript import document
from pyodide.ffi import create_proxy
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