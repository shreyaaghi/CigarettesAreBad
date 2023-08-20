import PySimpleGUI as gui
import webbrowser
from util import get_resources

font = ("Helvetica", 25)

def welcome():
  layout = [[gui.Text("Welcome", font=font)], 
            [gui.Text("this is an intro")], 
            [gui.Button("Information", key="Information Button")],
            [gui.Button("Quizzes", key="Quizzes Button")], 
            [gui.Button("Resources", key="Resources Button")], 
            [gui.Button("About", key="About Button")], 
            [gui.Button("Sources", key="Sources Button")]]
        
  return layout
  
def resources_ui():
  resources = get_resources()
  help = resources["help"]
  contacts = resources["contacts"]
  
  layout = [ # TODO Change font size of heading
    [gui.Button("Back", key="Back Button"), gui.Text("Resources", font=font)], 
    [gui.Text("These are resources:")],
    [gui.Text("Help")], 
  ]
  help_resource = [
    [
    gui.Text(resource["name"]), gui.Text(resource["description"]),
    gui.Text("\n"),
    gui.Text(resource["link"])
  ] for resource in help]
  layout = layout + help_resource
  layout = layout + [[gui.Text("Contacts")]]
  contacts_resource = [
    [
    gui.Text(resource["name"]), gui.Text(resource["description"]),
    gui.Text("\n"),
    gui.Text(resource["link"])  
  ] for resource in contacts]
  layout = layout + contacts_resource
  

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
      gui.Column(resources_ui(), scrollable=True, visible = False,  key = "resources screen")
    ]
  ]
  window = gui.Window("TeenTobaccoTermination", layout, resizable=True, element_justification='c', size = (375,667))
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
    if evt == "About Button":
      print("About Button Pressed")
    if evt == "Sources Button":
      print("Sources Button Pressed")
    if evt == "Back Button":
      cycleLayout(window, "welcome screen")
      print("Back Button Pressed")
    
  window.close()