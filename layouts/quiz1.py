import PySimpleGUI as gui

def radio(name, group, key):
  return gui.Radio(name, group, key=key, enable_events=True)
  
def quiz1():
  font = ("Helvetica", 25)
  layout = [
    [gui.Button("Back", key=("Quiz 1 Back Button")), gui.Text("General", font=font)],
  # question 1
    [gui.Text("1. Which of these bodily organs are affected by tobacco use over time?")],
    [radio("A: Heart", "group1", "q1.1.a")],
    [radio("B: Lungs", "group1", "q1.1.b")],
    [radio("C: Mouth", "group1", "q1.1.c")],
    [radio("D: All of the Above", "group1", "q1.1.d")],
    [gui.Text(" ")],
  # question 2
    [gui.Text("2. Which of the following substances is found in cigarettes and is known to be harmful to health?")],
    [radio("A: Vitamin C", "group2", "q1.2.a")],
    [radio("B: Nicotine", "group2", "q1.2.b")],
    [radio("C: Potassium", "group2", "q1.2.c")],
    [radio("D: Caffeine", "group2", "q1.2.d")],
    [gui.Text(" ")],
  # question 3
    [gui.Text("3. True or False: Vaping products are completely safe for non-smokers and have no health risks.")],
    [radio("True", "group3", "q1.3.a")],
    [radio("False", "group3", "q1.3.b")],
    [gui.Text(" ")],
  # question 4
    [gui.Text("4. Which age group is most vulnerable to nicotine addiction from smoking or vaping?")],
    [radio("A: Seniors", "group4", "q1.4.a")],
    [radio("B: Middle-aged individuals", "group4", "q1.4.b")],
    [radio("C: Adolescents and young adults", "group4", "q1.4.c")],
    [radio("Children under 5", "group4", "q1.4.d")],
    [gui.Text(" ")],
  # question 5
    [gui.Text("5. What is the main difference between smoking and vaping?")],
    [radio("A: Vaping involves inhaling nicotine, while smoking involves inhaling tar", "group5", "q1.5.a")],
    [radio("B: Smoking is a safer alternative to vaping", "group5", "q1.5.b")],
    [radio("C: Smoking produces water vapor, while vaping produces smoke", "group5", "q1.5.c")],
    [radio("D: Vaping has no negative health effects", "group5", "q1.5.d")],
    [gui.Text(" ")],
  # question 6
    [gui.Text("6. True or False: Quitting smoking/vaping can lead to immediate health benefits (improved lung function, reduced heart disease risk, etc.)")],
    [radio("True", "group6", "q1.6.a")],
    [radio("False", "group6", "q1.6.b")],
    [gui.Text(" ")],
  # question 7
    [gui.Text("7. What is the approximate percentage of deaths in the U.S. caused by smoking-related illnesses each year?")],
    [radio("A: 25%", "group7", "q1.7.a")],
    [radio("B: 20%", "group7", "q1.7.b")],
    [radio("C: 40%", "group7", "q1.7.c")],
    [radio("D: 15%", "group7", "q1.7.d")],
    [gui.Text(" ")],
  # question 8
    [gui.Text("8. CHALLENGE: Which of the following respiratory conditions has been linked to long-term smoking/vaping?")],
    [radio("A: Asthma", "group8", "q1.8.a")],
    [radio("B: Hiccups", "group8", "q1.8.b")],
    [radio("C: Dry mouth", "group8", "q1.8.c")],
    [radio("D: Allergic rhinitis", "group8", "q1.8.d")],
    [gui.Text(" ")],
  # question 9
    [gui.Text("9. True or False: Smoking increases the risk of developing lung cancer, but it has no significant impact on heart health.")],
    [radio("A: True", "group9", "q1.9.a")],
    [radio("B: False", "group9", "q1.9.b")],
    [gui.Text(" ")],
  # question 10
    [gui.Text("10. CHALLENGE: Which harmful chemical, found in both cigarettes and e-cigarettes, is known to increase the risk of heart diseases?")],
    [radio("A: Hydrogen", "group10", "q1.10.a")],
    [radio("B: Oxygen", "group10", "q1.10.b")],
    [radio("C: Nitrogen", "group10", "q1.10.c")],
    [radio("D: Formaldehyde", "group10", "q1.10.d")],
    [gui.Text(" ")],
  # submit button
    [gui.Button("Submit", key="Submit Button")]
  ]
  return layout

