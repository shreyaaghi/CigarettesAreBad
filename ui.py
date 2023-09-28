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
      gui.Column(welcome(), key = "welcome screen"), 
      gui.Column(resources_ui(), scrollable=True, visible = False,  key = "resources screen", size=size),
      gui.Column(quizzes_ui(), scrollable=False, visible = False, key = "quizzes screen", element_justification="c"),
      gui.Column(quiz1(), scrollable=True, visible = False, key = "quiz1 screen", element_justification="left", size=size), # TODO Add scrollable back?
      gui.Column(quiz1Answers(), scrollable=True, visible = False, key = "answer screen 1", element_justification="c", size=size),
      gui.Column(about(), key="about screen", visible=False),
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
    load_image("images/justSayNoFemale.png", window, "img", (200,200))
    load_image("images/teenVapingRise.png", window, "img3", (400,400))
    # load_image("images/what is in a cigarette.png", window, "img2", (400,400))
    
    img2 = window["img2"]
    # if cigarette_image == 'cigarette_contents':
    img2.draw_image(data=convert_image(f"images/{cigarette_image}.png", (400,200)),location=(0,200))

    if evt == "img2":
      x, y = vals["img2"]
      print(x,y)
      if 43 <= x <= 75:
        if 193 <= y <= 199:
          cigarette_image="brainDamage"
      if 2 <= x <= 27:
        if 192 <= y <= 199:
          cigarette_image = "cigarette_contents"
          # img2.draw_image(data=convert_image("images/brainDamage.png", (400,400)), location=(0,400))
      

    load_image(image_list[next_index], window, "carousel1", (500,500))
    if evt == "Next Image Button":
      if next_index < len(image_list) - 1:
        next_index = next_index + 1
      load_image(image_list[next_index], window, "carousel1", (500,500))
    if evt == "Previous Image Button":
      if next_index > 0:
        next_index = next_index - 1
      load_image(image_list[next_index], window, "carousel1", (500,500))
      
      """
        TODO
        Take the next image from your list of images, feed that into 
        load_image with the key being the key of the carousel.
        For example;
          load_image(images[next_image], window, "carousel")
        Where images is a list of image sources, next_image is the index of the next image, and carousel is the key of the image carousel, look at the load_image on line 77.
      """
    
  window.close()