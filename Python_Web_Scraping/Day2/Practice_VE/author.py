# Author : Akshay Tripathi
# Description: Scraping Job designation and company name from times job site
# Date: 14-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3059

import requests
from bs4 import BeautifulSoup

class QuoteScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape_quotes(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find all quote elements
            quote_elements = soup.find_all("span", class_="text")
            
            # Extract and print the text of each quote
            for quote in quote_elements:
                print(quote)
                
            # Find all author elements
            author_elements = soup.find_all("small", class_="author")
            
            # Extract and print the name of each author
            for index, author_element in enumerate(author_elements, start=1):
                author_name = author_element.get_text()
                print(f"Author {index}: {author_name}\n")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

# URL of the webpage to scrape
url = "http://quotes.toscrape.com/"

# Create an instance of the QuoteScraper class
quote_scraper = QuoteScraper(url)

# Call the scrape_quotes method to start scraping
quote_scraper.scrape_quotes()
