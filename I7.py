class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        for i in range(1, numRows):
            if ((numRows+1)*i-3)%2==0:
                print(s[i], end="")
            elif ((numRows+1)*i-1)%2==1:
                print(s[i], end="")
            else:
                print(s[i], end="")