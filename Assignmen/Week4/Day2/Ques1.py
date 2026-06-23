class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) == 0:
                    break

                node = stack.pop()
                value = node.val
                result.append(value)

                right_child = node.right
                current = right_child

        return result
