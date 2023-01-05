class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def move(i):
            if i >= n: return i%n
            if i < 0: return (i+n)%n
            return i

        checked = set()
        for i in range(n):
            if i in checked: continue
            checked.add(i)

            cycle = set()
            # find cycle starting point
            while move(i+nums[i]) not in cycle:
                i = move(i+nums[i])
                cycle.add(i)
                checked.add(i)
            cycleStart = move(i+nums[i])

            ### check if cycle size is greater than 1
            # we also need to make sure we don't move back and forth.
            # cycle is valid only if every node move toward same direction
            curr = cycleStart
            direction = 1 if nums[curr] > 0 else -1

            k = 1
            while cycleStart != move(curr+nums[curr]):
                curr = move(curr+nums[curr])
                nextDir = 1 if nums[curr] > 0 else -1
                if nextDir * direction < 0: # different direction
                    k = 1
                    break
                k += 1

            if k > 1: return True
                
        return False

# Follow-up
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def move(i):
            i += nums[i]
            if i >= n: return i%n
            if i < 0: return (i+n)%n
            return i

        for i in range(n):
            # we mark nums[i] = 0 as visited
            if nums[i] == 0: continue

            slow, fast = i, move(slow)
            # only move forward.
            while nums[fast] * nums[i] > 0 and nums[move(fast)] * nums[i] > 0:
                if slow == fast:
                    if slow == move(slow): break # self-cycle
                    return True
                slow = move(slow)
                fast = move(move(fast))
            
            # if not found, mark every node in current cycle as visited
            slow = i
            direction = nums[i]
            while nums[slow] * direction > 0:
                nxt = move(slow)
                nums[slow] = 0
                slow = nxt

        return False

