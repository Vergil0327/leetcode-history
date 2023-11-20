# Intuition

每個人期望的單位基本薪資為: wage[i]/quality[i]
題目要求被挑選的每個人的單位給付薪資必須 >= wage[i]/quality[i]
所以如果我們挑`wage[i]/quality[i]`越大的作為基準, 這樣就能有越多人符合他們的基本薪資條件

所以依照`wage[i]/quality[i]`排序後, 這樣在遍歷時, 當前員工就會是單位基本薪資最高的
所以過往員工會都符合基本薪資的條件
因此這時我們就能在排序後遍歷一遍, 嘗試計算以每個員工作為基準時的所需cost, 在找出全局最小cost

遍歷過程中, 如果要挑出剩下的**k-1**位員工並使得所需cost最小的話
由於total cost = (wage[i]/quality[i]) * k_sum(quality)
所以我們必須前面i-1位員工當中, 挑出前**k-1**位quality最少的員工
=> 所以我們必須維護一個size=k-1的max heap, 持續把較大quality的員工給剔除掉
