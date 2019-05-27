import RabinKarp as rmatch
from News import News

f1 = open('wordlist/positivewords.txt', 'r', encoding='utf-8')
f2 = open('wordlist/negativewords.txt', 'r', encoding='utf-8')
positive = f1.read().split('\n')
negative = f2.read().split('\n')

malaysia_url = 'https://www.thestar.com.my/tech/tech-news/2019/05/27/the-playdate-console-is-made-in-malaysia/'
shanghai_url = 'https://www.shine.cn/news/metro/1905275526/'
moscow_url = 'https://www.themoscowtimes.com/2019/05/27/inmate-dies-in-russia-after-being-tortured' \
              '-in-de-facto-murder-activists-say-a65753'
manila_url = 'https://www.manilanews.net/news/261212570/mayor-on-manobos-return-from-haran-it-my-duty-to-secure-them'
nyc_url = 'https://www.nydailynews.com/news/national/ny-unknown-soldier-tomb-flag-honor-washington-storms' \
           '-20190527-g6peddu6mbcrpnbpeiezuhccwe-story.html'
tokyo_url = 'https://japantoday.com/category/business/McDonald\'s-Japan-ordered-to-pay-¥21-mil-over-improper-labeling'
dhaka_url = ''

malaysia_news = News(malaysia_url).get_list()
shanghai_news = News(shanghai_url).get_list()
moscow_news = News(moscow_url).get_list()
manila_news = News(manila_url).get_list()
nyc_news = News(nyc_url).get_list()
tokyo_news = News(tokyo_url).get_list()
# dhaka_news = News(dhaka_url)

malaysia_news_positive, malaysia_news_negative = 0, 0
shanghai_news_positive, shanghai_news_negative = 0, 0
moscow_news_positive, moscow_news_negative = 0, 0
manila_news_positive, manila_news_negative = 0, 0
nyc_news_positive, nyc_news_negative = 0, 0
tokyo_news_positive, tokyo_news_negative = 0, 0

print(len(malaysia_news))
print('\nMalaysia Newspaper\n')

print(News(malaysia_url).title() + '\n')
for word in manila_news:
    for pattern in positive:
        if rmatch.search(pattern, word):
            malaysia_news_positive = malaysia_news_positive + 1
    for pattern in negative:
        if rmatch.search(pattern, word):
            malaysia_news_negative = malaysia_news_negative + 1
print('Positive word count: ' + str(malaysia_news_positive))
print('Negative word count: ' + str(malaysia_news_negative))
