
# Strings & Arrays (or rather lists in Python)

# 1.1 check if all chars in string are unique
# time complexity should be O(N), i.e. runs in linear time
def isunique(s):
    seen = {}
    for ch in s:
        if ch in seen: return False
        seen[ch] = 1
    return True

# 1.2 check if one string is permutation of the other
# time is again O(N)
def ispermut(s, other):
    if len(s) != len(other): return False
    m = {}
    for c in s: m[c] = m.get(c, 0) + 1
    for c in other:
        if m.get(c) is None: return False
        m[c] = m.get(c, 0) - 1
        if m[c] < 0: return False

    if sum(m.values()) != 0: return False
    return True 

# 1.3 replace spaces in string with %20
# again O(N)
def URLify(s):
    for idx, c in enumerate(chs:=list(s)):
        if chs[idx] == " ": chs[idx] = "%20"
    return ''.join(chs)

# 1.4 check if string is a permutation of a palindrom
# should be O(N)
def ispalindrom_permut(s):
    s = s.replace(" ", '').lower()
    # we count '' as palindrom
    if len(s) == 0 or len(s) == 1: return True

    # cbaba is permut of abcba, thus should be True
    counts = {}
    for c in s: counts[c] = counts.get(c, 0) + 1
    # each char needs to have a counterpart, abba -> aa bb
    if len(s) % 2 == 0: return all(cnt % 2 == 0 for cnt in counts.values())
    # if s len is odd, only one char can occur once
    return list(counts.values()).count(1) == 1 and all(cnt in {1,2} for cnt in counts.values())

# 1.5 check if other is one (or 0) edits (insert, replace or delete) away from s
# is again O(N), linear time
def one_away(s: str, other: str):
    if abs(len(s) - len(other)) > 1: return False
    if len(s) == len(other): return sum([a != b for a, b in zip(s, other)]) in {0, 1}

    # swap to handle delete as insert
    if len(s) > len(other):
        s, other = other, s
    # handle insertion, e.g. "pales" to "palbes" requires one insert
    inserted = False
    if len(s) < len(other):
        for i, c in enumerate(s):
            if other[i+1 if inserted else i] != c:
                if inserted: return False
                inserted = True
    return True

# 1.6 compress (here squeeze) string with character counts, e.g. aabbbc -> a2b3c1
# Notes: lowercase and uppercase characters allowed, nothing else,
# is compressed string not shorter than original one, return the latter.
# should be O(N) because we go through each character once, despite having an inner loop
def squeeze_with_counts(s: str):
    out = ""
    i = 0
    while i < len(s):
        cnt = 1
        curr = s[i]
        j = i+1
        while j < len(s) and s[j] == curr:
            cnt += 1
            j += 1

        out += curr + str(cnt)
        # implicitly fallbacks to i+=1 if inner loop is not entered, cute
        i = j
        cnt = 1

    ret = out if len(out) < len(s) else s
    return ret
