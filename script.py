import requests
from bs4 import BeautifulSoup
import json

# header
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}

first_link = "https://it-words.jp/"


def main():
    start_script = input("Do you start scraping?[Y/n]")
    if start_script == "" or start_script == "y" or start_script == "Y":
        print(load_index_urls(convert_html(first_link)))
    else:
        print("Bye")


def convert_html(target_url):
    r = requests.get(url=target_url, headers=headers)
    r.raise_for_status()  # Check status-code response from server. If not 200, stop scraping.
    print("Connection Successful")
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def load_index_urls(target_html):
    targetURLs = []

    result = target_html.find("div", class_="menuList_inner").select("a")
    for i in result:
        wordURL = i.get("href")
        targetURLs.append(wordURL)

    return targetURLs


if __name__ == "__main__":
    main()
