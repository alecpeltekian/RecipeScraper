import json
f = open('dataset.json')
import spacy
nlp=spacy.load("en_core_web_sm")

data = json.load(f)
measures = data["specifications"]["measures"]
vegetables = data["specifications"]["vegetables"]
meat = data["specifications"]["meat"]
seafood = data["specifications"]["seafood"]
poultry = data["specifications"]["poultry"]
spices = data["specifications"]["spices"]
cookingmedium = data["specifications"]["cookingmedium"]
preparations = data["specifications"]["preparations"]

preplist = ['prep', 'prepare', 'preperation', 'prepped', 'prepared', 'pre-prep', 'kind', 'type']
measurelist = ['how much', 'how many', 'quantity', 'measure', 'measurement']
deflist = ['what is', "what are"]
Dict = {}
    

ingredients = vegetables + meat + seafood + poultry + spices + cookingmedium

def Parse(list):

    for i in list:
        doc = nlp(i)
        temp = {}
        amount = ""
        unit = ""
        prep = ""
        name = ""
        prev = ""
        cat = "Other"
        for token in doc:
            if (token.text in measures):
                unit += token.text
            if (token.tag_ == "CD"):
                amount += token.text
            if (token.text in ingredients):
                name += token.text
                if (token.text in vegetables):
                    cat = "Vegetable"
                if (token.text in meat):
                    cat = "Meat"
                if (token.text in seafood):
                    cat = "Seafood"
                if (token.text in poultry):
                    cat = "Poultry"
                if (token.text in spices):
                    cat = "Spice"
                if (token.text in cookingmedium):
                    cat = "Cooking Medium"
            if (token.text in preparations):
                prep += token.text
            combined = prev + " " + token.text
            if (combined in ingredients):
                name = combined
            if (combined in measures):
                unit = combined
            if (combined in preparations):
                prep = combined
            prev = token.text
        temp = {"Quantity" : amount, "Unit" : unit, "Preperation" : prep, "Category" : cat}
        Dict[name] = temp
    return Dict


def IngredientQuestion(q):
    q = q.lower()
    doc = nlp(q)
    ingredient = ''
    prev = ""
    for token in doc:
        if (token.text in ingredients):
            ingredient = token.text
        combined = prev + " " + token.text
        if (combined in ingredients):
            ingredient = combined
        prev = token.text

    if(ingredient not in Dict.keys()):
        print("Not a valid ingredient, try again")
        return
    if any(p in q for p in preplist):
        if(Dict[ingredient]["Preperation"] == ""):
            string = ingredient + " does not require any prep before starting the recipe"
            print(string)
            return
        else:
            print(Dict[ingredient]["Preperation"])
            return
    if any(m in q for m in measurelist):
        string = Dict[ingredient]["Quantity"] + ' ' + Dict[ingredient]["Unit"]
        print(string)
        return
    if any(d in q for d in deflist):
        string = Dict[ingredient]["Category"] + ", look at https://en.wikipedia.org/wiki/" + ingredient.replace(" ", "_") + " for more information"
        print(string)
        return  
    else:
        print("Not a valid ingredient question, try rephrasing")
        return





test = Parse(['1.5 pounds salmon fillets', 'lemon pepper to taste', 'garlic powder to taste', 'salt to taste', '0.33333334326744 cup soy sauce', '0.33333334326744 cup brown sugar', '0.33333334326744 cup water', '0.25 cup vegetable oil'])
#print(test)
#print("onions" in Dict.keys())
IngredientQuestion("What is salmon")
#print(cookingmedium)

