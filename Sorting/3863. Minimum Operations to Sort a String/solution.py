class Solution:
    """
    the solution depends on the position of the minimum and maximum characters.

    Case 0: Already Sorted
    The string is already in non-descending order.
        Example: "abc", "defg"

    Case 1: One Side is "Locked"
    You only need to sort the part of the string that is messy. This works if the first character is already the smallest or the last character is already the largest.

        Condition: s[0] == min(s) OR s[n-1] == max(s)
        Example: "a c b" (Smallest 'a' is at index 0. Sort the rest.)
        Example: "b a c" (Largest 'c' is at index 2. Sort the rest.)

    Case 2: Standard Shuffle
    You need to move an extreme element into the middle first, then into its final place. This applies to most unsorted strings, including those with duplicate characters that "help" the sort.
    
        Condition: The string is not sorted, and Case 1 is not met, but we can move a "useful" character to the front or back in one partial sort.
        Example: "j g g" (Sort "j g" $\rightarrow$ "g j g". Then sort "j g" $\rightarrow$ "g g j". Total 2 ops.)Example: "b c a" (Sort "c a" $\rightarrow$ "a c". Then sort "b a" $\rightarrow$ "a b". Total 2 ops.)

    Case 3: Extreme Rotation
    This is the "worst-case" scenario. The smallest character is trapped at the very end, and the largest character is trapped at the very beginning, with no duplicates of those values available to bridge the gap.
    
        Condition: s[0] == max(s) AND s[n-1] == min(s) AND a partial sort cannot put a min/max in its final spot.
        Example: "e d c" (Max 'e' at start, Min 'c' at end. No other 'c' or 'e' to help.)
        Example: "c b a" (Classic 3-move rotation.)
    """
    def minOperations(self, s: str) -> int:
        n = len(s)
        chars = sorted(list(s))
        sorted_s = "".join(chars)
        
        # 1. Already sorted
        if s == sorted_s:
            return 0
        
        # 2. Impossible for length 2
        if n == 2:
            return -1
            
        # 3. Can be fixed in 1 move
        # (The first char is the smallest OR the last char is the largest)
        if s[0] == chars[0] or s[-1] == chars[-1]:
            return 1
            
        # 4. The 3-move "Extreme Rotation" case
        # If s[0] is the max and s[-1] is the min, 
        # it is 3 moves ONLY IF sorting the first part doesn't 
        # put the min in the first spot OR sorting the last part 
        # doesn't put the max in the last spot.
        
        if s[0] == chars[-1] and s[-1] == chars[0]:            
            prefix_sort_first = "".join(sorted(s[:-1]))[0]
            suffix_sort_last = "".join(sorted(s[1:]))[-1]
            
            if prefix_sort_first == chars[0] or suffix_sort_last == chars[-1]:
                return 2
            return 3
            
        return 2