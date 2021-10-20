# This program shows eyeglasses names and prices from the framesdirect site
import requests, re
from bs4 import BeautifulSoup

# Get content from the framesdirect site
r = requests.get('https://www.framesdirect.com/eyeglasses/').content
soup = BeautifulSoup(r, "lxml")

# Create two arrays that can store name and price of eyeglasses
glasses_name = []
glasses_price = []

# Extract glass name 
titles = soup.find_all("div", {"class":re.compile('(prod-title)')})
for t in titles: 
    glasses_name.append(t.find("a", {"class":re.compile('(prod-model)')}).text)

# Extract glass price
prices = soup.find_all("div", {"class":re.compile('(prod-bot)')})
for p in prices: 
    glasses_price.append(p.find("span", {"class":re.compile('(prod-aslowas)')}).text)

# If there are equal number of array elements in both arrays then it means
# that each element in both arrays corresponds to each other correctly. Then 
# print out information 
if len(glasses_name) == len(glasses_price):
    for x in range(len(glasses_name)):
        print("The price of a %s is %s" % (glasses_name[x], glasses_price[x]))


