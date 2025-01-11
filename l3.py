class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        leng = 0
        for i in range(len(s)):
            for  j in range(i,len(s)):
                if s[j] not in arr:
                    arr.append(s[j])
                else:
                    break

            leng = max(leng, len(arr))
        return leng