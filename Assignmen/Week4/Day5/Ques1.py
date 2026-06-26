class Solution:
    def isSymmetric(self, root):
        def check(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            outside = check(left.left, right.right)
            inside = check(left.right, right.left)

            return outside and inside

        if not root:
            return True

        return check(root.left, root.right)
