import requests
from bs4 import BeautifulSoup

URL = "hhttps://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.text)