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

    r = requests.get(url=targetURLs[0], headers=headers)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")

    targetWord = soup.h1.string
    print(targetWord)

    print(soup.find("div", class_="entryBody"))
    targetWordExplanation = soup.find("div", class_="entryBody").text  # .find_all("p")
    print(targetWordExplanation)

    print(r.url + "のスクレイピングを行いました．")
    print("ステータスコード：", r.status_code)
