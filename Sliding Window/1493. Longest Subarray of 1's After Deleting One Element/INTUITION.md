# Intuition

這題是要找一段最長連續的1並且必須得刪除一個數
由於是要找一段區間, 因此可以用sliding window

最多可以刪除一個0的sliding window
那我們就紀錄zero的數目, 如果zero > 1那就得縮小window

在合法狀態下, res = max(res, window.length - 1)
note. `-1` 是因為我們必須得刪除一個數