class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        records = {} # never_lose: bool (True: never lose, False: lose once)
        losers = set()
        for win, los in matches:
            if win not in losers:
                if win not in records:
                    records[win] = True
                # else: we don' care

            if los not in losers:
                if los not in records:
                    records[los] = False
                else:
                    if records[los]:
                        records[los] = False
                    else:
                        del records[los]
                        losers.add(los)
        return [sorted([player for player, never_lose in records.items() if never_lose]), sorted([player for player, never_lose in records.items() if not never_lose])]
