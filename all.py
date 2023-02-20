from recipe_scrapers import scrape_me

scraper = scrape_me('https://www.allrecipes.com/recipe/229559/best-ever-meat-loaf/')


scraper.host()
scraper.title()
scraper.total_time()
scraper.image()
print(scraper.ingredients())
scraper.instructions()
print(scraper.instructions_list())
scraper.yields()
scraper.to_json()
scraper.links()
scraper.nutrients()