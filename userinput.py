from Recipe import *

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
        choice = input("Enter your choice: ")
        if choice == "1":
            index += 1
        elif choice == "2" and index > 0:
            index -= 1
        elif choice == "3":
            pass
        else:
            QuestionAnswer(choice)
        if index == len(list):
            break
def QuestionAnswer(question):
    print(f"\n")
    question = question.lower()
    if ("ingredients" in question or "ingredient list" in question):
        print(ingredients)
        return
    print ("Invalid question, try rephrasing")
    return
list_navigation(steps)