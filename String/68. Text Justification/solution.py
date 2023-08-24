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
# # Intuition

# 1. find words in each line first
# 2. distribute spaces
#     - if current line is last line or only 1 word: left-justified
#     - else distribute spaces equally and distribute remainder of spaces from left to right
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        for word in words:
            if not lines or lines[-1][0] + len(word)+1 > maxWidth:
                lines.append([len(word), word])
            else:
                lines[-1][0] += len(word)+1
                lines[-1].append(word)

        def formatLine(words, isLastLine, wordsLength):
            if isLastLine or len(words)==1:
                s = " ".join(words)
                return s + " " * (maxWidth-len(s))
            else:
                numWords = len(words)
                totSpace = maxWidth - wordsLength
                space = totSpace//(numWords-1)
                extra = totSpace - (numWords-1)*space
                spaces = [space] * numWords
                for i in range(len(spaces)):
                    if extra:
                        spaces[i] += 1
                        extra -= 1
                
                s = ""
                for i, word in enumerate(words):
                    if i == len(words)-1:
                        s += word
                    else:
                        s += word + " " * spaces[i]

                return s
            return res

        res = []
        for i, line in enumerate(lines):
            wordsLength = line[0]-(len(line)-2)
            res.append(formatLine(line[1:], i == len(lines)-1, wordsLength))
        return res