
# Author : Akshay Tripathi
# Description: Automating Amazon Shopping Cart filter section with Selenium
# Version: 3.10.6
# Date: 16-Aug-2023
# Azure Ticket Link :https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3138

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonFilterAutomation:

    def __init__(self):
        self.chromedriver_path = '/home/shtlp_0015/Downloads/Selenium/Practice/Drivers/chromedriver'
        os.environ["webdriver.chrome.driver"] = self.chromedriver_path
        self.service = ChromeService()
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.delete_all_cookies()
    
    def setup(self):
        # Maximize the browser window
        self.driver.maximize_window()
        
    def apply_filters(self, product_name, min_price, max_price, ratings, brand, cpu_manufacturer, processor_count, operating_system, display_size):
        # Open Amazon homepage
        self.driver.get("https://www.amazon.com/")
        
        # Find the search input field and enter the product name
        search_input = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_input.send_keys(product_name)
        search_input.submit()
        
        # Click the "Filters" button
        filter_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "p_n_feature_thirteen_browse-bin/17869292011")))
        filter_button.click()
        
        # Enter the minimum price
        min_price_input = self.driver.find_element(By.ID, "low-price")
        min_price_input.clear()
        min_price_input.send_keys(min_price)
        
        # Enter the maximum price
        max_price_input = self.driver.find_element(By.ID, "high-price")
        max_price_input.clear()
        max_price_input.send_keys(max_price)
        
        # Apply the price range filter
        apply_price_filter_button = self.driver.find_element(By.XPATH, "//input[@title='Apply']")
        apply_price_filter_button.click()
        
        # Click the ratings filter
        ratings_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//i[contains(@aria-label, '{ratings}')]/ancestor::li/input")))
        ratings_filter.click()
        
        # Apply additional filters  
        brand_filter = self.driver.find_element(By.XPATH, f"//span[contains(text(), '{brand}')]/ancestor::li/input")
        brand_filter.click()

        cpu_manufacturer_filter = self.driver.find_element(By.XPATH, f"//span[text()='{cpu_manufacturer}']/preceding-sibling::input")
        cpu_manufacturer_filter.click()

        processor_count_filter = self.driver.find_element(By.XPATH, f"//span[text()='{processor_count}']/preceding-sibling::input")
        processor_count_filter.click()

        operating_system_filter = self.driver.find_element(By.XPATH, f"//span[text()='{operating_system}']/preceding-sibling::input")
        operating_system_filter.click()

        display_size_filter = self.driver.find_element(By.XPATH, f"//span[text()='{display_size}']/preceding-sibling::input")
        display_size_filter.click()
        
        # Enter minimum and maximum size
        min_size_input = self.driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Minimum Display Size')]")
        min_size_input.clear()
        min_size_input.send_keys("13")  # Example minimum size
        
        max_size_input = self.driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Maximum Display Size')]")
        max_size_input.clear()
        max_size_input.send_keys("15")  # Example maximum size
        
        # Click the "Go" button to apply display size filter
        go_button = self.driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Go')]")
        go_button.click()
    
    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    filter_automation = AmazonFilterAutomation()
    filter_automation.setup()
    
    # Apply filters with desired values
    filter_automation.apply_filters(
        product_name="laptop",
        min_price="500",
        max_price="1000",
        ratings="4 Stars & Up",
        brand="HP",
        cpu_manufacturer="Intel",
        processor_count="Quad Core",
        operating_system="Windows 10",
        display_size="15 Inch"
    )
    
    # Close the browser
    filter_automation.close_browser()
