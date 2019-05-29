import RabinKarp
import plotly.plotly as py
py.sign_in(username='aafham', api_key='ahiHeSFfv5QT5UiymhgH')


malaysiaIO = open('news/text/Malaysia.txt', 'r', encoding='utf-8')
malaysia_text = malaysiaIO.read().lower()
malaysia_text = malaysia_text.replace("\n", " ")
malaysiaIO.close()

jakartaIO = open('news/text/Jakarta.txt', 'r', encoding='utf-8')
jakarta_text = jakartaIO.read().lower()
jakartaIO.close()

manilaIO = open('news/text/Manila.txt', 'r', encoding='utf-8')
manila_text = manilaIO.read().lower()
manilaIO.close()

dhakaIO = open('news/text/Dhaka.txt', 'r', encoding='utf-8')
dhaka_text = dhakaIO.read().lower()
dhakaIO.close()

bandar_seri_begawanIO = open('news/text/Bandar Seri Begawan.txt', 'r', encoding='utf-8')
bandar_seri_begawan_text = bandar_seri_begawanIO.read().lower()
bandar_seri_begawanIO.close()

shanghaiIO = open('news/text/Shanghai.txt', 'r', encoding='utf-8')
shanghai_text = shanghaiIO.read().lower()
shanghaiIO.close()

tokyoIO = open('news/text/Tokyo.txt', 'r', encoding='utf-8')
tokyo_text = tokyoIO.read().lower()
tokyoIO.close()

positive_word = open('wordlist/positivewords.txt', 'r', encoding='utf-8')
positive_text = positive_word.read().lower().split('\n')

negative_word = open('wordlist/negativewords.txt', 'r', encoding='utf-8')
negative_text = negative_word.read().lower().split('\n')


# getting the frequency of positive, negative and neutral words in a text
def wordcount(text):
    total_length = len(text.split())
    count = 0
    positive = 0
    negative = 0

    for pat in positive_text:
        pat = pat.replace(" ", "")
        if RabinKarp.rabin_karp_matcher(pat, text):
            positive = positive + 1
            count = count + 1
    for pat in negative_text:
        pat = pat.replace(" ", "")
        if RabinKarp.rabin_karp_matcher(pat, text):
            negative = negative + 1
            count = count + 1
    # neutral word is equal to the total words in text minus the total count
    # of words that is positive or negative
    neutral = total_length - count
    return positive, negative, neutral


malaysia_pos, malaysia_neg, malaysia_neutral = wordcount(malaysia_text)
# dhaka_pos, dhaka_neg, dhaka_neutral = wordcount(dhaka_text)
# jakarta_pos, jakarta_neg, jakarta_neutral = wordcount(jakarta_text)
# bandar_seri_begawan_pos, bandar_seri_begawan_neg, bandar_seri_begawan_neutral = wordcount(bandar_seri_begawan_text)
# manila_pos, manila_neg, manila_eutralneutral = manila_text
# shanghai_pos, shanghai_neg, shanghai_neutral = wordcount(shanghai_text)
# tokyo_pos, tokyo_neg, tokyo_neutral = wordcount(tokyo_text)

print("Malaysia word count")
print("Positive word: " + str(malaysia_pos) + " word(s)")
print("Negative word: " + str(malaysia_neg) + " word(s)")
print("Neutral word: " + str(malaysia_neutral) + " word(s)")

# Graph
sent_value = ['Positive Word', 'Negative Word', 'Neutral Word']

data = {'x': sent_value, 'y': [malaysia_pos, malaysia_neg, malaysia_neutral
                               ], 'type': 'bar'}
# data = {'x': sent_value, 'y': [positive_frequency, negative_frequency, neutral_frequency], 'type': 'bar'}

layout = {'title': 'The Frequency of Positive and Negative Word',
          'autosize': False,
          'width': 800,
          'height': 700,
          'yaxis': {'title': 'Frequency of Word'},
          'xaxis': {'title': 'Type of Word'}}

py.plot([data], layout=layout)

# # Sentiment & Conclusion
# if positive_frequency > negative_frequency:
#     print('\nThe article is giving positive sentiment')
#     print('The country has positive political situation')
# elif negative_frequency > positive_frequency:
#     print('\nThe article is giving negative sentiment')
#     print('The country has negative political situation')
# else:
#     print('\nThe article is giving neutral sentiment')
#     print('The country has neutral political situation')
#
#
