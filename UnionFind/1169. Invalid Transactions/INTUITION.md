# Intuition - Union Find

想法是利用O(n^2)遍歷, 將同個人不同城市並且時間間隔小於等於60的不合法transaciton union在一起

之後就遍歷`n`個transaction看:
- 是否有跟其他人union在一起: 亦即`rank[i] > 1`
- 是否`amount > 1000`

將這些挑出來即可, 主框架如下:

```py
for i in range(n):
    name1, t1, amt1, city1= transactions[i].split(",")
    for j in range(n):
        name2, t2, _, city2 = transactions[j].split(",")
        if (name1 == name2 and city1 != city2 and abs(int(t2)-int(t1)) <= 60):
            union(i, j)

res = []
for i in range(n):
    _, _, amount, _ = transactions[i].split(",")
    if rank[find(i)] > 1 or int(amount) > 1000:
        res.append(transactions[i])
```

# Intuition - Array & Hashing (Time-Optimized)

但其實能想得簡單點, 我們將以`name`為key, 將[time, city]放入到hashmap裡
後續一樣遍歷transaction, 並再依據人名遍歷看當前transaction是否有跟其他transaction衝突即可

主框架如下:

```py
for t in transactions:
    name, t1, amount, city = t.split(",")
    t1, amount = int(t1), int(amount)
    if amount > 1000:
        res.append(t)
        continue

    elif name in transactionRecord:
        if any(abs(t2 - t1) <= 60 and city2 != city for t2, city2 in transactionRecord[name]):
            res.append(t)
```