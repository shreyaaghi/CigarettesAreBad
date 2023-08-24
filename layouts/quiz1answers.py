import PySimpleGUI as gui

def radio(name, group, key):
  return gui.Radio(name, group, key=key, enable_events=True)
  
def quiz1Answers():
  font = ("Helvetica", 25)
  layout = [
    [gui.Button("Back", key=("Quiz 1 Back Button")), gui.Text("General", font=font)],
    [gui.Text("Which of these bodily organs are affected by tobacco use over time?")],
    [gui.Text("You chose", key="q1.userchoice")],
    [gui.Text("The answer was", key="q1.answer")],
    [gui.Text("", key="q1.explain")]
  ]
  return layout
correct = 0
incorrect = 0
def checkAnswers(window, evt, vals):
  if vals["q1.1.d"]:
    correct += 1
    window["q1.userchoice"].update("D: All of the Above")
    window["q1.answer"].update("D: All of the Above")
  else:
    incorrect += 1
    for key in vals:
      if f"q1.1" in key:
        if vals[key] == True:
          # window["q1.answer"] = 
          pass
    # window["q1.userchoice"] = 

def checkAnswer(correctVal, userChoice):
  if correctVal == userChoice:
    # show they got it
    pass
  else:
    # show what the user chose, what the correct value was  
    pass
# TODO 
  

def checkQuiz1(window, evt, vals): # When should the check for answers occur?
  if evt == "check answers":
    checkAnswers(window, evt, vals)
  if evt == "q1.1.b":
    print(f"Quiz 1 B selected: {vals['q1.1.b']}")
  if evt == "q1.1.c":
    print(f"Quiz 1 C selected: {vals['q1.1.c']}")
  if evt == "q1.1.d":
    print(f"Quiz 1 D selected: {vals['q1.1.d']}")
  