# Intuition

直覺想到:

```py
case_insensitive = defaultdict(list)
word_dict = {}
vowel_err = {}
for i, word in enumerate(wordlist):
    word_dict[word] = i
    wordlow = word.lower()
    case_insensitive[wordlow].append(i)
    
    vowel_err[wordlow] = i
    queue = deque([wordlow])
    vowels = {"a", "e", "i", "o", "u"}
    while queue:
        s = queue.popleft()
        for j in range(len(s)):
            if s[j] in vowels:
                for v in vowels:
                    nxt = s[:j] + v + s[j+1:]
                    if nxt not in vowel_err:
                        vowel_err[nxt] = i
                        queue.append(nxt)

res = []
for q in queries:
    if q in word_dict:
        res.append(q)
    elif (ql := q.lower()) in case_insensitive:
        res.append(wordlist[case_insensitive[ql][0]])
    elif (ql := q.lower()) in vowel_err:
        res.append(wordlist[vowel_err[ql]])
    else:
        res.append("")
return res
```

但有更聰明的作法去對應vowel error:

由於我們可以任意更換vowel, 所以我們可以將vowel表示成一個任意的佔位符(placeholder):

ex. "abc" = "#bc" => 它可以代表"Abc", "ebc", "Ebc", "ibc", "Ibc", "obc", "Obc", "ubc", "Ubc"
如此一來, 我們便不需要BFS去找出所有可能vowel error