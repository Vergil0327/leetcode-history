# Intuition

很經典的prefix sum + hashmap的問題類型, 用來找符合條件的最長subarray

1. 要找`odd = even`的subarray, 我們可以用他們兩個的**diff**作為key來找出符合的subarray
2. 要找`xor(subarray) = 0`的subarray, 由於xor跟prefix sum有相同性質, 直接先求出prefix xor值後, 以xor為key找出相同的prefix xor值後, 代表兩個位置之間的xor即為0

我們要求的就是同時符合兩個條件的subarray, 所以我們將兩種情況產生一個複合key
丟到hashmap紀錄第一個符合這個key的位置後, 即可找出最長subarray

但別忘記考慮整個array符合條件的情況, 所以我們hashmap必須加上base value:
當整個subarray `odd - diff = 0`, 並且`xor=0`時, 此時index `i = n-1`, 所以base value為:

```py
seen = {(0, 0): -1}
```