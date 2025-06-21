

# Author : Akshay Tripathi
# Description: Testing Google Serch box using Selenium4
# Version: 3.10.6
# Date: 16-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3096/


import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleSearchTest:

    def __init__(self):
        # Define the ChromeDriver executable path
        self.chromedriver_path = '/home/shtlp_0015/Downloads/Selenium/Practice/Drivers/chromedriver'
        
        # Set the executable path for the ChromeService
        os.environ["webdriver.chrome.driver"] = self.chromedriver_path
        
        # Create an instance of ChromeService and ChromeOptions
        self.service = ChromeService()
        self.options = webdriver.ChromeOptions()
        
        # Create an instance of the Chrome WebDriver
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
    
    def setup(self):
        # Maximize the browser window
        self.driver.maximize_window()
        
    def perform_google_search(self):
        # Open Google search page
        self.driver.get("https://www.google.com/")
        
        # Find the search input field and enter the search term
        wait = WebDriverWait(self.driver, 40)
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_input.send_keys("Nature Images")
        
        # Submit the search
        search_input.submit()
    
    def get_search_results(self):
        # Wait for search results
        wait = WebDriverWait(self.driver, 10)
        search_results = wait.until(EC.presence_of_element_located((By.ID, "result-stats"))).text
        
        print("Search Results:", search_results)
    
    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    search_test = GoogleSearchTest()
    search_test.setup()
    search_test.perform_google_search()
    search_test.get_search_results()
    search_test.close_browser()
