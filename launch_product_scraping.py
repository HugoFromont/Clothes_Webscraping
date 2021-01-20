from selenium import webdriver
from bs4 import BeautifulSoup
import time

from scraping import driver_control

import os
import json

import pandas as pd



def process_html_page(num_page, driver):
    # Controle driver for go to the url
    html_page = driver_control.get_code_source(driver, url.format(num_page), time_to_sleep=5)

    # Extract product div
    soup = BeautifulSoup(html_page)
    list_div_product = soup.findAll("div", {"class": "pl-product-content"})

    # Extract information
    data = []
    for product in list_div_product:
        product_url = driver_control.get_product_url(product)
        description = driver_control.get_product_description(product)
        title = driver_control.get_product_title(product)
        img_url = driver_control.get_product_img(product)
        price_print, price_discount = driver_control.get_product_price(product)
        data.append([title, description, price_print, price_discount, product_url, img_url])

    # Add sexe and clother type information
    data = pd.DataFrame(data)
    data['sexe'] = sex
    data['type_clother'] = type_clother

    # Append data in the csv
    if not os.path.exists('data/data.csv'):
        pd.DataFrame(data).to_csv('data/data.csv', index=False)
    else:
        pd.DataFrame(data).to_csv('data/data.csv', mode='a', header=False, index=False)



########## Get configuration ##########
path_conf_json = os.path.normpath(os.path.join(os.getcwd(), "scraping", "conf.json"))

with open(path_conf_json, 'r') as config_file:
    config = json.load(config_file)

########## Define the webdriver ##########
driver = webdriver.Chrome('chromedriver/chromedriver')


# List of json first element
liste_sexe = config.keys()

for sex in liste_sexe:
    for type_clother in config[sex].keys():
        url = config[sex][type_clother]["url"]
        nb_page = config[sex][type_clother]["nb_page"]
        for num_page in range(1,nb_page + 1):
            print("Sex : {} - Clother type : {} - num_page : {}/{}".format(sex,type_clother,num_page,nb_page))
            process_html_page(num_page, driver)

