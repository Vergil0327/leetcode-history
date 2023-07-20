# Intuition

看起來是個模擬題
taskQueue -> assign task to free server with (smallest weight, smallest index)
=> 這邊會需要一個min heap, idleServers, 儲存[servers[i], i]代表閒置的servers

再來就持續把tasks加入到taskQueue裡, 一但min heap不為空, 便指派task到該server
這邊我們在用一個min heap, processed, 來代表處理中的server, 我們儲存server跟預計完成的時間[finished_t, [servers[i], i], j] where finished_t = t + tasks[i]
這邊應該要用min heap以時間作為key, 時間少的會優先完成, 完成後我們就更新我們的ans當前時間t = finished_t, 然後處理的任務是j

所以我們遍歷task並模擬整個流程即可, tasks本身就是taskQueue
1. 首先先檢查processed queue裡有沒有任何finished_t <= t的任務, 有的話完成並紀錄ans[j]並把server放回idle裡
2. 
   1. 如果有idle servers, 那就發派任務並且時間`t += 1`
   2. 如果沒有idle servers, 那就完成processed queue裡的一個任務, 然後一樣紀錄ans[j]並把server放回idle裡, 同時更新t = finished_t
3. 等到全部任務都發派出去後, 把processed queue裡未完成的指派任務依序完成並更新ans[j]即可

```py
def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        taskQueue = deque()
        idleServers = [[servers[i], i] for i in range(len(servers))] # servers[i], i
        heapq.heapify(idleServers)

        processed = []
        t = i = 0
        m = len(tasks)
        res = [-1] * m
        while i < m:
            while processed and processed[0][0] <= t:
                finished_t, server, task = heapq.heappop(processed)
                res[task] = server[1]
                heapq.heappush(idleServers, server)

                    
            if idleServers:
                server = heapq.heappop(idleServers)
                heapq.heappush(processed, [t+tasks[i], server, i])
                i += 1
                t += 1
            else:
                finished_t, server, task = heapq.heappop(processed)
                res[task] = server[1]
                heapq.heappush(idleServers, server)
                t = finished_t

        while processed:
            finished_t, server, task = heapq.heappop(processed)
            res[task] = server[1]

        return res
```

**但這卻會卡在某個case上**
ex. servers = [3,3,2], asks = [1,2,3,2,1,2]

原因出在那個`t += 1`, 我們一個時間只發派一個任務
但這題卻是允許multi-processing的, 也就是同個時間點可以發派多個任務出去
關鍵在於我們沒讀清楚題意:
"You will be able to process the jth task starting from the jth second beginning with the 0th task at second 0. "
"If multiple tasks need to be assigned, assign them in order of increasing index."

所以如果有多個任務在task queue裡, 並且有多個idle servers, 那我們就可以在同個時間點處理多個task (multi-processing)
1. 因此我們還是需要一個task queue, 然後我們遍歷j, task from tasks並持續加入到taskQueue裡. 在t=j時我們可以發派j-th task
2. 將加入task queue後先檢查processed queue, 所有finished_t <= j的server應已完成任務並重新加回到idleServers裡
3. 對於當前j-th task, 如果有idle servers, 那就指派任務並加入到processed queue裡並更新ans[j] = server_idx

等到全部task都加入到task queue裡後, 應該會剩下未指派的taskQueue以及忙碌中的process queue
這時就持續完成process queue並指派taskQueue裡的任務給server, 直到完成所有taskQueue裡的任務
