class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)

        def parseDigit(start):
            """
            returns (digit of parsed string, end index)
            """
            j = start
            while j < n and formula[j].isdigit():
                j += 1
            cnt = 1 if j == start else int(formula[start:j])
            return cnt, j-1
        
        def parseElement(start):
            """
            returns (element from parsed string, end index)
            """
            j = start+1
            while j < n and formula[j].islower():
                j += 1
            element = formula[start:j]
            return element, j-1

        stack = []
        cur = defaultdict(int) # {key: count}

        i = 0
        while i < n:
            if formula[i] == "(":
                stack.append(cur.copy())
                cur.clear()

            elif formula[i] == ")":
                i += 1

                cnt, endIdx = parseDigit(i)
                i = endIdx

                for key in cur.keys():
                    cur[key] *= cnt
                
                pop = stack.pop()
                for key, cnt in pop.items():
                    cur[key] += cnt

            elif formula[i].isupper():
                element, endIdx = parseElement(i)
                i = endIdx+1

                cnt, endIdx = parseDigit(i)
                i = endIdx

                cur[element] += cnt

            i += 1

        return "".join(
            key + (str(cnt) if cnt > 1 else "") for key, cnt in sorted(cur.items())
        )