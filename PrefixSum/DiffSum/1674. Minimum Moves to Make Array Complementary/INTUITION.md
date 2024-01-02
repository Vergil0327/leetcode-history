# Intuition

一個比較好想的是如果我們已知target pair sum, 該如何知道我們需要多少步才能使nums complementary?

nums[i] + nums[n-1-i] = x + y <= [1,limit] + [1,limit] = [2,limit]

1. 當target_pair_sum落在[2,min(x,y)+1): 需要2步
2. 當target_pair_sum落在[min(x,y)+1, x+y): 需要1步
3. 當target_pair_sum等於x+y: 需要0步
4. 當target_pair_sum落在[x+y+1, max(x,y)+limit+1): 需要1步
5. 當target_pair_sum落在[max(x,y)+limit+1:2*limit]: 需要2步

所以對於當前的pair_sum = nums[i] + nums[n-1-i] = x+y
他要變換成其他target_pair_sum所需的步數我們可以看target_pair_sum落在哪個區間來知道當前pair_sum需要幾步才能換過去

而每個pair我們都可以知道這麼一個範圍, 我們可以遍歷n//2個pair來算出這些範圍並疊加起來
如此一來, 我們只要遍歷介於`[2,2*limit]`範圍內所有可能target_pair_sum, 找出所需步數最少的一個即可

至於該怎麼將這些範圍透過程式碼的形式表達出從某段到某段區間的步數是2,1或0?
有點難想, 答案是**difference array**

可以想成:
- diff[2] += 2
- diff[min(x,y)+1] -= 1
- diff[x+y] -= 1
- diff[x+y+1] += 1
- diff[max(x,y)+limit+1] += 1
那這樣就表達出:
- [2,min(x,y)+1)需要步數是2
- [min(x,y)+1, x+y)需要步數是1
- [x+y]需要步數是0
- [x+y+1, max(x,y)+limit+1)需要步數是1
- [max(x,y)+limit+1, ]需要步數是2

再把每個pair_sum所求出的difference array都標記上去
我們就能得到一個疊加所有pair_sum的difference array的difference array
然後在遍歷difference array的範圍[2, 2*limit], 就能知道當前target_sum的所需步數變化, 在找出全局最小的所需步數即可

time: $O(nums.size/2 + 2*limit)$