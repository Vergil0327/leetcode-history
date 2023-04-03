# Intuition

由於店主只能在一個連續為`minutes`時間內行駛權力
所以我們可以維護一個長度為`minutes`的sliding window

首先先把所以非grumpy的分數先加總:
`res = curr = sum(customers[i] for i in range(n) if grumpy[i] == 0)`

再來我們就移動sliding window, 持續更新`curr`
只要window長度不超過minutes, 代表window所代表的時間段內所有grumpy[i]==1的分數都可以加到`curr`上
一但超出window, 那我們就把先前加上去的cumstomers[i] if grumpy[i] == 1給扣回去
如此一來，持續對分數取`res = max(res, curr)`即可找出最大值
