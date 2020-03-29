import requests
from bs4 import BeautifulSoup
import time

# header
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}

# To load index
primary_link = "https://it-words.jp/"


def main():
    start_script = input("Do you start scraping?[Y/n]")
    if start_script == "" or start_script == "y" or start_script == "Y":
        all_target_URLs = load_index_urls(convert_html(primary_link))
        for index_url in all_target_URLs:
            # A,B,C...9 のワードのリンク一覧を取得
            # index_url = https://it-words.jp/p/i-a.html
            print(index_url)
            words_url = load_words_title(index_url)  # https://A-AUTO, A2DP, ...
            for a_word in words_url:
                print(load_words_details(a_word))
                time.sleep(3)

    else:
        print("Bye")


def convert_html(target_url):
    r = requests.get(url=target_url, headers=headers)
    r.raise_for_status()  # Check status-code response from server. If not 200, stop scraping.
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def load_index_urls(target_html):
    targetURLs = []

    result = target_html.find("div", class_="menuList_inner").select("a")
    for i in result:
        wordURL = i.get("href")
        targetURLs.append(wordURL)
        # time.sleep(5)
    return targetURLs


def load_words_title(target_url):
    soup = convert_html(target_url)
    target_urls = []

    terms_table = soup.find("table", class_="term").select("a")
    for i in terms_table:
        target_urls.append(i.get("href"))
        # time.sleep(5)
    return target_urls


def load_words_details(target_url):  # https://...A-AUTO... .html
    soup = convert_html(target_url)

    term_title = soup.h1.string
    print(term_title)

    # print(soup.find("div", class_="entryBody")) #  <p>...</p>
    targetWordExplanation = soup.find("div", class_="entryBody").text
    return targetWordExplanation


if __name__ == "__main__":
    main()
