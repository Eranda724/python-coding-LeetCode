class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = str(x)
        n = len(p)
        for i in range(n):
            if x<0:
                return False
            else:
                if p[i] != p[n - 1 - i]:
                    return False
        return True 
            
