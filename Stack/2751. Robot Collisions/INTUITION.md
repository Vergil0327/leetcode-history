# Intuiion

看了example後的想法是我們可以**分左右然後對position排序**

對posotion排序後總體來看會是這樣
```
-> <- -> -> -> <- <- <- ->
```

如果我們分別用個有序的資料結構來分別儲存往左往右的機器人
那我們可以由左到右依序遍歷往左的機器人
對於left[i]來說, 他第一個撞到的往右機器人可以用`bisect_right-1`來找出index位置

```py
while left:
    p, h, idx = left[0]
    i = right.bisect_right((p, -1, -1))-1
```

如果存在著往右的機器人, i.e. `bisect_right()-1 >= 0`, 那麼:
1. 如果兩邊health相等, 那麼兩邊都移除
2. 如果往右機器人寫比較多, 那麼
   - 往右機器人`right[i].health-1`
   - 移除left[0]
3. 反之, 如果往左機器人寫比較多, 那麼
   - 移除right[i]
   - left[0].health-1

往左機器人一直移動直到左邊沒有任何往右機器人後
這時就可以將left[0]加入到result裡

由上面分析可知, 我們需要一個有序容器來分別儲存往左往右的機器人
再來還需要可以高效率移除element

由於題目constraint有說裡面每個位置都是unique
`- All values in positions are distinct`

所以我們可以用個`SortedSet`來儲存
然後持續遍歷left[0]並用binary search找出right[i]

等到遍歷完所有往左移動的機器人後
在把`right`裡面血量尚存的機器人依序加入到result裡幾可

```py
res = [0]*n

# 遍歷left開始相撞

for _, h, idx in right:
    res[idx] = h
return [v for v in res if v > 0]
```

# Other Solution

上面是比賽一開始想到的方式
但其實我們不需要用到ordered set, 僅需要sorting+stack來追蹤往左往右機器人即可

1. 我們首先對整體的position排序
2. 排序後我們我們開始由左往右遍歷
   1. 我們將moving-right robot加入到stack裡
   2. 當我們遍歷到moving-left robot時, 我們檢查看stack有沒有moving-right robot. 如果有那就開始依照提議相撞並調整血量

最後血量不為0的robot即為答案: `[h for h in healths if h > 0]`