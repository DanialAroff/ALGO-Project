import RabinKarp
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in(username='aafham', api_key='ahiHeSFfv5QT5UiymhgH')


malaysiaIO = open('news/text/Kuala Lumpur.txt', 'r', encoding='utf-8')
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


kl_pos, kl_neg, kl_neutral = wordcount(malaysia_text)
dhaka_pos, dhaka_neg, dhaka_neutral = wordcount(dhaka_text)
jakarta_pos, jakarta_neg, jakarta_neutral = wordcount(jakarta_text)
bsb_pos, bsb_neg, bsb_neutral = wordcount(bandar_seri_begawan_text)
manila_pos, manila_neg, manila_neutral = wordcount(manila_text)
shanghai_pos, shanghai_neg, shanghai_neutral = wordcount(shanghai_text)
tokyo_pos, tokyo_neg, tokyo_neutral = wordcount(tokyo_text)

print("Malaysia word count")
print("Positive word: " + str(kl_pos) + " word(s)")
print("Negative word: " + str(kl_neg) + " word(s)")
print("Neutral word: " + str(kl_neutral) + " word(s)")

x = ["Kuala Lumpur", "Dhaka", "Jakarta", "Bandar Seri Begawan", "Manila", "Shanghai", "Tokyo"]
positive_y = [kl_pos, dhaka_pos, jakarta_pos, bsb_pos, manila_pos, shanghai_pos, tokyo_pos]
negative_y = [kl_neg, dhaka_neg, jakarta_neg, bsb_neg, manila_neg, shanghai_neg, tokyo_neg]
neutral_y = [kl_neutral, dhaka_neutral, jakarta_neutral, bsb_neutral, manila_neutral,
             shanghai_neutral, tokyo_neutral]

# Graph
data = [
    go.Histogram(
        histfunc="sum",
        y=positive_y,
        x=x,
        name="Positive words"
    ),
    go.Histogram(
        histfunc="sum",
        y=negative_y,
        x=x,
        name="Negative words"
    ),
    go.Histogram(
        histfunc="sum",
        y=neutral_y,
        x=x,
        name="Neutral words"
    )
]
layout = go.Layout(
    title=go.layout.Title(
        text="Positive, Negative & Neutral Words",
        xref='paper',
        x=0
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Positive & Negative Word Count')
# sent_value = ['Positive Word', 'Negative Word', 'Neutral Word']
#
# data = {'x': sent_value, 'y': [malaysia_pos, malaysia_neg, malaysia_neutral
#                                ], 'type': 'bar'}
# # data = {'x': sent_value, 'y': [positive_frequency, negative_frequency, neutral_frequency], 'type': 'bar'}
#
# layout = {'title': 'The Frequency of Positive and Negative Word',
#           'autosize': False,
#           'width': 800,
#           'height': 700,
#           'yaxis': {'title': 'Frequency of Word'},
#           'xaxis': {'title': 'Type of Word'}}
#
# py.plot([data], layout=layout)


# Sentiment & Conclusion
def sentiment(positive_frequency, negative_frequency, city):
    print("\n" + city.upper())
    if positive_frequency > negative_frequency:
        print('The article is giving positive sentiment')
        print('So the country has positive political situation')
    elif negative_frequency > positive_frequency:
        print('The article is giving negative sentiment')
        print('So the country has negative political situation')


sentiment(kl_pos, kl_neg, "Kuala Lumpur")
sentiment(dhaka_pos, dhaka_neg, "Dhaka")
sentiment(jakarta_pos, jakarta_neg, "Jakarta")
sentiment(bsb_pos, bsb_neg, "bandar seri begawan")
sentiment(manila_pos, manila_neg, "Manila")
sentiment(shanghai_pos, shanghai_neg, "shanghai")
sentiment(tokyo_pos, tokyo_neg, "tokyo")
