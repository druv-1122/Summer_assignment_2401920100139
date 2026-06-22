class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None and q is not None:
            return False

        if p is not None and q is None:
            return False

        first_value = p.val
        second_value = q.val

        if first_value != second_value:
            return False

        left_side_check = self.isSameTree(p.left, q.left)
        right_side_check = self.isSameTree(p.right, q.right)

        if left_side_check == True and right_side_check == True:
            return True
        else:
            return False
