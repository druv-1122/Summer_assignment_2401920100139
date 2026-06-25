class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0

            current_sum = node.val + left + right

            if current_sum > self.max_sum:
                self.max_sum = current_sum

            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
