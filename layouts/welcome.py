from PIL import Image
import PySimpleGUI as gui
import io
import os
from util import get_config

config = get_config()
width, height = config['width'], config['height']

def welcome():
  font = ("Helvetica", 30)
  layout = [[gui.Text("Welcome", font=("Helvetica",100))], 
            [gui.Multiline("Welcome to the Teen Tobacco Termination menu. Navigate to the Information page to learn all about tobacco use in teens, the Quizzes page to test your knowledge on smoking & vaping, the Resources page to find places to get help or get involved, and the About page to learn more about the goal of Teen Tobacco Termination.", write_only = True, font=("Helvetica", 20), disabled=True, size = (width//22, 5))], 
            [gui.Button("Information", key="Information Button", size=(9,1), font=font)],
            [gui.Button("Resources", key="Resources Button", size=(9,1), font=font)], 
            [gui.Button("Quizzes", key="Quizzes Button", size=(7,1), font=font)], 
            [gui.Button("About", key="About Button", size=(7,1), font=font)], 
            [gui.Button("Sources", key="Sources Button", size=(7,1), font=font)]]
  return layout
