# Intuition

沒有什麼高深的算法，就是確認每個區間是不是arithmetic即可

確認方式也很直觀，就是排序再一一確認

但有另外一個方式可以不用排序即可確認，那就是用**Hashset**
我們找出min(interval), max(interval)
那麼每個數的間隔就應該是:max(interval)-min(interval) // (n-1)

將interval內的數全部加入到hashset，在確認是不是每個數都在hashset裡即可

唯一要注意的edge case是，當間隔為零的時候
這時確認min(interval)跟max(interval)有沒有相等即可