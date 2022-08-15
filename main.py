from bs4 import BeautifulSoup
import requests

# url = r"https://storage.kanzaki.ru/ANIME___/Bleach/"
# html_text = requests.get(url)
# soup = BeautifulSoup(html_text.content, 'lxml')
# links = soup.find_all('a')
# print(links[1]['href'])
video_url = requests.get(
    r"https://storage.kanzaki.ru/ANIME___/Bleach/%5bHorribleSubs%5d%20Bleach%20-%20266%20%5b720p%5d.mkv")
with open("video.mkv", "wb") as video:
    print('start')
    for chunk in video_url.iter_content(chunk_size=1024):
        print("staring")
        video.write(chunk)
        print('writing...')
    print("done!")
# python3
