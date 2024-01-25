from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
      self.steam = deque()
      self.small = SortedList()
      self.middle = SortedList()
      self.large = SortedList()
      self.sum = self.m1 = self.m2 = 0

      self.m = m
      self.k = k
        

    def addElement(self, num: int) -> None:
        m, k = self.m, self.k
        steam, small, middle, large = self.steam, self.small, self.middle, self.large
        if len(steam) >= m:
            remove = steam.popleft()
            self.sum -= remove
            if remove in small:
                small.remove(remove)
                self.m1 -= remove
                # balance k-small
                while middle and len(small) < k:
                    added = middle.pop(0)
                    small.add(added)
                    self.m1 += added
            elif remove in large:
                large.remove(remove)
                self.m2 -= remove
                # balance k-large
                while middle and len(large) < k:
                    added = middle.pop(-1)
                    large.add(added)
                    self.m2 += added
            else:
                middle.remove(remove)

        steam.append(num)
        self.sum += num

        small.add(num)
        self.m1 += num
        
        if len(small) > k:
            el = small.pop(-1)
            self.m1 -= el

            large.add(el)
            self.m2 += el
            if len(large) > k:
                el = large.pop(0)
                self.m2 -= el
                middle.add(el)

    def calculateMKAverage(self) -> int:
        total = self.sum
        m1, m2 = self.m1, self.m2
        m, k = self.m, self.k
        if len(self.steam) < m: return -1
        return floor((total-m1-m2) / (m - 2*k))