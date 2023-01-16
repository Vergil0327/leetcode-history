class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        missingLowercase = 1
        missingUppercase = 1
        misingDigit = 1
        repeatingSubseq = []
        curr = None
        repeatTimes = 1
        for i, ch in enumerate(password):
            if ch.isdigit():
                misingDigit = 0
            if ch.islower():
                missingLowercase = 0
            if ch.isupper():
                missingUppercase = 0
            if curr is None:
                curr = ch
                repeatTimes = 1
            else:
                if ch == curr:
                    repeatTimes += 1
                    if i == n-1 and repeatTimes >= 3:
                        repeatingSubseq.append(curr*repeatTimes)
                else:
                    if repeatTimes >= 3:
                        repeatingSubseq.append(curr*repeatTimes)
                    repeatTimes = 1
                    curr = ch
        
        # if length of repeating seq % 3 == 0, we can reduce one `replace` by deleting 1 character
        # if length of repeating seq % 3 == 1, we can reduce one `replace` by deleting 2 characters
        # if length of repeating seq % 3 == 2, we can reduce one `replace` by deleting 3 characters
        replace = 0
        delOne, delTwo = 0, 0
        while repeatingSubseq:
            seq = repeatingSubseq.pop()
            replace += len(seq)//3
            if len(seq)%3 == 0:
                delOne += 1
            elif len(seq)%3 == 1:
                delTwo += 1
        
        if n < 6:
            need = 6-n
            ops = missingLowercase + missingUppercase + misingDigit + replace
            # replace: 1 at most
            while need:
                if ops == 0: break
                need -= 1
                ops -= 1
            return max(6-n, ops)
        elif 6 <= n <= 20:
            # can cover each other
            # missingLowercase + missingUppercase + misingDigit <-> replace
            # ex. missing lowercase -> replace one with any lowercase
            # ex. missing uppercase -> replace one with any uppercase
            # ex. missing digit -> replace one with any digit
            missing = missingLowercase + missingUppercase + misingDigit
            return max(missing, replace)
        else:
            # check if deletion is enough to reduce `replace` operation
            # we can reduce one `replace` by deleting 1 character
            # we can reduce one `replace` by deleting 2 characters
            # we can reduce one `replace` by deleting 3 characters
            deletion = n-20
            while deletion > 0 and delOne > 0:
                deletion -= 1
                delOne -= 1
                replace -= 1
            while deletion >= 2 and delTwo > 0:
                deletion -= 2
                delTwo -= 1
                replace -= 1
            while deletion >= 3:
                deletion -= 3
                replace -= 1

            # missing and replace can cover each other
            missing = missingLowercase + missingUppercase + misingDigit
            return n-20 + max(missing, replace)
