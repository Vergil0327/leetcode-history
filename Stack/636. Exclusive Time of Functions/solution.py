class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def sort_by_timestamp(s):
            _id, tag, timestamp = s.split(":")
            return int(timestamp)
        logs.sort(key=sort_by_timestamp)
        
        res = [0] * n
        callstack = []
        current_t = 0
        for log in logs:
            _id, tag, timestamp = log.split(':')
            _id, timestamp = int(_id), int(timestamp)

            if tag == 'start':
                if callstack:
                    res[callstack[-1]] += timestamp - current_t 
                callstack.append(_id)
                current_t = timestamp
            else:
                res[callstack.pop()] += timestamp - current_t + 1
                current_t = timestamp + 1

        return res
