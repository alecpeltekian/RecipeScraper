from Recipe import *

def list_navigation(list):
    index = 0
    while index < len(list):
        print("Below are the list of instructions to create your choice of food")
        print("1. Choose next step")
        print("2. Go back to previous step")
        print("3. Repeat step")
        print(f"{list[index]} ({index + 1} of {len(list)})")
        choice = input("Enter your choice: ")
        if choice == "1" and index < len(list) - 1:
            index += 1
        elif choice == "2" and index > 0:
            index -= 1
        elif choice == "3":
            pass
        else:
            print("Invalid input. Please choose 1, 2, or 3.")
        if index == len(list):
            break

list_navigation(steps)