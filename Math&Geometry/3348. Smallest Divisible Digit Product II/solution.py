def fill(req, length):
    """
    This function generates the smallest zero-free number with a product divisible by a given req and with a certain number of digits.
    
    The fill function essentially finds the smallest number that has a product divisible by req using large digits first (9 down to 2) to minimize the numerical value.
    """

    # Initialize an empty list to store the digits of the result.
    ans = []
    
    # Try dividing `req` by digits from 9 down to 2.
    # This gives us the largest possible digits first, ensuring a smaller resulting number.
    for d in range(9, 1, -1):
        # Continue dividing `req` by `d` while it is divisible.
        while req % d == 0:
            ans.append(d)  # Add `d` to the result.
            req //= d      # Reduce `req` by dividing it by `d`.
    
    # Extend the answer to match the required length with ones (smallest possible digit).
    ans.extend([1] * max(0, length - len(ans)))
    
    # Reverse the list to get the smallest possible number and join it as a string.
    return "".join(map(str, reversed(ans)))

from math import gcd

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize `t` and check if it contains only the primes 2, 3, 5, or 7.
        n = len(num)  # Length of the input number string.
        
        T = t       # Create a copy of `t` for factorization.
        # Try dividing `T` by primes to see if it becomes 1.
        for p in [2, 3, 5, 7]:
            while T % p == 0:
                T //= p

        # If `T` is not reduced to 1, then `t` has prime factors other than 2, 3, 5, or 7.
        # Return "-1" as it's impossible to achieve the required product.
        if T != 1: return "-1"
        
        # Step 2: Compute `prefix` array where `prefix[i]` is the required divisibility for the prefix `num[:i]`.
        prefix = [t] * (n + 1)
        
        # Calculate the required divisibility by considering each digit of `num`.
        for i, x in enumerate(map(int, num)):
            if x == 0: break  # Stop if we encounter a zero.
            # Update `prefix[i+1]` by reducing `prefix[i]` with the GCD of `prefix[i]` and the current digit `x`.
            prefix[i + 1] = prefix[i] // gcd(prefix[i], x)
        
        # If the last element of `prefix` is 1, `num` itself meets the required divisibility.
        if prefix[-1] == 1: return num
        
        # Step 3: Find the position of the first '0' or end of string `num`.
        zero = num.find("0") % n
        
        # Step 4: Modify digits from right to left to find the smallest valid number.
        for i in range(zero, -1, -1):
            req = prefix[i]  # The required divisibility at position `i`.
            digits = n - 1 - i  # Remaining digits after position `i`.
            
            # Try to replace `num[i]` with the smallest digit greater than `num[i]`.
            for d in range(int(num[i]) + 1, 10):
                # Compute the suffix that would satisfy the required product.
                suffix = fill(req // gcd(req, d), digits)
                
                # If the length of `suffix` fits, return the resulting number.
                if len(suffix) <= digits:
                    return num[:i] + str(d) + suffix

        # If no valid number was found, construct a number with one extra digit.
        return fill(t, len(num) + 1)
