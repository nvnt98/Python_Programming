# chapter8.py
word = "mississippi"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)  # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# Views (dynamic)
print(freq.keys())     # dict_keys([...])
print(freq.items())    # dict_items([...])

# setdefault for grouping
groups = {}
for ch in word:
    groups.setdefault(ch, []).append(ch)

# defaultdict for cleaner counting/grouping
from collections import defaultdict
cnt = defaultdict(int)
for ch in word:
    cnt[ch] += 1

anagrams = defaultdict(list)
for w in ["eat", "tea", "ate", "bat"]:
    anagrams["".join(sorted(w))].append(w)
print(dict(anagrams))
