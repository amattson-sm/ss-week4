import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # get user input
    url = input("Enter a URL to scrape: ")

    # get page data
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # search soup
    views = soup.find("meta", itemprop="interactionCount")['content']

    # return value
    print(views)
