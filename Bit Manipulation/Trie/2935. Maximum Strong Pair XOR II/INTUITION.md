# Intuition   

```
|x - y| <= min(x, y)
=> if x > y: x - y <= y => x <= 2*y => x/2 <= y
=> if x < y: y - x <= x
=> if x = y: 0 <= x => because 1 <= x, y => strong pair => x^y = 0 => no need to consider it
```

所以我們可以對nums排序, 利用x <= 2y這條件可以發現這是個sliding window:
```
X X X X [X X X X X]
         y       x <= 2y => sliding window
```

自然而然能導出這個sliding window的主要框架:

```py
queue = collections.deque()
for num in nums:
    while queue and abs(num - queue[0]) > min(num, queue[0]):
        old = queue.popleft()
    
    queue.append(num)
    
    # Try to find the max answer from the tree
    # ...
```

但問題是該如何高效找出maximum XOR sum ?

> The problem involves finding the maximum XOR among pairs of numbers. The Trie data structure is commonly used to solve problems related to XOR operations, especially when dealing with binary representations of numbers. 

> Trie as a Data Structure for Binary Representation: A Trie is a tree-like data structure used to store a dynamic set or associative array where the keys are usually strings. In this case, each level of the Trie represents a bit in the binary representation of the numbers.

> Efficient Search for Maximum XOR: By traversing the Trie based on the bits of the numbers, you can find pairs of numbers with the maximum XOR efficiently. The idea is to maximize the XOR by choosing different bits at each level of the Trie.
> Complement Bit Check: The XOR operation is maximized when the bits at each position are different. The Trie helps efficiently check for the complement bit at each level.

> In summary, using a Trie allows us to explore the binary representation of numbers in a way that helps identify pairs that maximize the XOR operation. It's a common technique for solving problems related to XOR, and its efficiency comes from exploiting the binary nature of the XOR operation.

XOR operation => Trie
讓每一層代表一個bit, 每個節點是過往的合法nums[j]的bit位
當加入一個nums[i]時我們逐個bit來看

由於是要maximum XOR sum, 所以我們存的時候從高位往低位
這樣在找max sum時也從高位往低位搜尋, 如果當前的nums[i]的bit數值為`b`, 那就看有沒有存在一個**1-b**存在 (因為1^0跟0^1為1)