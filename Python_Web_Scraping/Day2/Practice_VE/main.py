from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.flipkart.com/').text

# print(html_text)
soup  = BeautifulSoup(html_text, 'lxml')

t_shirts=soup.find_all('li', class_= "_1kfTjk")
print(t_shirts)
