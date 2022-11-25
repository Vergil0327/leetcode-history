from __future__ import annotations
from collections import deque

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> list[NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """

# Copy & Flatten the Input: Recursion + Deque
class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        def flatten(nestedList):
            res = []
            queue = deque(nestedList)

            while queue:
                sz = len(queue)
                for _ in range(sz):
                    curr = queue.popleft()
                    if curr.isInteger():
                        res.append(curr.getInteger())
                    else:
                        l = flatten(curr.getList())
                        res.extend(l)
            return res

        self.l = deque(flatten(nestedList))
    
    def next(self) -> int:
        return self.l.popleft()
    
    def hasNext(self) -> bool:
        return self.l


# Space Optimized
# ref: https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80146/Real-iterator-in-Python-Java-C%2B%2B
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]] # [nested list, pointer (or index) to unflatten nested list]

    def next(self):
        nestedList, i = self.stack[-1]
        
        self.stack[-1][1] += 1 # increment index/pointer to next one
        return nestedList[i].getInteger()

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