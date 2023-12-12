# Intuition

ex.1 n = 5, sick = [0,4]
children沒有區別, 可以想成children[i] = 1為sick, children[i] = 0為healthy
那麼children = [1,0,0,0,1]

sec 1: 2個kid可以被傳染 [1,*,0,0,1] or [1,0,0,*,1]
sec 2: 一樣有2個kid可以被傳染 [1,1,*,0,1] or [1,1,0,*,1]
sec 3: 只剩1個kid[1,1,*,1,1]
=> 2^(3-1)種sequence

所以如果[1,0,0,0,1,0,0,1]
=> first group: 2^(3-1)
=> second group: 2^(2-1)
=> total: 2^(3-1) * 2^(2-1) = 4 * 2 = 8
=> 先感染一個group後再感染另一個group共有8種方法

但我們也能兩個group交替著進行感染, 1***1xx1
例如: **x*x, *xx**, ...
所以其實就是算他們的interweave subsequence方法數
所以是C(3+2)取3 = 5!/(3! * 2!)

所以如果總共有m個enclosed group, 大小分別是g1, g2, ..., gm
那麼方法數就是(g1*g2*...*gm)/(g1! * g2! *...*gm!)
由於除法不能進行modulo, 所以我們可以用inverse modulo, python有內建api: pow(x, -1, mod)

同時每個group自身又有2^(gm-1)種方法, 這些就再相乘

但要注意[0,0,0,1,...,1,0,0,0]兩側([0:sick[0]], [sick[-1]:]), 雖然能跟其他組一起交替排序
但組內都只有1種選擇