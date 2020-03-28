import requests
from bs4 import BeautifulSoup

targetUrl = 'https://it-words.jp/p/i-a.html'

# header
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}

r = requests.get(url=targetUrl, headers=headers)

if r.status_code != 200:
    print("エラー：ステータスコードを確認してください．")
    print("ステータスコード：" + str(r.status_code))
else:
    html = r.content
    soup = BeautifulSoup(html, "html.parser")

    targetURLs = []

    termsTable = soup.find("table", class_="term").select("a")
    for i in termsTable:
        wordURL = i.get("href")
        targetURLs.append(wordURL)

    print(targetURLs)

    print(r.url + "のスクレイピングを行いました．")
    print("ステータスコード：", r.status_code)
