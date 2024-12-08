# ---- Strings & Arrays (or rather lists in python) ----

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
    return "".join(chs)

# TODO: install mypy, see how to add types in python
