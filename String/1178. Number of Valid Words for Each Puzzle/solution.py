class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        counter = defaultdict(int)
        for word in words:
            bit = 0
            for ch in set(word):
                bit |= 1<<(ord(ch)-ord("a"))

            counter[bit] += 1

        res = []
        for puzzle in puzzles:
            bitmask = 0
            first_letter_bit = -1
            for ch in puzzle:
                if first_letter_bit == -1:
                    first_letter_bit = 1<<(ord(ch)-ord("a"))

                bitmask |= 1<<(ord(ch)-ord("a"))
            

            # iterate submask
            count = 0
            submask = bitmask
            while submask > 0:
                # word must contains the first letter of puzzle.
                if first_letter_bit&submask == first_letter_bit:
                    count += counter[submask]
                
                submask = (submask-1)&bitmask

            res.append(count)
        return res