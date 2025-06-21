
# Author : Akshay Tripathi
# Description: Testing Login page 
# Version: 3.10.6
# Date: 16-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3096/

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeHRMLoginTest:

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
        
    def perform_login(self):
        # Open the URL
        self.driver.get("http://opensource-demo.orangehrmlive.com/")
        
        # Find the username and password fields and enter values
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        
        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        
        # Click the Login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
        login_button.click()
    
    def verify_login(self):
        # Get the actual and expected titles
        actual_title = self.driver.title
        expected_title = "OrangeHRM"
        
        # Compare the titles and print result
        if actual_title == expected_title:
            print("Login Test Passed")
        else:
            print("Login Test Failed")
    
    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    login_test = OrangeHRMLoginTest()
    login_test.setup()
    login_test.perform_login()
    login_test.verify_login()
    login_test.close_browser()
































# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Define the ChromeDriver executable path
# chromedriver_path = '/home/shtlp_0015/Downloads/Selenium/Practice/Drivers/chromedriver'

# # Set the executable path for the ChromeService
# os.environ["webdriver.chrome.driver"] = chromedriver_path

# # Create an instance of ChromeService and ChromeOptions
# service = ChromeService()
# options = webdriver.ChromeOptions()

# # Create an instance of the Chrome WebDriver
# driver = webdriver.Chrome(service=service, options=options)

# # Maximize the browser window
# driver.maximize_window()

# # Open the URL
# driver.get("http://opensource-demo.orangehrmlive.com/")

# # Find the username and password fields and enter values
# wait = WebDriverWait(driver, 10)  # Set an explicit wait
# username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
# password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))


# username_field.send_keys("Admin")
# password_field.send_keys("admin123")

# # Click the Login button
# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
# login_button.click()

# # Get the actual and expected titles
# actual_title = driver.title
# expected_title = "OrangeHRM"

# # Compare the titles and print result
# if actual_title == expected_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")

# # Close the browser window
# driver.quit()



