# Better
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def format(i, j):
            if i == j:
                return words[i] + " " * (maxWidth - len(words[i]))

            totalLetters = sum(len(words[k]) for k in range(i, j+1))
            spaces = (maxWidth - totalLetters) // (j-i) # j can't equal to i, zero division error, handle by "if i ==j: ..."
            extra = (maxWidth - totalLetters) % (j-i)

            rslt = ""
            for k in range(i, j):
                rslt += words[k] + " " * (spaces + (1 if extra > 0 else 0))
                extra -= 1
            
            rslt += words[j] # we don't need to padd last word
            return rslt
        
        res = []
        i = 0
        while i < len(words):
            # find each line
            j = i
            wordLen = 0
            while j < len(words) and wordLen+len(words[j]) <= maxWidth:
                wordLen += 1 + len(words[j])
                j += 1
            j -= 1

            # padding
            if j == len(words)-1: # last line
                rslt = " ".join(words[i:j+1])
                rslt += " " * (maxWidth-len(rslt))
                res.append(rslt)
            else:
                # format words[i:j] both inclusive
                res.append(format(i, j))

            i = j
            i += 1

        return res


# first try
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        remain = deque(words)

        groups = []
        state = []
        currWordLen = 0

        # split group by group by maxWidth
        while remain:
            word = remain.popleft()
            
            numPad = len(state)
            if currWordLen+numPad+len(word)<=maxWidth:
                state.append(word)
                currWordLen += len(word)
            else:
                groups.append(state.copy())
                state.clear()

                state.append(word)
                currWordLen = len(word)
        else:
            groups.append(state.copy())
        

        res = []
        for strs in groups[:-1]: # 由於最後一個規則不同，是靠左對齊，因此特別處理
            n = len(strs)
            wordLen = sum([len(s) for s in strs])
            padding = maxWidth - wordLen

            padLen = padding//(n-1) if n-1>0 else 0
            padRemain = padding%(n-1) if n-1>0 else 0
            rslt = ""
            for j, s in enumerate(strs):
                if j != n-1:
                    extra = 1 if padRemain > 0 else 0
                    rslt += s + " " * (padLen+extra)
                    if padRemain > 0:
                        padRemain -= 1
                else:
                    rslt += s
            
            rslt += " " * (maxWidth-len(rslt))
            res.append(rslt)
        
        # 由於最後一個規則不同，是靠左對齊，因此特別處理
        lastWord = " ".join(groups[-1])
        lastWord += " " * (maxWidth-len(lastWord))
        res.append(lastWord)
        return res
