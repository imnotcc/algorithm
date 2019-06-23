class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _len = len(nums)
        
        if _len < 2:
            return []
        
        hashmap = {}
        
        for i in range(_len):
            key = str(target - nums[i])
            hashmap[key] = i
        for i in range(_len):
            key = str(target - nums[i])
            if key in hashmap:
                return [i,hashmap[key]]
        
        return [] 
        
