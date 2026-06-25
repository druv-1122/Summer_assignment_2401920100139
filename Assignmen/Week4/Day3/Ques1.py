class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        if val < root.val:
            left_result = self.searchBST(root.left, val)
            return left_result
        
        elif val > root.val:
            right_result = self.searchBST(root.right, val)
            return right_result
        
        return None
