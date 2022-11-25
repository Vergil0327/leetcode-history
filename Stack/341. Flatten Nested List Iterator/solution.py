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