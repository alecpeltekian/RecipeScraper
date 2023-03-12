from recipe_scrapers import scrape_me
import json
f = open('dataset.json')
import spacy
nlp=spacy.load("en_core_web_sm")
import re

data = json.load(f)
health = data["specifications"]["healthyToUnhealthy"]
veggie = data["specifications"]["nonvegToVeg"]
indianFood = data["specifications"]["anyToIndian"]
chineseFood = data["specifications"]["anyToChinese"]
Gluten = data["specifications"]["anyToglutenfree"]




print("Provide a valid Allrecipes.com url/"
      "of recipe of your choice or type 'exit' to cancel.  ")
req_url = (input("Enter recipe URL : "))

scraper = scrape_me(req_url)

#print(scraper.ingredients())
ingredients = scraper.ingredients()
instructions = scraper.instructions()
#ingredients.append("333333 almond butter")
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

def anyToChinese(ingredients, instructions):
      shagun = []
      alec = []
      for i in range(len(ingredients)):
            for j in chineseFood:
                  if j['other'] in ingredients[i]:
                        ingredients[i] = ingredients[i].replace(j['other'], j['chinese'])
                        shagun.append(j['other'])
                        alec.append(j['chinese'])
      for k in range(len(shagun)):
            instructions = instructions.replace(shagun[k], alec[k])
            
      
      return ingredients, instructions

def anyToGlutenFree(ingredients, instructions):
      shagun = []
      alec = []
      for i in range(len(ingredients)):
            for j in Gluten:
                  if j['other'] in ingredients[i]:
                        ingredients[i] = ingredients[i].replace(j['other'], j['gluten-free'])
                        shagun.append(j['other'])
                        alec.append(j['gluten-free'])
      for k in range(len(shagun)):
            instructions = instructions.replace(shagun[k], alec[k])
            
      
      return ingredients, instructions
def singleSwap(ingredients, instructions):
      question= input("What ingredient do you want to replace, in the form: 'Replace X with Y':")
      N=2
      R=4
      res=""
      res1=""
      count=0
      count1 = 0
      for ele in question:
            if ele == ' ':
                  count = count + 1
                  if count == N:
                        break
                  res = ""
            else :
                  res = res + ele
      for ele in question:
            if ele == ' ':
                  count1 = count1 + 1
                  if count1 == R:
                        break
                  res1 = ""
            else :
                  res1 = res1 + ele
      instructions = instructions.replace(res, res1)
      for i in range(len(ingredients)):
            ingredients[i] = ingredients[i].replace(res, res1)
      return ingredients, instructions

def scaleIngredients(ingredients, instructions):
      scale = (input("Enter a number to scale ingredient(0.5, 2, etc.): "))
      scale = float(scale)
      for i in range(len(ingredients)):
            l = []
            l2 = []
            for t in ingredients[i].split():
                  try:
                        l.append(float(t))
                        l2.append(t)
                  except ValueError:
                        pass
            print(l, l2)
            if (len(l) > 0):
                  orig = l2[0]
                  num = l[0]
                  new = num * scale
                  ingredients[i] = ingredients[i].replace(orig, str(new))

      return ingredients, instructions


print(ingredients)
trans = (input("Type 5 to transform your recipe: "))
print(trans)
print(trans ==5)

if trans == '5':
      print(f"\n")
      print("Below are the list of transformations you can use:")
      print("1. Healthy to Unhealthy")
      print("2. Unhealthy to Healthy")
      print("3. Vegeterian to NonVegeterian")
      print("4. NonVegeterian to Vegeterian")
      print("5. To Indian Style!")
      print("6. To Chinese Style!")
      print("7. To Gluten free")
      print("8. Replace Single Ingredient")
      print("9. Scale up or down")
      print("10. Repeat")
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
            ingredients, instructions = anyToChinese(ingredients, instructions)
      elif choice == "7":
            ingredients, instructions = anyToGlutenFree(ingredients, instructions)
      elif choice == "8":
            ingredients, instructions = singleSwap(ingredients, instructions)
      elif choice == "9":
            ingredients, instructions = scaleIngredients(ingredients, instructions)
      elif choice == "10":
            pass

        
#healthy_ingred, healthy_instrum = healthyToUnhealthy(ingredients, instructions)
#unhealthy_ingred, unhealthy_instrum = unhealthToHealthy(ingredients, instructions)
#veg_ingred, veg_instrum = vegToNonVeg(ingredients, instructions)
#nonveg_ingred, nonveg_instrum = nonVegToVeg(ingredients, instructions)
#indian_ingred, indian_instrum = anyToIndian(ingredients, instructions)

#print(indian_ingred, indian_instrum)

print(ingredients)
print(instructions)
    
#https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/

steps = instructions.split(".")