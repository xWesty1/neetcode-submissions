class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        out = []
        dih = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dih:
                out += [dih[diff], i]
                return out
            dih[nums[i]] = i
        return out