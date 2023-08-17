from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# response = requests.get("https://aceplora.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title.string),
# artice_tags = soup.find_all(name="span", class_="titleline")

articles = soup.find_all(name="span", class_="titleline")


artice_texts = []
artice_links = []

for article_tag in articles:
    text = article_tag.getText()
    artice_texts.append(text)
    link = article_tag.get("a")
    # artice_links.append(link)

artice_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]
largest_number = max(artice_upvotes)

largest_number_index = artice_upvotes.index(largest_number)
print(largest_number_index)

print(artice_texts[largest_number_index])
# print(artice_texts)
# print(artice_links)
# print(artice_upvotes)
# for tag in artice_tag:
#     print(tag.getText())
# artice_text = artice_tag.getText()
# print(artice_tag.getText())
