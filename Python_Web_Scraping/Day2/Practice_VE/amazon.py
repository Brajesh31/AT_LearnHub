import requests
from bs4 import BeautifulSoup

# URL of the Amazon bestsellers in electronics
url = "https://www.amazon.com/best-sellers-electronics/zgbs"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Create a Beautiful Soup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all product elements
product_elements = soup.find_all("div", class_="zg-item-immersion")

# Iterate through each product element
for index, product_element in enumerate(product_elements, start=1):
    # Find the element containing the product title
    title_element = product_element.find("div", class_="p13n-sc-truncate-desktop-type2")
    
    # Find the element containing the product price
    price_element = product_element.find("span", class_="p13n-sc-price")
    
    # Check if both title and price elements are found
    if title_element and price_element:
        # Extract and clean the product title and price
        product_title = title_element.get_text().strip()
        product_price = price_element.get_text().strip()
        
        # Print the product title and price
        print(f"Product {index}: {product_title}")
        print(f"Price: {product_price}\n")
# Author : Akshay Tripathi
# Description: Scraping Job designation and company name from times job site
# Date: 14-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3059

from bs4 import BeautifulSoup
import requests

class AmazonScrapper:
    def __init__(self, url):
        self.url = url
    
    def scrape_jobs(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")

            bottle_name = soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")
            # bottle_price= soup.find_all("span", class_="a-price-whole")
            for name, in bottle_name:
                print(name.text)
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")


# URL of the page to scrape
url = "https://www.amazon.com/s?k=water+bottles&crid=17P36KY48C1D9&sprefix=water+bottles+%2Caps%2C532&ref=nb_sb_noss_2"

# Create an instance of the JobScraper class
job_scraper = AmazonScrapper(url)

# Call the scrape_jobs method to start scraping
job_scraper.scrape_jobs()
