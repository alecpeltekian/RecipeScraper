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
preparations = data["specifications"]["preparations"]

ingredients = vegetables + meat + seafood + poultry + spices

def Parse(list):
    Dict = {}
    

    for i in list:
        doc = nlp(i)
        temp = {}
        amount = ""
        unit = ""
        prep = ""
        name = ""
        prev = ""
        for token in doc:
            if (token.text in measures):
                unit += token.text
            if (token.tag_ == "CD"):
                amount += token.text
            if (token.text in ingredients):
                name += token.text
            if (token.text in preparations):
                prep += token.text
            combined = prev + " " + token.text
            if (combined in ingredients):
                name = combined
            if (combined in measures):
                unit = combined
            prev = token.text
        temp = {"Quantity" : amount, "Unit" : unit, "Preperation" : prep}
        Dict[name] = temp
    return Dict
test = Parse(['1.5 pounds salmon fillets', 'lemon pepper to taste', 'garlic powder to taste', 'salt to taste', '0.33333334326744 cup soy sauce', '0.33333334326744 cup brown sugar', '0.33333334326744 cup water', '0.25 cup vegetable oil'])

print(test)

