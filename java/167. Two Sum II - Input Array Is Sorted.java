class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int ptr1 = 0, ptr2 = numbers.length - 1;
        int[] result = new int[2];
        while(ptr1 < ptr2) {
            if(numbers[ptr1] + numbers[ptr2] == target) {
                result[0] = ptr1+1;
                result[1] = ptr2+1;
                return result;
            } else if(numbers[ptr1] + numbers[ptr2] < target) 
                ptr1+=1;
            else
                ptr2-=1;       
        }
        return result;
    }

    public static void main(String args[]) {
        Solution solution = new Solution();
        System.out.println(List.of(solution.twoSum(new int[]{2,7,11,15}, 9)))
    }
}