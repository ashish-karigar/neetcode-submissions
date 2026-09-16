class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            diff = target-nums[i]
            for j in range(i+1, n):
                if diff == nums[j] and i!=j:
                    return[i,j]

            
        