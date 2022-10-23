# god-like optimal solution
# https://leetcode.com/problems/determine-if-two-events-have-conflict/discuss/2734120/JavaC%2B%2BPython-Easy-1-liner-Solutions
class GodLikeSolution:
  def haveConflict(self, event1, event2):
      return max(event1[0],event2[0]) <= min(event1[1],event2[1])

class GodLikeSolution:
  def haveConflict(self, event1, event2):
        return event1[0] <= event2[1] and event2[0] <= event1[1]

# Explanation
#
# Given 2 segment [left1, right1], [left2, right2],
# how can we check whether they overlap?
#
# If these two intervals overlap, it should exist a value x,
# such that
#   left1 <= x <= right1 && left2 <= x <= right2
# so that
#   max(left1, left2) <= x <= min(right1, right 2)
# so that
#   left1 <= right2 && left2 <= right1

# These two are the sufficient and necessary conditions,
# for two interval overlaps.

class BetterSolution:
    def getSec(self, time):
        hr, minute = time[0:2], time[3:]
        return int(hr)*60+int(minute)

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = self.getSec(event1[0]), self.getSec(event1[1])
        start2, end2 = self.getSec(event2[0]), self.getSec(event2[1])
    
        # [left1, right1] [left2, right2]
        # left1 <= x <= right1 && left2 <= x <= right2
        # => max(left1, left2) <= x <= min(right1, right2)
        # => left1 <= right2 and left2 <= right1
            
        return start1 <= end2 and start2 <= end1

class BetterSolution:
    def getSec(self, time):
        hr, minute = time[0:2], time[3:]
        return int(hr)*60+int(minute)

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = self.getSec(event1[0]), self.getSec(event1[1])
        start2, end2 = self.getSec(event2[0]), self.getSec(event2[1])
        
        # [left1, right1] [left2, right2]
        # left1 <= x <= right1 && left2 <= x <= right2
        # => max(left1, left2) <= x <= min(right1, right2)
        
        end = min(end1, end2)
        start = max(start1, start2)
            
        return end >= start

class DumbSolution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        arr = sorted([event1, event2])
        end = arr[0][1]
        start = arr[1][0]

        if int(end[0:2]) < int(start[0:2]): # hour
            return False
        elif end[0:2] == start[0:2]: # minute
            if int(end[3:]) < int(start[3:]):
                return False
            else:
                return True
            
        return True
        