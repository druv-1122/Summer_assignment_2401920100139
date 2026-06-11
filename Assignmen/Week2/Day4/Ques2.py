class Solution(object):
    def decodeString(self, s):
        count_stack = []
        string_stack = []

        current_string = ""
        current_num = 0

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)

            elif ch == '[':
                count_stack.append(current_num)
                string_stack.append(current_string)

                current_num = 0
                current_string = ""

            elif ch == ']':
                repeat_times = count_stack.pop()
                previous_string = string_stack.pop()

                current_string = previous_string + current_string * repeat_times

            else:
                current_string += ch

        return current_string
