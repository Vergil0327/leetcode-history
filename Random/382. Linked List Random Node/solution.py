# time: O(n)
# space: O(n)
import random


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.pool = []
        curr = head
        while curr:
            self.pool.append(curr.val)
            curr = curr.next

    def getRandom(self) -> int:
        return random.choice(self.pool)

# ! Follow-Up: Reservoir Sampling
# for i-th element, `1/i` possibilities to pick and `1-1/i` not to pick
# Proof:
# for i-th element in total n elements
# possibility of picking i-th is:
# 1/i * (1-1/(i+1)) * (1-1/(i+2)) * ... * (1-1/n)
# pick i x not pick i+1 x not pic i+2 x ... x not pick n-th
# = 1/i * i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n
# = 1/n

# time: O(n)
# space: O(1)
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.root = head

    def getRandom(self) -> int:
        curr = self.root
        i = 0
        res = curr.val
        while curr:
            i += 1
            if 0 == random.randint(0, i-1): # 1/i to choose, 1-1/i not to choose
                res = curr.val
            curr = curr.next
        return res
