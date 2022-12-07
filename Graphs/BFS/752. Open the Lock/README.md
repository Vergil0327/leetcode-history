[752. Open the Lock](https://leetcode.com/
problems/open-the-lock/)

`Medium`

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

```
Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
```

Constraints:

- 1 <= deadends.length <= 500
- deadends[i].length == 4
- target.length == 4
- target will not be in the list deadends.
- target and deadends[i] consist of digits only.

<details>
<summary>Hint 1</summary>

We can think of this problem as a shortest path problem on a graph: there are `10000` nodes (strings `'0000'` to `'9999'`), and there is an edge between two nodes if they differ in one digit, that digit differs by 1 (wrapping around, so `'0'` and `'9'` differ by 1), and if *both* nodes are not in `deadends`.
</details>

<details>
<summary>Video Explanation</summary>

[Neetcode](https://www.youtube.com/watch?v=Pzg3bCDY87w)
</details>

<details>
<summary>Hint 1 - Solution</summary>

```go
func openLock(deadends []string, target string) int {
  deadendsMap := map[string]bool{}
  for _, deadend := range deadends {
    deadendsMap[deadend] = true
  }


  visited := map[string]bool{}
  turns := 0
  queue := []string{"0000"}
  for len(queue) > 0 {
    for _, node := range queue {
      queue = queue[1:]

      if _, ok := deadendsMap[node]; ok {
        continue
      }

      if node == target {
        return turns
      }

      if visited[node] {
        continue
      }
      
      visited[node] = true

      for i:=0; i<4; i++ {
        plus1 := string('0' + (node[i]-'0'+1)%10)
        minus1 := string('9' - ('9'-node[i]+1)%10)

        queue = append(queue, node[:i] + plus1 + node[i+1:])
        queue = append(queue, node[:i] + minus1 + node[i+1:])
      }
    }

    turns += 1
  }
    
  return -1
}
```
</details>

<details>
<summary>Solution 2</summary>

如果我們知道起點與終點，那我們可以用雙向BFS來提高效率
用set代替queue方便查詢有沒有交集，雙方交會即結束
由於遍歷過程中不可改變hashset，利用一個temporary hashset儲存下一round的節點

[Bi-direction BFS](https://labuladong.github.io/algo/4/31/110/)
```python
class Solution:
    def wheelLock(self, lock: str):
        res = []
        charArr = list(lock)
        for i in range(len(charArr)):
            ch = charArr[i]
            if ch == '9':
                charArr[i] = '0'
            else:
                charArr[i] = chr(ord(ch)+1 )
            res.append("".join(charArr))
            
            if ch == '0':
                charArr[i] = '9'
            else:
                charArr[i] = chr(ord(ch)-1 )
            res.append("".join(charArr))
            
            charArr[i] = ch

        return res
    
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for dead in deadends:
            visited.add(dead)
        
        # edge case: "0000" in deadend
        if "0000" in visited:
            return -1

        q1, q2 = set(), set()
        q1.add("0000")
        q2.add(target)
        step = 0
        while q1 and q2:
            tmp = set()
            for node in q1:
                if node in visited: continue
                if node in q2: return step

                visited.add(node)
                for nxt in self.wheelLock(node):
                    if nxt not in visited:
                        tmp.add(nxt)
            step += 1
            q1 = q2
            q2 = tmp
        return -1
```
</details>