class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        current_node = root

        left_child = current_node.left
        right_child = current_node.right

        left_depth = self.maxDepth(left_child)
        right_depth = self.maxDepth(right_child)

        bigger_depth = 0

        if left_depth > right_depth:
            bigger_depth = left_depth
        elif right_depth > left_depth:
            bigger_depth = right_depth
        else:
            bigger_depth = left_depth

        total_depth = bigger_depth + 1

        answer = total_depth

        return answer
