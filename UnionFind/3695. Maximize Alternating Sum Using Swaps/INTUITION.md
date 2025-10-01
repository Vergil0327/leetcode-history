# Intuition

**Core Insight**

1. The key is understanding what the swaps allow us to do: if we can swap positions within a connected component, we can arrange values in ANY order within that component.

ex. If we can swap [0,2] and [1,2]:

We can move values between positions 0, 1, and 2
These three positions form a connected component
Within this component, we can arrange values in ANY order!

> Key Realization: Use Union-Find (DSU) to find which positions can exchange values with each other.

2. Understanding the Alternating Sum

    nums[0] - nums[1] + nums[2] - nums[3] + nums[4] - ...
    (+)      (-)       (+)       (-)       (+)

- Even indices contribute positively (+)
- Odd indices contribute negatively (-)

Goal: Maximize this sum = Make even positions as large as possible, odd positions as small as possible.

3. Optimal Arrangement Within Each Component

Consider a component with positions [0, 1, 3] containing values [5, 2, 8]:

- Position 0 is even (+)
- Position 1 is odd (-)
- Position 3 is odd (-)

Strategy:

- Put the largest values on even indices (they're added)
- Put the smallest values on odd indices (they're subtracted)

So arrange as: [8, 2, 5] → contribution = 8 - 2 - 5 = 1

For a component with:

- `E` for even positions
- Values: `[v1, v2, ..., vk]`

Optimal contribution = `2 * sumTopE - sumAll`

Why this formula?
Let's say we have values [v1, v2, v3, v4, v5] and E = 2 even positions.

- sumAll = v1 + v2 + v3 + v4 + v5 (total of all values)
- sumTopE = v5 + v4 (sum of 2 largest values)

If we put the top E values on even positions:

```
Contribution = (v5 + v4) - (v3 + v2 + v1)
             = (v5 + v4) - (sumAll - v5 - v4)
             = (v5 + v4) - sumAll + (v5 + v4)
             = 2 * sumTopE - sumAll
```

### Overview

```md
1. Build connected components using Union-Find from swaps
2. For each component:
   - Count how many positions are even (E)
   - Collect all values in this component
   - Sort values and take top E largest ones
   - Contribution = 2 * sum(top E) - sum(all)
3. Sum contributions from all components
```