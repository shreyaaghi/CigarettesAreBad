from PIL import Image
import PySimpleGUI as gui
import io
import os
import json
def read(filename):
  contents = []
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      contents.append(line)
  return contents


def get_resources():
  resources = []
  with open("links/resources.json") as f:
    resources = json.load(f)
  return resources


def get_config():
  config = {}
  with open("layouts/config.json") as f:
    config = json.load(f)
  return config

def load_image(path, window, key, size=(100,100)):
    try:
        img = Image.open(path)
        img.thumbnail(size)
        image_byte = io.BytesIO()
        img.save(image_byte, format='PNG')
        image_byte = image_byte.getvalue()
        window[key].update(data=image_byte)
        return image_byte
    except:
        print(f"Unable to open {path}!")