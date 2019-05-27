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
        list_of_words = text.split()

        # remove non-alphanumeric characters like ! and &
        word = ''
        list_of_words = [re.sub(r'\W+', '', word) for word in list_of_words]

        return list_of_words

    def title(self):
        return self.article.title

    def html(self):
        return self.article.html
