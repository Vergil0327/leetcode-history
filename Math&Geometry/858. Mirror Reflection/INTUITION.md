# Intuition
--- p ---  0
\          |
 \         |
  \        |
   \       |
    \    q |
     \     |
      \    |
       \ p |1
       /
      /

由於入射等於反射
我們可以把鏡像空間延伸, 讓光線再撞到前方鏡子後繼續往同個方向往前
想成光線撞擊左右兩邊鏡子反射並持續往前走
每一次反射都往前`q`距離, 而兩邊每隔`p`距離就有一個接收器
所以當n*q = m*p時, 這時就代表光線撞到了接收器
所以第一個接收器的位置就是p跟q的最小公倍數
然後再透過`n`以及`m`即可判斷光線是撞到哪個接收器
- 當n為奇數時, 光線撞的是對側鏡子 (1或0)
    - 再看m為奇數時 => 1
    - 當m為偶數時 => 0
- 當n為偶數時, 撞的是同側鏡子 (2或發射位置)