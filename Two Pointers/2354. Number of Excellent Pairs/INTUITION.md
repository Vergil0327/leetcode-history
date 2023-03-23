# Intuition

From observation:

X X X X X X X X X
Y Y Y Y Y Y Y Y Y
OR: get every non duplicate 1-bit
AND: get every duplicate 1-bit

num1: 1 1 1 1 1 0 0 0 1 0 1
num2: 0 1 1 1 0 1 1 0 1 1 0
AND: 4
OR: 10
count1(num1) + count1(num2) = 7 + 7 = 14

Therefore:
```
  count1(num1&num2) + count1(num1|num2) >= k
= count1(num1) + count1(num2) >= k
```

既然知道第二個條件其實是兩個數 1 bit 的個數相加的話
並且重複數字其實我們只計算一次，所以我們可以先用一個hashset來去除重複的數

在去除重複後，由於我們關心的是每個數再轉成二進位的時候，每個bit位有多少個1
所以我們先把nums處理一下，數看看他們有多少個1-bit，然後排個序

```py
arr = sorted([bin(num).count("1") for num in SET])
```

處理完後我們可以試著想, 當從i=0開始時, 我們是不是可以找到一個滿足條件的j
由於我們由小到大排過序，所以當我們找到下一個i後, j肯定只會繼續往左移動找到下一個滿足條件的j'
所以整體會是個由兩側往相反方向移動的two pointers

X X X X X X X X X X X
i ->             <- j

X X X X X [X X X X X X]
i       j

每當我們找到一個合適的j, 對於arr[i]來說他等於找到了n-(j+1)個配對
當我們將`i`全部遍歷過一遍, 即可得到答案