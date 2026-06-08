class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char_count = {}

        for ch in s:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

        for ch in t:
            if ch not in char_count:
                return False

            char_count[ch] -= 1

            if char_count[ch] < 0:
                return False

        for count in char_count.values():
            if count != 0:
                return False

        return True
