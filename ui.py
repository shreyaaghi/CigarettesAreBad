# chore, doc, feat, fix
import PySimpleGUI as gui
import webbrowser
from layouts.welcome import welcome
from layouts.resources import resources_ui
from layouts.quizzes import quizzes_ui
from layouts.quiz1 import quiz1, handleQuiz1
from layouts.quiz1answers import quiz1Answers, checkQuiz1
from layouts.about import about
from layouts.information import information

from util import get_config, load_image, convert_image

config = get_config()

font = ("Helvetica", 25)
size = (config['width'], config['height'])



def cycleLayout(window, activeLayout):
  screens = ["welcome screen", "resources screen", "quizzes screen", "quiz1 screen", "answer screen 1", "about screen", "information screen"]
  window[activeLayout].update(visible = True)
  for screen in screens:
    if screen == activeLayout:
      continue
    window[screen].update(visible = False)
  

def ui():
  gui.theme("LightBrown10")
  
  layout = [
    [
      gui.Column(welcome(), key = "welcome screen", element_justification="c"), 
      gui.Column(resources_ui(), scrollable=True, visible = False,  key = "resources screen", size=size),
      gui.Column(quizzes_ui(), scrollable=False, visible = False, key = "quizzes screen", element_justification="c"),
      gui.Column(quiz1(), scrollable=True, visible = False, key = "quiz1 screen", element_justification="left", size=size), # TODO Add scrollable back?
      gui.Column(quiz1Answers(), scrollable=True, visible = False, key = "answer screen 1", element_justification="c", size=size),
      gui.Column(about(), key="about screen", visible=False, element_justification='c'),
      gui.Column(information(), key="information screen", scrollable=True, visible=False, element_justification="left", size=size)
    ]
  ]
  window = gui.Window("TeenTobaccoTermination", layout, resizable=True, element_justification='c', size = size)
  cigarette_image = 'cigarette_contents'

  while True:
    image_list = ["images/anatomyOfACigarette.png", "images/whatIsvapeb.png"]
    next_index = 0

    evt, vals = window.read()

    

    if evt == gui.WIN_CLOSED:
      break
    if evt == "Information Button":
      cycleLayout(window, "information screen")
      print("Info Button Pressed")
    if evt == "Quizzes Button":
      cycleLayout(window, "quizzes screen")
      print("Quizzes Button Pressed")
    if evt == "Resources Button":
      cycleLayout(window, "resources screen")
      print("Resources Button Pressed")
    if evt == "About Button":
      cycleLayout(window, "about screen")
      print("About Button Pressed")
    if evt == "Sources Button":
      print("Sources Button Pressed")
    if "Back Button" in evt: 
      cycleLayout(window, "welcome screen")
      print("Back Button Pressed")
    if evt == "Quiz 1 Button":
      cycleLayout(window, "quiz1 screen")
      print("Quiz 1 Button Pressed")
    if evt == "Submit Button 1":
      cycleLayout(window, "answer screen 1")
      checkQuiz1(window, evt, vals)
      print("Submit 1 Button Pressed")
    if "Link" in evt:
      print(evt)
      webbrowser.open(evt.split(": ")[-1])
    handleQuiz1(evt, vals)
    load_image("images/justSayNoFemale.png", window, "img", (300,300))
    load_image("images/teenVapingRise.png", window, "img3", (500,500))
    load_image("images/ads.png", window, "img4", (300,400))
    load_image("images/jackie.png", window, "img5", (300,400))
    load_image("images/healthy.png", window, "img6", (300,400))
    load_image("images/organs!.png", window, "img7", (500,500))
    load_image("images/secondhand.png", window, "img8", (500,500))
    load_image("images/brainDamage.png", window, "img9", (500,500))
    load_image("images/college.png", window, "img10", (500,600))
    load_image("images/bioImage.png", window, "img11", (700,700))
    # load_image("images/what is in a cigarette.png", window, "img2", (400,400))
    
    img2 = window["img2"]
    # if cigarette_image == 'cigarette_contents':
    img2.draw_image(data=convert_image(f"images/{cigarette_image}.png", (500,300)),location=(0,300))

    if evt == "img2":
      x, y = vals["img2"]
      print(x,y)
      # dye
      if 480 <= x <= 492:
        if 73 <= y <= 107:
          cigarette_image="dye"
      # candle
      if 56 <= x <= 91:
        if 248 <= y <= 261:
          cigarette_image="candle"
      # tolune
      if 302 <= x <= 344:
        if 218 <= y <= 246:
          cigarette_image="tolune"
      # acetic acid
      if 1 <= x <= 27:
        if 105 <= y <= 139:
          cigarette_image="acetic acid"
      # bbq lighter
      if 183 <= x <= 215:
        if 122 <= y <= 147:
          cigarette_image="bbq lighter"
      # batteries
      if 48 <= x <= 66:
        if 191 <= y <= 198:
          cigarette_image="batteries"
      # carbonm
      if 229 <= x <= 256:
        if 42 <= y <= 59:
          cigarette_image="carbonm"
      # lighter fluid
      if 3 <= x <= 22:
        if 159 <= y <= 176:
          cigarette_image="lighter fluid"
      # nicotine
      if 336 <= x <= 359:
        if 155 <= y <= 175:
          cigarette_image="nicotine"
      # poison
      if 139 <= x <= 173:
        if 33 <= y <= 57:
          cigarette_image="poison"
      # rocket
      if 311 <= x <= 348:
        if 21 <= y <= 37:
          cigarette_image="rocket"
      # sewer
      if 55 <= x <= 78:
        if 52 <= y <= 78:
          cigarette_image="sewer"
      # toilet
      if 364 <= x <= 388:
        if 119 <= y <= 138:
          cigarette_image="toilet"
      # back button
      if 4 <= x <= 8:
        if 282 <= y <= 285:
          cigarette_image = "cigarette_contents"
          # img2.draw_image(data=convert_image("images/brainDamage.png", (400,400)), location=(0,400))
      

    load_image(image_list[next_index], window, "carousel1", (600,400))
    if evt == "Next Image Button":
      if next_index < len(image_list) - 1:
        next_index = next_index + 1
      load_image(image_list[next_index], window, "carousel1", (600,400))
    if evt == "Previous Image Button":
      if next_index > 0:
        next_index = next_index - 1
      load_image(image_list[next_index], window, "carousel1", (600,400))
      
      """
        TODO
        Take the next image from your list of images, feed that into 
        load_image with the key being the key of the carousel.
        For example;
          load_image(images[next_image], window, "carousel")
        Where images is a list of image sources, next_image is the index of the next image, and carousel is the key of the image carousel, look at the load_image on line 77.
      """
    
  window.close()