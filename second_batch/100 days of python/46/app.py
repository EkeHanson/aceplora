from bs4 import BeautifulSoup
import requests


with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")
# all_paragraph_tags = soup.find_all(name="p")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")

company_url = soup.select_one(selector="p a")
company_url = soup.select_one(selector="#name")
company_url = soup.select(selector=".heading")
print(company_url)
