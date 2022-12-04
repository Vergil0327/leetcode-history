# time:O(n)
# space:O(n)
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)

        for i in range(n):
            nextIdx = (i+1)%n
            if words[i][-1] != words[nextIdx][0]: return False
        return True
        
# time:O(n)
# space: O(1)
class OptimizedSolution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)
        for i in range(n):
            if sentence[i] == " " and sentence[i-1] != sentence[i+1]:
                return False
        return sentence[0] == sentence[-1]