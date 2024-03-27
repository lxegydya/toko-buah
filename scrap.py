import requests
from bs4 import BeautifulSoup
# from pymongo import MongoClient

# client=MongoClient('')
data = requests.get("https://www.bilibili.tv/id/anime")

soup = BeautifulSoup(data.text,'html.parser')

animes = soup.select('.bstar-video-card')

for anime in animes:
    title = anime.select_one('.bstar-video-card__title-text').text.strip()
    genre = anime.select_one('.bstar-video-card__desc').text.split('/').pop().strip()
    # image = anime.find('img', class_='bstar-image__img')['src']
    # image = anime.select_one('.bstar-image__img').get('src')
    image = anime.select_one('.bstar-image__img')['src'].split('@')[0]

    print(title, '|', genre, '|', image)