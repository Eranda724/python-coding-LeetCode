class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = [1,2,3]
        n = 2**len(nums)
        result = []

        for i in range(n):
            subset = []
            for j in range(len(nums)):
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        
        return result
