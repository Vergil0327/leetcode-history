"""
Maximum Number:

Greedy: Put largest possible digit (9) at each position from left to right
999... until sum is exhausted

Minimum Number:

Key insight: We need to avoid leading zeros

1. Reserve 1 for the first digit (so it's never 0)
2. Fill positions from right to left with maximum possible digits
3. Put remaining sum + 1 in the first position
"""
m, s = map(int, input().split())

if s == 0:
    print("0 0" if m == 1 else "-1 -1")

elif s > 9 * m:
    print("-1 -1")

else:
    # Maximum
    max_result = ""
    remaining = s
    for _ in range(m):
        d = min(9, remaining)
        max_result += str(d)
        remaining -= d

    # Minimum
    min_digits = [0] * m
    remaining = s - 1  # Reserve 1 for first position

    for i in range(m - 1, 0, -1):
        d = min(9, remaining)
        min_digits[i] = d
        remaining -= d

    min_digits[0] = remaining + 1
    min_result = ''.join(map(str, min_digits))

    print(f"{min_result} {max_result}")