class Solution(object):
    def isValid(self, s):
        stack = []

        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            else:
                if len(stack) == 0:
                    return False

                top_element = stack.pop()

                if bracket_map[ch] != top_element:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
