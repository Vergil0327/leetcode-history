# Intuition

既然是求最短路徑，我們可以想成是Graph然後用BFS進行搜尋
雖然沒有講明右邊界，但推敲一下會發現我們最遠其實就走到`current position - b <= max(maxForbidden, x)`即可，再遠其實回頭也走不到目的地了

由於不可連續往後跳，因此我們的`queue`紀錄位置跟方向兩個訊息
並且一開始就可以把所有forbidden的位置加入到`visited` hashset裡

那這邊要特別注意的是，當初卡住的點也是因為這幾點:

1. 我們`visited` hashset要連方向一起儲存，因為回頭跳的時候即使往前跳抵達過那位置，我們還是有可能回頭的時候需要那個位置，因此不管`queue`或是`visited`都要記錄方向

2. 當初直接用這行`if curr - b > rightLimit: continue`卡在前面，

    ```py
    while queue:
        for _ in range(len(queue)):
            curr, didBackward = queue.popleft()
            if curr == x: return jumps
            if curr - b > rightLimit: continue

            if (curr+a, False) not in visited:
                visited.add((curr+a, False))
                queue.append((curr+a, False))

            if (curr-b, True) not in visited and not didBackward and curr-b>=0:
                visited.add((curr-b, True))
                queue.append((curr-b, True))
    ```

    但這很明顯有個邏輯錯誤，這時我們往後跳的選擇也一起被skip掉了，因此應該為
    
    ```py
    while queue:
    for _ in range(len(queue)):
        curr, didBackward = queue.popleft()
        if curr == x: return jumps

        if curr - b <= rightLimit and (curr+a, False) not in visited:
            visited.add((curr+a, False))
            queue.append((curr+a, False))

        if (curr-b, True) not in visited and not didBackward and curr-b>=0:
            visited.add((curr-b, True))
            queue.append((curr-b, True))
    ```
    超出`rightLimit`不往後跳，但在`curr - b < 0`之前，都可以往回跳