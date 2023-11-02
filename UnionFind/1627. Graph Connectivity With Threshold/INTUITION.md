# Intuition

一開始能想到的是:
把[1,n]範圍city全部拆出合法factors (必須 > threshold), 這樣會有約2*sqrt(n)個因數
如果該cityA 有 a, b, c 3個合法factor, 那麽就會與其他factor有a或b或c的city也連接再一起
並且由於cityA的關係, 擁有a, b, c任一factor的所有城市也都會連接在一起
所以如果從city出發, 會變成找出city的factor, 並把含有這些factor的city連接再一起
=> 會有很多重複的作業

這時其實可以改從factor出發, 也可想成從city出發, factor/city由小到大遍歷
從上述觀察會發現city底下的每個factor都會因為city而連接再一起, 所以反過來說
我們從小到大遍歷的這些city的倍數, 也都是連接再一起的
所以我們由小到大把這些大於threshold的city與其倍數都透過union-find連接在一起的話
在queries的時候就能直接以~O(1)查找
