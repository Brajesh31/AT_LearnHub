# Author : Akshay Tripathi
# Description: Scraping Job designation and company name from times job site
# Date: 14-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3059

from bs4 import BeautifulSoup
import requests

class JobScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape_jobs(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")
            companies = soup.find_all("header", class_="clearfix")
            for company in companies:
                print(company.text)
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")


# URL of the page to scrape
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation="

# Create an instance of the JobScraper class
job_scraper = JobScraper(url)

# Call the scrape_jobs method to start scraping
job_scraper.scrape_jobs()
