class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            while s[r] in numSet:
                numSet.remove(s[l])
                l += 1
            

            w = (r - l) + 1

            longest = max(longest, w) 
            numSet.add(s[r])


        return longest
 