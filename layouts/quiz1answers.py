import PySimpleGUI as gui

def getAnswers():
  return {
  # question 1
    "q1.1.a": "A: Heart", 
    "q1.1.b": "B: Lungs", 
    "q1.1.c": "C: Mouth", 
    "q1.1.d": "D: All of the Above", 
  # question 2
    "q1.2.a": "A: Vitamin C", 
    "q1.2.b": "B: Nicotine", 
    "q1.2.c": "C: Potassium", 
    "q1.2.d": "D: Caffeine", 
  # question 3
    "q1.3.a": "A: True", 
    "q1.3.b": "B: False", 
  # question 4
    "q1.4.a": "A: Seniors", 
    "q1.4.b": "B: Middle-aged individuals", 
    "q1.4.c": "C: Adolescents and young adults", 
    "q1.4.d": "D: Children under 5", 
  # question 5
    "q1.5.a": "A: Vaping involves inhaling nicotine, while smoking involves inhaling tar", 
    "q1.5.b": "B: Smoking is a safe alternative to vaping", 
    "q1.5.c": "C: Smoking produces water vapor, while vaping produces smoke", 
    "q1.5.d": "D: Vaping has no negative health effects", 
  # question 6
    "q1.6.a": "A: True", 
    "q1.6.b": "B: False", 
  # question 7
    "q1.7.a": "A: 25%", 
    "q1.7.b": "B: 20%", 
    "q1.7.c": "C: 40%", 
    "q1.7.d": "D: 15%", 
  # question 8
    "q1.8.a": "A: Asthma", 
    "q1.8.b": "B: Hiccups", 
    "q1.8.c": "C: Dry mouth", 
    "q1.8.d": "D: Allergic rhinitis", 
  # question 9
    "q1.9.a": "A: True", 
    "q1.9.b": "B: False", 
  # question 10
    "q1.10.a": "A: Hydrogen", 
    "q1.10.b": "B: Oxygen", 
    "q1.10.c": "C: Nitrogen", 
    "q1.10.d": "D: Formaldehyde", 
  }
  
def radio(name, group, key):
  return gui.Radio(name, group, key=key, enable_events=True)
  
