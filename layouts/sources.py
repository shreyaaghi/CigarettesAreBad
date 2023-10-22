import PySimpleGUI as gui
from util import get_config, get_citations
import webbrowser

config = get_config()
width, height = config['width'], config['height']

def sources():
    citations = get_citations()
    print(citations)
    font = ("Helvetica", 20)
    layout = [
    [gui.Button("Back", key="Sources Back Button"), gui.Text("Sources:",font=('Helvetica', 40))], 
    [gui.Text("", font=font)], 
    ]
    citationResource = [
        [
            gui.Multiline(f"{citation['citation']}", size = (width//20, 9), font=("Helvetica", 20),write_only=True,enable_events=True,key=f"Citation Link: {citation['link']}")
            for citation in citations
        ]
    ]
    layout += citationResource
    return layout