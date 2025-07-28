class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        # Build prime edges by using prime factorization
        teleport = defaultdict(list)
        for i in range(n):
            p = 2
            num = nums[i]
            while p * p <= num:
                if num % p == 0:
                    teleport[p].append(i)
                    while num % p == 0:
                        num //= p
                p += 1
            if num > 1:
                teleport[num].append(i)

        pq = [(0, 0)] # (step, position)
        distance = [inf] * n
        distance[0] = 0
        while pq:
            step, pos = heapq.heappop(pq)
            if step > distance[pos]: continue

            # jump backward
            if pos-1 >= 0 and step+1 < distance[pos-1]:
                distance[pos-1] = step+1
                heapq.heappush(pq, (step+1, pos - 1))
            
            # jump forward
            if pos+1 < n and step+1 < distance[pos+1]:
                distance[pos+1] = step+1
                heapq.heappush(pq, (step+1, pos + 1))

            if nums[pos] in teleport:
                for nxt in teleport[nums[pos]]:
                    if nxt != pos and step+1 < distance[nxt]:
                        distance[nxt] = step+1
                        heapq.heappush(pq, (step+1, nxt))
                del teleport[nums[pos]]
        return distance[n-1]