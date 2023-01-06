# Recursion
# move global index `i` to traverse `s`
class Solution:
    def deserialize(self, s):
        i = 0
        def parse(s):
            nonlocal i
            if s[i] == "[":
                i += 1
                vector = NestedInteger()
                while s[i] != "]":
                    vector.add(parse(s))
                    if s[i] == ",":
                        i += 1
                i += 1 # to skip "]"
                return vector
            else:
                start = i
                end = i
                while end<len(s) and s[end] in "0123456789-":
                    end += 1
                i = end
                return NestedInteger(int(s[start:end]))

        return parse(s)

# Stack
# two cases:
# case 1, s is vector:
#   s = [num, [num, num], num] -> return top
# case 2, s is single num:
#   s = "num" -> top is None, return NestedInteger(int(num))
class Solution:
    def deserialize(self, s):
        available = set("1234567890-")
        stack, num, top = [], "", None
        for c in s:
            if c in available:
                num += c
            elif c == "[":
                elem = NestedInteger()
                if stack:
                    stack[-1].add(elem)
                stack.append(elem)
            elif c == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                top = stack.pop()
            elif c == "," and num:
                elem = NestedInteger(int(num))
                num = ""
                stack[-1].add(elem)
        return top if top else NestedInteger(int(num))
