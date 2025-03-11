class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        block_comment = False
        buffer = ""
        for line in source:
            i = 0
            while i < len(line):
                if line[i:i+2] == '//' and not block_comment:
                    i = len(line)
                elif line[i:i+2] == '/*' and not block_comment:
                    block_comment = True
                    i += 1
                elif line[i:i+2] == '*/' and block_comment:
                    block_comment = False
                    i += 1
                elif not block_comment:
                    buffer += line[i]
                i += 1

            if buffer and not block_comment:
                res.append(buffer)
                buffer = ""
        return res
