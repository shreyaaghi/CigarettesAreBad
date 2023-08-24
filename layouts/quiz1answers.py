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
    [gui.Text("Which of these bodily organs are affected by tobacco use over time?")],
    [gui.Text("You chose: "), gui.Text("", key="q1.1.userchoice")],
    [gui.Text("The answer was: "), gui.Text("", key="q1.1.answer")],
  ]
  return layout
  
def checkAnswers(window, evt, vals):
  print("Check answers called")
  correct = 0
  incorrect = 0
  answers = getAnswers()
  if vals["q1.1.d"]:
    correct += 1
    window["q1.1.userchoice"].update("D: All of the Above")
  else:
    incorrect += 1
    answerText = ""
    
    labels = [val for val in vals if isinstance(val, str)]
    for val in labels:
      if "q1.1" in val:
        if vals[val] == True:
          answerText = answers[val]
          break
    window["q1.1.userchoice"].update(answerText)
    window["q1.1.answer"].update("D: All of the Above")

  

def checkQuiz1(window, evt, vals): # When should the check for answers occur?
  checkAnswers(window, evt, vals)
  