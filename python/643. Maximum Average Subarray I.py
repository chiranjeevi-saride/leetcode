'''
Time = O(n)
Space = O(1)
'''
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val = 0
        window_sum = 0
        if k < 1:
            return max_val
        
        for i in range(k):
            window_sum += nums[i]

        max_val = window_sum
    
        for i in range(k, len(nums)):
             window_sum += nums[i] - nums[i - k]
             if window_sum >  max_val:
                max_val = window_sum
        
        return max_val / k
    

def main():
    solution = Solution()
    #TC1 - 12.75
    print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
    #TC2 - 5.00000
    print(solution.findMaxAverage([5], 1))

if __name__ == "__main__":    
    main()