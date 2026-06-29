import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.tasnimnews.com/fa/service/77/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"

response = requests.get(url)
response.encoding = 'utf-8'
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

title_list = []

article = soup.select("section.news-container.top-news-service > section.content > article.list-item ")
for item in article:
    title = item.select('h2')[0].text.strip()
    link = item.select_one('a').get('href')
    full_link = "https://www.tasnimnews.com" + link

    title_list.append([title, full_link])

with open('data.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["عنوان خبر", "لینک خبر"]) 
    writer.writerows(title_list)
