
# Author : Akshay Tripathi
# Description: Testing gmail login
# Version: 3.10.6
# Date: 16-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3096/


import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Define the ChromeDriver executable path
chromedriver_path = '/home/shtlp_0015/Downloads/Selenium/Practice/chromedriver'

# Set the executable path for the ChromeService
os.environ["webdriver.chrome.driver"] = chromedriver_path

# Create an instance of ChromeService and ChromeOptions
service = ChromeService()
options = webdriver.ChromeOptions()

# Create an instance of the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Step 2: Open the Google Chrome browser
driver.maximize_window()

# Step 3: Delete all cookies
driver.delete_all_cookies()

# Step 4: Navigate to Gmail homepage
driver.get("https://www.gmail.com/")

# Step 5: Enter username in the username text box
username_field = driver.find_element_by_id("identifierId")
username_field.send_keys("xyz11@gmail.com")

# Step 6: Click on the Next button
next_button = driver.find_element_by_id("identifierNext")
next_button.click()

# Adding a short delay for the next page to load
time.sleep(2)

# Step 7: Enter password in the password text box
password_field = driver.find_element_by_name("password")
password_field.send_keys("#######")

# Step 8: Click on the Next button
signin_button = driver.find_element_by_id("passwordNext")
signin_button.click()

# Adding a delay to observe the successful login (you might use WebDriverWait for real-world scenarios)
time.sleep(5)

# Step 9: Close the Browser
driver.quit()
