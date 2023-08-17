import PySimpleGUI as gui
import webbrowser
def welcome():
  layout = [[gui.Text("Welcome")], 
            [gui.Text("this is an intro")], 
            [gui.Button("Information", key="Information Button")],
            [gui.Button("Quizzes", key="Quizzes Button")], 
            [gui.Button("Resources", key="Resources Button")], 
            [gui.Button("Get Involved", key="Get Involved Button")],
            [gui.Button("About", key="About Button")], 
            [gui.Button("Sources", key="Sources Button")]]
  return layout
  
def resources():
  layout = [[gui.Button("Back", key="Back Button"), gui.Text("Resources")], [gui.Text("these are resources")]]
  return layout


def cycleLayout(window, activeLayout):
  screens = ["welcome screen", "resources screen"]
  # Set the active layout key to visible, set every other layout to invisible (visible = True / visible = False)
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
      gui.Column(resources(), visible = False,  key = "resources screen")
    ]
  ]
  window = gui.Window("Cigarettes are bad", layout, element_justification='c')
  while True:
    evt, vals = window.read()
    if evt == gui.WIN_CLOSED:
      break
    if evt == "Information Button":
      print("Info Button Pressed")
    if evt == "Quizzes Button":
      print("Quizzes Button Pressed")
    if evt == "Resources Button":
      cycleLayout(window, "resources screen")
      print("Resources Button Pressed")
    if evt == "Get Involved Button":
      print("Get Involved Button Pressed")
    if evt == "About Button":
      print("About Button Pressed")
    if evt == "Sources Button":
      print("Sources Button Pressed")
    if evt == "Back Button":
      cycleLayout(window, "welcome screen")
      print("Back Button Pressed")
    
  window.close()