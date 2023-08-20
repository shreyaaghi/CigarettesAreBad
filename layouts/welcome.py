import PySimpleGUI as gui

def welcome():
  font = ("Helvetica", 25)
  layout = [[gui.Text("Welcome", font=font)], 
            [gui.Text("this is an intro")], 
            [gui.Button("Information", key="Information Button")],
            [gui.Button("Quizzes", key="Quizzes Button")], 
            [gui.Button("Resources", key="Resources Button")], 
            [gui.Button("About", key="About Button")], 
            [gui.Button("Sources", key="Sources Button")]]
  return layout
