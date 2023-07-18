# Intuition
see example 1.

words = [cd, f, kl]

目的是要確認suffix有沒有在words裡, 每次我們都從後往前看有沒有存在
```

stream of letters = abcdefghijkl
____________ => abcdefghijkl
 ___________ => bcdefghijkl
  __________ => cdefghijkl
   _________ => defghijkl
    ________ => efghijkl
     _______ => fghijkl
      ______ => ghijkl
       _____ => hijkl
        ____
         ___
          __
           _
```

如果我們建立一個Trie, 將每個word從後往前加入到Trie裡
```
Trie:
d -> c
f
l -> k
```

那這樣我們對於當前的stream of letters就可以一樣從後往前, 藉由Trie來判斷當前的suffix
有沒有存在於Trie裡

另外能直覺想到的還有, 如果當前stream of letters的長度小於每個len(words[i]), 那就能直接返回False.
