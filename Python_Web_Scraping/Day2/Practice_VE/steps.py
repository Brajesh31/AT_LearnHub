import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.walmart.com/search?q=shirt"

# Send a GET request to the URL
page = requests.get(url)

print(page.text)
