# Intuition

**Definition**
`left`
- ready to cross the bridge to pick up the box.
- prioritize with lowest efficiency

`right`
- ready to cross the bridge to put down the box.
- prioritize with lowest efficiency

`picking`
- busy in picking up box.
- prioritize with the process time. choose the most recent one to finish picking up

`putting`
- busy in putting down box.
- prioritize with the process time. choose the most recent one to finish putting down

then, keep sending worker to work until `n` is 0.

# Approach

### Preprocess
- let's process workers their effeciency and put in max heap `left`
- use currTime to know the timeline

### Simulation

- if someone in the `right` ready to cross the bridge, send them to put down the box
    - increment time with `rightToLeft` time

    ```
    currTime += time[-i][2]
    heapq.heappush(putting, [currTime+time[-i][3], eff, i])
    ```

- if someone in the `left` ready to cross the bridge, send them to pick up the box
    - increment time with `leftToRight` time
    - decrement `n`
    ```
    currTime += time[-i][0]
    n -= 1
    heapq.heappush(picking, [currTime+time[-i][1], eff, i])
    ```
- if no one is waiting for crossing the bridge, find one who is about to finish his work.
    - choose from `picking` and `putting`

After `n` becomes 0, there must exist:
- someone waiting to cross the bridge from `right` to `left`
- someone busy in picking up

1. send those who is ready to cross the bridge from `right` to `left` first
    - increment current time by `rightToLeft` time
    - while they are crossing the bridge, those finish picking go to `right`

2. send last few workers who are still picking up boxes back
    - update currentTime to last one's finish time and increment by `rightToLeft` time

Now, every workers are back to left finally...

# Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$
