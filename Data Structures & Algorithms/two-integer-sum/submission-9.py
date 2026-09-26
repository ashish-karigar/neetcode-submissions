class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in hash_map:
        #         return [hash_map[diff], i]
        #     hash_map[n] = i
        # return 0

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[nums[i]] = i
        return 0
