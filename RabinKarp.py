
# Python program for Naive Pattern Searching


def search(pat, txt):
    M = len(pat)
    N = len(txt)
    match = False

    # A loop to slide pat[] one by one
    for i in range(N-M + 1):
        # For current index i, check for pattern match
        for j in range(M):
            if txt[i + j] != pat[j]:
                break
            if j == M-1:  # if pat[0...M-1] = txt[i, i + 1, ...i + M-1]
                match = True

    return match


# Driver program to test the above function
txt = "Tetzalipotca"
pat = "pot"
search(pat, txt)

# This code is contributed by Bhavya Jain
