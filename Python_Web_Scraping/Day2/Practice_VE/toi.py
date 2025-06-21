
# Author : Akshay Tripathi
# Description: Scraping Job designation and company name from times job site
# Date: 14-Aug-2023
# Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3059

import requests

from bs4 import BeautifulSoup

class TOI:
    def __init__(self,url):
            self.url=url

    def news(self):
          response= requests.get(self.url)
          
          if response.status_code==200:
                soup= BeautifulSoup(response.content,"lxml")
                news=soup.find_all("div", class_="clearfix")
                for headlines in news:
                      print (headlines.text)
          else:
                print("request failed")


url="https://timesofindia.indiatimes.com/india/chandrayaan-3-in-circular-orbit-vikram-set-to-separate-tomorrow/articleshow/102756988.cms"

news_scrapper=TOI(url)

news_scrapper.news()
