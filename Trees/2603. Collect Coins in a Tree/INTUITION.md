# Intuition

首先我們可以觀察出最外圍的葉子節點如果本身沒有coin的話, 我們是絕對不需要走到的
因為在走到之前就已經離其他帶有coin的葉子節點前兩步即收集完全部coin

所以首先我們可以從每個不帶有coin的leaf node開始
由外往內把這些節點從這棵樹中移除掉

p.s. 這邊要注意的是，我們要一路走到底，如果移除後的leaf node仍然不帶有coin, 我們要繼續把所有不帶有coin的leaf node全部移除

**這樣最後會剩下一顆葉子節點都帶有coin的樹**

那棵樹就會像是example 1的樣子，我們需要走的節點就是刨除掉從剩下帶有coin的leaf node往回走兩步後剩下的節點數

所以我們可以用類似topological sort的概念
我們把這棵樹從最外面的leaf node開始刨除掉兩個節點後
我們看剩下的節點數有多少

每當我們刨除掉leaf node，我們就把他們的indegree設為0
這樣最後剩下的節點就是那些indegree >= 1的節點

如下所示，如果最後剩下五個節點，那我們要走的步數就是他們的邊的個數乘2

ex. n = 5 -> min steps = (5-1)*2
X - X - X
        |
    X - X
        

# Complexity

- time complexity

$$O(n)$$

雖然topological sort的時間複雜度為(E+V), 但由於這是顆樹
所以邊的個數為常數2, 因此時間複雜度為O(n)