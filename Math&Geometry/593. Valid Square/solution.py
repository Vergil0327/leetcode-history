class Solution:
    def validSquare(self, p1, p2, p3, p4):
        if p1==p2==p3==p4:return False
        def dist(x,y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        ls=[dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)]
        ls.sort()

        # 總共四個邊+兩個對角線
        if ((side:=ls[0])==ls[1]==ls[2]==ls[3]) and ((diag:=ls[4])==ls[5]) and diag>side:
            return True
        return False