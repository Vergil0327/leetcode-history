# Intuition

words的數據規模`<=14`
代表我們每個words的subset組共有 2^14=16384 種選擇

我們可以將能用的letters存成hashmap然後進行backtracking
- pick or not pick
  - pick: += score where score = sum(# of words[i][j] * score[ch])

我們提前將每個words[i]處理成一個size最多為26的hashmap. {character: count}

那麼最終backtracking的time complexity為: O(2^n * 26)