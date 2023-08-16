class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        numFreq = defaultdict(set)
        res = 2 # both [X,X] and [X,Y] are valid case
        for i, num in enumerate(nums):
            if num in freq and num in numFreq[freq[num]]:
                numFreq[freq[num]].remove(num)
                if not numFreq[freq[num]]:
                    del numFreq[freq[num]]

            freq[num] += 1
            numFreq[freq[num]].add(num)
            
            if len(numFreq) == 1:
                _, SET = next(iter(numFreq.items()))

                # nums = xxxxxx or nums = a b c d e f
                if len(SET) == 1 or len(SET) == i+1:
                    res = i+1

            if len(numFreq) == 2:
                arr = sorted(numFreq.items()) # sort by freq
                freq1, set1 = arr[0]
                freq2, set2 = arr[1]

                # nums = XXX YYY Z
                v1 = next(iter(set1))
                if len(set1) == 1 and freq[v1] == 1:
                    res = i+1
                
                # nums = XXX YYY ZZZZ
                v2 = next(iter(set2))
                if len(set2) == 1 and freq[v2]-1 == freq[v1]:
                    res = i+1

        return res