class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h_set = set()
        window_start = 0
        max_len = 0
        for window_end in range(len(s)):
            while s[window_end] in h_set:
                h_set.remove(s[window_start])
                window_start += 1
            h_set.add(s[window_end])
            max_len = max(window_end - window_start + 1, max_len)
        return max_len
    

def main():
        solution = Solution()
        #TC1 - 3
        print(solution.lengthOfLongestSubstring("abcabcbb"))
        #TC2 - 1
        print(solution.lengthOfLongestSubstring("bbbbb"))
        #TC3 - 3
        print(solution.lengthOfLongestSubstring("pwwkew"))


if __name__ == "__main__":
    main()