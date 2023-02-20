from recipe_scrapers import scrape_me


print("Welcome to The Interactive Cookbook. Provide a valid Allrecipes.com url/"
      "of recipe of your choice or type 'exit' to cancel. ")
req_url = (input("Enter recipe URL : "))

scraper = scrape_me(req_url)

print(scraper.ingredients())
#print(scraper.instructions())
print(scraper.instructions_list())