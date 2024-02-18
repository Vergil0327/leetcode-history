# Intuition

brute force:
    
```py
for i in range(n):
    for j in range(i+1, n):
        if words[j].startswith(words[i]) and words[j].endswith(words[i]):
            res += 1
return res
```

數據量高達10^5 => O(n^2) 肯定是不行的
由左到右遍歷, 對於當前的words[i]來說, 他其實是之前遍歷過的單字的isPrefixAndSuffix裡的nums[j]
如果我們能在遍歷的過程中建立一個可以高校查詢prefix or suffix的資料結構的話, 那這題就能解了

查prefix首先想到的是Trie這個資料結構
而suffix也只需要倒過來建立Trie即可
因為條件是必須同時滿足prefix跟suffix, 所以我們以(prefix, suffix)同時作為key加入到trie裡
這樣之後比對就直接比(words[i][0], words[i][-1])有沒有存在, 有的話再看(words[i][1], words[i][-2]), ...
如果一路比到最後都存在, 我們就看Trie裡有多少個word即可, 所以不只需要(prefix[], suffix[j])作為key, 還得紀錄word_count

因此我們只要遍歷過程中持續將words[i]加入到trie裡, 對於當前的words[i]來說
他在加到trie的過程中, 中間遇到的所有word都是他的prefix and suffix, 我們把這些加總起來即可知道對於words[i]來說
在他之前有多少個可以跟他組成合法pair
所以我們遍歷的, 其實是isPrefixAndSuffix定義裡的words[j]
