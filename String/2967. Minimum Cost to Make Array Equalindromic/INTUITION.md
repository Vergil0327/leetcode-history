# Intuition

受先, 由於palindromic number <= 10^9
我們可以先將這些給找出來, 然後再從中找出適合的palindromic number

由於是palindromic number, 我們只需要遍歷[1,10^5]然後在鏡像一下即可生成全部合法palindromic number
```py
palindromic = []
for num in range(1, 10**5+1):
    palindromic.append(int(str(num) + str(num)[::-1]))   # even length
    palindromic.append(int(str(num) + str(num)[:-1:-1])) # odd length
palindromic.sort()
```

再來就是看怎麼找出那個適合的palindromic number `X`使得全部nums[i]轉成`X`後cost最少

nums = [X X X X X X X X X X X]
先不管是不是palindromic number, 要使得nums換成相同數字後絕對值差最小
那肯定是將nums[i]轉成中位數
但由於我們要的是**equalindromic**, 也就是這個中位數必須還是palindromic number
所以我們結合兩個條件, 我們要找的就是離中位數最近的palindromic

因此我們將nums排序後找出中位數, 然後再找出離中位數最近的palindromic number
然後再計算他們的cost即可

這邊我們找出palindromic numbers後一樣排序
這樣就能透過binary search找出離中位數最近的位置
我們在該index前後找出有可能是答案的palindromic number後計算cost取最小的即可