def quiz1Answers():
  font = ("Helvetica", 25)
  layout = [
    [gui.Button("Back", key=("Quiz Answers Back Button")), gui.Text("General", font=font)],
  # question 1
    [gui.Text("Which of these bodily organs are affected by tobacco use over time?", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.1.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.1.key", font=('Helvetica',25)), gui.Text("", key="q1.1.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
  # question 2
    [gui.Text("Which of the following substances is found in cigarettes and is known to be harmful to health?", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", font=('Helvetica',25), key="q1.2.userchoice")],
    [gui.Text("The answer was -->", key="q1.2.key", font=('Helvetica',25)), gui.Text("", key="q1.2.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
  # question 3
    [gui.Text("True or False: Vaping products are completely safe for non-smokers and have no health risks.", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.3.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.3.key", font=('Helvetica',25)), gui.Text("", key="q1.3.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
  # question 4
    [gui.Text("Which age group is most vulnerable to nicotine addiction from smoking or vaping?", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.4.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.4.key", font=('Helvetica',25)), gui.Text("", key="q1.4.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
   # question 5
    [gui.Text("What is the main difference between smoking and vaping?", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.5.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.5.key", font=('Helvetica',25)), gui.Text("", key="q1.5.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
  # question 6
    [gui.Text("True or False: Quitting smoking/vaping can lead to immediate health benefits (improved lung function, reduced heart disease risk, etc.)", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.6.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.6.key", font=('Helvetica',25)), gui.Text("", key="q1.6.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
   # question 7
    [gui.Text("What is the approximate percentage of deaths in the U.S. caused by smoking related illnesses each year?", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.7.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.7.key", font=('Helvetica',25)), gui.Text("", key="q1.7.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
  # question 8
    [gui.Text("CHALLENGE: Which of the following resipiratory conditions has been linked to long-term smoking/vaping?", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.8.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.8.key", font=('Helvetica',25)), gui.Text("", key="q1.8.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
  # question 9
    [gui.Text("True or False: Smoking increases the risk of developing lung cancer, but it has no significant impact on heart health.", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.9.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.9.key", font=('Helvetica',25)), gui.Text("", key="q1.9.answer", font=('Helvetica',25))],
    [gui.Text(" ")],
  # question 10
    [gui.Text("CHALLENGE: Which harmful chemical, found in both cigarettes and e-cigarettes, is known to increase the risk of heart diseases?", font=('Helvetica',25))],
    [gui.Text("You chose -->", font=('Helvetica',25)), gui.Text("", key="q1.10.userchoice", font=('Helvetica',25))],
    [gui.Text("The answer was -->", key="q1.10.key", font=('Helvetica',25)), gui.Text("", key="q1.10.answer", font=('Helvetica',25))],
    [gui.Text(" ")]
  ]
  return layout
  
def checkAnswers(window, evt, vals):
  correct = 0
  incorrect = 0
  answers = getAnswers()
  labels = [val for val in vals if isinstance(val, str)]
  # question 1
  if vals["q1.1.d"]:
    correct += 1
    window["q1.1.userchoice"].update("D: All of the Above")
    window["q1.1.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.1" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.1.userchoice"].update(answerText)
    window["q1.1.answer"].update("D: All of the Above")
  # question 2
  if vals["q1.2.b"]:
    correct += 1
    window["q1.2.userchoice"].update("B: Nicotine")
    window["q1.2.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.2" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.2.userchoice"].update(answerText)
    window["q1.2.answer"].update("B: Nicotine")
  # question 3
  if vals["q1.3.b"]:
    correct += 1
    window["q1.3.userchoice"].update("B: False")
    window["q1.3.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.3" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.3.userchoice"].update(answerText)
    window["q1.3.answer"].update("B: False")
  # question 4
  if vals["q1.4.c"]:
    correct += 1
    window["q1.4.userchoice"].update("C: Adolescents and young adults")
    window["q1.4.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.4" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.4.userchoice"].update(answerText)
    window["q1.4.answer"].update("C: Adolescents and young adults")
  # question 5
  if vals["q1.5.a"]:
    correct += 1
    window["q1.5.userchoice"].update("A: Vaping involves inhaling nicotine, while smoking involves inhaling tar")
    window["q1.5.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.5" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.5.userchoice"].update(answerText)
    window["q1.5.answer"].update("A: Vaping involves inhaling nicotine, while smoking involves inhaling tar")
  # question 6
  if vals["q1.6.a"]:
    correct += 1
    window["q1.6.userchoice"].update("A: True")
    window["q1.6.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.6" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.6.userchoice"].update(answerText)
    window["q1.6.answer"].update("A: True")
  # question 7
  if vals["q1.7.b"]:
    correct += 1
    window["q1.7.userchoice"].update("B: 20%")
    window["q1.7.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.7" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.7.userchoice"].update(answerText)
    window["q1.7.answer"].update("B: 20%")
  # question 8
  if vals["q1.8.a"]:
    correct += 1
    window["q1.8.userchoice"].update("A: Asthma")
    window["q1.8.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.8" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.8.userchoice"].update(answerText)
    window["q1.8.answer"].update("A: Asthma")
  # question 9
  if vals["q1.9.a"]:
    correct += 1
    window["q1.9.userchoice"].update("B: False")
    window["q1.9.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.9" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.9.userchoice"].update(answerText)
    window["q1.9.answer"].update("B: False")
  # question 10
  if vals["q1.10.d"]:
    correct += 1
    window["q1.10.userchoice"].update("D: Formaldehyde")
    window["q1.10.key"].update(visible = False)
  else:
    incorrect += 1
    answerText = ""
    for val in labels:
      if "q1.10" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.10.userchoice"].update(answerText)
    window["q1.10.answer"].update("D: Formaldehyde")

  

def checkQuiz1(window, evt, vals): # When should the check for answers occur?
  checkAnswers(window, evt, vals)
  