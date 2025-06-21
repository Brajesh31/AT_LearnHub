
# Author : Akshay Tripathi
# Description: Testing Google Serch box using Selenium4
# Version: 3.10.6
# Date: 16-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3096/

import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Define the ChromeDriver executable path
chromedriver_path = '/home/shtlp_0015/Downloads/Selenium/Practice/Drivers/chromedriver'

# Set the executable path for the ChromeService
os.environ["webdriver.chrome.driver"] = chromedriver_path

# Create an instance of ChromeService and ChromeOptions
service = ChromeService()
options = webdriver.ChromeOptions()

# Create an instance of the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Maximize the browser window
driver.maximize_window()

# Open the Google homepage
driver.get("https://www.google.com/")

# Wait for 10 seconds
time.sleep(10)

# Close the browser window
driver.quit()
