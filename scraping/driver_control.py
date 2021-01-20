from bs4 import BeautifulSoup
import time
import re

def get_code_source(driver, url, time_to_sleep = 5):
    """Extract html source code from url.
       Check if html page is a robot controleur.
       If html page is trap robot wait a user action.

    Parameters
    ----------
    driver : selenium  driver
    url : str
    time_to_sleep : int

    Returns
    -------
    str : html source code
    """
    # go to url link
    driver.get(url)
    # Time to sleep for loading
    time.sleep(time_to_sleep)
    # html code source
    html_page = driver.page_source
    # Wait if html page is a trap robot
    while "navigator.userAgent&&navigator.userAgent" in html_page:
        time.sleep(40)
        html_page = driver.page_source

    return html_page


def get_product_url(product):
    """Extract product url form a product div

    Parameters
    ----------
    div_product : str

    Returns
    -------
    str : the produt url
    """
    try:
        product_url = product.find("a", {"class" : "pl-product-link"})["href"]
        product_url = "https://www.laredoute.fr" + product_url
    except:
        product_url = ""

    return product_url


def get_product_description(product):
    """Extract product description form a product div

    Parameters
    ----------
    div_product : str

    Returns
    -------
    str : the produt url
    """
    try:
        img_html = product.find('img', alt=True)
        description = img_html['alt']
    except:
        description = ""

    return description



def get_product_title(product):
    """Extract product title form a product div

    Parameters
    ----------
    div_product : str

    Returns
    -------
    str : the produt url
    """
    try:
        img_html = product.find('img', alt=True)
        title = img_html['title']
    except:
        title = ""

    return title



def get_product_img(product):
    """Extract product url image form a product div

    Parameters
    ----------
    div_product : str

    Returns
    -------
    str : the produt image url
    """

    # Image url
    try:
        img_html = product.find('img', alt=True)
        url_img_1 = img_html['src']
    except:
        url_img_1 = ""

    try:
        img_html = product.find('img', alt=True)
        url_img_2 = img_html['data-src']
    except:
        url_img_2 = ""
    img_url = url_img_1 if "http" in url_img_1 else url_img_2

    return img_url

def get_product_price(product):
    """Extract product price

    Parameters
    ----------
    div_product : str

    Returns
    -------
    str : produt prices
    """
    # product print
    try:
        price_print = product.find("span", {"class": "product-price"}).contents
        price_print = re.findall(r"[0-9]*,[0-9]*", str(price_print))[0].replace(',', '.')
    except:
        price_print = ""
    # product discount
    try :
        price_not_discount = product.find("del", {"class": "product-original-price pl-original-price"}).contents
        price_not_discount = re.findall(r"[0-9]*,[0-9]*", str(price_not_discount))[0].replace(',', '.')
    except:
        price_not_discount = ""

    if price_not_discount=="":
        original_price = price_print
    else:
        original_price = price_not_discount

    return price_print, original_price