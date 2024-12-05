class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        parent = list(range(n))
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        for i in range(n):
            name1, t1, amt1, city1= transactions[i].split(",")
            for j in range(n):
                name2, t2, _, city2 = transactions[j].split(",")
                if (name1 == name2 and city1 != city2 and abs(int(t2)-int(t1)) <= 60):
                    union(i, j)

        res = []
        for i in range(n):
            _, _, amount, _ = transactions[i].split(",")
            if rank[find(i)] > 1 or int(amount) > 1000:
                res.append(transactions[i])
        return res


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        transactionRecord = defaultdict(list)

        for t in transactions:
            name, t1, amount, city = t.split(",")
            t1, amount = int(t1), int(amount)
            transactionRecord[name].append([t1, city])

        for t in transactions:
            name, t1, amount, city = t.split(",")
            t1, amount = int(t1), int(amount)
            if amount > 1000:
                res.append(t)
                continue

            elif name in transactionRecord:
                if any(abs(t2 - t1) <= 60 and city2 != city for t2, city2 in transactionRecord[name]):
                    res.append(t)

        return res