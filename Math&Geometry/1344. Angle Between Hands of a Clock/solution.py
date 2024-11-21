class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 一圈360度, 共60個刻度, 一個刻度等於 360/60度
        one_step = 360 // 60
        
        # 1時為5格, 然後再加上minutes給的偏移量為 (minutes/60) * 5
        # 便能計算出格數
        h = (hour%12) * 5 + minutes*5/60

        # 時跟分的格數相減, 再乘上一格為6度即可計算出其中一個夾角
        deg = abs(h - minutes) * one_step

        # 兩個夾角取小即為答案
        return min(deg, 360 - deg)