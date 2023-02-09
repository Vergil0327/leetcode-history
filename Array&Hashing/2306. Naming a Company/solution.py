class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # suffix = defaultdict(set)
        groupByFirst = defaultdict(set)
        for idea in ideas:
            # suf = idea[1:]
            # suffix[suf].add(idea[0])
            groupByFirst[idea[0]].add(idea[1:])

        res = 0
        for i in range(26):
            a = chr(ord("a")+i)
            if a not in groupByFirst: continue
            for j in range(i+1, 26):
                b = chr(ord("a")+j)
                if b not in groupByFirst: continue

                common = len(groupByFirst[a]&groupByFirst[b])
                res += (len(groupByFirst[a])-common) * (len(groupByFirst[b])-common)*2

        return res

# {'offee': {'c', 't'}, 'onuts': {'d'}, 'ime': {'t'}}
# {'c': {'offee'}, 'd': {'onuts'}, 't': {'offee', 'ime'}}

class Solution_TLE:
    def distinctNames(self, ideas: List[str]) -> int:
        groupBySuffix = defaultdict(set)
        for idea in ideas:
            suf = idea[1:]
            groupBySuffix[suf].add(idea[0])

        res = 0
        items = list(groupBySuffix.items())
        for i in range(len(items)):
            set_a = items[i][1]
            for j in range(i+1, len(items)):
                set_b = items[j][1]
                common = len(set_a&set_b)
                res += (len(set_a)-common) * (len(set_b)-common) * 2

        return res