# chore, doc, feat, fix
import PySimpleGUI as gui
import webbrowser
from layouts.welcome import welcome
from layouts.resources import resources_ui
from layouts.quizzes import quizzes_ui

font = ("Helvetica", 25)
size = (500, 667)


def cycleLayout(window, activeLayout):
  screens = ["welcome screen", "resources screen", "quizzes screen"]
  window[activeLayout].update(visible = True)
  for screen in screens:
    if screen == activeLayout:
      continue
    window[screen].update(visible = False)
  

def ui():
  gui.theme("LightBlue")
  layout = [
    [
      gui.Column(welcome(), key = "welcome screen"), 
      gui.Column(resources_ui(), scrollable=True, visible = False,  key = "resources screen", size=size),
      gui.Column(quizzes_ui(), scrollable=False, visible = False, key = "quizzes screen")
    ]
  ]
  window = gui.Window("TeenTobaccoTermination", layout, resizable=True, element_justification='c', size = size)
  while True:
    evt, vals = window.read()
    if evt == gui.WIN_CLOSED:
      break
    if evt == "Information Button":
      print("Info Button Pressed")
    if evt == "Quizzes Button":
      cycleLayout(window, "quizzes screen")
      print("Quizzes Button Pressed")
    if evt == "Resources Button":
      cycleLayout(window, "resources screen")
      print("Resources Button Pressed")
    if evt == "About Button":
      print("About Button Pressed")
    if evt == "Sources Button":
      print("Sources Button Pressed")
    if "Back Button" in evt: # changed from evt == "Back Button"
      cycleLayout(window, "welcome screen")
      print("Back Button Pressed")
    
  window.close()