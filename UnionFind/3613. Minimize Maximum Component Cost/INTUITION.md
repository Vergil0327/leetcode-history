# Intuition

反過來想, 一開始有n個節點, 也就是n個connected components
再來Greedy方式想:

我們從`weight`最小的邊開始, `weight`由小到大相連, 每成功連一次, `connected components+1`
並且由於我們邊是由小到大, 所以每相連一次, maximum cost會增加, 為了獲得minimum possible value of the maximum cost
一旦形成k個connected componenets, 後續剩下的較大的邊都是我們要移除的對象

因此連過的邊的最大值即為我們所求的最小值