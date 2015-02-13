#!/usr/bin/env python


import requests
from textblob import TextBlob
from bs4 import BeautifulSoup


URL = 'http://techcrunch.com/2015/02/12/apple-adds-more-security-to-imessage-and-facetime-with-two-factor-authentication/'


def get_content_from_url(url):
    return requests.get(url).text

def get_text_from_html(txt):
    soup = BeautifulSoup(txt)
    article = soup.find('div', class_='article-entry').find('p')
    return article

def main():
    article = get_text_from_html(get_content_from_url(URL))
    content = (' ').join([p.string for p in article])
    an = TextBlob(content)
    print an.sentences


if __name__ == '__main__':
    main()
