class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> hset = new HashSet();
        int windowStart = 0, maxLength = 0;
        for(int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            while(hset.contains(s.charAt(windowEnd))) {
                hset.remove(s.charAt(windowStart));
                windowStart++;
            }
            hset.add(s.charAt(windowEnd));
            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }
        return maxLength; 
    }
}