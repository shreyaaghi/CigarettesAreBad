from PIL import Image
import PySimpleGUI as gui
import io
import os
from util import get_config

config = get_config()
width, height = config['width'], config['height']

def about():
  font = ("Helvetica", 40)
  layout = [
    [gui.Button("Back", key="About Back Button"), gui.Text("About", font=font)],
    [gui.Image(key="img11"), gui.Multiline("My name is Shreya Aghi, and I am an 8th grader in San Francisco. Earlier this year, I joined a local organization known as BACR which specializes in multiple community issues. One that specifically stood out to me is tobacco control among teens. I learned that  over 90% of daily adult cigarette smokers began smoking before the age of 18. Tobacco products are often advertised specifically towards young audiences, and it has become more and more common to see middle and high schoolers using tobacco products. I wanted to help raise awareness towards this issue so we can help keep teenagers safe and eliminate the use of tobacco in minors. You can be apart of the solution, and it starts by opening the app.", write_only = True, disabled=True, size = (width//8, 17), font=('Helvetica',30))]
  ]
  return layout