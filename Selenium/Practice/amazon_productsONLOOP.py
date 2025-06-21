

# Author : Akshay Tripathi
# Description: Automating Amazon Shopping Cart PRODUCT ON LOOP with Selenium
# Version: 3.10.6
# Date: 16-Aug-2023
# Azure Ticket Link :https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3138

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonProduct:

    def __init__(self):
        # Set the path to the ChromeDriver executable
        self.chromedriver_path = '/home/shtlp_0015/Downloads/Selenium/Practice/Drivers/chromedriver'
        os.environ["webdriver.chrome.driver"] = self.chromedriver_path
        
        # Initialize ChromeService and ChromeDriver instances
        self.service = ChromeService()
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.delete_all_cookies()
    
    def setup(self):
        # Maximize the browser window
        self.driver.maximize_window()
        
    def open_product(self, product_name):
        # Open Amazon homepage
        self.driver.get("https://www.amazon.com/")
        
        # Find the search input field and enter the product name
        search_input = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_input.send_keys(product_name)
        search_input.submit()
        
        # Click on the first product in search results
        first_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a")))
        first_product.click()
    
    def close_product(self):
        # Go back to the previous page
        self.driver.back()
    
    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    # List of products to loop through
    products = ["harry potter", "laptop", "smartphone", "earphones", "speakers"]
    
    # Create an instance of the AmazonProduct class
    product_loop = AmazonProduct()
    
    # Set up the browser window
    product_loop.setup()
    
    try:
        # Loop through each product and perform actions
        for product in products:
            product_loop.open_product(product)
            time.sleep(5)  # Adjust the delay between opening products
            product_loop.close_product()
            time.sleep(2)  # Adjust the delay between closing and opening the next product
    except KeyboardInterrupt:
        pass  # Allow the loop to be interrupted by pressing Ctrl+C
    
    # Close the browser window at the end
    product_loop.close_browser()
