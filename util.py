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
