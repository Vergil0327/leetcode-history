[630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

`Hard`

There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

```
Example 1:
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Example 2:
Input: courses = [[1,2]]
Output: 1

Example 3:
Input: courses = [[3,2],[4,3]]
Output: 0
```

Constraints:

- 1 <= courses.length <= 10^4
- 1 <= durationi, lastDayi <= 10^4

<details>
<summary>Hint 1</summary>

During iteration, say I want to add the current course, currentTotalTime being total time of all courses taken till now, but adding the current course might exceed my deadline or it doesn’t.

1. If it doesn’t, then I have added one new course. Increment the currentTotalTime with duration of current course.
</details>

<details>
<summary>Hint 2</summary>

2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.
* No harm done and I might have just reduced the currentTotalTime, right?
* What preprocessing do I need to do on my course processing order so that this swap is always legal?
</details>

<details>
<summary>Solution 1</summary>
[article here](https://leetcode.com/problems/course-schedule-iii/solution/)

```java
public class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        Integer[][] memo = new Integer[courses.length][courses[courses.length - 1][1] + 1];
        return schedule(courses, 0, 0, memo);
    }
    public int schedule(int[][] courses, int i, int time, Integer[][] memo) {
        if (i == courses.length)
            return 0;
        if (memo[i][time] != null)
            return memo[i][time];
        int taken = 0;
        if (time + courses[i][0] <= courses[i][1])
            taken = 1 + schedule(courses, i + 1, time + courses[i][0], memo);
        int not_taken = schedule(courses, i + 1, time, memo);
        memo[i][time] = Math.max(taken, not_taken);
        return memo[i][time];
    }
}
```

Time complexity : O(n*d). 
memomemo array of size nxd is filled once. Here, n refers to the number of courses in the given coursescourses array and d refers to the maximum value of the end day from all the end days in the coursescourses array.

Space complexity : O(n*d). memomemo array of size nxd is used.
</details>

<details>
<summary>Solution 2</summary>

```java
public class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        PriorityQueue < Integer > queue = new PriorityQueue < > ((a, b) -> b - a);
        int time = 0;
        for (int[] c: courses) {
            if (time + c[0] <= c[1]) {
                queue.offer(c[0]);
                time += c[0];
            } else if (!queue.isEmpty() && queue.peek() > c[0]) {
                time += c[0] - queue.poll();
                queue.offer(c[0]);
            }
        }
        return queue.size();
    }
}
```
</details>