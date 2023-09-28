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


def convert_image(path, size):
   try:
      img = Image.open(path)
      img.thumbnail(size)

      image_byte = io.BytesIO()

      new_image = Image.new("RGBA", size, "WHITE")
      new_image.paste(img, (0, 0))
      new_image.convert("RGB").save(image_byte, format="PNG")

      image_byte = image_byte.getvalue()

      return image_byte
   except:
      print(f"Unable to open {path}!")

def load_image(path, window, key, size):
    image_byte = convert_image(path, size)
    window[key].update(data=image_byte)
    return image_byte
    