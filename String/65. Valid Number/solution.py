# Brute Force
class Solution:
    def isNumber(self, s: str) -> bool:
        SET = set(s)
        if len(set("abcdfghijklmnopqrstuvwxyz") & SET) > 0: return False
        if len(set("ABCDFGHIJKLMNOPQRSTUVWXYZ") & SET) > 0: return False
        counter = Counter(s)
        if counter["e"] > 1 or counter["E"] > 1: return False

        def check(s):
            if not s: return False
            counter = Counter(s)
            if counter["+"] > 1 or counter["-"] > 1: return False

            operator = None
            if s[0] == "+" or s[0] == "-":
                operator = s[0]
                s = s[1:]
            if operator is not None and len(s) == 0: return False

            if "." in set(s):
                i = s.index(".")
                a, b = s[:i], s[i+1:]
                if not a and not b: return False
                if a and not a.isdigit(): return False
                if b and not b.isdigit(): return False

                return True
            else:
                return s.isdigit()

        if "e" in SET or "E" in SET:
            e = s.index("e") if "e" in SET else -1
            E = s.index("E") if "E" in SET else -1
            idx = max(e, E)
            a, b = s[:idx], s[idx+1:]

            # "6e6.5"
            if "." in b: return False
            return check(a) and check(b)
        else:
            return check(s)