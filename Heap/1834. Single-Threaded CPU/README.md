[1834. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/description/)

`Medium`

You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

```
Example 1:
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

Example 2:
Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
```

Constraints:

- tasks.length == n
- 1 <= n <= $10^5$
- 1 <= enqueueTimei, processingTimei <= $10^9$

<details>
<summary>Hint 1</summary>

To simulate the problem we first need to note that if at any point in time there are no enqueued tasks we need to wait to the smallest enqueue time of a non-processed element

</details>

<details>
<summary>Hint 2</summary>

We need a data structure like a min-heap to support choosing the task with the smallest processing time from all the enqueued tasks

</details>

<details>
<summary>Solution</summary>

基本思路
同時控制三個變量（開始時間、處理時間、索引）的有序性，並考慮這三個變量優先級：

首先應該考慮開始時間，因為只要到了開始時間，任務才進入可執行狀態；

其次應該考慮任務的處理時間，在所有可以執行的任務中優先選擇處理時間最短的；

如果存在處理時間相同的任務，那麽優先選擇索引最小的。

所以這道題的思路是：

先根據任務「開始時間」排序，維護一個時間線變量 now 來判斷哪些任務到了可執行狀態，然後借助一個優先級隊列 pq 對「處理時間」和「索引」進行動態排序。

利用優先級隊列動態排序是有必要的，因為每完成一個任務，時間線 now 就要更新，進而產生新的可執行任務。

```java
class Solution {
    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        // 把原始索引也添加上，方便后面排序用
        ArrayList<int[]> triples = new ArrayList<>();
        for (int i = 0; i < tasks.length; i++) {
            triples.add(new int[]{tasks[i][0], tasks[i][1], i});
        }
        // 数组先按照任务的开始时间排序
        triples.sort((a, b) -> {
            return a[0] - b[0];
        });

        // 按照任务的处理时间排序，如果处理时间相同，按照原始索引排序
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[1] != b[1]) {
                // 比较处理时间
                return a[1] - b[1];
            }
            // 比较原始索引
            return a[2] - b[2];
        });

        ArrayList<Integer> res = new ArrayList<>();
        // 记录完成任务的时间线
        int now = 0;
        int i = 0;
        while (res.size() < n) {
            if (!pq.isEmpty()) {
                // 完成队列中的一个任务
                int[] triple = pq.poll();
                res.add(triple[2]);
                // 每完成一个任务，就要推进时间线
                now += triple[1];
            } else if (i < n && triples.get(i)[0] > now) {
                // 队列为空可能因为还没到开始时间，
                // 直接把时间线推进到最近任务的开始时间
                now = triples.get(i)[0];
            }

            // 由于时间线的推进，会产生可以开始执行的任务
            for (; i < n && triples.get(i)[0] <= now; i++) {
                pq.offer(triples.get(i));
            }
        }

        // Java 语言特性，将 List 转化成 int[] 格式
        int[] arr = new int[n];
        for (int j = 0; j < n; j++) {
            arr[j] = res.get(j);
        }
        return arr;
    }
}
```
</details>