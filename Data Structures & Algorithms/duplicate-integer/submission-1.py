class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0)+1

        # print(hash_map)

        for k in hash_map:
            print(hash_map[k])
            if hash_map[k]>1:
                return True
            
        return False
        