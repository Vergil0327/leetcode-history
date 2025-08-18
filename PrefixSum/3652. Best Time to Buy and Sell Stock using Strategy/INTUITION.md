# Intuition

先計算不做任何**modification**能賺多少
然後再用sliding window去計算出修改後的區間, 加上左右兩側未修改的區間能賺多少
取全局最小即可

所以我們可以先用prefix sum紀錄不做修改時, 每段區間能賺多少
至於sliding window的部分, 一樣透過prefix sum預先處理`prices`, 即可快速計算修改後的區間能賺多少了.

- earned1 = 未修改
- earned2 = min(未修改區間 + 修改區間 + 未修改區間)

answer = min(earned1, earned2)