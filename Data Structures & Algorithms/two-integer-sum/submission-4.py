class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        n = len(nums)
        for i in range(0, n):
            diff = target-nums[i]
            if diff in freq_map:
                return [freq_map[diff], i]
            freq_map[nums[i]] = i

            
        