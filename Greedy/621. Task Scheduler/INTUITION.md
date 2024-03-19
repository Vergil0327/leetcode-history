# Intuition

模擬整個情境

1. 優先使用high frequency (greedy) => 可以用priority queue
2. 紀錄前個當前字母的index => 未使用過或是間隔 i - prevIdx > n, 那就可以用當前字母
3. 遍歷完全部仍無適用task => 那就idle

time: O((tasks.size + idle) * log(26))

# Optimized

如果我們有四種Task: A, B, C, D, E
其中他們的frequency分別是: maxFreq, maxFreq, freqC, freqD where freqC, freqD, freqE < maxFreq

也就是出現最多次的character是X跟Y, 皆為maxFrequency
任務分配上肯定是優先使用X跟Y, 並且每個X跟X之間, Y跟Y之間要相隔**n**個tasks
相當於我們有maxFreq個rows, 並且rows.size至少為`n+1`, 圖形化後如下
那這樣肯定是個最優的合法解, 每個字母距離下個自己間隔都為`n`

```
{X Y .....} => size = n+1
 X Y .....
 X Y .....
 X Y .....
 X Y ..... 
 X Y .....
 X Y .....
 X Y 
```

那再來我們就**從上往下**, **從左往右**把idle的位置"."填充上task, 那這樣整體每個task都會間隔`n`

```
{X Y C D...} => size = n+1
 X Y C D...
 X Y C D...
 X Y C D...
 X Y C E... 
 X Y C E...
 X Y C ....
 X Y 
```

如果最後未填充完, 那就是所有的"."都得填充idle, 整體所需時間為: **(maxFreq-1) * n + # of maxFreq**

那如果tasks多過`n+1`呢? 那就是繼續往後填
最終所需時間就是`tasks.size`

```
{X Y C DXXXY} => size > n+1
 X Y C DXXXY
 X Y C DXXXY
 X Y C DXXXY
 X Y C EXXX 
 X Y C EXXX
 X Y C XXXX
 X Y 
```

由於兩種情況只會擇一出現, 最終答案就是**max((maxFreq-1) * (n+1) + # of maxFreq, tasks.size)**

time complexity: $O(tasks.size)$