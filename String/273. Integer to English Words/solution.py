class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"

        separators = ["", "Thousand", "Million", "Billion"]
        nums = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen"] + [t[0:-2] + "teen" for t in tens[5:]]

        # split into chunks with size of 3
        s = str(num)[::-1]
        strs = []
        for i in range(0, len(s), 3):
            strs.append(s[i:i+3][::-1])
        
        res = []
        for s in strs:
            eng = ""
            n = len(s)
            if n == 3:
                if nums[int(s[0])]:
                    eng += nums[int(s[0])] + " " + "Hundred"

                if s[1] == "1":
                    if teens[int(s[2])]:
                        if eng: eng += " "
                        eng += teens[int(s[2])]
                elif s[1] == "0":
                    if nums[int(s[2])]:
                        if eng: eng += " "
                        eng += nums[int(s[2])]
                else:
                    if eng: eng += " "
                    eng += tens[int(s[1])] + (" " + nums[int(s[2])] if nums[int(s[2])] else "")

            elif n == 2:
                if s[0] == "1":
                    eng += teens[int(s[1])]
                else:
                    eng += tens[int(s[0])] + (" " + nums[int(s[1])] if nums[int(s[1])] else "")
            else:
                eng += nums[int(s[0])]
                
            res.append(eng)
        
        ans = []
        for i in range(len(res)):
            if not res[i]: continue
            ans.append(res[i] + (" " + separators[i] if separators[i] else ""))

        return " ".join(reversed(ans))