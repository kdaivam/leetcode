class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(n-1):
            ans = self.helper(ans)        
        return ans
    
    def helper(self, n):
        ans = ""
        i = 0
        cnt = 1
        while i < len(n)-1:
            if n[i] == n[i+1]:
                cnt += 1
            else:
                ans += str(cnt) + n[i]
                cnt = 1                
            i += 1                
        ans += str(cnt) + n[i]
        return ans