# Intuition

由於我們可以同時跑任意多個task，因此先前該時段如果已經有running task，後面就可以一起平行處理
所以我們要盡可能讓每個task有最大的overlap

```
sort by end_time

---------
-----------
   --------
      -----
---------------
    ---------------
   ------------------
              -------
                  ---
---------------------
```

所以首先我們對每個task的end time排序
那對於每個task的時間範圍[start, end]來說，最佳策略就是盡可能把task排在越後面越好
這樣就能盡可能讓task在時間上有重疊，以達到task最大的重複利用

那如果同樣結果對start time做排序呢?
```
同樣結果sort by start_time

---------
-----------
---------------
---------------------
   --------
   ------------------
    ---------------
      -----
              -------
                  ---
```

會發現他們最大重疊區域會落在中間，並不好找
如果我們優先把task排在越靠前的位置，後面也享受不到好處, 因為實際上如果對start_time做排序
是要將task排在區間中間的某個位置才會有最大重疊



- 如果是要找**the minimum number of intervals to cover whole range**, 那就對start_time做排序
- 如果是要找**the maximum number of intervals that are non-overlapping**, 那就對end_time做排序

由於這題是要盡可能讓overlapping越多越好，也就是盡可能讓non-overlapping interval越少越好
所以我們可以對end_time做排序，然後盡可能地把task排在後頭讓他們盡可能重疊