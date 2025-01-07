class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)):
            j=i+1
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        return []
    
    solution = Solution()
    nums = list(map(int, input().split()))
    target = int(input())
    print(Solution.twoSum(nums, target))