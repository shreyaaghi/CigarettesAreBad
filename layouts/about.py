import PySimpleGUI as gui

def about():
  font = ("Helvetica", 25)
  layout = [
    [gui.Button("Back", key="About Back Button"), gui.Text("About", font=font)],
    [gui.Image(source = "images/bioImage.png")]
  ]
  return layout