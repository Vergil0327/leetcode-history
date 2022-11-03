
"""
Intuition:

1. found two sides of palindrome such as ab & ba
2. found valid middle such as aa, bb
3. max length = even number of middle + two sides + (single middle if exists)
    - think ab cc dd cc ba
    - even number of middle (cc cc) + two sides (ab ba) + single middle (dd)
"""
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        middlePart = defaultdict(lambda: 0)
        count = defaultdict(lambda: 0)
        
        longest = 0
        for word in words:
			      # found valid middle of palindrome. 'aa' 'bb' 'cc'
            if word[0]==word[1]:
                middlePart[word] += 1
                continue
			
			      # found 'ab' & 'ba' in hashmap
            if word[::-1] in count:
                longest += 4
                count[word[::-1]] -= 1
                if count[word[::-1]] == 0:
                    del count[word[::-1]]
            else:
                count[word] += 1

        hasMiddle = False # 'aa' 'bb' 'aa' -> valid palindrome
        for num in middlePart.values():
            if num%2 != 0:
                hasMiddle = True
                break

        # middlePart -> 'aa': 2 -> 2//2 = 1 -> means 'aaaa'
        longest += sum(x//2 for x in middlePart.values())*4
        return longest + 2 if hasMiddle else longest

# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/discuss/2771999/Python3-Hash-map-approach-with-line-by-line-comments!
class SolutionOptimized:
    def longestPalindrome(self, words: List[str]) -> int:
    	
    	### count the frequency of each word in words
        counter = Counter(words)
        
        ### initialize res and mid. 
        ### mid represent if result is in case1 (mid=1) or case2 (mid=0)
        res = mid = 0 

        for word in counter.keys():
            
            if word[0]==word[1]:
            	### increase the result by the word frequency
                res += counter[word] if counter[word]%2==0 else counter[word]-1
                ### set mid to 1 if frequency is odd (using bit-wise OR to make it short)
                mid |= counter[word]%2
            
            elif word[::-1] in counter:
            	### increase the result by the minimum frequency of the word and its reverse
            	### we do not do *2 because we will see its reverse later
                res += min(counter[word],counter[word[::-1]])
        
        ### since we only count the frequency of the selected word
        ### times 2 to get the length of the palindrome
        return (res + mid) * 2