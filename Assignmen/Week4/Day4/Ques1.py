class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        current_value = targetSum - root.val

        if root.left is None and root.right is None:
            if current_value == 0:
                return True
            else:
                return False

        left_side = self.hasPathSum(root.left, current_value)
        right_side = self.hasPathSum(root.right, current_value)

        if left_side or right_side:
            return True

        return False
