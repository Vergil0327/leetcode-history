# Intuition

首先想到的是:
1. search: 對於某部`movie`, 要找前五小的`price`:
   - 所以想到的是會需要一個hashmap紀錄每個`movie`所在的(price, shop)位置, 這時我們可以用**SortedList**來幫助我們排序, 以迅速找出前五小的movie
   - sl = { movie: SortedList[(price, shop), ...] }
   - 這樣就能以O(1)時間找出前五個價錢

```py
def search(self, movie: int) -> List[int]:        
    return [self.sl[movie][i][1] for i in range(min(5, len(self.sl[movie])))]
```

2. rent(shop, movie) & drop(shop, movie)兩個一起看: 
   1. rent:
      - 單純把(shop, movie)從`sl`中移除, 我們可以直接用sl.remove((price, shop))即可
      - 這時會發現我們必須知道該`shop`裡的`movie`的`price`, 由於每間只會有一個copy => unique, 所以我們在一開始用個**hashmap**來紀錄每家`shop`的每個`movie`的price
        - `self.prices[shop][movie] = price for shop, move, price in entries`
   2. drop:
      - 由於我們要把租出去的`movie`重新加回來, 所以我們需要額外再用一個**hashmap**來紀錄我們在`rent`步驟所租出去的movie
        - 在`rent`步驟中, 把每個租出去的都紀錄下來: `self.rented[shop][movie] = price`
        - 這樣在`drop`這裡時, 就能拿到所有資訊再把該`movie`重新放回`sl`裡以供查詢

```py
def rent(self, shop: int, movie: int) -> None:
    price = self.prices[shop][movie]
    self.sl[movie].remove((price, shop))
    self.rented[shop][movie] = price

def drop(self, shop: int, movie: int) -> None:
    price = self.rented[shop][movie]
    self.sl[movie].add((price, shop))
    del self.rented[shop][movie]
```

3. report: 找出前五便宜的`movie`
   - 跟**search**一樣概念, 我們用**SortedList**來維護一個有序的entries, 裡面每個item為`[price, shop, movie]`
   - 那這樣就能以O(1)時間直接找出前5便宜的movie

```py
def report(self) -> List[List[int]]:
    res = [] # shop, movie
    for i in range(min(5, len(self.rep))):
        _, shop, movie = self.rep[i]
        res.append([shop, movie])
    
    return res
```