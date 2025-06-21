import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartMobileSearch:

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
        
    def search_mobiles(self, product_category):
        # Open Flipkart website
        self.driver.get("https://www.flipkart.com/")
        
        # Close login popup if it appears
        close_popup_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='_2KpZ6l _2doB4z']"))
        )
        close_popup_button.click()
        
        # Search for the product category (in this case, mobile phones)
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_input.send_keys(product_category)
        search_input.submit()
        
        print("Mobile search completed.")

    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    mobile_search = FlipkartMobileSearch()
    mobile_search.setup()
    mobile_search.search_mobiles("mobile phones")
    mobile_search.close_browser()
