class Solution:
    def buildTree(self, preorder, inorder):
        index_map = {}
        for i in range(len(inorder)):
            index_map[inorder[i]] = i

        self.pre_idx = 0

        def construct(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            mid = index_map[root_val]

            root.left = construct(left, mid - 1)
            root.right = construct(mid + 1, right)

            return root

        return construct(0, len(inorder) - 1)
