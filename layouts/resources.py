import PySimpleGUI as gui
from util import get_resources
import webbrowser

def resources_ui():
  resources = get_resources()
  help = resources["help"]
  contacts = resources["contacts"]
  font = ("Helvetica", 19)
  layout = [
    [gui.Button("Back", key="Resources Back Button"), gui.Text("Resources", font=font)], 
    [gui.Text("These are resources:")],
    [gui.Text("Help", font=font)], 
  ]
  help_resource = [
    [
      gui.Multiline(f"{resource['name']}: {resource['description']}", disabled=True),
      gui.Multiline(resource['link'], write_only=True, key=f"Help Link: {resource['link']}", enable_events=True)
  ] for resource in help]
  layout = layout + help_resource
  layout = layout + [[gui.Text("Contacts", font=font)]]
  contacts_resource = [
    [ 
      gui.Multiline(f"{resource['name']}: {resource['description']}", disabled=True),
      gui.Multiline(resource['link'], write_only=True, key=f"Contact Link: {resource['link']}", enable_events=True)
  ] for resource in contacts]
  layout = layout + contacts_resource
  return layout