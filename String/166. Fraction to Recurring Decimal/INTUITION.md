# Intuition

首先答案先分兩種:

case 1: 整數
首先判斷有沒有餘數，如果沒餘數代表能整除，直接返回整除後的字串

case 2: 浮點數

1. 先判斷正負號
2. 再來就是模擬對餘數的長除法
   -  持續對`餘數 * 10`直到除盡
   -  或者直到餘數重複 -> 代表我們需要一個`hashmap`或`hashset`來記住這項資訊

跳出while-loop後我們會發現我們需要知道餘數重複時的index的位置，這樣我們才知道需要在哪邊加上括號來表示循環小數

因此我們需要的是一個`Hashmap`來記住餘數有沒有重複，若有重複的話是在字串的哪個位置開始重複

# Complexity

- time complexity

$$O(len(answer))$$

- space complexity

$$O(n)$$