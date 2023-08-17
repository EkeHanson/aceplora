from bs4 import BeautifulSoup
import requests


with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify)
# print(soup.titile)
# print(soup.titile.string)
print(soup.a["href"])
print(soup.p)
