from News import News
from newspaper import Article

shanghai = "https://www.shine.cn/news/metro/1905275526/"
dhaka = "https://www.dhakatribune.com/bangladesh/dhaka/2019/05/25/dncc-mayor-footpaths-must-be-kept-clear-to-reduce-" \
        "tailbacks"
manila = "https://www.manilanews.net/news/261212570/mayor-on-manobos-return-from-haran-it-my-duty-to-secure-them"
tokyo = "https://japantoday.com/category/business/McDonald's-Japan-ordered-to-pay-¥21-mil-over-improper-labeling"
bandarseribegawan = "https://borneobulletin.com.bn/prince-malik-attends-khatam-al-quran-2/"
jakarta = "https://www.thejakartapost.com/news/2019/05/27/jokowi-eyes-young-people-in-next-cabinet.html"
malaysia = "https://www.thestar.com.my/tech/tech-news/2019/05/27/the-playdate-console-is-made-in-malaysia/"


def save_news(url, city):
    article = Article(url, keep_article_html=True, language='en')
    article.download()
    article.parse()
    article.nlp()

    page = open(city + '.html', 'w', encoding='utf-8')
    page.write(article.html)
    page.close()


save_news(shanghai, 'Shanghai')
save_news(dhaka, 'Dhaka')
save_news(manila, 'Manila')
save_news(tokyo, 'Tokyo')
save_news(bandarseribegawan, 'Bandar Seri Begawan')
save_news(jakarta, 'Jakarta')
save_news(malaysia, 'Malaysia')
