class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        # Pad low with leading zeros to make low and high the same length
        low = '0' * (len(high) - len(low)) + low

        mod = 10**9 + 7  
        n = len(high)
        
        @cache
        def dfs(i, is_greater_than_low, is_less_than_high, last_digit, leadingZero):
            # Base case: if we have processed all digits, we have found a valid stepping number
            if i == n:  return 1

            total = 0
            # Determine the starting and ending digit for the current iition
            start = int(low[i]) if not is_greater_than_low else 0
            end = int(high[i]) + 1 if not is_less_than_high else 10
            # Iterate over all isible digits for the current iition
            for digit in range(start, end):
                # We can append this digit if we haven't appended a non-zero digit yet (have leading zeros) 
                # or if its absolute difference with the last digit is 1
                if leadingZero or abs(last_digit - digit) == 1:
                    # Recurse to the next iition, updating the flags and last digit
                    total += dfs(i + 1, 
                                 is_greater_than_low or digit > int(low[i]), 
                                 is_less_than_high or digit < int(high[i]), 
                                 digit,
                                 leadingZero and digit == 0)
            # Return the total count modulo mod to keep the number manageable
            return total % mod

        return dfs(0, False, False, -1, True)
