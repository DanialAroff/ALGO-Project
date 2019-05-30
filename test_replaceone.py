import RabinKarp as rk
text = "The the guy has the money money on it but drop it in the last day"
pat = "the"

print(text)
if rk.rabin_karp_matcher(pat, text):
    text = text.lower().replace("the ", "", 1)
print(text)


print(rk.rabin_karp_matcher("the", "The"))
