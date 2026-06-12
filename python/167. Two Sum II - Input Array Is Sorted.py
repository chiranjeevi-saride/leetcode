from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr2: int = len(numbers) - 1
        ptr1: int = 0
        while(ptr1 < ptr2):
            if(numbers[ptr1] + numbers[ptr2] == target):
                return [ptr1+1, ptr2+1]
            elif(numbers[ptr1] + numbers[ptr2] < target):
                ptr1+=1
            else:
                ptr2-=1    

solution = Solution()

#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
print(solution.twoSum([2,7,11,15], 9))    


#Input: numbers = [2,3,4], target = 6
#Output: [1,3]
print(solution.twoSum([2,3,4], 6))   