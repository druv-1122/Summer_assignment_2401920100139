class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right

            current_length = right - left + 1

            if current_length > max_length:
                max_length = current_length

        return max_length
