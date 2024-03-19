class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())
        numMaxFreq = sum(int(freq == maxFreq) for freq in count.values())

        return max((maxFreq-1)*(n+1) + numMaxFreq, len(tasks))