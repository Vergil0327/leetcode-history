class Solution:
    def intToRoman(self, num: int) -> str:    
        digits = deque(map(int, str(num)))
        res = ""
        power = len(digits)-1
        while digits:
            d = digits.popleft()
            
            if 0 < d < 4:
                n = d
                while n > 0:
                    if power == 3:
                        res += "M"
                    elif power == 2:
                        res += "C"
                    elif power == 1:
                        res += "X"
                    else:
                        res += "I"
                    n -= 1

            if d == 4:
                if power == 2:
                    res += "CD"
                elif power == 1:
                    res += "XL"
                else:
                    res += "IV"
            
            if 5 <= d < 9:
                if power == 2:
                    res += "D"
                elif power == 1:
                    res += "L"
                else:
                    res += "V"

                n = d-5
                while n > 0:
                    if power == 2:
                        res += "C"
                    elif power == 1:
                        res += "X"
                    else:
                        res += "I"
                    n -= 1
            if d == 9:
                if power == 2:
                    res += "CM"
                elif power == 1:
                    res += "XC"
                else:
                    res += "IX"

            power -= 1
        return res