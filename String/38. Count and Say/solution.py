class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        i = 1
        s = "1"

        while i < n:

            # use two pointers to split into substring
            pairs = deque()
            l, r, cnt = 0, 0, 0
            while r < len(s):
                cnt += 1
                r += 1

                if r == len(s) or s[r] != s[l]:
                    pairs.appendleft([s[l], cnt])
                    cnt = 0
                    l = r

            # generate string
            t = ""
            for digit, freq in pairs:
                t = str(freq)+digit+t

            s = t
            i += 1
        return s

# Concise
def countAndSay(n):
    result = "1"
    for _ in range(n - 1):
        s = '' # accumulator string

        # iterate the characters (digits) grouped by digit
        for digit, group in itertools.groupby(result):
            count = len(list(group)) # eg. the 2 in two 1s 
            s += "%i%s" % (count, digit) # create the 21 string and accumulate it
        result = s # save to result for the next for loop pass

    # return the accumulated string
    return result