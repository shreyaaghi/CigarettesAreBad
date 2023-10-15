import PySimpleGUI as gui
from util import get_config
import webbrowser

config = get_config()
width, height = config['width'], config['height']

layout = [[gui.Multiline("")]]