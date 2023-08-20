import PySimpleGUI as gui
def quizzes_ui():
  font = ("Helvetica", 25)
  layout = [
    [gui.Button("Back", key="Quiz Back Button"), gui.Text("Quizzes", font=font)]
  ]
  return layout