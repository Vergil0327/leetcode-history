class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = [[pt,gt] for pt, gt in sorted(zip(plantTime, growTime), key= lambda time: -time[1])]
        print(arr)
        
        total = 0
        plantTime = 0
        growTime = 0
        for pt, gt in arr:
            plantTime += pt
            total = max(total, plantTime + gt)
        return total
                   