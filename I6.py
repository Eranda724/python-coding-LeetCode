class Solution:
    def reverse(self, x: int) -> int:
        p = str(x)
        for i in range(len(p)):
            if p[0] == "-":
                if int("-" + p[:0:-1]) < -2**31:
                    return 0
                else:
                    return int("-" + p[:0:-1])
            else:
                if int(p[::-1]) > 2**31 - 1:
                    return 0
                else:
                    return int(p[::-1])