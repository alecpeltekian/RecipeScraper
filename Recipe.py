from recipe_scrapers import scrape_me
import json
f = open('dataset.json')
import spacy
nlp=spacy.load("en_core_web_sm")

data = json.load(f)
health = data["specifications"]["healthyToUnhealthy"]
veggie = data["specifications"]["nonvegToVeg"]
indianFood = data["specifications"]["anyToIndian"]




print("Provide a valid Allrecipes.com url/"
      "of recipe of your choice or type 'exit' to cancel.  ")
req_url = (input("Enter recipe URL : "))

scraper = scrape_me(req_url)

#print(scraper.ingredients())
ingredients = scraper.ingredients()
instructions = scraper.instructions()
ingredients.append("333333 almond butter")
#print("HDWHWDHW", ingredients)
# print(health)
print(type(instructions))

def healthyToUnhealthy(ingredients, instructions):
      shagun = []
      alec = []
      for i in range(len(ingredients)):
            for j in health:
                  if j['healthy'] in ingredients[i]:
                        ingredients[i] = ingredients[i].replace(j['healthy'], j['unhealthy'])
                        shagun.append(j['healthy'])
                        alec.append(j['unhealthy'])
      for k in range(len(shagun)):
            instructions = instructions.replace(shagun[k], alec[k])
            
      
      return ingredients, instructions

def unhealthToHealthy(ingredients, instructions):
      shagun = []
      alec = []
      for i in range(len(ingredients)):
            for j in health:
                  if j['unhealthy'] in ingredients[i]:
                        ingredients[i] = ingredients[i].replace(j['unhealthy'], j['healthy'])
                        shagun.append(j['unhealthy'])
                        alec.append(j['healthy'])
      for k in range(len(shagun)):
            instructions = instructions.replace(shagun[k], alec[k])
            
      
      return ingredients, instructions

def vegToNonVeg(ingredients, instructions):
      shagun = []
      alec = []
      for i in range(len(ingredients)):
            for j in veggie:
                  if j['veg'] in ingredients[i]:
                        ingredients[i] = ingredients[i].replace(j['veg'], j['nonveg'])
                        shagun.append(j['veg'])
                        alec.append(j['nonveg'])
      for k in range(len(shagun)):
            instructions = instructions.replace(shagun[k], alec[k])
            
      
      return ingredients, instructions

def nonVegToVeg(ingredients, instructions):
      shagun = []
      alec = []
      for i in range(len(ingredients)):
            for j in veggie:
                  if j['nonveg'] in ingredients[i]:
                        ingredients[i] = ingredients[i].replace(j['nonveg'], j['veg'])
                        shagun.append(j['nonveg'])
                        alec.append(j['veg'])
      for k in range(len(shagun)):
            instructions = instructions.replace(shagun[k], alec[k])
            
      
      return ingredients, instructions

def anyToIndian(ingredients, instructions):
      shagun = []
      alec = []
      for i in range(len(ingredients)):
            for j in indianFood:
                  if j['other'] in ingredients[i]:
                        ingredients[i] = ingredients[i].replace(j['other'], j['indian'])
                        shagun.append(j['other'])
                        alec.append(j['indian'])
      for k in range(len(shagun)):
            instructions = instructions.replace(shagun[k], alec[k])
            
      
      return ingredients, instructions

trans = (input("Type 5 to transform your recipe:"))

if trans == 5:
      print(f"\n")
      print("Below are the list of transformations you can use:")
      print("1. Healthy to Unhealthy")
      print("2. Unhealthy to Healthy")
      print("3. Vegeterian to NonVegeterian")
      print("4. NonVegeterian to Vegeterian")
      print("5. To Indian Style!")
      print("6. Repeat")
      choice = input("Enter your choice: ")
      if choice == "1":
            ingredients, instructions = healthyToUnhealthy(ingredients, instructions)
      elif choice == "2":
            ingredients, instructions = unhealthToHealthy(ingredients, instructions)
      elif choice == "3":
            ingredients, instructions = vegToNonVeg(ingredients, instructions)
      elif choice == "4":
            ingredients, instructions = nonVegToVeg(ingredients, instructions)
      elif choice == "5":
            ingredients, instructions = anyToIndian(ingredients, instructions)
      elif choice == "6":
            pass

        
#healthy_ingred, healthy_instrum = healthyToUnhealthy(ingredients, instructions)
#unhealthy_ingred, unhealthy_instrum = unhealthToHealthy(ingredients, instructions)
#veg_ingred, veg_instrum = vegToNonVeg(ingredients, instructions)
#nonveg_ingred, nonveg_instrum = nonVegToVeg(ingredients, instructions)
indian_ingred, indian_instrum = anyToIndian(ingredients, instructions)

print(indian_ingred, indian_instrum)


    
#https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/

steps = instructions.split(".")