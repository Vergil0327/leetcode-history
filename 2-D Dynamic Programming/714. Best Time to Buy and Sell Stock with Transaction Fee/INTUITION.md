# bottom-up DP

## Intuition

**dp definition**

hold[i]: the maximum money until i-th day when holding stock, which means state after we bought the stock
sold[i]: the maximum money until i-th day after sold stock

**state transfer**

hold[i] can comes from:

  1. hold[i-1]: keep holding stock from `i-1` day to `i` day
  2. sold[i-1]-prices[i]: we sold stock at `i-1` day and bought current stock at `i` day

choose maximum between these two states above

sold[i] can comes from:

  1. sold[i-1]: keep current state from `i-1` to `i` day
  2. hold[i-1]+prices[i]-fee: we hold/bought stock at `i-1` day and sold stock at `i` day with `fee` cost

choose maximum between these two states above

the final answer should be sell all the stock at last day after we always choose maximum money strategy

## Complexity

- time complexity

$$O(N)$$

- space complexity

$$O(N)$$