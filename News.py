from bs4 import BeautifulSoup
from newspaper import Article
import re


class News:
    def __init__(self, url):
        self.url = url
        self.article = Article(self.url, keep_article_html=True, language='en')
        self.article.download()
        self.article.parse()
        self.article.nlp()

    def get_text(self):
        """
        get all the text in the article from the html
        :return: text
        """
        soup = BeautifulSoup(self.article.html, features="lxml")
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.text

        return text

    def get_list(self):
        """
        get the list of words inside the article
        :return: list of words from the article
        """
        soup = BeautifulSoup(self.article.html, features="lxml")
        for script in soup(["script", "style"]):
            script.extract()

        # get text
        text = soup.get_text()

        # splitting text into list of words
        wordslist = text.split()

        # remove non-alphanumeric characters like ! and &
        word = ''
        wordslist = [re.sub(r'\W+', '', word) for word in wordslist]

        # count empty elements in the list
        empty_element = 0
        for word in wordslist:
            if word is '':
                empty_element = empty_element + 1

        # to remove empty elements from the list
        init_length = len(wordslist)  # initial length of the list
        for i in range(len(wordslist)):
            if i == init_length - empty_element - 1:
                break
            if wordslist[i] is '':
                del wordslist[i]
                i = i - 1

        return wordslist

    def title(self):
        return self.article.title

    def html(self):
        return self.article.html
