import RabinKarp
import plotly.plotly as py
import plotly.graph_objs as go
import time
py.sign_in(username='DanialHarith', api_key='NyqKPpTtwYfr4nyZwcYP')

start = time.time()

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


# getting the no. of positive, negative and neutral words in the text
kl_pos, kl_neg, kl_neutral = wordcount(malaysia_text)
dhaka_pos, dhaka_neg, dhaka_neutral = wordcount(dhaka_text)
jakarta_pos, jakarta_neg, jakarta_neutral = wordcount(jakarta_text)
bsb_pos, bsb_neg, bsb_neutral = wordcount(bandar_seri_begawan_text)
manila_pos, manila_neg, manila_neutral = wordcount(manila_text)
shanghai_pos, shanghai_neg, shanghai_neutral = wordcount(shanghai_text)
tokyo_pos, tokyo_neg, tokyo_neutral = wordcount(tokyo_text)

print("\nKuala Lumpur's article word count")
print("Positive word: " + str(kl_pos) + " word(s)")
print("Negative word: " + str(kl_neg) + " word(s)")
print("Neutral word: " + str(kl_neutral) + " word(s)")

print("\nDhaka's article word count")
print("Positive word: " + str(dhaka_pos) + " word(s)")
print("Negative word: " + str(dhaka_neg) + " word(s)")
print("Neutral word: " + str(dhaka_neutral) + " word(s)")

print("\nJakarta's article word count")
print("Positive word: " + str(jakarta_pos) + " word(s)")
print("Negative word: " + str(jakarta_neg) + " word(s)")
print("Neutral word: " + str(jakarta_neutral) + " word(s)")

print("\nBandar Seri Begawan's article word count")
print("Positive word: " + str(bsb_pos) + " word(s)")
print("Negative word: " + str(bsb_neg) + " word(s)")
print("Neutral word: " + str(bsb_neutral) + " word(s)")

print("\nManila's article word count")
print("Positive word: " + str(manila_pos) + " word(s)")
print("Negative word: " + str(manila_neg) + " word(s)")
print("Neutral word: " + str(manila_neutral) + " word(s)")

print("\nShanghai's article word count")
print("Positive word: " + str(shanghai_pos) + " word(s)")
print("Negative word: " + str(shanghai_neg) + " word(s)")
print("Neutral word: " + str(shanghai_neutral) + " word(s)")

print("\nTokyo's article word count")
print("Positive word: " + str(tokyo_pos) + " word(s)")
print("Negative word: " + str(tokyo_neg) + " word(s)")
print("Neutral word: " + str(tokyo_neutral) + " word(s)")

x = ["Kuala Lumpur", "Dhaka", "Jakarta", "Bandar Seri Begawan", "Manila", "Shanghai", "Tokyo"]
positive_y = [kl_pos, dhaka_pos, jakarta_pos, bsb_pos, manila_pos, shanghai_pos, tokyo_pos]
negative_y = [kl_neg, dhaka_neg, jakarta_neg, bsb_neg, manila_neg, shanghai_neg, tokyo_neg]
neutral_y = [kl_neutral, dhaka_neutral, jakarta_neutral, bsb_neutral, manila_neutral,
             shanghai_neutral, tokyo_neutral]

################
#    Graph     #
################
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
    )
    # ),
    # go.Histogram(
    #     histfunc="sum",
    #     y=neutral_y,
    #     x=x,
    #     name="Neutral words"
    # )
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


############################
#  Sentiment & Conclusion  #
############################
def sentiment(positive_frequency, negative_frequency, city):
    print("\n" + city.upper())
    if positive_frequency > negative_frequency:
        print('The article is giving positive sentiment')
        print('So the country has positive political situation')
    elif negative_frequency > positive_frequency:
        print('The article is giving negative sentiment')
        print('So the country has negative political situation')


print("\nConcluding the cities' political situation")
sentiment(kl_pos, kl_neg, "kuala lumpur")
sentiment(dhaka_pos, dhaka_neg, "dhaka")
sentiment(jakarta_pos, jakarta_neg, "jakarta")
sentiment(bsb_pos, bsb_neg, "bandar seri begawan")
sentiment(manila_pos, manila_neg, "manila")
sentiment(shanghai_pos, shanghai_neg, "shanghai")
sentiment(tokyo_pos, tokyo_neg, "tokyo")

end = time.time() - start
print("\nTotal running time: " + str(end) + "s")
