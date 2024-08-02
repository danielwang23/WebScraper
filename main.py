import requests
from bs4 import BeautifulSoup
import pandas as pd

import random
# import os
# from openpyxl import load_workbook

# Check your current IP address
# ip_check_url = "http://httpbin.org/ip"
# response = requests.get(ip_check_url)
# print("Current IP Address:", response.json()["origin"])

#=====================================================================#

current_page = 1

data = []

proceed = True

while(proceed == True):
    print("Currently scraping page: " + str(current_page))
    url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    if soup.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soup.find_all("li", class_ ="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item = {}

            item['Title'] = book.find("img").attrs["alt"]

            item['Link'] = "https://books.toscrape.com/catalogue/"+book.find("a").attrs["href"]

            item['Price'] = book.find("p", class_="price_color").text[2:] #the .text part gets rid of tag when printed out

            item['Stock'] = book.find("p", class_="instock availability").text.strip() #.strip removes extra space between in stock availability

            # print(item['Stock'])
            data.append(item)

    current_page +=1
    
#Create dataframe
df = pd.DataFrame(data)
#Two options to save data list
df.to_excel("scrapedbook.xlsx")
# df.to_csv("scrapedbook.csv")

