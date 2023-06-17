# Intuition

1. change each tap into interval [start_pos, end_pos] based on ranges[i]
2. sort by start_pos and problem turn into finding minimum interval to cover whole range
3. iterate pos and find maximum cover interval greedily for pos, after that, update pos to interval[j].end_pos and res += 1
as for finding maximum cover interval, we can choose one of interval while intervals[j].start_time <= current_position
4. if we can't find any interval to cover current position, just return -1 directly
