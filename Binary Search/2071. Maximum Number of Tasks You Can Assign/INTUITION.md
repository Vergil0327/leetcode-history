# Intuition

tasks可以優先選小的來盡可能分配，看最多能選幾件tasks
但要分配給哪個worker或是worker+pill並沒有優劣
example
tasks = [5,9,8,5,9]
workers = [1,6,4,2,6], pills = 1, strength = 5
ans = 3

所以至少可以先對tasks排序，然後來看我們最多可以選幾件

那排序後tasks越多肯定越難達成，並且也有單調性質，如果能完成最簡單的5件，那麼4件也肯定可以
所以我們可以用binary search去猜最多能做幾件

那再來就是看我們如何去查看能不能完成了

假設我們當前需要完成最簡單的`k`件task
我們肯定是從最難的先來看，如果能被完成，那就分配下去，畢竟是肯定要完成這個task也肯定要有人去做的

如果不行，我們再來考慮誰來吃pill然後完成
吃pill的這個人，最佳解肯定是吃了之後能剛剛好完成的人，這樣最物盡其用
而這個貪心思想可以透過對workers排序後，以二分搜尋來找到

由於找到後我們比需把當前這個worker從workers中剔除，因此我們可以用Sorted List來完成
以C++來說就是multiset，Java就是Treemap

因此整個check function邏輯如下:

```
tasks.sort()

def check(numTask, pills):
    把 worker 加到SortedList裡
    
    task: 從後往前遍歷task
        如果SortedList[-1] >= task:
            代表能被完成，移除SortedList[-1]，然後繼續看下一個task
        如果不行那就看還有沒有pill:
            i = SortedList.bisect_left(task-strength)
            如果找不到worker (i == len(SortedList))，代表無法完成，返回False
            如果找到，那就把i-th worker從SortedList移除，並且pills-1
        如果沒人能完成也沒pill
            那就返回False
    遍歷完後代表都能完成，返回True
```