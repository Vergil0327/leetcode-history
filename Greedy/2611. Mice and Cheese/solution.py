class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], K: int) -> int:
        rewards = sorted(zip(reward1, reward2), key=lambda x: x[0]-x[1], reverse=True)
        
        curr = k = 0
        for a, b in rewards:
            if k < K:
                curr += a
                k += 1
            else:
                curr += b
        return curr