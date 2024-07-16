# -*- coding: utf-8 -*-
"""Google AI Assistant

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jJLyrQ8GN_GoZMaGSuWIH8E503Osrx61
"""

def ask_question(name):
  ques = 'Hey ' + name + ' what do you want ? '
  ques = input(ques)
  return ques

ask_question("nutan")

def classify_questions(ques):
    device_lst = ['Set an alarm', 'set a reminder', 'send a message', 'call']
    personal_lst = {'who are you?': 'I am Jarvis', 'who created you?': 'I am created by your username'}

    device = False
    for i in device_lst:
        if i in ques:
            device = True
            break

    if device:
        print("This question is related to Device things, which is not supported in our Google Assistant")

    personal_question = False
    for i in personal_lst:
        if i in ques:
            personal_question = True
            break

    if personal_question:
        print(f"Hey, I am a personal assistant created by your name")

    goahead_with_web_search = not (device or personal_question)
    return goahead_with_web_search

# Example usage:
ques = "Set an alarm"
result = classify_questions(ques)
print("Go ahead with web search:", result)

classify_questions("Who are you?")

!pip install -q -U google-generativeai

import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from IPython.display import Audio, display


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
from google.colab import userdata

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-1.5-flash')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# response = model.generate_content("What is judicial system?")

response.text

to_markdown(response.text)



def ask_gemini(ques):
  response = model.generate_content(ques)

  return response.text

"""# New Section"""

have_any_other_ques = 'y'
name = ''
while have_any_other_ques == 'y':
  if name == '':
    name = input("What is your name?")
  q = ask_question(name)
  go_ahead = classify_questions(q)
  answer = ''
  if go_ahead == True:
    answer = ask_gemini(q)
  print(answer)
  speak(answer)


  have_any_other_ques = input("Do you have any other questions??")

"""# New Section"""

! pip install gTTS

from gtts import gTTS

tts = gTTS('hello')

tts.save('audio.mp3')

def speak(answer):
  tts = gTTS(answer)
  tts.save('audio.mp3')
  display(Audio('audio.mp3', autoplay=True))

speak("room is cosy")