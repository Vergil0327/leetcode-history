MX = 50001
divisors = [[] for _ in range(MX)]
for x in range(1, MX):
    for y in range(x, MX, x):
        divisors[y].append(x)

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        countNum = Counter(nums)
        countD = Counter()  # countD[d]: number of (i) with nums[i] % d == 0
        for num, freq in countNum.items():
            for d in divisors[num]:
                countD[d] += freq

        countG = Counter()  # countG[g]: number of (i < j) with gcd(nums[i], nums[j]) == g
        for g in range(mx, 0, -1):
            c = countD[g]
            if c <= 1:
                continue
            countG[g] = c * (c - 1) // 2
            countG[g] -= sum(countG[x] for x in range(2 * g, mx + 1, g))
        
        gList = []
        vList = []
        for g, v in sorted(countG.items()):
            gList.append(g)
            vList.append(v)
        presumV = list(accumulate(vList))

        res = []
        for q in queries:
            i = bisect_right(presumV, q)
            res.append(gList[i])
        return res
    

class PrimeFactor:
    def __init__(self, n):
        self.n = n
        # calculate the minimum prime factor for all numbers from 1 to self.n
        self.min_prime = [0] * (self.n + 1)
        self.min_prime[1] = 1
        # determine whether all numbers from 1 to self.n are prime numbers
        self.prime_factor = [[] for _ in range(self.n + 1)]
        self.prime_factor_cnt = [0]*(self.n+1)
        self.prime_factor_mi_cnt = [0] * (self.n + 1)
        # calculate all factors of all numbers from 1 to self.n, including 1 and the number itself
        self.all_factor = [[], [1]] + [[1, i] for i in range(2, self.n + 1)]
        self.euler_phi = list(range(self.n+1))
        self.build()

        return

    def build(self):

        # complexity is O(nlogn)
        for i in range(2, self.n + 1):
            if not self.min_prime[i]:
                self.min_prime[i] = i
                for j in range(i * i, self.n + 1, i):
                    if not self.min_prime[j]:
                        self.min_prime[j] = i

        for num in range(2, self.n + 1):
            pre = num // self.min_prime[num]
            self.prime_factor_cnt[num] = self.prime_factor_cnt[pre] + int(self.min_prime[num] != self.min_prime[pre])
            cur = num
            p = self.min_prime[cur]
            cnt = 0
            while cur % p == 0:
                cnt += 1
                cur //= p
            self.prime_factor_mi_cnt[num] = self.prime_factor_mi_cnt[cur] + cnt

        # complexity is O(nlogn)
        for num in range(2, self.n + 1):
            i = num
            phi = num
            while num > 1:
                p = self.min_prime[num]
                cnt = 0
                while num % p == 0:
                    num //= p
                    cnt += 1
                self.prime_factor[i].append((p, cnt))
                phi =  phi // p * (p - 1)
            self.euler_phi[i] = phi

        # complexity is O(nlogn)
        for i in range(2, self.n + 1):
            for j in range(i * i, self.n + 1, i):
                self.all_factor[j].append(i)
                if j > i * i:
                    self.all_factor[j].append(j // i)
        for i in range(self.n + 1):
            self.all_factor[i].sort()
        return

    def comb(self, a, b):
        # Use prime factor decomposition to solve the values of combinatorial mathematics
        # and prime factor decomposition O ((a+b) log (a+b))
        cnt = defaultdict(int)
        for i in range(1, a + 1):  # a!
            for num, y in self.prime_factor[i]:
                cnt[num] += y
        for i in range(1, b + 1):  # b!
            for num, y in self.prime_factor[i]:
                cnt[num] -= y
        for i in range(1, a - b + 1):  # (a-b)!
            for num, y in self.prime_factor[i]:
                cnt[num] -= y
        ans = 1
        for w in cnt:
            ans *= w ** cnt[w]
        return ans

    def get_prime_numbers(self):
        return [i for i in range(2, self.n + 1) if self.min_prime[i] == 0]

pf = PrimeFactor(5*10**4+10)


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        count = [0]*(mx+1)
        for num in nums:
            for p in pf.all_factor[num]:
                count[p] += 1

        # calculate # of pairs
        for q in range(mx+1):
            count[q] = count[q]*(count[q]-1)//2

        # remove dupliates
        for q in range(mx, 0, -1):
            for j in range(q+q, mx+1, q):
                count[q] -= count[j]

        pre = list(accumulate(count))

        res = []
        for q in queries:
            res.append(bisect.bisect_left(pre, q+1))
        return res