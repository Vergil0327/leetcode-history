# Intuition

從過往合法的time interval中挑出與當前booked time重疊的區間
然後再看這之間有沒有任意兩區間重疊, 如果有, 那就代表發生tripple booking

time: O(nlogn) for each `book` call. (O(n^2) overall)

# Optimization

這題能進一步將時間將至O(n) for each `book` call

1. 將每個時間區段加入到`self.calendar`裡
2. 將有重疊的區間加入到`self.overlaps`
3. 那這樣之後每個`book` call就只需要查看`self.overlaps`裡有沒有與[start, end]相交的區間即可

```py
class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i: # double-booking overlap with [start, end)
                return False

        for i, j in self.calendar:
            if start < j and end > i: # overlap with [start, end)
                self.overlaps.append((max(start, i), min(end, j)))

        self.calendar.append((start, end))
        return True
```