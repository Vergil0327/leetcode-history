class Solution:
    def isValid(self, code: str) -> bool:
        # "<![CDATA["  CDATA_CONTENT   "]]>"
        # "<TAG_NAME>" TAG_CONTENT     "</TAG_NAME>"

        def checkTagName(tag):
            if not tag.isupper(): return False
            if not (tag.isdigit() or tag.isalpha()): return False
            if len(tag) < 1 or len(tag) > 9: return False
            return True

        stack = []
        n = len(code)
        i = 0
        foundFirstTag = False

        while i < n:
            if i+8<n and code[i:i+9] == "<![CDATA[": # CDATA
                if not stack: return False # must exist open-closed tag

                stack.append(code[i:i+9])
                i += 9
                i0 = i
                while i+2 < n and code[i:i+3] != "]]>":
                    i += 1
                if i+2 == n: return False
                stack.pop()
                i += 3
            elif i+1 < n and code[i:i+2] == "</": # closed tag
                i += 2
                i0 = i
                while i < n and code[i] != ">":
                    i += 1
                if i == n: return False

                TAG_NAME = code[i0:i]
                if not stack or stack[-1] != TAG_NAME: return False
                
                stack.pop()
                i += 1
            elif code[i] == "<": # open tag
                i += 1
                i0 = i

                while i < n and code[i] != ">":
                    i += 1
                if i == n: return False
                
                TAG_NAME = code[i0:i]
                if not checkTagName(TAG_NAME): return False

                if not foundFirstTag:
                    if i0-1 != 0: return False # ex. "!!!<DIV>XXX</DIV>"
                    if code[-1-len(TAG_NAME):-1] != TAG_NAME: return False
                    foundFirstTag = True

                stack.append(TAG_NAME)
                i += 1
            else:
                i += 1

        if stack: return False
        if not foundFirstTag: return False
        return True
