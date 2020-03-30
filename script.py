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
                print(load_words_details(a_word))
                time.sleep(600)  # time until loading next term
            else:
                print(words_url)
    else:
        print("Bye")


def convert_html(target_url):
    """
    Load a HTML and format it to HTML.
    :param target_url: All URL used in this scraping tool.
    :return:HTML made by requests and Beautifulsoup4.
    """
    while True:
        try:
            r = requests.get(url=target_url, headers=headers, timeout=1)
            r.raise_for_status()  # Check status-code. If not 200, return error.
            soup = BeautifulSoup(r.content, "html.parser")
        except Timeout:
            time.sleep(600)
            convert_html(target_url)
        else:
            return soup


def load_index_urls(target_html):
    """
     This function loads HTML from https://it-words.jp/ only first.
    :param target_html: https://it-words.jp/
    :return: URL list of term's index
    """
    targetURLs = []

    result = target_html.find("div", class_="menuList_inner").select("a")
    for i in result:
        wordURL = i.get("href")
        targetURLs.append(wordURL)

    return targetURLs


def load_words_title(target_url):
    """
    By using index-URL, this function loads URL each a term.
    :param target_url: An index URL loaded index oad_index_urls function
    :return: A URL list of an index loaded load_index_urls function
    """
    soup = convert_html(target_url)
    target_urls = []

    terms_table = soup.find("table", class_="term").select("a")
    for i in terms_table:
        print(i.text)
        target_urls.append(i.get("href"))

    return target_urls


def load_words_details(target_url):
    """
    This function loads a summary of a term.
    :param target_url: A term's URL
    :return: A term's summary
    """
    soup = convert_html(target_url)

    term_title = soup.h1.string
    if term_title == "ただ今メンテナンス中です":
        targetWordSummary = "ERROR:page maintenance\nFailed to load summary."
    else:
        print(term_title)
        targetWordSummary = soup.find("div", class_="entryBody").text

    return targetWordSummary


if __name__ == "__main__":
    main()
    print("Success")
