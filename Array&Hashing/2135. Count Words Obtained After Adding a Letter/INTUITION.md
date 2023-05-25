# Intuition

這題的第二格操作說可以任意排序, 這提示我們字符順序並不重要
所以我們可以用一個長度為26的array來紀錄每個字母出現的次數, 並用這個array來代表當前詞

所以我們只要遍歷`targetWords`, 然後每個處理成一個長度為26的`footprint` array後
我們再根據操作一回過頭找當前target能不能透過操作而得到即可

根據操作一可知, startWord跟targetWord會只差一個字符, 所以我們遍歷targetWord的footprint時
只要看到出現次數為1的字母, 我們便檢查看看有沒有存在在`startWords`裡即可

這樣的時間複雜度為$O(26n)$

# Optimization

根據constraint 4: No letter occurs more than once in any string of startWords or targetWords.

可知道每個字符出現的次數最多就一次, 所以其實用bitmask即可