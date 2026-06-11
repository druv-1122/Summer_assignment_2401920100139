class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        result = []

        for word in words:
            reversed_word = ""

            for i in range(len(word) - 1, -1, -1):
                reversed_word += word[i]

            result.append(reversed_word)

        return " ".join(result)
