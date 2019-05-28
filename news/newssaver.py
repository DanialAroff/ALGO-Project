from News import News
from newspaper import Article

shanghai = "https://www.shine.cn/news/metro/1905275526/"
dhaka = ""
manila = "https://www.manilanews.net/news/261212570/mayor-on-manobos-return-from-haran-it-my-duty-to-secure-them"
tokyo = "https://japantoday.com/category/business/McDonald's-Japan-ordered-to-pay-¥21-mil-over-improper-labeling"
bandarseribegawan = ""
jakarta = ""
malaysia = "https://www.thestar.com.my/tech/tech-news/2019/05/27/the-playdate-console-is-made-in-malaysia/"


def save_news(url, city):
    article = Article(url, keep_article_html=True, language='en')
    article.download()
    article.parse()
    article.nlp()

    page = open('news/' + city + '.html', 'w', encoding='utf-8')
    page.write(article.html)
    page.close()
