# Intuition

x = 000110101110
把x想成bitmask, 我們要做的就逐漸把`0`的部分轉成1, 並且數值由小到大
使得nums[i+1]&nums[i] == x並且nums[i+1]為nums[i]的next greater valid element

那麼nums[0]肯定是從x開始, 我們再來要做的就是操作n-1次, 每次都找下一個next greater

ex. x = 0 0 0 1 1 1 0 0 1 0
next  = 0 0 0 1 1 1 0 0 1 1

next  = 0 0 0 1 1 1 0 1 1 0
next  = 0 0 0 1 1 1 0 1 1 1

next  = 0 0 0 1 1 1 1 0 1 0
next  = 0 0 0 1 1 1 1 0 1 1
next  = 0 0 0 1 1 1 1 1 1 0
next  = 0 0 0 1 1 1 1 1 1 1

...

基本上就是:

next = prev+1 | x => x 想成必須存在的bitmask
那這樣反覆進行到第n-1次即為答案
time: O(n)
但由於n高達10^8 => O(n)會TLE
代表我們只能往log(n)去想, 也就是我們要分配1到各個0位置, 並且一次分配2^i個1's bit

ex1: n=3, x=4=100, output = [4,5,6]
5 0b101
6 0b110

目標在x的所有1位置不動情況下, 去分配n-1個bits
n-1 = 2 = "10" => 相當於我們在x的所有0位置去分配10
x = 1 0 0
n-1 target = 1"10" 

ex2: n = 2, x = 7 = 000111

n-1 = 1 ="1"
n-1 target = 00"1"111

我們要找的是第n-1大的valid element, 相當於n-1的bits分配到所有x的"0"位置
如此一來就清楚了

我們由右往左遍歷64個bits of x (n, x <= 10^8 => log2(10^8) < 27)
其中當x's bit=1時, 我們是不能動的 => skip
當x's bit=0時, 我們就依序分配n-1的bit
