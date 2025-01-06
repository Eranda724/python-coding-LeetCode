class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

solution = Solution()
nums = list(map(int, input("Enter the array: ").strip("[]").split(',')))
target = int(input("Enter the target: "))
print(solution.twoSum(nums, target))
