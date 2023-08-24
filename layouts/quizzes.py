import PySimpleGUI as gui
def quizzes_ui():
  font = ("Helvetica", 25)
  layout = [
    [gui.Button("Back", key="Quiz Back Button"), gui.Text("Quizzes", font=font)],
    [gui.Button("Quiz 1", key="Quiz 1 Button")]
  ]
  return layout