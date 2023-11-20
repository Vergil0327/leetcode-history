class Solution:
    """
    三輛車各自收各自負責的類型 => 三輛車獨自運作
    由於不需要一定得收到最後一間, 所以就收到最後一間有自己負責的垃圾即可
    """
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        timePicking = 0
        timeDriving = 0
        M = P = G = 0
        for i in range(len(garbage)):
            timePicking += len(garbage[i])
            if i > 0:
                timeDriving += travel[i-1]
            if "M" in garbage[i]:
                M = timeDriving
            if "P" in garbage[i]:
                P = timeDriving
            if "G" in garbage[i]:
                G = timeDriving

        return timePicking + M + P + G