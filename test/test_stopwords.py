import RabinKarp


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

klIO = open('news/text/Kuala Lumpur.txt', 'r', encoding='utf-8-sig')
kl_text = klIO.read().lower()
kl_text = kl_text.replace("\n", " ")
klIO.close()

jakartaIO = open('news/text/Jakarta.txt', 'r', encoding='utf-8-sig')
jakarta_text = jakartaIO.read().lower()
kl_text = kl_text.replace("\n", " ")
jakartaIO.close()

manilaIO = open('news/text/Manila.txt', 'r', encoding='utf-8-sig')
manila_text = manilaIO.read().lower()
kl_text = kl_text.replace("\n", " ")
manilaIO.close()

dhakaIO = open('news/text/Dhaka.txt', 'r', encoding='utf-8-sig')
dhaka_text = dhakaIO.read().lower()
dhaka_text = dhaka_text.replace("\n", " ")
dhakaIO.close()

bandar_seri_begawanIO = open('news/text/Bandar Seri Begawan.txt', 'r', encoding='utf-8-sig')
bandar_seri_begawan_text = bandar_seri_begawanIO.read().lower()
bandar_seri_begawan_text = bandar_seri_begawan_text.replace("\n", " ")
bandar_seri_begawanIO.close()

shanghaiIO = open('news/text/Shanghai.txt', 'r', encoding='utf-8-sig')
shanghai_text = shanghaiIO.read().lower()
shanghai_text = shanghai_text.replace("\n", " ")
shanghaiIO.close()

tokyoIO = open('news/text/Tokyo.txt', 'r', encoding='utf-8-sig')
tokyo_text = tokyoIO.read().lower()
tokyo_text = tokyo_text.replace("\n", " ")
tokyoIO.close()


def word_count(text):
    stop_count = 0
    list_of_words = text.split()
    for word in stopwords:
        if RabinKarp.rabin_karp_matcher(word, text):
            stop_count = stop_count + 1
    return stop_count, len(list_of_words)


kl_stop_count, kl_total_words = word_count(kl_text)
dhaka_stop_count, dhaka_total_words = word_count(dhaka_text)
jakarta_stop_count, jakarta_total_words = word_count(jakarta_text)
bsb_stop_count, bsb_total_words = word_count(bandar_seri_begawan_text)
manila_stop_count, manila_total_words = word_count(manila_text)
shanghai_stop_count, shanghai_total_words = word_count(shanghai_text)
tokyo_stop_count, tokyo_total_words = word_count(tokyo_text)

print("\""+str(kl_stop_count)+"\"")
print(kl_stop_count)
print(dhaka_stop_count)
print(jakarta_stop_count)
print(bsb_stop_count)

