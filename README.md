#Clothes Scraping

##Overview
In this project, we created a python script for collect a clothes database.
The data are collected in "la redoute" website with webscrapings technicals.
We use the selenium library for control a web driver and scrap data. So you need to download a web driver.
In the chromedriver directory, there are the webdriver for google chrome with Windows.

##Installation
To install and run the application just clone the repository.
```{commandline}
git clone #####
```
You must then install the necessary libraries for this project.
```{commandline}
pip install -r requirements.txt
```
##Seting
There are a config file at *scraping/conf.json*. In this config file, i saved the url template for acced to each clothes type and also the page number.

For exemple :
```{json}
{
  "homme" : {
    "t_shirt": {
      "url": "https://www.laredoute.fr/pplp/100/157938/244/cat-286.aspx?pgnt={}#shoppingtool=treestructureguidednavigation&srt=noSorting",
      "nb_page": 62
      },
      ...
  }
}
```
##Execution
To create the first data frame, you need to execute the  following commandline

```{commandline}
python launch_product_scraping.py
``` 
This script will create a csv at *data/data.csv*. and it will look like :

| sex  | type_clother | title                  | description            | price | price_2 | url_product | img_url         |
|-------|--------------|------------------------|------------------------|-------|---------|-------------|-----------------|
| homme | t_shirt      | T-shirt col rond ...   | T-shirt col rond ...   | 14.99 | 14.99   | https://... | https://....jpg |
| homme | t_shirt      | T-shirt logo Small ... | T-shirt logo Small ... | 44.9  | 44.9    | https://... | https://....jpg |
| ...   | ...          | ...                    | ...                    | ...   | ...     | ...         | ...             |

After this step, we need to launch a second python script for download the clothes images.

```{commandline}
python launch_download_img.py
```

The script will download each product image and save its at *data/images/image_{product_id}.jpg*
