# Neetcode: https://www.youtube.com/watch?v=amnrMCVd2YI

# use min heap to form hand of straight from minimal card
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        
        # counter = collections.Counter(hand)
        counter = defaultdict(lambda: 0)
        for card in hand:
            counter[card] += 1
        
        minH = list(counter.keys())
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]
            
            for card in range(first, first+groupSize):
                if card not in counter:
                    return False
                
                counter[card] -= 1
                if counter[card] == 0:
                    if card != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

class SolutionOptimized:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        if groupSize == 1: return True
        
        # counter = collections.Counter(hand)
        counter = defaultdict(lambda: 0)
        for card in hand:
            counter[card] += 1
        
        minH = list(counter.keys())
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]
            numStraights = counter[first]
            for card in range(first, first+groupSize):
                if card not in counter:
                    return False
                
                # we can decrease counter[card] by the number of first card of straight,
                # and see if any card after it is not enough to form a straight
                counter[card] -= numStraights
                if counter[card] < 0:
                    return False
                if counter[card] == 0:
                    heapq.heappop(minH)
        return True