# Intuition

從example 1可發現，我們要找的是一段subarray，其XOR和為0
例如[4,4] => binary form = [100, 100]
例如[3,1,2] => binary form = [11, 1, 10]

example 1.
nums = [4,3,1,2,4]
   100 -> 4
    11 -> 3
     1 -> 1
    10 -> 2
   100 -> 4

那對於要找一段和為0的subarray, 我們可以試著用prefix sum去想
如果我們把example 1轉成prefix sum, 可得:
prefix sum = [100 111 110 100 000]

其中可發現，當presum為0時，或是當前的presum[i]之前出現過時，代表我們找到了一段subarray其XOR和為零
[100 111 110 100] 000
 100         100 -> 前面有一段subarray XOR和為100，現在又找了一個subarray XOR和為100 -> 相減為0

[100 111 110 100 000]
                 000

所以我們可以用一個hashmap去紀錄有多少個presum[i]
每當我們找到相同的presum[i]，就代表找到多少個相減為零的subarray

由於presum[0]本身已經是一個合法的subarray，所以我們hashmap的base case為
hashmap[0] = 1

這樣每當找到一個已經存在於hashmap的presum[i]，就代表找到hashmap[presum[i]]個subarray