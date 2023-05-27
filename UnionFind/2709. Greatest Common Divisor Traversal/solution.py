class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True # edge case

        # Sieve of Eratosthenes
        mx = max(nums)
        primes = []
        isPrime = [0, 0] + [1] * (mx-1)
        for i in range(2, int(math.sqrt(mx))+1):
            if not isPrime[i]: continue
            primes.append(i)
            for j in range(i*i, mx+1, i):
                isPrime[j] = 0

        # find factors of each nums[i]
        edges = []
        for num in nums:
            if num == 1: return False # edge case: [1,1]
            factors = []

            cur = num
            for p in primes:
                if cur%p != 0: continue

                factors.append(p)
                while cur%p == 0:
                    cur //= p
            if cur != 1:
                factors.append(cur)

            edges.append([factors, num])

        # Union nums[i] with its factors
        parent = list(range(mx+1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for (neighbors, node) in edges:
            for nei in neighbors:
                if (x := find(nei)) == (y := find(node)): continue
                if x <= y:
                    parent[y] = x
                else:
                    parent[x] = y

        # check if all the nums[i] are connected together
        groups = set()
        for num in nums:
            groups.add(find(num))

        return len(groups) == 1