# chore, doc, feat, fix
import PySimpleGUI as gui
import webbrowser
from layouts.welcome import welcome
from layouts.resources import resources_ui
from layouts.quizzes import quizzes_ui
from layouts.quiz1 import quiz1, handleQuiz1
from layouts.quiz1answers import quiz1Answers, checkQuiz1

font = ("Helvetica", 25)
size = (500, 667)


def cycleLayout(window, activeLayout):
  screens = ["welcome screen", "resources screen", "quizzes screen", "quiz1 screen", "answer screen 1"]
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
      gui.Column(quizzes_ui(), scrollable=False, visible = False, key = "quizzes screen", element_justification="c"),
      gui.Column(quiz1(), scrollable=True, visible = False, key = "quiz1 screen", element_justification="c", size=(935,667)), # TODO Add scrollable back?
      gui.Column(quiz1Answers(), scrollable=True, visible = False, key = "answer screen 1", element_justification="c", size=(935,667))
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
    handleQuiz1(evt, vals)
    
  window.close()