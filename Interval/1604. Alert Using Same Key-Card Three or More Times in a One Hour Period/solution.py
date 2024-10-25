class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        arr = list(sorted(zip(keyTime, keyName)))

        res = set()
        log = defaultdict(list)
        for time, name in arr:
            t = int(time[:2]) * 60 + int(time[3:])
            log[name].append(t)
            if len(log[name]) >= 3 and t-log[name][-3] <= 60:
                res.add(name)
        return list(sorted(res))