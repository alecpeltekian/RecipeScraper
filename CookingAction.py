
import spacy
nlp=spacy.load("en_core_web_sm")


from recipe_scrapers import scrape_me


print("Welcome to The Interactive Cookbook. Provide a valid Allrecipes.com url/"
      "of recipe of your choice or type 'exit' to cancel. ")
req_url = (input("Enter recipe URL : "))

scraper = scrape_me(req_url)

#print(scraper.ingredients())
print(scraper.instructions())

instructions = scraper.instructions()
steps = instructions.split(".")


def list_navigation(list):
    index = 0
    for _ in list:
        print("Below are the list of instructions to create your choice of food")
        print("1. Choose next step")
        print("2. Go back to previous step")
        print("3. Repeat step")
        print(f"{list[index]} ({index + 1} of {len(list)})")
        t=nlp(list[index])
        for token in t:
          if token.tag_=='VB':
            print(token.text)
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

