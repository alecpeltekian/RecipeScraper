from Scraper import RecipeFetcher

rf = RecipeFetcher()

print("Welcome to Hell's Kitchen. Provide a valid Allrecipes.com url/"
      "of recipe of your choice or type 'exit' to cancel. ")
req_url = (input("Enter recipe URL : "))

recipe = (rf.scrape_recipe(req_url))

print(recipe)