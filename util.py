def read(filename):
  contents = []
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      contents.append(line)
  return contents