class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(p):
                    p = s[i:j]
        return p
