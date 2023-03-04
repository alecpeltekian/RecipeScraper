from Recipe import *
import json
f = open('dataset.json')
data = json.load(f)
import spacy
import en_core_web_sm
#nlp = spacy.load("en_core_web_sm")
nlp=en_core_web_sm.load()
import pywhatkit as kit 
from time import sleep
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')
from IngredientParse import *

tools = data["specifications"]["tools_vessels"]
actions = data["specifications"]["actions"]

def list_navigation(list):
    index = 0
    list.pop()
    list.append("Are you sure you want to exit this recipe? Type 1 to exit")
    while index < len(list):
        print(f"\n")
        print("Below are the list of instructions to create your choice of food")
        print("1. Choose next step")
        print("2. Go back to previous step")
        print("3. Repeat step")
        print(f"{list[index]} ({index + 1} of {len(list)})")
        stored = list[index]
        p=stored
        q=stored
        choice = input("Enter your choice: ")
        if choice == "1":
            index += 1
        elif choice == "2" and index > 0:
            index -= 1
        elif choice == "3":
            pass
        else:
            QuestionAnswer(choice, p, q)
        if index == len(list):
            break
def QuestionAnswer(question, p, q):
    print(f"\n")
    question = question.lower()
    doc = nlp(question)
    tool = ""
    ingredquestion = False
    for token in doc:
            if (token.text in tools):
                tool = token.text
            if (token.text in ingred):
                ingredquestion = True
    if ("ingredients" in question or "ingredient list" in question):
        print(ingredients)
        return
    elif 'how long' in question or "how much time" in question:

        question=question.split(" ")
        flag1=0
        for i in question:
            for j in actions:
                if i==j:
                    s=i
                    break

        p=p.lower()
        flag=False
        flagp=0
        tok_dummy = ''
        if s in p:
            doc2=nlp(p)
            for token in doc2:
              if flag:
                flag = False
      
                if(token.text == 'minutes' or token.text == 'min' or token.tag_=='NNS' or token.text=='hour' or token.text=='hr' or token.text=='seconds' or token.text=='secs'):
                  print(tok_dummy, token.text)
                  flagp=1
                  break

              if token.tag_=='CD':
                tok_dummy = token.text
                flag = True

            if flagp==0:
                string4 = q[q.find('until'):].strip()
                print(string4) 
        return
    elif ("how" in question and ingredquestion == False):
        kit.playonyt(question)
        return
    elif len(tool) > 0:
        input_string = tool
        word = wordnet.synsets(input_string)
        print(word[0].definition())
        return
    elif ingredquestion:
        answ = IngredientQuestion(question, ingreddict)
        print(answ)
        return   
    print ("Invalid question, try rephrasing")
    return
ingreddict = Parse(ingredients)
list_navigation(steps)