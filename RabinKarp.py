# d is the number of characters in the input alphabet
d = 256


def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = pow(d, M-1)

    result = False
    for i in range(M):  # preprocessing
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q
    for s in range(N - M + 1):  # note the +1
        if p == t:  # check character by character
            match = True
            for i in range(M):
                if pat[i] != txt[s + i]:
                    match = False
                    break
            if match:
                result = True
        if s < N - M:
            t = (t - h * ord(txt[s])) % q  # remove letter s
            t = (t * d + ord(txt[s + M])) % q  # add letter s+m
            t = (t + q) % q  # make sure that t >= 0
    return result


def rabin_karp_matcher(pattern, text):
    return search(pattern, text, 101)


txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101  # A prime number
print(search(pat, txt, q))

# This code is contributed by Bhavya Jain
