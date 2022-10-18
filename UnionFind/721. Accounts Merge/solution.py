class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [1 for i in range(len(accounts))]
        
        def find(account):
            p = parent[account]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(acnt1, acnt2):
            p1, p2 = find(acnt1), find(acnt2)
            if p1 == p2:
                return False
            
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        email2Account = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email2Account:
                    union(i, email2Account[email])
                email2Account[email] = i
        
        res = collections.defaultdict(list)
        for email, account in email2Account.items():
            res[find(account)].append(email)
            
        return [[accounts[account][0]] + sorted(emails) for account, emails in res.items()]
                
        