import requests
from bs4 import BeautifulSoup
import time
from requests.exceptions import Timeout

# header
headers = {"User-Agent": ""}

# To load index
primary_link = "https://it-words.jp/"


def main():
    start_script = input("Do you start scraping?[Y/n]")
    if start_script == "" or start_script == "y" or start_script == "Y":
        all_target_URLs = load_index_urls(convert_html(primary_link))
        for index_url in all_target_URLs:
            print(index_url)
            words_url = load_words_title(index_url)
            for a_word in words_url:
                time.sleep(10)
                print(load_words_details(a_word))
    else:
        print("Bye")


def convert_html(target_url):
    while True:
        try:
            r = requests.get(url=target_url, headers=headers, timeout=30)
            r.raise_for_status()  # Check status-code response from server. If not 200, stop scraping.
            soup = BeautifulSoup(r.content, "html.parser")
            return soup
            break
        except Timeout:
            convert_html(target_url)


def load_index_urls(target_html):
    targetURLs = []

    result = target_html.find("div", class_="menuList_inner").select("a")
    for i in result:
        wordURL = i.get("href")
        targetURLs.append(wordURL)

    return targetURLs


def load_words_title(target_url):
    soup = convert_html(target_url)
    target_urls = []

    terms_table = soup.find("table", class_="term").select("a")
    for i in terms_table:
        target_urls.append(i.get("href"))

    return target_urls


def load_words_details(target_url):
    soup = convert_html(target_url)

    term_title = soup.h1.string
    print(term_title)

    targetWordExplanation = soup.find("div", class_="entryBody").text

    return targetWordExplanation


if __name__ == "__main__":
    main()
