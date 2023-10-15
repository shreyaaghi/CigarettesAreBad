import PySimpleGUI as gui

def welcome():
  font = ("Helvetica", 30)
  layout = [[gui.Text("Welcome", font=("Helvetica",100))], 
            [gui.Text("this is an intro")], 
            [gui.Button("Information", key="Information Button", size=(9,1), font=font)],
            [gui.Button("Resources", key="Resources Button", size=(9,1), font=font)], 
            [gui.Button("Quizzes", key="Quizzes Button", size=(7,1), font=font)], 
            [gui.Button("About", key="About Button", size=(7,1), font=font)], 
            [gui.Button("Sources", key="Sources Button", size=(7,1), font=font)]]
  return layout
