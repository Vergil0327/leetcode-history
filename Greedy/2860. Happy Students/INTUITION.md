# Intuition

- 如果我們選nums[j], 代表必須達成`total select > nums[j]`, 因此所有`<= nums[j]`的nums[i]都必須選
    - 因為如果我們不選任何一個 `<= nums[j]` 的nums[i], 代表我們的total select就必須小於該nums[i], 但是`nums[i] <= nums[j]`, 這會牴觸我們選nums[j]的必要條件`total select > nums[j]`
- 同樣地, 如果我們不選nums[j], total select必須`< nums[j]`, 那代表所有`>= nums[j]`的nums[i]都不能選
    - 不然的話, 我們只要選了任意一個`>= nums[j]`的nums[i], 那代表total select也必須` > nums[i]`, 這樣子我們永遠無法有一個合法的方式使得`total select < nums[j] and total select > nums[i] where nums[j] <= nums[i]`

因此:
1. If a student with nums[i] = x is selected, all the students with nums[j] <= x must be selected.

2. If a student with nums[i] = x is not selected, all the students with nums[j] >= x must not be selected.

由於選了nums[i]之後, 所有<= nums[i]的數都必須全選
因此這時我們可以對nums[i]排個序, 這樣的話對於nums[i]這個位置:

- 如果選了nums[i], nums[:i]必須也全選, 此時的selected = i+1
    - 我們在判斷如果`selected > nums[i+1]`, 那麼當前這個selected group就是合法的 => `res += 1`
    - 如果selected <= nums[i+1], 代表我們必須再多選幾個進來, 由於已經排序, 選進來的必須符合selcted > nums[i]
- 如果不選nums[i], 那麼這在nums[:i-1]就討論過了