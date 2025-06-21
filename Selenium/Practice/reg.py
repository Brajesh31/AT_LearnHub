import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationFormAutomation:

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
        
    def fill_and_submit_registration_form(self, name, email, password):
        # Open registration page of the sample website
        self.driver.get("https://www.example.com/register")
        
        # Fill out the registration form fields
        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        
        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)
        
        # Submit the registration form
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Print success message if registration is successful
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'success')]"))
        )
        print(success_message.text)

    def close_browser(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    registration_automation = RegistrationFormAutomation()
    registration_automation.setup()
    registration_automation.fill_and_submit_registration_form("John Doe", "john@example.com", "securepassword")
    registration_automation.close_browser()
