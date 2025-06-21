"""
Author : Akshay Tripathi
Description: U.S. Census Bureau's QuickFacts website automation Scraping Test
Version : 1.0
Date: 21 August 2023
Azure Ticket Link : 

"""


#Importing required liberaries
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json

#Defining class CensusScraper
class CensusScraper:

    #Constructor Method: initializes driver path
    def __init__(self, chrome_driver_path):
        self.chrome_driver_path = chrome_driver_path
        self.driver = self.setup_driver()

    #method to setup chrome web driver
    def setup_driver(self):
        service = Service(self.chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        return driver

    # Remove emoji from the input string
    def get_cleaned_text(self, input_string):
      # Find the index of the last newline character
      last_newline_index = input_string.rfind('\n')
      # Extract the substring after the last newline character (if present)
      extracted_string = input_string[last_newline_index + 1:] if last_newline_index != -1 else input_string
      return extracted_string

    

    #Method to Scrape data from a table on the webpage
    def scrape_table_data(self, table):
        table_bodies = table.find_elements(By.TAG_NAME, 'tbody')
        state_data = []

        for tbody in table_bodies:
            table_heads = tbody.find_elements(By.TAG_NAME, 'th')
            table_rows = tbody.find_elements(By.TAG_NAME, 'tr')

            if table_heads:
                parameter = table_heads[0].text
                fields = []

                for table_row in table_rows:
                    table_data = table_row.find_elements(By.TAG_NAME, 'td')

                    if len(table_data) == 2:
                        parameter_type = table_data[0].text
                        field = {
                            parameter_type: self.get_cleaned_text(table_data[1].text)
                        }
                        fields.append(field)

                parameter_fields = {
                    parameter: fields
                }
                state_data.append(parameter_fields)

        return state_data
    
    # Navigate to a specified county and state combination
    def navigate_to_county_state(self, county_name, state_name):
        wait = WebDriverWait(self.driver, 10)
        url = f"https://www.census.gov/quickfacts/fact/table/{county_name}county{state_name}/PST045222"
        self.driver.get(url)

        tables = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'table')))
        state_data = []

        for idx, table in enumerate(tables):
            if idx != 0:
                state_data.extend(self.scrape_table_data(table))

        complete_state_data = {
            "state": state_name,
            "county": county_name,
            "result_url": url,
            "data": state_data
        }

        return complete_state_data

    # Get data for all county and state combinations
    def get_all_data(self, csv_file_path, json_file_path):

        self.driver.maximize_window()
        data = pd.read_csv(csv_file_path, usecols=[0, 1])#header name
        unique_data = data.drop_duplicates()

        final_data = []
        for _, row in unique_data.iterrows():
            country = row.iloc[1].lower()
            state = row.iloc[0].lower()

            final_data.append(self.navigate_to_county_state(country, state))

        final_data_json = json.dumps(final_data, indent=4)

        with open(json_file_path, "w") as json_file:
            json_file.write(final_data_json)


if __name__ == "__main__":
    # Paths
    chrome_driver_path = os.path.join(os.getcwd(), 'Drivers', 'chromedriver')    
    json_file_path = os.path.join(os.getcwd(), 'Output/output.json')
    csv_file_path = os.path.join(os.getcwd(), 'Input/census_geo_sheet.csv')

    # Instantiate the CensusScraper class and perform data extraction
    data_scraper = CensusScraper(chrome_driver_path)
    data_scraper.get_all_data(csv_file_path, json_file_path)