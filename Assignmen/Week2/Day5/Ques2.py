class Solution(object):
    def compress(self, chars):
        index = 0
        i = 0

        while i < len(chars):
            current_char = chars[i]
            count = 0

            while i < len(chars) and chars[i] == current_char:
                i += 1
                count += 1

            chars[index] = current_char
            index += 1

            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

        return index
