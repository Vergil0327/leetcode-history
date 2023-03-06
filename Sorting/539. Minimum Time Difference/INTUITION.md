# Intuition

首先想到的是將24小時制全化成分鐘制度

```py
times = []
for tp in timePoints:
    [hr, minute] = tp.split(":")
    times.append(int(hr)*60+int(minute))
```

再來我們將時間排個序然後看相鄰兩個時間間隔幾分
然後把這個想成是個環形數組，首位時間跟末位時間也是相鄰的兩個最近的時間，一樣得查看他們的時間間隔
所以排序後我們在把第一位時間加到最後，這樣等等遍歷相鄰時才不會漏掉比對第一位跟最後一位時間

同時加到最後的同時把他加上`60*24`分鐘，這樣我們就能統一用`times[i+1]-times[i]`來看相鄰的**順時針**間隔時間

```py
times.sort()
times.append(times[0]+60*24)
```

這邊要注意的是兩個時間點，我們必須看有兩種間隔，一種是順時鐘轉，另一種是逆時針轉
順時針的時間間隔為`times[i+1]-times[i]`
逆時針則為`24*60 - times[i+1]-times[i]`

```py
diff = inf
for i in range(len(times)-1):
    a, b = times[i], times[i+1]
    diff = min(diff, min(b-a, 60*24-(b-a)))
```