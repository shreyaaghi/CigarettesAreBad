from PIL import Image
import PySimpleGUI as gui
import io
import os
from util import get_config

# load_image("images/refusal.png", window, "img")

config = get_config()
width, height = config['width'], config['height']

def information():
    font = {"Helvetica", 30}
    layout = [
        [gui.Button("Back", key="Information Back Button"), gui.Text("Information", font=font)],
        [gui.Multiline("The National Cancer Institute reports that over 90% of adult smokers started before age 18, emphasizing the alarming issue of teenage smoking. Experimenting with cigarettes can lead to severe health consequences. To prevent addiction, it's crucial to educate young people early about the risks and factors contributing to teen tobacco use. This section explores these aspects, aiming to empower both teenagers and their caregivers to make informed choices.", key="introText", write_only = True, font=font, disabled=True, size = (width//20, 12)), gui.Image(key="img")],
        [gui.Text("What is a Cigarette?", font=font), gui.Image(key="carousel1")]
    ]
    return layout