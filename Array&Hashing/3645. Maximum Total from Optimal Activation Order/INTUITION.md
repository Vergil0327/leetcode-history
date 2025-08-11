# Intuition

> 條件1: To activate an inactive element at index i, the number of currently active elements must be strictly less than limit[i].

首先想到依照limit[i]來排序, 再依序activate element[j]


> 條件3: After each activation, if the number of currently active elements becomes x, then all elements j with limit[j] <= x become permanently inactive, even if they are already active.

代表limit[i]如果有很多個, 最多只能取limit[i]個, 所以我們取最大的前limit[i]個.
ex. limit[i]=4時, value = 1,2,3,4,5,6,7,8
由於取4個後, 根據條件3, 當limit[i] <= activated values時會永久inactive
因此, 對於每個limit[i] group, 最多取`min(limit[i], len(group[limit[i]]))`個

並且由於取到limit[i]時, 之前所有取過的都會變成inactive(但分數已經加總上去)

ex. 取到limit[i]=5時, 最多可以取到5個
取的過程不管總共的activated values有到五個還是沒有
取過的那些(limit[i] < 5)都會變成inactive而不計算在**currently** activated values裡
所以對於每個limit[i] group, 我們都可以取到最多合法數量min(limit[i], len(group[limit[i]]))個

代表我們無需考慮先前已經取過的activated values數量

所以最終我們僅需要遍歷每個limit[i] group, 然後把最大的前`min(limit[i], len(group[limit[i]]))`個數加總到最終答案即可