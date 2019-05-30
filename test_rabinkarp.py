import RabinKarp
import time

start = time.time()

malaysiaIO = open('news/text/Kuala Lumpur.txt', 'r', encoding='utf-8')
malaysia_text = malaysiaIO.read().lower()
malaysia_text = malaysia_text.replace("\n", " ")
malaysiaIO.close()

dhakaIO = open('news/text/Dhaka.txt', 'r', encoding='utf-8')
dhaka_text = dhakaIO.read().lower()
dhaka_text = dhaka_text.replace("\n", " ")
dhakaIO.close()

positive_word = open('wordlist/positivewords.txt', 'r', encoding='utf-8')
positive_text = positive_word.read().lower().split('\n')
negative_word = open('wordlist/negativewords.txt', 'r', encoding='utf-8')
negative_text = negative_word.read().lower().split('\n')

positive = 0
negative = 0

print(malaysia_text)
for pat in positive_text:
    pat = pat.replace(" ", "")
    if RabinKarp.rabin_karp_matcher(pat, malaysia_text):
        positive = positive + 1
for pat in negative_text:
    pat = pat.replace(" ", "")
    if RabinKarp.rabin_karp_matcher(pat, malaysia_text):
        negative = negative + 1

neutral = len(malaysia_text.split()) - positive - negative

print(positive_text)

print("Malaysia word count")
print("Positive word: " + str(positive) + " word(s)")
print("Negative word: " + str(negative) + " word(s)")
# print("Neutral word: " + str(neutral) + " word(s)")

end = time.time() - start
print("\nRunning time: " + str(end) + "s")
