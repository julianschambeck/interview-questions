
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

# TODO: install mypy, see how to add types in python

