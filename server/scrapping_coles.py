# Author: The Vinh Ly
# Date: 25/07/2022


from inspect import classify_class_attrs
from pydoc import classname
from bs4 import BeautifulSoup
import requests

# target detail class name
arg_detail = {
    'name': 'product-name',
    'brand': 'product-brand',
    'price': 'price-container',
    'info': 'product-info',
    'discount': 'discount-text',
    'saved': 'product-save-value'
}

# variable
product_names = []
product_brands = []
product_prices = []

# get the source file
url = "https://shop.coles.com.au/a/national/everything/browse"

# get the source text
source_text = requests.get(url).text

# get the data
soup = BeautifulSoup(source_text, "lxml")

# Get specific data, using class.
print('search for: '+ arg_detail['name'])
product = soup.find('div', classname='product ')
print(product)
names = soup.find('span', classify_class_attrs=arg_detail['name'])

print(names)