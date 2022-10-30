from typing import List
from collections import defaultdict
import heapq


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        N = len(creators)
        
        popularity = defaultdict(lambda: 0)
        maxViewMovie = defaultdict(list) # [maxView, maxViewMovie]
        for i in range(N):
            popularity[creators[i]] += views[i]
            if not maxViewMovie[creators[i]]:
                maxViewMovie[creators[i]] = [views[i], ids[i]]
            else:
                currView, currId = maxViewMovie[creators[i]]
                if views[i] > currView:
                    maxViewMovie[creators[i]] = [views[i], ids[i]]
                elif views[i] == currView and ids[i] < currId:
                    maxViewMovie[creators[i]][1] = ids[i]

        maxPopu = max(popularity.values())
        
        return [[creator, maxViewMovie[creator][1]] for creator, p in popularity.items() if p == maxPopu]


class SolutionFirstTry:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        N = len(creators)
        
        movies = defaultdict(list)
        for i in range(N):
            movies[creators[i]].append([views[i], ids[i]])
        
        pq = []
        for creator, movies in movies.items():
            total = 0
            maxView = float('-inf')
            maxViewID = ""
            for view, movieID in movies:
                total += view
                if view > maxView:
                    maxView = view
                    maxViewID = movieID
                elif view == maxView and movieID < maxViewID:
                    maxViewID = movieID
            
            heapq.heappush(pq, [-total, creator, maxViewID])
        
        
        res = []
        maxPopu = pq[0][0]
        while pq and pq[0][0] == maxPopu:
            _, creator, viewID = heapq.heappop(pq)
            res.append([creator, viewID])
        return res