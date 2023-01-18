# Hash By Person
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        compBelongsTo = defaultdict(set)
        for person, comps in enumerate(favoriteCompanies):
            for comp in comps:
                compBelongsTo[comp].add(person)

        res = []
        for person, comps in enumerate(favoriteCompanies):
            otherPersons = set([i for i in range(n) if i != person])
            for comp in comps:
                otherPersons &= compBelongsTo[comp]
                if not otherPersons:
                    break
            if not otherPersons:
                res.append(person)
        return res

# Hash By Company
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        SETS = [set(favoriteCompanies[i]) for i in range(n)]
        res = []
        for i in range(n):
            isSubset = False
            for j in range(n):
                if i == j: continue
                if len(SETS[i]) > len(SETS[j]): continue
                if len(SETS[i] & SETS[j]) == len(SETS[i]):
                    isSubset = True
                    break
            if not isSubset:
                res.append(i)
        return res

# Optimized by bitmask
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        d=defaultdict(int)
        for i,comps in enumerate(favoriteCompanies):
            v=1<<i
            for comp in comps:
                d[comp] |= v
        res=[]
        for i,comps in enumerate(favoriteCompanies):
            curr = ~(1<<i)
            for comp in comps:
                curr &= d[comp]
                if not curr:
                    break
            if not curr:
                res.append(i)
        return res