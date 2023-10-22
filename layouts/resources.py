import PySimpleGUI as gui
from util import get_resources
from util import get_config
import webbrowser

config = get_config()
width, height = config['width'], config['height']

def resources_ui():
  resources = get_resources()
  help = resources["help"]
  contacts = resources["contacts"]
  font = ("Helvetica", 30)
  layout = [
    [gui.Button("Back", key="Resources Back Button"), gui.Text("Resources", font=('Helvetica', 40))], 
    [gui.Text("Help:", font=font)], 
    [gui.Text(" ")]
  ]
  help_resource = [
    [
      gui.Multiline(f"{resource['name']}: {resource['description']}", disabled=True, size = (width//20, 3), font=('Helvetica', 20)),
      gui.Multiline(resource['link'], write_only=True, key=f"Help Link: {resource['link']}", enable_events=True, font=('Helvetica', 20))
  ] for resource in help]
  layout = layout + help_resource
  layout = layout + [[gui.Text(" ")]]
  layout = layout + [[gui.Text("Contacts:", font=font)]]
  layout = layout + [[gui.Text(" ")]]
  contacts_resource = [
    [ 
      gui.Multiline(f"{resource['name']}: {resource['description']}", disabled=True, font=('Helvetica', 20), size = (width//20, 7)),
      gui.Multiline(resource['link'], write_only=True, key=f"Contact Link: {resource['link']}", enable_events=True, font=('Helvetica', 20)), 
  ] for resource in contacts]
  layout = layout + contacts_resource
  return layout