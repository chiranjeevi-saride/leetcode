from typing import List

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        map: List[int] = {}
        for ptr in range(len(nums)):
            diff = target - nums[ptr]
            if map.get(diff) is not None:
                return [map.get(diff), ptr]
            else:
                map[nums[ptr]] = ptr
        return []

    

solution = Solution()
#TC1 - [0,1]
print(solution.twoSum([2,7,11,15], 9))
#TC1 - [1,2]
print(solution.twoSum([3,2,4], 6))
#TC1 - [0,1]
print(solution.twoSum([3,3], 6))