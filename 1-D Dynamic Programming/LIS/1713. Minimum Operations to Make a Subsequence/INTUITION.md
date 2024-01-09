# Intuition

target = [A B C D]
arr = [X X X X A B X A X D]

minimum number of operations needed to make target a subsequence of arr = len(target) - length of the longest subsequence of target in arr

target2id = { target[i]: i }
target[i]的index `target2id[target[i]]`代表他們的順序, 將這個index視為id來看的話, 這target_id順序會是由小到大遞增
而我們要找的就是在arr中的最長的subsequence of target, 以他們的id來看的話, 就是在arr中找一個最長遞增子序列(LIS) of target_id
那既然是要找LIS (longest Increasing Subsequence), 我們可以用nlogn的時間來找到(binary search + greedy)

所以想法是將distinct target[i]用他們的index作為id代替, 維護一個LIS of target_id
那最終答案就是: `len(target) - len(LIS)`

所以回顧一下, 這題最重要的突破口就是: 

> target[i]是distinct的, 所以他們的index可以作為ID來代表他們的順序位置
> 如此一來, 就可以轉成維護一個LIS of ID