from sortedcontainers import SortedList

# O(nlog(n)): 接龍遊戲 (card game patience)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        
        groups = SortedList() # [card, groupSize]
        for card in sorted(hand):
            if not groups:
                groups.add([card, 1])
                continue
            
            idx = groups.bisect_right([card])

            if groups[idx-1][0] == card-1:
                if groups[idx-1][1] == groupSize-1:
                    groups.pop(idx-1)
                else:
                    groups[idx-1][0] = card
                    groups[idx-1][1] += 1
            else:
                groups.add([card, 1])
            
        return len(groups) == 0
            

        # 1,2,2,3,3,4,6,7,8
        # [[1]]
        # [[1,2]]
        # [[1,2],[2]]
        # [[1,2,3],[2]] -> [[2]]
        # [[2,3]]
        # [[2,3,4]] -> []
        # [[6]]
        # [[6,7]]
        # [[6,7,8]] -> []
        

# https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
class SolutionTLE:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        
        count = collections.Counter(hand)
        
        for card in sorted(count):
            # pair up consecutive card groups
            # pair up [card, card+1, ..., card+groupSize-1] for every card
            # count[card] should decrease to zero exactly
            for currCard in range(card, card+groupSize)[::-1]:
                count[currCard] -= count[card]
                if count[currCard] < 0:
                    return False
        
        return True

# O(MlogM + N), where M is the number of different cards.
class SolutionOptimized:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        
        counter = collections.Counter(hand)
        
        tailCard, openGroups = -1, 0
        straight = collections.deque()

        for card in sorted(counter):
            if openGroups > counter[card]: return False
            if openGroups > 0 and card > tailCard+1: return False
            
            straight.append(counter[card] - openGroups)
            tailCard, openGroups = card, counter[card]

            if len(straight) == groupSize: # form straights
                openGroups -= straight.popleft()
        return openGroups == 0