def checkAnswers(vals):
  pass

def handleQuiz1(evt, vals): # When should the check for answers occur?
# question 1
  if evt == "q1.1.a":
    print(f"Quiz 1 1A selected: {vals['q1.1.a']}")
  if evt == "q1.1.b":
    print(f"Quiz 1 1B selected: {vals['q1.1.b']}")
  if evt == "q1.1.c":
    print(f"Quiz 1 1C selected: {vals['q1.1.c']}")
  if evt == "q1.1.d":
    print(f"Quiz 1 1D selected: {vals['q1.1.d']}")
# question 2
  if evt == "q1.2.a":
    print(f"Quiz 1 2A selected: {vals['q1.2.a']}")
  if evt == "q1.2.b":
    print(f"Quiz 1 2B selected: {vals['q1.2.b']}")
  if evt == "q1.2.c":
    print(f"Quiz 1 2C selected: {vals['q1.2.c']}")
  if evt == "q1.2.d":
    print(f"Quiz 1 2D selected: {vals['q1.2.d']}")
# question 3
  if evt == "q1.3.a":
    print(f"Quiz 1 3A selected: {vals['q1.3.a']}")
  if evt == "q1.3.b":
    print(f"Quiz 1 3B selected: {vals['q1.3.b']}")
# question 4
  if evt == "q1.4.a":
    print(f"Quiz 1 4A selected: {vals['q1.4.a']}")
  if evt == "q1.4.b":
    print(f"Quiz 1 4B selected: {vals['q1.4.b']}")
  if evt == "q1.4.c":
    print(f"Quiz 1 4C selected: {vals['q1.4.c']}")
  if evt == "q1.4.d":
    print(f"Quiz 1 4D selected: {vals['q1.4.d']}")
# question 5
  if evt == "q1.5.a":
    print(f"Quiz 1 5A selected: {vals['q1.5.a']}")
  if evt == "q1.5.b":
    print(f"Quiz 1 5B selected: {vals['q1.5.b']}")
  if evt == "q1.5.c":
    print(f"Quiz 1 5C selected: {vals['q1.5.c']}")
  if evt == "q1.5.d":
    print(f"Quiz 1 5D selected: {vals['q1.5.d']}")
  # question 6
  if evt == "q1.6.a":
    print(f"Quiz 1 6A selected: {vals['q1.6.a']}")
  if evt == "q1.6.b":
    print(f"Quiz 1 6B selected: {vals['q1.6.b']}")
  # question 7
  if evt == "q1.7.a":
    print(f"Quiz 1 7A selected: {vals['q1.7.a']}")
  if evt == "q1.7.b":
    print(f"Quiz 1 7B selected: {vals['q1.7.b']}")
  if evt == "q1.7.c":
    print(f"Quiz 1 7C selected: {vals['q1.7.c']}")
  if evt == "q1.7.d":
    print(f"Quiz 1 7D selected: {vals['q1.7.d']}")
# question 8
  if evt == "q1.8.a":
    print(f"Quiz 1 8A selected: {vals['q1.8.a']}")
  if evt == "q1.8.b":
    print(f"Quiz 1 8B selected: {vals['q1.8.b']}")
  if evt == "q1.8.c":
    print(f"Quiz 1 8C selected: {vals['q1.8.c']}")
  if evt == "q1.8.d":
    print(f"Quiz 1 8D selected: {vals['q1.8.d']}")
# question 9
  if evt == "q1.9.a":
    print(f"Quiz 1 9A selected: {vals['q1.9.a']}")
  if evt == "q1.9.b":
    print(f"Quiz 1 9B selected: {vals['q1.9.b']}")
# question 10
  if evt == "q1.10.a":
    print(f"Quiz 1 10A selected: {vals['q1.10.a']}")
  if evt == "q1.10.b":
    print(f"Quiz 1 10B selected: {vals['q1.10.b']}")
  if evt == "q1.10.c":
    print(f"Quiz 1 10C selected: {vals['q1.10.c']}")
  if evt == "q1.10.d":
    print(f"Quiz 1 10D selected: {vals['q1.10.d']}")
    
  