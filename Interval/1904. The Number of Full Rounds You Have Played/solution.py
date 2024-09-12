class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        hr1, mn1 = loginTime.split(":")
        hour_start = int(hr1)
        minute_start = ((int(mn1)+14)//15)*15
        
        hr2, mn2 = logoutTime.split(":")
        hour_end = int(hr2)
        minute_end = (int(mn2)//15) * 15

        logout = hour_end * 60 + minute_end
        login = hour_start * 60 + minute_start
        if int(hr2) * 60 + int(mn2) < int(hr1) * 60 + int(mn1):
            logout += 24*60

        return max(0, (logout-login)) // 15
