from newspaper import Article
from bs4 import BeautifulSoup
import re

stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
             'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being',
             'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did',
             "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few',
             'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having',
             'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him',
             'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into',
             'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't",
             'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other',
             'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd",
             "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's",
             'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they',
             "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under',
             'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't",
             'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why',
             "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've",
             'your', 'yours', 'yourself', 'yourselves']


url = 'https://japantoday.com/category/business/McDonald\'s-Japan-ordered-to-pay-¥21-mil-over-improper-labeling'

# untuk download artikel daripada internet
article = Article(url, keep_article_html=True, language='en')
article.download()
article.parse()
article.nlp()

page = open('news/Dhaka.html', 'w', encoding='utf-8')
page.write(article.html)
page.close()


# to extract text from the html. BeautifulSoup untuk dapatkan text drp HTML
soup = BeautifulSoup(article.html, features="lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()

# get text
text = soup.get_text()

# splitting text into list of words
wordslist = text.split()

# remove non-alphanumeric characters like ! and &
word = ''
wordslist = [re.sub(r'\W+', '', word) for word in wordslist]

filtered = filter(lambda x: not re.match(r'^\s*$', x), text)
#
# # count empty elements in the list
# empty_element = 0
# for word in wordslist:
#     if word is '':
#         empty_element = empty_element + 1
#
# # to remove empty elements from the list
# init_length = len(wordslist)  # initial length of the list
# for i in range(len(wordslist)):
#     if i == init_length - empty_element - 1:
#         break
#     if wordslist[i] is '':
#         del wordslist[i]
#         i = i - 1
#
# print(wordslist)
# print('Word count: ' + str(len(wordslist)))

print(text)
