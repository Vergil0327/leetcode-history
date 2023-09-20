class Solution:
    def parse(self, s:str) -> Tuple[bool, float, str]:
        """
        returns a tuple:
            isRationalNumber bool
            rationalNumber float: only valid if isRationalNumber == True
            nonRationalNumber str: only valid if isRationalNumber == False
        """

        i = s.find("(")
        if i == -1:
            return True, float(s), ""

        nonRepeating = s[:i]
        repeating = s[i+1:-1]
        SET = set(repeating)
        if len(SET) == 1 and next(iter(SET)) == "0":
            return True, float(nonRepeating), ""

        if len(SET) == 1 and next(iter(SET)) == "9":
            arr = ["0"] + list(nonRepeating)
            if arr[-1] != ".":
                # 1.0(9) => decimal = ["0", "1", ".", str(0+1)]
                arr[-1] = str(int(arr[-1])+1)
            else:
                # 1.(9) => decimal = ["0", str(1+1),"."]
                arr[-2] = str(int(arr[-2])+1)

            carry = 0
            for i in range(len(arr)-1, -1, -1):
                if arr[i] == ".": continue
                cur = int(arr[i])+carry
                arr[i] = str(cur%10)
                carry = cur//10
                
            return True, float("".join(arr)), ""
        return False, 0, (nonRepeating + repeating*30)[:30]


    def isRationalEqual(self, s: str, t: str) -> bool:
        isRationalS, valS, strS = self.parse(s)
        isRationalT, valT, strT = self.parse(t)

        if isRationalS != isRationalT:
            return False
        
        if isRationalS:
            # 判斷兩個float是否相等, 用他們的差是否足夠小比較好
            return abs(valS-valT) < 1e-12
        else:
            return strS == strT
