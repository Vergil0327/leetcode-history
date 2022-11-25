### Copy & Flatten the Input: Recursion + Deque

#### Preproecess

1. store nested list in a deque
2. process one by one
   1. if it is an integer, append to results
   2. if it is a list, recursively flatten the list and extend the results

#### Next

just popleft one by one

#### HasNext

just check if list is empty or not

but there is a downside here, we'll copy all ther list.

as a iterator, we should only process one by each call

### Space Optimized From Previous One

we can put `flatten` step within `hasNext` function

whenever we call `hasNext`, we flatten nestedList until we find the integer

use doubly-end queue to get O(1) in append item at first position

### Space Optimized By Stack with Index Pointer

我們可以定義這樣一個資料結構:

```python
stack = [[nestedList, 0]] # [nested list, pointer (or index) to unflatten nested list]
```

stack裡的每個item皆為 `[nestedList, pointer]`
pointer用來記錄目前的nestedList我們處理到哪

**讓我們來看`hasNext（）`:**

首先我們先找出stack的top item(stack[-1])

1. 如果我們的pointer `i`已經走到底，代表我們已經整個nestedList攤平了，我們可以直接將它移除
2. 如果pointer `i`還沒走到底，那我們藉由`isInteger()`確認目前pointer指的是`interger`或是`nestedList`
   1. 如果是 integer, 那就返回True
   2. 如果是 nestedList:
      1. 那我們將其攤平並加入stack，因為是新的nestedList，pointer設為0
      2. 同時別忘記將pointer `i` 往右移，指向下個未處理的item

```python
def hasNext(self):
        stack = self.stack
        while stack:
            nestedList, i = stack[-1]

            if i == len(nestedList): # we've processed all the item in current nestedList.
                stack.pop() # nothing left in current nestedList. just pop it out
            else:
                curr = nestedList[i]
                if curr.isInteger():
                    return True

                stack[-1][1] += 1 # increment index/pointer to next one
                stack.append([curr.getList(), 0]) # append nested nestedList
        return False
```

**同理`next（）`也是一樣道理**

1. 找出目前的nestedList，也就是stack的top item
2. 直接返回目前nestedList裡pointer `i` 指向的item
   - 返回前別忘記更新pointer `i`，記得往右移，移向下一位

```python
def next(self):
        nestedList, i = self.stack[-1]
        
        self.stack[-1][1] += 1 # increment index/pointer to next one
        return nestedList[i].getInteger()
```