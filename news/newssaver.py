# For the purpose of saving the article in html and txt file only
from News import News

shanghai = "https://www.shine.cn/news/metro/1905275526/"
dhaka = "https://www.dhakatribune.com/bangladesh/dhaka/2019/05/25/dncc-mayor-footpaths-must-be-kept-clear-to-reduce-" \
        "tailbacks"
manila = "https://www.manilanews.net/news/261212570/mayor-on-manobos-return-from-haran-it-my-duty-to-secure-them"
tokyo = "https://japantoday.com/category/business/McDonald's-Japan-ordered-to-pay-¥21-mil-over-improper-labeling"
bandarseribegawan = "https://borneobulletin.com.bn/prince-malik-attends-khatam-al-quran-2/"
jakarta = "https://www.thejakartapost.com/news/2019/05/28/jakarta-councillors-to-visit-riau-islands-to-study-deputy-" \
          "governor-election.html"
malaysia = "https://www.thestar.com.my/tech/tech-news/2019/05/27/the-playdate-console-is-made-in-malaysia/"


def save_html(url, city):
    article = News(url)

    html = article.html()
    page = open('HTML/' + city + '.html', 'w', encoding='utf-8')
    page.write(html)
    page.close()


def save_text(url, city):
    c = News(url)

    with open('text/' + city + '.txt', 'r', encoding='utf-8') as filehandle:
        lines = filehandle.readlines()
    with open('text/' + city + '.txt', 'w', encoding='utf-8') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)


try:
    save_html(shanghai, 'Shanghai')
    save_html(dhaka, 'Dhaka')
    save_html(manila, 'Manila')
    save_html(tokyo, 'Tokyo')
    save_html(bandarseribegawan, 'Bandar Seri Begawan')
    save_html(jakarta, 'Jakarta')
    save_html(malaysia, 'Malaysia')

    save_text(shanghai, 'Shanghai')
    save_text(dhaka, 'Dhaka')
    save_text(manila, 'Manila')
    save_text(tokyo, 'Tokyo')
    save_text(bandarseribegawan, 'Bandar Seri Begawan')
    save_text(jakarta, 'Jakarta')
    save_text(malaysia, 'Malaysia')

    print("Files has been saved!")
except IOError:
    print("ERROR!!")
