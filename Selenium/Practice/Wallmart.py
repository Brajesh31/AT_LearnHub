import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WalmartProductSearch:

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
        
    def search_and_add_to_cart(self, product_name):
        # Open Walmart website
        self.driver.get("https://www.walmart.com/")
        
        # Find the search input field and enter the product name
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.presence_of_element_located((By.ID, "global-search-input")))
        search_input.send_keys(product_name)
        
        # Submit the search
        search_input.submit()
        
        # Click on the first product from search results
        first_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-result-gridview-item")))
        first_product.click()

        # Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".prod-ProductCTA--primary")))
        add_to_cart_button.click()
    
    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    product_search = WalmartProductSearch()
    product_search.setup()
    product_search.search_and_add_to_cart("laptop")
    product_search.close_browser()
