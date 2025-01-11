class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        des = sorted(coins, reverse=True)
        count = 0
        for i in range(len(des)):
            if amount == 0:
                return count
            if amount >= des[i]:
                while amount >= des[i]:
                    amount -= des[i]
                    count += 1
        if amount == 0:
            return count
        return -1