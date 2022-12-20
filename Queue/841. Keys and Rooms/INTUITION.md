# Intuition

Simulate process by using **queue**

- enter `room0`, take all the keys, then visit unvisited rooms:
        
    append to queue, consume them, then find next unvisited ones

# Complexity
- Time complexity:
$$O(ROOMS + KEYS)$$

- Space complexity:
$$O(ROOMS)$$
